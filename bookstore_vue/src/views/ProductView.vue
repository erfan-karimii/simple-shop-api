<template>
    <div class="page-product">
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-bind:src="product.image">
                </figure>
                <h1 class="title">{{ product.title }}</h1>
                <p>{{ product.description }}</p>
            </div>
            <div class="column is-3">
                <h2 class="subtitle">Information</h2>
                <p><strong>price:</strong>${{ product.price }}</p>
                <div class="field has-addons mt-6">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantity">
                    </div>
                    <div class="control">
                        <a class="button is-dark" @click="addToCart">Add to cart</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default{
    name:'Product',
    data(){
        return{
            quantity : 1,
            product : {},
        }
    },
    mounted(){
        this.get_product()
    },
    methods:{
        async get_product(){
            this.$store.commit('setIsLoading',true)
            
            const id = this.$route.params.product_id
            await axios.get(`/book/api/v1/book-detail/${id}/`)
            .then(response=>{
                this.product = response.data
                document.title = this.product.title + "| BookStore"
            })
            .catch(error=>{
                console.log(error)
            })

            this.$store.commit('setIsLoading',false)

        },
        addToCart(){
            if (isNaN(this.quantity || this.quantity<1)) {
                this.quantity = 1
            }

            const item ={
                quantity:this.quantity,
                product:this.product,
            }
            this.$store.commit('addToCart',item)
            toast({
                message:"added to cart",
                type:"is-success",
                dismissible:true,
                pauseOnHover:true,
                duration:2000,
                position:'bottom-right',
            })
        }
    }
    
}
</script>