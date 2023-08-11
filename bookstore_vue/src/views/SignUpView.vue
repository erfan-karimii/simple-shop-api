<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign up</h1>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input class="input" type="text" v-model="username">
                        </div>
                    </div>
                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input class="input" type="password" v-model="password">
                        </div>
                    </div>
                    <div class="field">
                        <label>Repeat Password</label>
                        <div class="control">
                            <input class="input" type="password" v-model="password2">
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
            username :'',
            password : '',
            password2 : '',
            errors : []
        }
    },
    methods:{
        submitForm(){
            this.errors = []
            if (this.username === '') {
                this.errors.push('the username is required.')
            }

            if (this.password === '') {
                this.errors.push('password is required.')
            }

            if (this.password !== this.password2) {
                this.errors.push('the passwords doesn\'t match.')
            }

            if (!this.errors.length) {
                const formData = {
                    username : this.username,
                    password : this.password,
                }
                // axios.
            }
        }
    }
}
</script>