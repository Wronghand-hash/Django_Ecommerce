<template> 
  <ProductCard></ProductCard>
</template>


<script>
import ProductCard from "../components/ProductCard"
export default {
    props:["id"],
    components:{ProductCard},

    computed:{
        Product(){
            return this.$store.state.Prodcut;
        }
    },
    
    mounted(){
        this.$store.dispatch('getProduct', this.id)
    }
}
</script>