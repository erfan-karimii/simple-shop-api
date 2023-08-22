<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <strong>BookStore</strong>
        </router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu=!showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active':showMobileMenu}">
        <div class="navbar-start">
          <div class="navbar-item">
            <form action="/search" method="get">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="what are you looking for?" name="query">
                </div>
                <div class="control">
                  <button  class="button is-success">
                    <span class="icon">
                      <i class="fas fa-search"></i>
                    </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
        <div class="navbar-end">
          <router-link 
          v-for="category in categories"
          :key="category.id"  
          :to = "`/category/${category.id}`" 
          class="navbar-item">
          {{ category.name }}
        </router-link>
          <div class="navbar-item">
            <div class="buttons">
              <template v-if="this.$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-light">My Account</router-link>
              </template>
              <template v-else>
                <router-link to="/log-in" class="button is-light">Log in</router-link>
              </template>
              <CartButton/>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading':$store.state.isLoading}">
      <div class="lds-dual-ring"></div>
    </div>
    <section class="section">
      <router-view/>

    </section>
    <footer class="footer">
      <!-- how use variabale or some calculations to write this year not static 2023? -->
      <p class="has-text-centered">Copy Right (c) 2023</p>
    </footer>
  </div>
</template>

<script>
import axios from "axios";
import CartButton from "@/components/CartButton.vue"

export default {
  data(){
    return{
      showMobileMenu:false,
      cart:{
        items:[],
      },
      categories:[],
    }
  },
  beforeCreate(){
    this.$store.commit('initializeStore')

    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common['Authorization'] = "Bearer " + token
    }else{
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  components:{
    CartButton
  },
  mounted(){
    this.cart = this.$store.state.cart
    this.getNavBar()
  },
  methods:{
    getNavBar(){  
        axios.get(`/book/api/v1/category/`)
        .then(response=>{
            this.categories = response.data
        })
        .catch(error=>{
            console.log(error)
        })
    },
  },

}
</script>

<style lang="scss">
@import '../node_modules/bulma';

.lds-dual-ring{
  display: inline-block;
  width: 80px;
  height: 80px;
}

.lds-dual-ring:after{
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;

}

@keyframes lds-dual-ring {
  0%{
    transform: rotate(0deg);
  }
  100%{
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3;
  &.is-loading{
    height: 80px;
  }
}

</style>
