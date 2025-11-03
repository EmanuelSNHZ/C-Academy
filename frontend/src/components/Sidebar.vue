<template>
    <aside :class="['sidebar', { 'is-expanded': isExpanded }]">

        <div class="sidebar-header">
            <span class="logo-placeholder"></span>
            <h3 v-if="isExpanded"></h3>
        </div>

        <ul class="nav-links">
            <li>
                <router-link to="/student/inicio">
                    <span class="icon-placeholder"></span>
                    <span v-if="isExpanded" class="link-text">Inicio</span>
                </router-link>
            </li>
            <li>
                <router-link to="/student/cursos">
                    <span class="icon-placeholder"></span>
                    <span v-if="isExpanded" class="link-text">Cursos</span>
                </router-link>
            </li>
            <li>
                <router-link to="/student/calendario">
                    <span class="icon-placeholder"></span>
                    <span v-if="isExpanded" class="link-text">Calendario</span>
                </router-link>
            </li>
            <li>
                <router-link to="/student/certificados">
                    <span class="icon-placeholder"></span>
                    <span v-if="isExpanded" class="link-text">Certificados</span>
                </router-link>
            </li>
            <li>
                <router-link to="/student/perfil">
                    <span class="icon-placeholder"></span>
                    <span v-if="isExpanded" class="link-text">Editar Perfil</span>
                </router-link>
            </li>
        </ul>

        <footer class="sidebar-footer">
            <a href="#" @click.prevent="logout">
                <span class="icon-placeholder"></span> 
                <span v-if="isExpanded" class="link-text">Cerrar Sesión</span>
            </a>
        </footer>

    </aside>
</template>

<script setup>
    defineProps({
        isExpanded : {
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
    transition: width 0.3 ease;

    display: flex;
    flex-direction: column;
    overflow: hidden; /* Evita que el texto se vea cuando colapse */

    // Cuando se expande
    .sidebar,
    .is-expanded {
        width: 25rem;
    }

    .sidebar-header {
        display: flex;
        align-items: center;
        padding: 2rem;
        height: 7rem;
        min-height: 7rem; // para que no se achique

        h3 {
            margin-left: 1rem;
            font-size: 1.25rem;
            white-space: nowrap; /* Hace que el texto no se parta */
        }

        .logo-placeholder,
        .icon-placeholder {
            display: inline-block;
            width: 3rem;
            height: 3rem;
            min-width: 3rem; // Evita que se achique
            background: #FFFFFF33; // Temporal para testear
            border-radius: 4px;
        }
    }

    .sidebar-header,
    .logo-placeholder {
        background: #FFFFFF66;
    }

    .navlinks {
        list-style: none;
        padding: 0;
        margin: 2rem 0;
        flex-grow: 1; // Ocupa el espacio disponible

        a {
            display: flex;
            align-items: center;
            counter-reset: $grisClaro;
            text-decoration: none;
            height: 5rem;
            padding: 0 2.5rem;
            transition: background 0.2s ease, color 0.2s ease;
            white-space: nowrap;
        }

        a,
        .link-text {
            margin-left: 1.5rem;
        }

        // hover

        .router-link-active {
            background: $gris;
            color: $blanco !important;
            font-weight: 600;
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

            &:hover {
                color: $rojo;
            }
        }
    }
}

</style>