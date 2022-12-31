<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h4 class="title has-text-centered">My account</h4>
            </div>

                <div class="column is-4">
                    <div class="box">
                        <p class="title has-text-centered">User information</p>
                        <p>ID:{{  user.id }}</p>
                        <p>Username: {{ user.username }}</p>
                        <p>First name: {{ user.first_name }}</p>
                    </div>
                </div>
                <div class="column is-4">
                    <div class="box">
                        <p class="title has-text-centered">Change password</p>
                        <p>ID:{{  user.id }}</p>
                        <p>Username: {{ user.username }}</p>
                        <p>First name: {{ user.first_name }}</p>
                        <p>First name: {{ user.first_name }}</p>
                    </div>
                </div>
                <div class="column is-4">
                    <div class="box">
                        <p class="title has-text-centered">My suggestions</p>
                        <p>Looking for a movie not on platform?</p>
                        <p>Give suggestions</p>
                        <p>COMING SOON!</p>
                    </div>
                </div>
                <div class="column is-4">
                    <div class="box">
                        <p class="title has-text-centered">My wishlist</p>
                        <p>ID:{{  user.id }}</p>
                        <p>Username: {{ user.username }}</p>
                        <p>First name: {{ user.first_name }}</p>
                    </div>
                </div>
                <div class="column is-4">
                    <div class="box">
                        <p class="title has-text-centered">My watched list</p>
                        <p>ID:{{  user.id }}</p>
                        <p>Username: {{ user.username }}</p>
                        <p>First name: {{ user.first_name }}</p>
                    </div>
                </div>
                <div class="column is-4">
                    <div class="box">
                        <p class="title has-text-centered">My ratings</p>
                        <p>ID:{{  user.id }}</p>
                        <p>Username: {{ user.username }}</p>
                        <p>First name: {{ user.first_name }}</p>
                    </div>
                </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'MyAccountView',
        data() {
            return {
                user: {}
             }
        },
        mounted() {
            this.getUser()
        }, 
        methods: {
            async getUser() {
                const userID = this.$store.state.user.id

                await axios
                 .get(`/api/users/${userID}/`)
                 .then(response => {
                    this.user = response.data

                })
                .catch(error => {
                    console.log(error)
                 })
             }
        }
    }
</script>

<style scoped>
p {
    color: #F1F1E6;
    font-size: 95%;
    font-family: 'Trebuchet Ms', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}

.box {
    color: #F1F1E6;
    background-color: #041220;
    font-family: 'Trebuchet Ms', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}

.title {
    color: #F1F1E6;
    font-family: 'Trebuchet Ms', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}
</style>