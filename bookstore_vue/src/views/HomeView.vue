<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6" >
      <div class="hero-body has-text-centered">
        <p class="title mb-6" >
          Welcome to BookStore
        </p>
        <p class="subtitle">
          the best online book store
        </p>
      </div>
    </section>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">latest products</h2>
      </div>
      <ProductBox
      v-for="product in latestProducts"
      v-bind:key="product.id"
      v-bind:product="product"
      />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import ProductBox from '@/components/ProductBox'
export default {
  name: 'HomeView',
  data(){
    return{
      latestProducts:[]
    }
  },
  components: {
    ProductBox
  },
  mounted(){
    this.getLatestProducts(),
    document.title = "Home | BookStore"
  },
  methods:{
    async getLatestProducts(){
      this.$store.commit('setIsLoading',true)

      await axios.get('/book/api/v1/book-list/')
      .then(response =>{
        this.latestProducts = response.data
        
      })
      .catch(error=>{
        console.log(error)
      })

      this.$store.commit('setIsLoading',false)
    }
  }
}
</script>

