<template>
    <div :class="messageClass">
      {{ message.content }}
    </div>
  </template>
  
  <script>
  export default {
    name: 'ChatMessage',
    props: {
      message: {
        type: Object,
        required: true
      }
    },
    computed: {
      messageClass() {
        return [
          'p-3 rounded-lg max-w-xs shadow',
          {
            'bg-blue-100 self-end': this.message.sender === 'user',
            'bg-gray-100 self-start': this.message.sender === 'assistant'
          }
        ];
      }
    }
  };
  </script>
  