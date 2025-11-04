import { createRouter, createWebHistory } from 'vue-router'
import Login from './views/Login.vue'
import AdminDashboard from './views/AdminDashboard.vue'
// Dashboard y vistas hijas de estudiantes
import StudentDashboard from './views/StudentDashboard.vue'
import StudentInicio from './views/student/Inicio.vue'
import StudentCursos from './views/student/Cursos.vue'
import StudentCalendario from './views/student/Calendario.vue'
import StudentCertificados from './views/student/Certificados.vue'
import StudentPerfil from './views/student/Perfil.vue'


const routes = [
  { path: '/',
    component: Login,
    meta: { hideHeader: true }
  },            // Página inicial -- Login
  { path: '/admin',
    component: AdminDashboard
  },
  { path: '/student',
    component: StudentDashboard,
    meta: { requiresAuth: true },
    redirect: '/student/inicio',
    children: [
      {
        path: 'inicio',
        name: 'StudentInicio',
        component: StudentInicio
      },
      {
        path: 'cursos',
        name: 'StudentCursos',
        component: StudentCursos
      },
      {
        path: 'calendario',
        name: 'StudentCalendario',
        component: StudentCalendario
      },
      {
        path: 'certificados',
        name: 'StudentCertificados',
        component: StudentCertificados
      },
      {
        path: 'perfil',
        name: 'StudenPerfil',
        component: StudentPerfil
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem("authToken")
  const role = localStorage.getItem("role")

  if (!token && to.path !== "/") {
    // Si no hay token y no está en login -- redirigir
    return next("/")
  }

  if (to.path.startsWith("/admin") && role !== "admin") {
    return next("/")
  }

  if (to.path.startsWith("/student") && role !== "student") {
    return next("/")
  }

  next()
})


export default router