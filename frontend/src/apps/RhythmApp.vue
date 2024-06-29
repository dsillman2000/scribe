<script setup>
import AudioPlayer from '../components/AudioPlayer.vue';
import BPMEntry from '../components/BPMEntry.vue';
import ScribeButton from '../components/ScribeButton.vue';
</script>

<template>
    <!-- placeholder -->
     <div class="rhythm-settings">
        <h3>Rhythm settings</h3>
        <p>Here you can adjust the rhythm settings for the metronome.</p>
        
        <BPMEntry @change="setBpm"/>
    </div>
    <div class="next-exercise-button">
        <ScribeButton @click="getNextExercise">Next exercise</ScribeButton>
    </div>
    <div class="rhythm-audio-player">
        <AudioPlayer :key="audioPlayerKey" :url="url" />
    </div>
</template>

<script>
export default {
    name: 'RhythmApp',
    components: [AudioPlayer, BPMEntry, ScribeButton],
    data() {
        return {
            audioPlayerKey: 0,
            url: null,
            bpm: 120
        }
    },
    methods: {
        setBpm(event) {
            console.log("Setting BPM to: ", event.target.value);
            this.bpm = event.target.value;
        },
        rebuildAudioPlayer() {
            this.audioPlayerKey += 1;
        },
        getNextExercise() {
            console.log("Getting next exercise with BPM: ", this.bpm);
            // fetch next exercise
            const exerciseSeed = Date.now();
            this.url = `${process.env.VUE_APP_API_URL}/exercises/rhythm/${exerciseSeed}?bpm=${this.bpm}&count_in=4`;
            console.log("Requesting audio from: ", this.url);
            this.rebuildAudioPlayer();
        }
    }
}
</script>

<style scoped>
div.rhythm-settings {
    border: 1px solid #cceade;
    border-radius: 4px;
    /* margin: 10px; */
    padding: 10px 50px 30px;
    width: width;
    display: inline-block;
}

div.next-exercise-button {
    margin: 10px;
    padding: 10px;
    width: width;
}

</style>