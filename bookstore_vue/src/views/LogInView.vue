<template>
    <div class="page-log-in">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log In</h1>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input class="input" type="email" v-model="email">
                        </div>
                    </div>
                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input class="input" type="password" autocomplete="on" v-model="password">
                        </div>
                    </div>
                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">LogIn</button>
                        </div>
                    </div>
                    <hr>
                    Or <router-link to="/log-in">click here</router-link> to sign up!
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default{
    name:'LogIn',
    data(){
        return{
            email :'',
            password : '',
            errors : []
        }
    },
    mounted(){
        document.title = 'Log In | bookstore'
    },
    methods:{
        submitForm(){
            this.errors = []
            if (this.email === '') {
                this.errors.push('the email is required.')
            }

            if (this.password === '') {
                this.errors.push('password is required.')
            }

            if (!this.errors.length) {
                const formData = {
                    email : this.email,
                    password : this.password,
                }
                axios.post('/api/token/',formData)
                .then(response=>{
                    const token = response.data.access
                    this.$store.commit('setToken', token)
                    
                    axios.defaults.headers.common["Authorization"] = "Bearer " + token

                    localStorage.setItem("token", token)

                    const toPath = this.$route.query.to || '/cart'
                    this.$router.push(toPath)
                })
                .catch(error=>{
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                        console.log(JSON.stringify(error.response.data));
                    }else if(error.message){
                        this.errors.push('Something went wrong. Please try again later')
                        console.log(JSON.stringify(error));
                    }
                })
            }
        }
    }
}
</script>