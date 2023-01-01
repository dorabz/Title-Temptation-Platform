<template>
    <div class="modal" :class="{ 'is-active': isModalActive }">
      <!-- modal background -->
      <div class="modal-background"></div>
      <!-- modal content -->
      <div class="modal-content">
        <div class="card">
          <div class="card-content">
            <p class="modal-card-title">Rate movie {{ movie.title }}</p>
            <hr style="height: 1px; background-color: lightblue;" />
            <div class="field">
            <label class="label"> <strong>Rating</strong></label>
            <div class="control has-icons-left has-icons-right">
                <input class="input is-info" type="number" min="0" max="10" step="0.1" 
                placeholder="Enter a rating between 0 and 10" v-model.number="rating" :disabled="existingRating !== null"
                />
            </div>
            </div>
            <button class="button is-success is-pulled-right" @click="rateMovie(movie)">Submit</button>
        <button class="button is-pulled-right" @click="$emit('close')">Cancel</button>
          </div>
        </div>
      </div>
      <!-- close button -->
      <button class="modal-close is-large" @click="closeModal"></button>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import {toast} from 'bulma-toast'
  export default {
    name: 'RateModal',
    props: {
      movie: {
        type: Object,
        required: true
      }
    },
    data() {
      return {
        isModalActive: true,
        rating: 0,
        existingRating: null,
      }
    },
    mounted() {
        this.getExistingRating();
    },
    methods: {
      closeModal() {
        this.isModalActive = false
        this.$emit('close')
      },
      async getExistingRating() {
        try {
            const response = await axios.get(`/api/ratings?user=${this.$store.state.user.id}&movie=${this.movie.id}`)
            if (response.data.find(r => r.movie === this.movie.id))  {
                this.existingRating = response.data.find(r => r.movie === this.movie.id).rating;
                this.rating = this.existingRating;
            }
        } catch (error) {
            console.log(error);
        }
    },
      async rateMovie(movie) {
        try {
            const response = await axios.get(`/api/ratings?user=${this.$store.state.user.id}&movie=${this.movie.id}`)
            if (response.data.find(r => r.movie === this.movie.id)) {
            // a rating object with this movie and this user exists
                console.log(response.data.find(r => r.movie === this.movie.id))
                this.$emit('close')
                toast({
                    message: `${movie.title} already rated.`,
                    type: 'is-danger',
                    duration: 3000,
                    position: 'bottom-center',
                    dismissible: true
                })
            } else {
            // a rating object with this movie and this user does not exist            
            const data = {
            user: this.$store.state.user.id,
            movie: this.movie.id,
            rating: this.rating
            }
            await axios.post('/api/ratings/', data)

            // Close the modal and show a success message
            this.$emit('close')
            toast({
            message: `${movie.title} rated succesfully.`,
            type: 'is-success',
            duration: 3000,
            position: 'bottom-center',
            dismissible: true
            })
        }
        } catch (error) {
            console.log(error)
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

.field {
    color: white;
    font-family: 'Trebuchet Ms', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}


  </style>
  