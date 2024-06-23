<template>
    <div class="scribe-card" style="width: 80%">
        <div class="scribe-card-body">
            <h1>Scribe</h1>
            <br>
            <slot></slot>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ScribeCard',
}
</script>

<style>
div.scribe-card {
    border: 1px solid #cceade;
    border-radius: 4px;
    margin: 10px;
    padding: 10px;
    width: width;
    display: inline-block;
}
</style>