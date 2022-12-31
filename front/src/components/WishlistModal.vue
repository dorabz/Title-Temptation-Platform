<template>
    <div class="modal" :class="{ 'is-active': isModalActive }">
      <!-- modal background -->
      <div class="modal-background"></div>
      <!-- modal content -->
      <div class="modal-content">
        <div class="card">
          <div class="card-content">
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

          </div>
        </div>
      </div>
      <!-- close button -->
      <button class="modal-close is-large" @click="closeModal"></button>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  export default {
    name: 'WishlistModal',
    props: {
      movie: {
        type: Object,
        required: true
      }
    },
    data() {
      return {
        isModalActive: true
      }
    },
    methods: {
      closeModal() {
        this.isModalActive = false
        this.$emit('close')
      },
    formatDuration(duration) {
        // Parse the duration string into days, hours, and minutes
        const days = parseInt(duration.split(":")[0], 10);
        const hours = parseInt(duration.split(":")[1], 10);
        const minutes = parseInt(duration.split(":")[2], 10);

        // Calculate the total number of hours and minutes
        const totalHours = days * 24 + hours;
        const totalMinutes = totalHours * 60 + minutes;

        // Format the duration as "x hr y mins"
        let formattedDuration = "";
        if (totalHours > 0) {
            formattedDuration += `${totalHours} hr `;
        }
        if (minutes > 0) {
            formattedDuration += `${minutes} mins`;
        }

        return formattedDuration;
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
  