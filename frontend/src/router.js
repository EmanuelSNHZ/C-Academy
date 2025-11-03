import { createRouter, createWebHistory } from 'vue-router'
import Login from './views/Login.vue'
import AdminDashboard from './views/AdminDashboard.vue'
import StudentDashboard from './views/StudentDashboard.vue'

const routes = [
  { path: '/',
    component: Login,
    meta: { hideHeader: true }
  },            // Página inicial → Login
  { path: '/admin',
    component: AdminDashboard
  },
  { path: '/student',
    component: StudentDashboard
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
    // Si no hay token y no está en login → redirigir
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