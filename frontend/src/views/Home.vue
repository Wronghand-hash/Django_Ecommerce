<template>
  <div class="home">
    <div>
      <!-- <v-toolbar class="d-flex " dense color="lime lighten-1">
        <v-btn class="indigo darken-2 white--text my-4">
          Login
        </v-btn>
        <v-btn class="indigo darken-2 white--text">
          Signup
        </v-btn>
        <v-btn class="indigo darken-2 white--text">
          About
        </v-btn>
        <v-btn class="indigo darken-2 white--text">
          Shop
        </v-btn>
      </v-toolbar> -->
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
