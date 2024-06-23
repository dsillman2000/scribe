<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
    <div class="scribe-app-button-div" style="width: 50%">
        <RouterLink :to=href>
            <button class="scribe-app-button">
                {{ app.replace('-', ' ') }}
            </button>
        </RouterLink>
    </div>
</template>

<script>
export default {
    name: 'ScribeAppButton',
    props: {
        app: String,
        href: String
    }
}
</script>

<style>
div.scribe-app-button-div {
    margin: 10px;
    padding: 10px;
    width: width;
    display: inline-block;
}

button.scribe-app-button {
    background-color: #cceade;
    border: none;
    color: #2c3e50;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 4px;
    padding: 10px 24px;
    border: 1px solid #cceade;
}

button.scribe-app-button:hover {
    background-color: #2c3e50;
    color: #cceade;
}

button.scribe-app-button:active {
    background-color: #546372;
    color: #cceade;
}
</style>