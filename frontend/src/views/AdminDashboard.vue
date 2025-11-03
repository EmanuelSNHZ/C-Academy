<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'

const message = ref("")

onMounted(async () => {
  try {
    const res = await axios.get("http://127.0.0.1:5000/admin/dashboard", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("authToken")}`
      }
    })
    message.value = res.data.message
  } catch (err) {
    message.value = "Error al cargar el dashboard"
  }
})
</script>

<template>
  <h1>{{ message }}</h1>
</template>
