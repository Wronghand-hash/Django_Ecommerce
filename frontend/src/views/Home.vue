<template>
  <div class="home" color="#DFDFDF">
    <div>
      <v-img class="home-background" max-height=900 src="@/assets/images/tabitha-turner--_bSa4Sn1Bs-unsplash.jpg"></v-img>
      <!-- <v-img class="van-pic" absolute right max-height=700 max-width=400 src="@/assets/images/tyler-nix-6mze64HRU2Q-unsplash.jpg" ></v-img> -->
    </div>
    <div class="right-pic">
    </div>
    <div>
      <productlist></productlist>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
// @ is an alias to /src
import productlist from "@/components/ProductList.vue";
import Footer from "@/components/Footer.vue"

export default {
  name: "Home",
  components: {
    productlist,
    Footer
  }
};
</script>

<style scoped>
  
  /* .home-background {
    filter: blur(1px);
  -webkit-filter: blur(1px);
  } */
</style>