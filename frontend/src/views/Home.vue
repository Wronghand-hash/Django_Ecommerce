<template>
  <div id="main">
    <Navbar id="navbar" />
    <v-spacer></v-spacer>
    <v-content>
      <v-container>
      <component :class="{ 'animate__zoomIn' : ShowProducts}" class="animate__animated"  :is="component"></component>
      <div v-show="ShowProducts == false" id="switch">
        <v-btn
          class="animate__animated animate__jello animate__infinite"
          @click="component = 'ProductList' , ShowProducts = true"
          >View Products</v-btn
        >
      </div>
      </v-container>
      <!-- <MiniCart /> -->
      <!-- <Footer id="footer" /> -->
    </v-content>
  </div>
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
  data() {
    return {
      component: "MainPage",
      ShowProducts: false
    };
  },
};
</script>

<style scoped>
/* .home-background {
    filter: blur(1px);
  -webkit-filter: blur(1px);
  } */
#switch {
  position: absolute;
  left: 43%;
  bottom: -40%;
  z-index: 1;
}
#main {
  background-image: url("../assets/images/tabitha-turner--_bSa4Sn1Bs-unsplash.jpg");
  height: 100%;
  display: block;
  background-position: center;
  background-size: cover;
}
#dynamic {
  position: relative;
  top: 50%;
}
#footer {
  position: relative;
  bottom: 0;
}

</style>
