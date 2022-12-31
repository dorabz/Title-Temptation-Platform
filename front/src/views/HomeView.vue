<template>
<section class="hero is-info is-fullheight">
            <div class="hero-body">
                <div class="container has-text-centered">
                    <div class="column is-6 is-offset-3">
                        <h1 class="title">
                            Title Temptation
                        </h1>
                        <h2 class="subtitle">
                          Tempted by the title, hooked by the movie.
                        </h2>
                        <router-link to="/register" class="button is-light">Register and get started</router-link>

                    </div>
                </div>
            </div>

    </section>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView'
}
</script>

<style scoped>
.hero.is-info {
  background: linear-gradient(
      rgba(0, 0, 0, 0.088),
      rgba(0, 0, 0, 0.5)
    ), url('https://images.pexels.com/photos/1040159/pexels-photo-1040159.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2') no-repeat center center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}
</style>