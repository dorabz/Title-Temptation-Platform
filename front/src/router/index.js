import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import HomeView from '../views/HomeView.vue'
import RegisterView from '../views/RegisterView.vue'
import LoginView from '../views/LoginView.vue'
import MyAccountView from '../views/MyAccountView.vue'
import MoviesView from '../views/MoviesView.vue'
import WishlistView from '../views/WishlistView.vue'
import WatchedView from '../views/WatchedView.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterView
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccountView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/movies',
    name: 'Movies',
    component: MoviesView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/wishlist',
    name: 'Wishlist',
    component: WishlistView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/watched',
    name: 'Watched',
    component: WatchedView,
    meta: {
      requireLogin: true
    }
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/login')
  } else {
    next()
  }
})

export default router
