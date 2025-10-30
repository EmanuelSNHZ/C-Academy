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

export default router