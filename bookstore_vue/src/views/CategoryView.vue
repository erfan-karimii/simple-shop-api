<template>
    <div class="category-page">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">{{ category.name }}</h2>
            </div>
            <ProductBox
            v-for="product in category.books"
            v-bind:key="product.id"
            v-bind:product="product"
            />
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
import ProductBox from '@/components/ProductBox'

export default{
    name: 'Category',
    data(){
        return{
            category: {
                
            }
        }
    },
    components: {
        ProductBox
    },
    mounted(){
        this.getCategory()
    },
    watch:{
        $route(to,from){
            if(to.name === 'category'){
                this.getCategory()
            }
        }
    },
    methods:{
        async getCategory(){
            this.$store.commit('setIsLoading',true)
            const cat_id = this.$route.params.category_id

            await axios.get(`/book/api/v1/category/${cat_id}/`)
            .then(response=>{
                this.category = response.data
                document.title = "Category " + this.category.name + " | BookStore"
            })
            .catch(error=>{
                console.log(error),
                toast({
                message:"something went wrong please try again later.",
                type:"is-danger",
                dismissible:true,
                pauseOnHover:true,
                duration:2000,
                position:'bottom-right',
                })
            })

            this.$store.commit('setIsLoading',false)

        }
    }
}
</script>