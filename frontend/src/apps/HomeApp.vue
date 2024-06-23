<template>
  <ScribeCard>
    <ScribeAppButton app="rhythm" href="/rhythm" />
  </ScribeCard>
</template>

<script>
import ScribeCard from '../components/ScribeCard.vue'
import ScribeAppButton from '../components/ScribeAppButton.vue'

export default {
  name: 'HomeApp',
  components: {
    ScribeCard,
    ScribeAppButton
  }
}
</script>

<style>
html {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #cceade;
  background-color: #2c3e50;
  margin-top: 60px;
}
</style>
