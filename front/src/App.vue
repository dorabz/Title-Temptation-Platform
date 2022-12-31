<template>
  <div>
      <Navbar />

      <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading }">
            <div class="lds-dual-ring"></div>
        </div>

      <section class="section">
          <router-view/>
      </section>

      <Footer />
  </div>
</template>


<script>
    import axios from 'axios'
    import Navbar from '@/components/Navbar'
    import Footer from '@/components/Footer'
    
    export default {
        name: 'App',
        components: {
            Navbar,
            Footer
        },
        beforeCreate() {
            this.$store.commit('initializeStore')

            if (this.$store.state.token) {
                axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token
            } else {
                axios.defaults.headers.common['Authorization'] = ""
            }
        }
    }
</script>


<style lang="scss">
@import '../node_modules/bulma';
.lds-dual-ring {
    display: inline-block;
    width: 80px;
    height: 80px;
}
.lds-dual-ring:after {
    content: " ";
    display: block;
    width: 64px;
    height: 64px;
    margin: 8px;
    border-radius: 50%;
    border: 6px solid #ccc;
    border-color: #ccc transparent #ccc transparent;
    animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}
.is-loading-bar {
    height: 0;
    overflow: hidden;
    -webkit-transition: all 0.3s;
    transition: all 0.3s;
    
    &.is-loading {
        height: 80px;
    }
}
.section {
    background-color: #071D33;
    color: white;
    position: relative;
    min-height: 100%;
}

body{
    margin-bottom: 50px; /* Set this to the height of your footer */
    background-color: #071D33;
    color: white;
    font-family: "DejaVu Sans", "Bitstream Vera Sans", "Segoe UI", "Lucida Grande", Verdana, Tahoma, Arial, sans-serif;
}
html, body {
  height: 100%;
}

</style>
