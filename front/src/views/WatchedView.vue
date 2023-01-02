<template>
    <div class="container">
      <div class="columns is-multiline">
        <div class="column is-12">
          <h1 class="title">Watched</h1>
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
                <button @click="deleteFromWatched(movie)"> 
                  <font-awesome-icon icon="times" /> </button>
            </td>
            <td>  
              <button @click="openRateModal(movie)">
                <font-awesome-icon icon="star" />
              </button>
            </td>
            </tr>
            </tbody>
          </table>
          <!-- movie details modal -->
          <watched-modal
            v-if="showWatchedModal"
            v-bind:movie="selectedMovie"
            @close="showWatchedModal = false"
          />
          <rate-modal
            v-if="showRateModal"
            v-bind:movie="selectedMovie"
            @close="showRateModal = false"
          />
        </div>
      </div>
    </div>
  </template>
  
  <script>

  import WatchedModal from '@/components/WatchedModal.vue'
  import RateModal from '@/components/RateModal.vue'
  import axios from 'axios'
  import {toast} from 'bulma-toast'
  
  import { library } from '@fortawesome/fontawesome-svg-core'
  import { faInfoCircle, faTimes, faStar } from '@fortawesome/free-solid-svg-icons'
  import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
  library.add(faInfoCircle, faTimes, faStar)

  export default {
    name: 'MoviesView',
    components: {
      WatchedModal,
      FontAwesomeIcon,
      RateModal
    },
    data() {
      return {
        movies: [" "],
        selectedMovie: null,
        showWatchedModal: false,
        showRateModal: false,

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
          await this.$store.dispatch('fetchWatched', userId)
          this.movies = []

          for (const watchedItem of this.$store.state.watched) {
            const movie = await axios.get(`/api/movies/${watchedItem.movie}/`)
            this.movies.push(movie.data)
          }
        } catch(error) {
          console.log(error)
        } finally {
          this.$store.commit('setIsLoading', false)
        }
      },
      showMovieDetails(movie) {
        this.selectedMovie = movie
        this.showWatchedModal = true
      },
      openRateModal(movie) {
        this.selectedMovie = movie
        this.showRateModal = true
      },
      async deleteRate(movie) {
        try {
            const response = await axios.get(`/api/ratings?user=${this.$store.state.user.id}&movie=${movie.id}`)
            if (response.data.find(r => r.movie === movie.id))  {
                const rateId = response.data.find(r => r.movie === movie.id).id
                await axios.delete(`/api/ratings/${rateId}`)
            }
        } catch (error) {
            console.log(error);
        }
      },
      async deleteFromWatched(movie) {
        try {
          await this.$store.dispatch('deleteFromWatched', movie)
          this.deleteRate(movie)
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