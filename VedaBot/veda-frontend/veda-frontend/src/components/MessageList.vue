<template>
    <div class="flex flex-col p-4 space-y-4 overflow-y-auto">
      <ChatMessage v-for="msg in messages" :key="msg.id" :message="msg" />
    </div>
  </template>
  
  <script>
  import { mapState } from 'vuex';
  import ChatMessage from './ChatMessage.vue';
  
  export default {
    name: 'MessageList',
    components: {
      ChatMessage
    },
    computed: {
      ...mapState(['messages'])
    },
    mounted() {
      this.$store.dispatch('fetchMessages');
    }
  };
  </script>
  