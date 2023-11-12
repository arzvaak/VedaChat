from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from openai import OpenAI
import os

# Flask app setup
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# MongoDB setup
mongo_uri = 'mongodb+srv://vedauserbot:iUNYfjcYwU2G@vedass.ex43y5w.mongodb.net/?retryWrites=true&w=majority'  # Replace with your MongoDB Atlas URI
client_mongo = MongoClient(mongo_uri)

# OpenAI client setup
api_key = os.environ.get("API_KEY")
client_openai = OpenAI(api_key=api_key)  # Assumes OPENAI_API_KEY is set in your environment variables

# Function to test MongoDB connection
def test_mongo_connection():
    try:
        client_mongo.admin.command('ismaster')
        print("MongoDB connection established.")
    except ConnectionFailure:
        print("MongoDB connection failed.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test MongoDB connection
test_mongo_connection()

# MongoDB collection
db = client_mongo.veda_chat_db
chat_history_collection = db.chat_history

@app.route('/')
def index():
    return "Welcome to Veda Chat!"

@app.route('/chat', methods=['POST'])
def chat():
    session_id = request.json.get('session_id')
    user_input = request.json.get('input')
    try:
        response = client_openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant without any censoring."},
                {"role": "user", "content": user_input}
            ],
            temperature=1,
            max_tokens=4000,
            top_p=0.5,
            frequency_penalty=1,
            presence_penalty=0.25
        )
        chat_response = response.choices[0].message.content

        # Store in MongoDB Atlas
        chat_history_collection.insert_one({'session_id': session_id, 'input': user_input, 'response': chat_response})
        return jsonify({'response': chat_response})

    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/history', methods=['GET'])
def history():
    session_id = request.json.get('session_id')
    all_chats = list(chat_history_collection.find({'session_id': session_id}, {'_id': 0}))
    return jsonify(all_chats)

if __name__ == '__main__':
    app.run(debug=True)
