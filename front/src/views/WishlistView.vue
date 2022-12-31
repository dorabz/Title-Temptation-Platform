<template>
    <div class="container">
      <div class="columns is-multiline">
        <div class="column is-12">
          <h1 class="title">My Wishlist</h1>
          <table class="table is-fullwidth">
            <thead>
              <tr>
                <th>Title</th>
                <th>Genre</th>
                <th>IMDB rating</th>
                <th>Users rating</th>
                <th></th>
                <th></th>
                <th></th>
              </tr>
            </thead>
            <tbody>
                <tr
              v-for="movie in movies"
              v-bind:key="movie.id"
              @click="showMovieDetails(movie)">
              <td class="has-text-centered">{{ movie.title }}</td>
              <td class="has-text-centered">
                    <span
                    class="tag is-info"
                    v-for="genre in movie.genres"
                    v-bind:key="genre.id"
                    style="margin-right: 5px;">
                    {{ genre.name }}
                    </span>
              </td>
              <td class="has-text-centered">
                <span class="tag is-danger">{{ movie.imdb_rating }}</span>
            </td>
            <td class="has-text-centered">
                <span class="tag is-link">{{ movie.users_rating }}</span>
            </td>
            <td>  
                <font-awesome-icon icon="info-circle" />
            </td>
            <td>  
                <button @click="deleteFromWishlist(movie)">
                  <font-awesome-icon icon="times-circle" /> </button>
                  
            </td>
            <td>  
                <button @click="moveToWatched(movie)">
                  <font-awesome-icon icon="check-circle" /> </button>
            </td>
            </tr>
            </tbody>
          </table>
          <!-- wishlists details modal -->
          <wishlist-modal
            v-if="selectedMovie"
            v-bind:movie="selectedMovie"
            @close="selectedMovie = null"
          />
        </div>
      </div>
    </div>
  </template>
  
  <script>

  import WishlistModal from '@/components/WishlistModal.vue'
  import axios from 'axios'
  
  
  import { library } from '@fortawesome/fontawesome-svg-core'
import { faInfoCircle, faTimesCircle, faCheckCircle } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faInfoCircle, faTimesCircle, faCheckCircle)

  export default {
    name: 'WishlistView',
    components: {
      WishlistModal,
      FontAwesomeIcon
    },
    data() {
      return {
        movies: [" "],
        selectedMovie: null
      }
    },
    mounted() {
      this.getMovies()
    },
    methods: {
      async getMovies() {
        this.$store.commit('setIsLoading', true)
        const userId = this.$store.state.user.id

        const wishlist = await axios.get(`/api/wishlist/?user=${userId}`)
        this.movies = []

        for (const wishlistItem of wishlist.data) {
          const movie = await axios.get(`/api/movies/${wishlistItem.movie}/`)
          this.movies.push(movie.data)
        }

        this.$store.commit('setIsLoading', false)
      },
      showMovieDetails(movie) {
        this.selectedMovie = movie
      },
      async deleteFromWishlist(movie) {
        const userId = this.$store.state.user.id
        const wishlist = await axios.get(`/api/wishlist/?user=${userId}`)
        const wishlistToDelete = wishlist.data.find(item => item.movie === movie.id)
        await axios.delete(`/api/wishlist/${wishlistToDelete.id}/`)
        this.getMovies()
      },
      async moveToWatched(movie) {  
        const userId = this.$store.state.user.id            
        this.deleteFromWishlist(movie)
          
          const data = {
            user: userId,
            movie: movie.id
          }

          await axios.post('/api/watched/', data)
            .then(response => {
              console.log(response.data)
              
            })
        this.getMovies()
      },
    }
  }
  </script>
    
<style scoped>

.table tbody tr:hover {
  background-color: #2F4865;
}

.table th{
    color: #F1F1E6;
    background-color:#2F4865;
    font-family: 'Trebuchet Ms', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    text-align: center;
}

.table {
    color: #F1F1E6;
    background-color: #041220;
    font-family: 'Trebuchet Ms', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}

.title {
    color: #F1F1E6;
    font-family: 'Trebuchet Ms', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}

</style>