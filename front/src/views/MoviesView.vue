<template>
    <div class="container">
      <div class="columns is-multiline">
        <div class="column is-12">
          <h1 class="title">Movies</h1>
          <form @submit.prevent="getMovies">
                    <div class="field has-addons">
                        <div class="control">
                            <input type="text" class="input" v-model="query">
                        </div>
                        <div class="control">
                            <button class="button is-success">Search</button>
                        </div>
                    </div>
            </form>
            <br/>
          <table class="table is-fullwidth">
            <thead>
              <tr>
                <th>Title</th>
                <th>Genre</th>
                <th>IMDB rating</th>
                <th>Users rating</th>
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
              <td >  
                <font-awesome-icon icon="info-circle" />
              </td>
            </tr>
            </tbody>
          </table>
          <div class="buttons is-pulled-right">
                <button class="button  is-small" @click="goToPreviousPage()" v-if="showPreviousButton">Previous</button>
                <button class="button  is-small" @click="goToNextPage()" v-if="showNextButton">Next</button>
          </div>
          <!-- movie details modal -->
          <movie-details-modal
            v-if="selectedMovie"
            v-bind:movie="selectedMovie"
            @close="selectedMovie = null"
          />
        </div>
      </div>
    </div>
  </template>
  
<script>

  import MovieDetailsModal from '@/components/MovieDetailsModal.vue'
  import axios from 'axios'
  
  import { library } from '@fortawesome/fontawesome-svg-core'
  import { faInfoCircle } from '@fortawesome/free-solid-svg-icons'
  import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
  library.add(faInfoCircle)

  export default {
    name: 'MoviesView',
    components: {
      MovieDetailsModal,
      FontAwesomeIcon
    },
    data() {
      return {
        movies: [" "],
        selectedMovie: null,
        showNextButton: false,
        showPreviousButton: false,
        currentPage: 1,
        query: '',
      }
    },
    mounted() {
      this.getMovies()
    },
    methods: {
      goToNextPage() {
        this.currentPage += 1
        this.getMovies()
      },
      goToPreviousPage() {
        this.currentPage -= 1
        this.getMovies()
      },
      async getMovies() {
        this.$store.commit('setIsLoading', true)

        this.showNextButton = false
        this.showPreviousButton = false

        await axios
          .get(`/api/movies/?page=${this.currentPage}&search=${this.query}`)
          .then(response => {
            this.movies = response.data.results

            if (response.data.next) {
              this.showNextButton = true
            }
            if (response.data.previous) {
              this.showPreviousButton = true
            }
          })
          
        this.$store.commit('setIsLoading', false)
      },
      showMovieDetails(movie) {
        this.selectedMovie = movie
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
.button {
    color: #F1F1E6;
    background-color: #041220;
    font-family: 'Trebuchet Ms', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}

</style>