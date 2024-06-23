<script setup>
import AudioPlayer from '../components/AudioPlayer.vue';

const url = `${process.env.VUE_APP_API_URL}/api/beep?format=mp3`;
</script>

<template>
    <!-- placeholder -->
    <AudioPlayer :url="url" />
</template>

<script>
export default {
    name: 'RhythmApp',
    components: [],
}
</script>