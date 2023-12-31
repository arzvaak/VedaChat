import { createStore } from 'vuex';
import axios from 'axios';

export default createStore({
  state: {
    messages: [],
    sessionId: localStorage.getItem('sessionId') || ''
  },
  mutations: {
    addMessage(state, message) {
      state.messages.push(message);
    },
    setMessages(state, messages) {
      state.messages = messages;
    },
    setSessionId(state, sessionId) {
        state.sessionId = sessionId;
        localStorage.setItem('sessionId', sessionId);
      }
  },
  actions: {
    generateSessionId({ commit }) {
      let sessionId = Math.random().toString(36).substring(2, 15);
      commit('setSessionId', sessionId);
    },
    async fetchMessages({ commit, state }) {
      // Ensure we have a session ID
      if (!state.sessionId) {
        this.dispatch('generateSessionId');
      }
      try {
        const response = await axios.post('https://faas-blr1-8177d592.doserverless.co/api/v1/web/fn-32596cb4-3128-4e97-a348-3e2cc30f2b34/default/veda-backend/history', { session_id: state.sessionId });
        commit('setMessages', response.data);
      } catch (error) {
        console.error('Error fetching messages:', error);
      }
    },
    async sendMessage({ commit, state }, messageContent) {
      const message = { content: messageContent, sender: 'user' };
      commit('addMessage', message);
      try {
        const response = await axios.post('https://faas-blr1-8177d592.doserverless.co/api/v1/web/fn-32596cb4-3128-4e97-a348-3e2cc30f2b34/default/veda-backend/chat', { input: messageContent, session_id: state.sessionId });
        const responseMessage = { content: response.data.response, sender: 'assistant' };
        commit('addMessage', responseMessage);
      } catch (error) {
        console.error('Error sending message:', error);
      }
    }
  }
});