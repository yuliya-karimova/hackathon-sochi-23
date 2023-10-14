import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'
import Analysis from './views/Analysis.vue'
import Compare from './views/Compare.vue'

const routes = [
  { path: '/home', component: Home },
  { path: '/analysis', component: Analysis },
  { path: '/compare', component: Compare },
]

const router = createRouter({
  history: createWebHistory('/hackathon-sochi-23/'),
  routes
})

export default router