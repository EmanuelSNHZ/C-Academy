<template>
  <div id="app">
    <Header v-if="!$route.meta.hideHeader" /> <!-- Oculta el Header en el Login-->
    <router-view /> <!-- Aquí se renderiza Login, Admin o Student -->
  </div>
</template>

<script>
import Header from './components/Header.vue'
export default { components: { Header } }
</script>
