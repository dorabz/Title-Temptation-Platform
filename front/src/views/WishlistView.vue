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
              v-bind:key="movie.id">
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
            <td @click="showMovieDetails(movie)">
                <font-awesome-icon icon="info-circle" />
              </td>
            <td>  
                <button @click="deleteFromWishlist(movie)">
                  <font-awesome-icon icon="times" /> </button>
                  
            </td>
            <td>  
                <button @click="moveToWatched(movie)">
                  <font-awesome-icon icon="check" /> </button>
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
  import {toast} from 'bulma-toast'
  
  import { library } from '@fortawesome/fontawesome-svg-core'
  import { faInfoCircle, faTimes, faCheck } from '@fortawesome/free-solid-svg-icons'
  import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
  library.add(faInfoCircle, faTimes, faCheck)

  export default {
    name: 'WishlistView',
    components: {
      WishlistModal,
      FontAwesomeIcon
    },
    data() {
      return {
        movies: [" "],
        selectedMovie: null,
      }
    },
    mounted() {
      this.getMovies()
    },
    methods: {
      
      async getMovies() {
        this.$store.commit('setIsLoading', true)
        const userId = this.$store.state.user.id

        try {
          await this.$store.dispatch('fetchWishlist', userId)
          this.movies = []

          for (const wishlistItem of this.$store.state.wishlist) {
            const movie = await axios.get(`/api/movies/${wishlistItem.movie}/`)
            this.movies.push(movie.data)
          }
        } catch(error) {
          console.log(error)
        } finally {
          this.$store.commit('setIsLoading', false)
        }
      },
      async deleteFromWishlist(movie) {
        try {
          await this.$store.dispatch('deleteFromWishlist', movie)
          this.getMovies()
          toast({
              message: `${movie.title} has been deleted.`,
              type: 'is-danger',
              duration: 3000,
              position: 'bottom-center',
              dismissible: true
            })
        } catch (error) {
          console.log(error)
        }
      },
      async moveToWatched(movie) {
        try {
          await this.$store.dispatch('moveToWatched', movie)
          this.getMovies()
          toast({
              message: `${movie.title} has been moved to Watched list.`,
              type: 'is-warning',
              duration: 3000,
              position: 'bottom-center',
              dismissible: true
            })
        } catch (error) {
          console.log(error)
        }
      },
      showMovieDetails(movie) {
        this.selectedMovie = movie
      }
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