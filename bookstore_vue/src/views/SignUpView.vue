<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign up</h1>
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
                    <div class="field">
                        <label>Repeat Password</label>
                        <div class="control">
                            <input class="input" type="password" autocomplete="on" v-model="password2">
                        </div>
                    </div>
                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">SignUp</button>
                        </div>
                    </div>
                    <hr>
                    Or <router-link to="/log-in">click here</router-link> to log in!
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default{
    name:'SignUp',
    data(){
        return{
            email :'',
            password : '',
            password2 : '',
            errors : []
        }
    },
    mounted(){
        document.title = 'Sign Up | bookstore'
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

            if (this.password !== this.password2) {
                this.errors.push('the passwords doesn\'t match.')
            }

            if (!this.errors.length) {
                const formData = {
                    email : this.email,
                    password : this.password,
                    password1 : this.password2,
                }
                axios.post('/account/api/v1/user-registration/',formData)
                .then(response=>{
                    toast({
                        message: response.data,
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover:true,
                        duration:2000,
                        position:'bottom-right'
                    })
                    this.$route.push('/log-in')
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