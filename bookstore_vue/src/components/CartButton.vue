<template>
    <router-link to="/cart" class="button is-success">
        <span class="icon"><i class="fas fa-shopping-cart"></i></span>
        <span>Cart ({{ totalCartLength }})</span>
    </router-link>
<template/>


<script>
export default{
    name:'CartButton',
    data(){
        return{
            cart:{
                items:[],
            },
        }
    },
    mounted(){
        this.cart = this.$store.state.cart
    },
    computed:{
        totalCartLength:{
            get(){
                let totalLength = 0
                for (let i = 0; i < this.cart.items.length; i++) {
                    totalLength += this.cart.items[i].quantity;        
                }
                return totalLength
            },
            set(value){
                this.cart.items = []
            }
        let totaotalLength
        },
    },
    methods:{
        recomputedTotalCartLength(){
            
        }
    }
}
</script>