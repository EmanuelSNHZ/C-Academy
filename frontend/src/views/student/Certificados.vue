<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'

const data = ref(null) 
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    const res = await axios.get("http://127.0.0.1:5000/student/certificados", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("authToken")}`
      }
    })

    data.value = res.data

  } catch (err) { 
    console.error("Error al cargar la vista:", err)
    error.value = "Hubo un error al cargar el contenido."
  
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div>
    <h1>Vista de Certificados</h1>
  </div>
</template>

<style lang="scss" scoped>
pre {
    background-color: $grisOscuro;
    padding: 1rem;
    border-radius: 8px;
    white-space: pre-wrap;
}

</style>
