<template>
  <aside :class="['sidebar', { 'is-expanded': isExpanded }]">

    <div class="sidebar-header">
      <h3 v-if="isExpanded">C-Academy</h3> 
    </div>

    <ul class="nav-links">
      <li>
        <router-link to="/student/inicio">
          <img :src="inicioIconUrl" alt="Inicio" class="icon-img" />
          <span v-if="isExpanded" class="link-text">Inicio</span>
        </router-link>
      </li>
      <li>
        <router-link to="/student/cursos">
          <img :src="cursosIconUrl" alt="Cursos" class="icon-img" />
          <span v-if="isExpanded" class="link-text">Cursos</span>
        </router-link>
      </li>
      <li>
        <router-link to="/student/calendario">
          <img :src="calendarioIconUrl" alt="Calendario" class="icon-img" />
          <span v-if="isExpanded" class="link-text">Calendario</span>
        </router-link>
      </li>
      <li>
        <router-link to="/student/certificados">
          <img :src="certificadosIconUrl" alt="Certificados" class="icon-img" />
          <span v-if="isExpanded" class="link-text">Certificados</span>
        </router-link>
      </li>
      <li>
        <router-link to="/student/perfil">
          <img :src="perfilIconUrl" alt="Perfil" class="icon-img" />
          <span v-if="isExpanded" class="link-text">Editar Perfil</span>
        </router-link>
      </li>
    </ul>

    <footer class="sidebar-footer">
      <a href="#" @click.prevent="logout">
        <img :src="logoutIconUrl" alt="Cerrar Sesión" class="icon-img" />
        <span v-if="isExpanded" class="link-text">Cerrar Sesión</span>
      </a>
    </footer>

  </aside>
</template>

<script setup>
import inicioIconUrl from '@/assets/icons/house.svg'
import cursosIconUrl from '@/assets/icons/book-text.svg'
import calendarioIconUrl from '@/assets/icons/calendar-days.svg'
import certificadosIconUrl from '@/assets/icons/graduation-cap.svg'
import perfilIconUrl from '@/assets/icons/user-pen.svg'
import logoutIconUrl from '@/assets/icons/log-out.svg'

import { useRouter } from 'vue-router'
const router = useRouter()

defineProps({
  isExpanded: {
    type: Boolean,
    default: true
  }
})

function logout() {
  alert('Cerrando Sesión...');
  router.push('/login')
}

</script>
    
<style lang="scss" scoped>
.sidebar {
  width: 8rem;
  height: 100dvh;
  position: fixed;
  top: 0;
  left: 0;
  background-color: $grisOscuro;
  color: $blanco;
  transition: width 0.3s ease;
  display: flex;
  flex-direction: column;
  overflow: hidden;

  &.is-expanded {
    width: 25rem;
  }

  .sidebar-header {
    display: flex;
    align-items: center;
    padding: 2rem;
    // padding-left: 2.5rem;
    height: 7rem;
    min-height: 7rem;

    h3 {
    //   margin-left: 1rem;
      font-size: 2.5rem;
      white-space: nowrap;
      margin: 0 auto;
    }
  }

  .logo-img,
  .icon-img {
    width: 3rem;
    height: 3rem;
    min-width: 3rem; 
  }

//   .logo-img {}


  .nav-links {
    padding: 0;
    margin: 2rem 0;
    flex-grow: 1;
    list-style: none;

    a {
      display: flex;
      align-items: center;
      color: $grisClaro;
      text-decoration: none;
      height: 5rem;
      padding: 0 2.5rem;
      transition: background 0.2s ease, color 0.2s ease;
      white-space: nowrap;

      .link-text {
        margin-left: 1.5rem;
      }

      &:hover {
        background: #FFFFFF1a;
        color: $blanco;
      }

      &.router-link-active {
        background: $gris;
        color: $blanco !important;
        font-weight: 600;
      }
    }
  }

  .sidebar-footer {
    padding-bottom: 2rem;

    a {
      display: flex;
      align-items: center;
      color: $grisClaro;
      text-decoration: none;
      height: 5rem;
      padding: 0 2.5rem;
      white-space: nowrap;

      .link-text {
        margin-left: 1.5rem;
      }

      &:hover {
        color: $rojo;
      }
    }
  }
}
</style>