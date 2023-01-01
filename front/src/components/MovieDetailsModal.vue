<template>
    <div class="modal" :class="{ 'is-active': isModalActive }">
      <!-- modal background -->
      <div class="modal-background"></div>
      <!-- modal content -->
      <div class="modal-content">
        <div class="card">
          <div class="card-content">

            <div class="notification is-danger" v-if="errors.length">
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>

            <h1 class="modal-card-title">{{ movie.title }}</h1>
            <hr style="height: 1px; background-color: lightblue;" />
            <p><strong>Description: </strong> </p>
                <div class="notification is-info">
                <p>{{ movie.description }}</p></div>
           
            <p><strong>Genre: </strong>
                <span
                  class="tag is-info"
                  v-for="genre in movie.genres"
                  v-bind:key="genre.id"
                  style="margin-right: 5px;">
                  {{ genre.name }}
                </span>
            </p>
            <p><strong>Duration: </strong> 
                
                {{ formatDuration(movie.duration) }}
            </p>
            <p><strong>Release year: </strong> 
              <span class="tag is-white">{{ movie.release_year }}</span>
            </p>
            
            <p ><strong>IMDB rating: </strong>  
                <span class="tag is-danger">{{ movie.imdb_rating }}</span>
            </p>
            <p><strong>Users rating: </strong>  <span class="tag is-link">{{ movie.users_rating }}</span></p>

          
            <button class="button is-pulled-right" :class="{ 'is-success': isAddedToWishlist }" @click="addToWishlist(movie)">
                <template v-if="isAddedToWishlist">
                  Added to wishlist
                </template>
                <template v-else>
                  Add to wishlist
                </template>
            </button>

            <button class="button is-pulled-right" :class="{ 'is-success': isAddedToWatched }" @click="addToWatched(movie)">
                <template v-if="isAddedToWatched">
                  Added to watched
                </template>
                <template v-else>
                  Add to watched
                </template>
            </button>
            
          </div>
        </div>
      </div>
      <button class="modal-close is-large" @click="closeModal"></button>
    </div>
</template>
  
<script>
  import axios from 'axios'
  import {toast} from 'bulma-toast'

  export default {
    name: 'MovieDetailsModal',
    props: {
      movie: {
        type: Object,
        required: true
      }
    },
    data() {
      return {
        isModalActive: true,
        isAddedToWishlist: false,
        isAddedToWatched: false,
        errors: []
      }
    },
    created() {
      this.$store.dispatch('fetchWishlist')
      this.$store.dispatch('fetchWatched')
    },
    methods: {
      closeModal() {
        this.isModalActive = false
        this.$emit('close')
      },
      formatDuration(duration) {
          const days = parseInt(duration.split(":")[0], 10);
          const hours = parseInt(duration.split(":")[1], 10);
          const minutes = parseInt(duration.split(":")[2], 10);
          const totalHours = days * 24 + hours;

          let formattedDuration = "";
          if (totalHours > 0) {
              formattedDuration += `${totalHours} hr `;
          }
          if (minutes > 0) {
              formattedDuration += `${minutes} mins`;
          }
          return formattedDuration;
      },
      async addToWishlist(movie) {
        this.errors = []
        const userId = this.$store.state.user.id
        const watched = this.$store.state.watched
        const wishlist = this.$store.state.wishlist
     
        if (watched.some(item => item.movie === movie.id)) {
          this.errors.push('This movie is already in the watched list. It cannot be added to the wishlist.')
        } else if (wishlist.some(item => item.movie === movie.id)) {
          this.errors.push('This movie is already in the wishlist.')
        } else {
          // Movie is not in the watched list, add it to the wishlist
          try {
            const response = await axios.post('/api/wishlist/', {
              user: userId,
              movie: movie.id
            })

            // Update the wishlist state
            this.$store.commit('setWishlist', response.data.wishlist)
            this.isAddedToWishlist = true
            this.$emit('close')
            toast({
              message: `${movie.title} has been added to your wishlist.`,
              type: 'is-success',
              duration: 3000,
              position: 'bottom-center',
              dismissible: true
            })
          } catch (error) {
            console.log(error)
          }
        }
      },
      async addToWatched(movie) {
        this.errors = []
        const userId = this.$store.state.user.id
        const watched = this.$store.state.watched
        const wishlist = this.$store.state.wishlist
        

        if (wishlist.some(item => item.movie === movie.id)) {
          this.errors.push('This movie is already in the wishlist. It cannot be added to the watched list.')
        } else if (watched.some(item => item.movie === movie.id)) {
          this.errors.push('This movie is already in the watched list.')
        } else {
          // Movie is not in the wishlist, add it to the watched list
          try {
            const response = await axios.post('/api/watched/', {
              user: userId,
              movie: movie.id
            })

            // Update the watched state
            this.$store.commit('setWatched', response.data.watched)
            this.isAddedToWatched = true
            this.$emit('close')
            toast({
              message: `${movie.title} has been added to your watched list.`,
              type: 'is-success',
              duration: 3000,
              position: 'bottom-center',
              dismissible: true
            })
          } catch (error) {
            console.log(error)
          }
        }
      },
    }
  }
</script>
  
<style scoped>
  
.modal-card-title{
    color: #F1F1E6;
    font-family: 'Trebuchet Ms', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    text-align: center;
}

.card {
    color: #F1F1E6;
    background-color: #041220;
    font-family: 'Trebuchet Ms', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}

.title {
    color: #F1F1E6;
    font-family: 'Trebuchet Ms', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}
strong{
    color: #F1F1E6;
    font-family: 'Trebuchet Ms', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}
.button {
    margin-right: 5px;
}

</style>
  