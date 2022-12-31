<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h2 class="title has-text-centered">Register</h2>
            
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" name="email" class="input is-info" v-model="username" placeholder="e.g. name@gmail.com">
                        </div>
                    </div>


                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" name="password1" class="input is-info" v-model="password1" placeholder="at least 8 characters">
                        </div>
                    </div>

                    <div class="field">
                        <label>Repeat password</label>
                        <div class="control">
                            <input type="password" name="password2" class="input is-info" v-model="password2" placeholder="repeat password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success is-pulled-right">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    import {toast} from 'bulma-toast'

    export default {
        name: 'RegisterView',
        data() {
            return {
                username: '',
                password1: '',
                password2: '',
                errors: []
            }
        },
        methods: {
            async submitForm() {
                this.errors = []

                if (this.username === '') {
                    this.errors.push('The email is missing')
                }

                if (this.password1 === '') {
                    this.errors.push('The password is too short')
                }

                if (this.password1 !== this.password2) {
                    this.errors.push('The passwords are not matching')
                }

                if (!this.errors.length) {
                    this.$store.commit('setIsLoading', true)

                    const formData = {
                        username: this.username,
                        password: this.password1
                    }

                    await axios
                        .post('/api/users/', formData)
                        .then(response => {
                            toast({
                                message: 'Account was created, please log in',
                                type: 'is-success',
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 2000,
                                position: 'bottom-right',
                            })

                            this.$router.push('/login')
                        })
                        .catch(error => {
                            if (error.response) {
                                for (const property in error.response.data) {
                                    this.errors.push(`${property}: ${error.response.data[property]}`)
                                }
                            } else if (error.message) {
                                this.errors.push('Something went wrong. Please try again!')
                            }
                        })
                    
                    this.$store.commit('setIsLoading', false)
                }
            }
        }
    }
</script>

<style scoped>
.title {
    color: white;
    font-family: 'Trebuchet Ms', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}

.field {
    color: white;
    font-family: 'Trebuchet Ms', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}
</style>