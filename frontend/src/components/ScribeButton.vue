<template>
    <button class="scribe-button">
        <slot></slot>
    </button>
</template>

<script>
export default {
    name: 'ScribeButton'
}
</script>

<style>
button.scribe-button {
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

button.scribe-button:hover {
    background-color: #2c3e50;
    color: #cceade;
}

button.scribe-button:active {
    background-color: #546372;
    color: #cceade;
}
</style>