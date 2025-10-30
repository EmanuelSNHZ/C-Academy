<template>
  <header class="header">
    <nav>
      <router-link to="/">Inicio</router-link>
      <router-link to="/login">Academia</router-link>
    </nav>
  </header>
</template>

<script>
export default {
  name: "Header"
}
</script>

<style scoped>
.header {
  background: #222;
  padding: 1rem;
}
nav a {
  color: white;
  margin-right: 1rem;
  text-decoration: none;
}
</style>
