<template>
    <div class="audio-player">
        <audio controls>
            <source :src="url" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>
    </div>
</template>

<script>
export default {
    name: 'AudioPlayer',
    props: {
        url: {
            type: String,
            required: true
        }
    }
}
</script>