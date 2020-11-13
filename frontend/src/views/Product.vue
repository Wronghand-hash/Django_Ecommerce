<template> 
  <div class="row mt-5" v-if="Product">
    <div class="col-4">
      <img :src="Product.image" class="w-100" />
    </div>
    <div class="col-8">
      <h1>{{ Product.title }}</h1>
      <h3>${{ Product.price }}</h3>

      <input type="text" v-model.number="quantity" class="text-center col-1 mr-2 p-1" />
      <button class="btn btn-primary" @click="addToCart()">Add to Cart</button>

      <p class="mt-4">{{ Product.description }}</p>
    </div>
  </div>
</template>


<script>
export default {
    props:["id"],

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