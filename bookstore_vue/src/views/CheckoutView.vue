<template>
    <div class="checkout-page">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>
            <div class="column is-12 box">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                        v-for="item in cart.items"
                        v-bind:key="item.product.id"
                        >
                            <td>{{ item.product.title }}</td>
                            <td>{{ item.product.price }}</td>
                            <td>{{ item.quantity }}</td>
                            <td>${{ getItemTotal(item).toFixed(2) }}</td>
                        </tr>
                    </tbody>
                    <tfoot>
                        <tr>
                            <td colspan="2">Total</td>
                            <td>{{ cartTotalLength }}</td>
                            <td>${{ cartTotalPrice.toFixed(2) }}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>
            <div class="column is-12 box">
                <h2 class="subtitle">Shipping details</h2>
                <p class="has-text-gray mb-4">* All fields are required</p>
                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label>First Name</label>
                            <div class="control">
                                <input type="text" class="input" v-model="first_name">
                            </div>
                        </div>
                        <div class="field">
                            <label>Last Name</label>
                            <div class="control">
                                <input type="text" class="input" v-model="last_name">
                            </div>
                        </div>
                    </div>
                    <div class="column is-6">
                        <div class="field">
                            <label>Phone</label>
                            <div class="control">
                                <input type="text" class="input" v-model="phone">
                            </div>
                        </div>
                        <div class="field">
                            <label>Address</label>
                            <div class="control">
                                <input type="text" class="input" v-model="address">
                            </div>
                        </div>
                    </div>
                </div>
                <div class="notification is-danger mt-4" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error" >{{ error }}</p>
                </div>
                
                <hr>

                <div id="card-element" class="mb-5"></div>
                <template v-if="cartTotalLength">
                    <hr>

                    <button class="button is-dark" @click="submitForm">Pay With Strip</button>
                </template>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default{
    name : "Checkout",
    data() {
        return{
            cart:{
                items:[]
            },
            stripe :{},
            card:{},
            first_name:'',
            last_name:'',
            phone:'',
            address:'',
            errors:[],
        }
    },
    mounted(){
        document.document = "Checkout | Bookstore"
        this.cart = this.$store.state.cart

        if (this.cartTotalLength > 0) {
            this.stripe = Stripe('pk_test_51NeE3LKPpPCkTws449PhgaGCLVcYxQ5u1PdeBPdk4ztvBKo80eRlLff0dan0oYKFob1SnPB12AyL3gnHqRzr0y9X00HfrEa0tQ')
            const elements = this.stripe.elements();
            this.card = elements.create('card', { hidePostalCode: true })

            this.card.mount('#card-element')
        }

    },
    methods:{
        getItemTotal(item){
            return item.quantity * item.product.price
        },
        submitForm(){
            if (this.first_name === '') {
                this.errors.push('first_name is required')
            }
            if (this.last_name === '') {
                this.errors.push('last_name is required')
            }
            if (this.email === '') {
                this.errors.push('email is required')
            }
            if (this.phone === '') {
                this.errors.push('phone is required')
            }
            if (this.address === '') {
                this.errors.push('address is required')
            }
            if (this.place === '') {
                this.errors.push('place is required')
            }
            if (!this.errors.length) {
                this.$store.commit('setIsLoading',true)

                this.stripe.createToken(this.card).then(result =>{
                    if (result.error) {
                        this.$store.commit('setIsLoading',false)

                        this.errors.push('Somthing went wrong with stripe. Please try again later')

                        console.log(result.error.message);
                    }else{
                        this.stripeTokenHandler(result.token)
                    }
                })
            }
        },
        async stripeTokenHandler(token){
            const items = []
            for (let i = 0; i < this.cart.items.length; i++) {
                const item = this.cart.items[i];
                const obj = {
                    book : item.product.id,
                    quantity : item.quantity,
                    price : item.product.price * item.quantity,
                }
                items.push(obj)
                
            }

            const data = {
                'first_name' : this.first_name,
                'last_name' : this.last_name,
                'phone_number' : this.phone,
                'address' : this.address,
                'orderitem_set' : items,
                'stripe_token' : token.id

            }

            await axios.post('/cart/api/v1/checkout/',data)
                .then(response =>{
                    this.$store.commit('clearCart')
                    this.$emit('computed-trigger');
                    this.$router.push('/success')
                })
                .catch(error=>{
                    this.errors.push('Somthing went wrong. Please try again later')
                    console.log(error);
                })
                this.$store.commit('setIsLoading',false)

        }
    },
    computed:{
        cartTotalLength(){
            return this.cart.items.reduce((acc,curVal)=>{
                return acc += curVal.quantity
            },0)
        },
        cartTotalPrice(){
            return this.cart.items.reduce((acc,curVal)=>{
                return acc += curVal.product.price * curVal.quantity
            },0)
        },
    }
}
</script>