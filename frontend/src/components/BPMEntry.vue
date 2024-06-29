<template>
    <div class="bpm-entry">
        <label for="bpm">BPM</label>
        <input type="number" id="bpm" name="bpm" min="1" max="300" :value="bpm" />
    </div>
</template>

<script>
export default {
    name: 'BPMEntry',
    props: {
        bpm: {
            type: Number,
            default: 120
        }
    }
}
</script>

<style scoped>

div.bpm-entry {
    padding: 5px;
    display: flex;
    flex-direction: row;
    justify-content: center;
}

div.bpm-entry > label {
    width: 30%;
    text-align: center;
    padding-right: 20px;
}

div.bpm-entry > input {
    width: 30%;
    text-align: left;
}

</style>