import { createApp } from 'vue';
import App from './App.vue';
import store from './store'; // Ensure you import the store
import './assets/styles.css'; // Tailwind CSS file

const app = createApp(App);
app.use(store); // Use the store
app.mount('#app');
