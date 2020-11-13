<template>
  <v-content>
    <Navbar />
    <MainPage />
    <ProductList />
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
</style>