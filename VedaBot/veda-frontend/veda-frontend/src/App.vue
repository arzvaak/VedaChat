<template>
  <div class="min-h-screen flex flex-col bg-gray-100">
    <header class="bg-blue-600 text-white text-center py-4 shadow-md">
      <h1 class="text-3xl font-semibold">Veda Chat</h1>
    </header>

    <div class="flex-grow overflow-hidden">
      <MessageList />
    </div>

    <MessageInput />
  </div>
</template>

<script>
import MessageList from './components/MessageList.vue';
import MessageInput from './components/MessageInput.vue';

export default {
  name: 'App',
  components: {
    MessageList,
    MessageInput
  }
};
</script>
