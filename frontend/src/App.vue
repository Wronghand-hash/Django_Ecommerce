<template>
  <v-app class="grey lighten-4">
    <Navbar />
    <v-main>
      <!-- <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link> -->
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
// import HelloWorld from "./components/HelloWorld";
import Navbar from "./components/Navbar";

export default {
  name: "App",

  components: {
    Navbar
  },

  data: () => ({
    //
  })
};
</script>
