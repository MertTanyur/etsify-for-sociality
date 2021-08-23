import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
import FetchLink from '../views/FetchLink.vue'
import AllProducts from '../views/AllProducts.vue'
import SpecificProduct from '../views/SpecificProduct.vue'
import Devlog from '../views/Devlog.vue'
import ProjectDescription from '../views/ProjectDescription.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'FetchLink',
    component: FetchLink
  },
  {
    path: '/allProducts',
    name: 'AllProducts',
    component: AllProducts
  },
  {
    path: '/specificProduct',
    name: 'SpecificProduct',
    component: SpecificProduct
  },
  {
    path: '/projectDescription',
    name: 'ProjectDescription',
    component: ProjectDescription
  },
  {
    path: '/devlog',
    name: 'Devlog',
    component: Devlog
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({

  routes
})

export default router
