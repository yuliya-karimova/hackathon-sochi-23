import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'
import Analysis from './views/Analysis.vue'
import Compare from './views/Compare.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/analysis', component: Analysis },
  { path: '/compare', component: Compare },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router