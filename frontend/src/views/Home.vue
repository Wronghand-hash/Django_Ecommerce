<template>
  <v-content>
    <Navbar />
    <MainPage />
    <div id="scroll">
      <v-btn class="animate__animated animate__jello animate__infinite" v-scroll-to="'#productlist'">View Products</v-btn>
    </div>
    <ProductList id="productlist" />
    <MiniCart />
    <Footer />
  </v-content>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";
import MainPage from "@/components/MainPage.vue";
import ProductList from "@/components/ProductList.vue";
import Footer from "@/components/Footer.vue";
import MiniCart from "../components/MiniCart.vue";

export default {
  name: "Home",
  components: {
    Navbar,
    MainPage,
    ProductList,
    Footer,
    MiniCart,
  },
};
</script>

<style scoped>
/* .home-background {
    filter: blur(1px);
  -webkit-filter: blur(1px);
  } */
  #scroll{
    position: relative;
    left: 43%;
    bottom: 10%;
    z-index: 1;
  }
</style>
