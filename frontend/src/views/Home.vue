<template>
  <div class="home pa-0" color="#DFDFDF">
    <Navbar />
    <MainPage />
    <ProductList />
    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";
import MainPage from "@/components/MainPage.vue"
import ProductList from "@/components/ProductList.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "Home",
  components: {
    Navbar,
    MainPage,
    ProductList,
    Footer
  }
};
</script>

<style scoped>


.p-home {
  position: absolute;
  font-style: normal;
  font-weight: normal;
  font-size: 60px;
  color: #ffffff;
}

.home-background {
  height: 100%;
}
</style>