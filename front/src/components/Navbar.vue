<template>
    <nav class="navbar">
        <div class="navbar-brand">
            <a class="navbar-item" href="#">
            <img src="../assets/logo.png" alt="Logo">
          </a>
          <router-link to="/" class="navbar-item routerlink">
               <a>Title Temptation</a>
            </router-link>
        </div>

        <div class="navbar-menu">
            <div class="navbar-end">
                <template v-if="$store.state.isAuthenticated">
                    <router-link to="/movies" class="navbar-item">All Movies</router-link>
                    <router-link to="/wishlist" class="navbar-item">Wishlist  <font-awesome-icon icon="heart" /></router-link>
                    <router-link to="/watched" class="navbar-item">Watched</router-link>
                </template>

                <div class="navbar-item">
                    <div class="buttons">
                        <template v-if="!$store.state.isAuthenticated">
                            <router-link to="/register" class="button is-light">Register</router-link>
                            <router-link to="/login" class="button is-success">Log in</router-link>
                        </template>
                        <template v-else>
                            <router-link to="/my-account" class="button is-info">My account</router-link>
                            <button @click="logout()" class="button is-danger">Log out</button>
                        </template>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
import { library } from '@fortawesome/fontawesome-svg-core'
import { faHeart } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faHeart)

  import axios from 'axios'
  
    export default {
        name: 'Navbar',
        components: {
            FontAwesomeIcon
        },
        methods: {
            async logout() {
                await axios
                    .post('/api/token/logout/')
                    .then(response => {
                        console.log('Logged out')
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
                
                axios.defaults.headers.common['Authorization'] = ''
                this.$store.commit('removeToken')
                this.$router.push('/')
            },
    }
}
</script>

<style scoped>
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 1rem;
    background-color: #041220;
    color: white;
    font-family: 'Trebuchet Ms', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}
.navbar-item {
    color: white;
}
a {
    color: white;
}

</style>