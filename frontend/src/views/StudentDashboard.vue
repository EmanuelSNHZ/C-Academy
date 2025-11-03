<template>
  <div :class="['student-layout', { 'sidebar-expanded': isSidebarExpanded }]">
    
    <Sidebar :is-expanded="isSidebarExpanded" />

    <div class="page-container">
      <button>
        <img src="" alt="">
      </button>
    </div>
  </div>
  <div>
    <h1>{{ message }}</h1>
    <p>Este es el panel de estudiante protegido por JWT.</p>
  </div>
</template>


<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'
import Sidebar from '../components/Sidebar.vue'

const message = ref("")

onMounted(async () => {
  try {
    const res = await axios.get("http://127.0.0.1:5000/student/dashboard", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("authToken")}`
      }
    })
    message.value = res.data.message
  } catch (err) {
    message.value = "Error al cargar el dashboard de estudiante"
  }
})
</script>