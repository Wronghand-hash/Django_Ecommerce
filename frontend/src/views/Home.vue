<template>
  <div class="home">
    <div>
      <v-img class="home-background" max-height=900 src="@/assets/images/alex-shutin-kKvQJ6rK6S4-unsplash.jpg"></v-img>
      <!-- <v-img class="van-pic" absolute right max-height=700 max-width=400 src="@/assets/images/tyler-nix-6mze64HRU2Q-unsplash.jpg" ></v-img> -->
    </div>
    <div class="right-pic">
    </div>
    <div>
      <productlist></productlist>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import productlist from "@/components/ProductList.vue";

export default {
  name: "Home",
  components: {
    productlist
  }
};
</script>

<style scoped>
  
  .home-background {
    filter: blur(2px);
  -webkit-filter: blur(2px);
  }
</style>