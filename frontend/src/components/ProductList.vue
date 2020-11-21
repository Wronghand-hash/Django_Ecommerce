
  <!-- <v-container>
    <v-row no-gutters >
      <v-col lg=4 cols=12>
        <ProductCard
         
          v-for="Product in Products"
          :key="Product.id"
          :Product="Product"
        />
      </v-col>
    </v-row>
  </v-container> -->

<template>
  <!-- <v-container class="grey lighten-5">
    <v-row>
      <v-col cols="2" sm="6" md="4" class="d-flex child-flex" lg="4">
        <ProductCard
          class="ma-5"
          v-for="Product in Products"
          :key="Product.id"
          :Product="Product"
        ></ProductCard>
      </v-col>
    </v-row>
  </v-container> -->

  <v-sheet>
    <v-slide-group v-model="model" center-active show-arrows>
      <ProductCard
        enter-active-class="animate__animated animate__fadeInDown"
        leave-active-class="animate__animated animate__fadeOutUp"
        class="ma-5"
        v-for="Product in Products"
        :key="Product.id"
        :Product="Product"
        v-slot="{ active, toggle }"
        :color="active ? 'primary' : 'grey lighten-1'"
        height="200"
        width="100"
        @click="toggle"
      ></ProductCard>
      <v-row class="fill-height" align="center" justify="center">
        <v-scale-transition>
          <v-icon
            v-if="active"
            color="black"
            size="48"
            v-text="'mdi-close-circle-outline'"
          ></v-icon>
        </v-scale-transition>
      </v-row>
    </v-slide-group>
  </v-sheet>
</template>
<script>
import ProductCard from "./ProductCard";

export default {
  name: "ProductList",
  components: {
    ProductCard,
  },

  props: ["Product"],

  mounted() {
    this.$store.dispatch("getProducts");
  },
  computed: {
    Products() {
      return this.$store.state.Products;
    },
  },

  // created() {
  //   axios.get("http://127.0.0.1:8000/api/store/" , {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`} })
  //   .then(response => {
  //     this.$store.state.APIData = response.data;
  //   })
  //   .catch(err => {
  //     console.log(err);
  //   })
  // },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
v-container {
  position: relative;
  right: 10%;
}
</style>
