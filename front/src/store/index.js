import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    isLoading: false,
    isAuthenticated: false,
    token: '',
    user: {
      id: 0,
      username: '',
    },
    wishlist: [],
    watched: [],
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.user.username = localStorage.getItem('username')
        state.user.id = localStorage.getItem('userid')
        state.wishlist = JSON.parse(localStorage.getItem('wishlist'))
      } else {
        state.token = ''
        state.isAuthenticated = false
        state.user.id = 0
        state.user.username = ''
        state.wishlist = []
      }
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    },
    setUser(state, user) {
      state.user = user
    },
    setWishlist(state, wishlist) {
      state.wishlist = wishlist
    },
    setWatched(state, watched) {
      state.watched = watched
    },
  },
  actions: {
    async fetchWatched({ commit }) {
      try {
        const response = await axios.get(`/api/watched/?user=${this.state.user.id}`)
        commit('setWatched', response.data)
      } catch (error) {
        console.log(error)
      }
    },
    async fetchWishlist({ commit }) {
      try {
        const response = await axios.get(`/api/wishlist/?user=${this.state.user.id}`)
        commit('setWishlist', response.data)
      } catch (error) {
        console.log(error)
      }
    },
    async deleteFromWishlist({ commit }, movie) {
      try {
        // Find the wishlistItemId of the movie you want to delete
        const wishlistItemId = this.state.wishlist.find(item => item.movie === movie.id).id
        // Delete the movie from the wishlist using the wishlistItemId
        await axios.delete(`/api/wishlist/${wishlistItemId}/`)
        // After the item has been deleted, fetch the updated wishlist from the API and commit it to the state
        const response = await axios.get(`/api/wishlist/?user=${this.state.user.id}`)
        commit('setWishlist', response.data)
      } catch (error) {
        console.log(error)
      }
    },
    async moveToWatched({ commit }, movie) {
      const wishlistItemId = this.state.wishlist.find(item => item.movie === movie.id).id
      try {
        const data = {
          user: this.state.user.id,
          movie: movie.id
        }
        // Send the POST request to add the movie to the watched list
        await axios.post('/api/watched/', data)
        // After the movie has been added to the watched list, delete it from the wishlist
        await axios.delete(`/api/wishlist/${wishlistItemId}/`)
        // Fetch the updated wishlist and watched lists from the API and commit them to the state
        const wishlistResponse = await axios.get(`/api/wishlist/?user=${this.state.user.id}`)
        commit('setWishlist', wishlistResponse.data)
        const watchedResponse = await axios.get(`/api/watched/?user=${this.state.user.id}`)
        commit('setWatched', watchedResponse.data)
      } catch (error) {
        console.log(error)
      }
    },
    async deleteFromWatched({ commit }, movie) {
      try {
        // Find the wishlistItemId of the movie you want to delete
        const watchedItemId = this.state.watched.find(item => item.movie === movie.id).id
        // Delete the movie from the wishlist using the wishlistItemId
        await axios.delete(`/api/watched/${watchedItemId}/`)
        // After the item has been deleted, fetch the updated wishlist from the API and commit it to the state
        const response = await axios.get(`/api/watched/?user=${this.state.user.id}`)
        commit('setWatched', response.data)
      } catch (error) {
        console.log(error)
      }
    },
  }
})
