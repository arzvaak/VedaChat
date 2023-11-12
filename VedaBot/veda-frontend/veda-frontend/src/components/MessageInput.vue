<template>
    <div class="p-4 bg-white border-t-2 border-gray-200">
      <div class="flex gap-2">
        <input 
          v-model="newMessage" 
          @keyup.enter="submitMessage" 
          type="text" 
          class="flex-1 p-2 border rounded-lg focus:outline-none focus:border-blue-300" 
          placeholder="Type a message..."
        />
        <button 
          @click="submitMessage" 
          class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 focus:outline-none"
        >
          Send
        </button>
      </div>
    </div>
  </template>
  
  <script>
  import { mapActions } from 'vuex';
  
  export default {
    name: 'MessageInput',
    data() {
      return {
        newMessage: ''
      };
    },
    methods: {
      ...mapActions(['sendMessage']),
      submitMessage() {
        if (this.newMessage.trim() !== '') {
          this.sendMessage(this.newMessage);
          this.newMessage = '';
        }
      }
    }
  };
  </script>
  