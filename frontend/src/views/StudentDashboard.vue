<template>
  <div :class="['student-layout', { 'sidebar-expanded': isSidebarExpanded }]">

    <Sidebar :is-expanded="isSidebarExpanded" />

    <div class="page-container">

      <button @click="toggleSidebar" class="sidebar-toggle">
        <img :src="menuIconUrl" alt="Menú" class="icon-img" />
      </button>
      
      <main class="main-content">
        <router-view /> 
      </main>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Sidebar from '../components/Sidebar.vue' 
import menuIconUrl from '@/assets/icons/menu-violeta.svg'

const isSidebarExpanded = ref(true)

function toggleSidebar() {
  isSidebarExpanded.value = !isSidebarExpanded.value
}
</script>

<style lang="scss">
.student-layout {
  display: flex;
  background: $fondo;
  min-height: 100dvh;

  .page-container {
    flex-grow: 1;
    position: relative;
    padding: 2rem;
    transition: margin-left 0.3s ease;

    .sidebar-toggle {
      position: absolute;
      top: 1.5rem;
      left: 1.5rem; 
      background: $grisOscuro;
      border: 1px solid $grisOscuro;
      border-radius: 0.8rem;
      width: 4rem;
      height: 4rem;
      cursor: pointer;
      z-index: 100;
      
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 0;

      &:hover {
        background: $gris;
      }
      
      .icon-img {
        width: 2rem;
        height: 2rem;
      }
    }
  }

  &.sidebar-expanded {
    .page-container {
      margin-left: 25rem;
    }
  }

  &:not(.sidebar-expanded) {
    .page-container {
      margin-left: 8rem;
    }
  }
}
</style>