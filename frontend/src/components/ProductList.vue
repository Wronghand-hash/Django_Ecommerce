<template> 
  <v-container class="my-5">
    <v-layout row wrap>
      <v-flex xs12 sm6 md4 lg3>
        <ProductCard
          v-for="Product in Products"
          :key="Product.id"
          :Product="Product"
        />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import ProductCard from "./ProductCard"; 

export default {
  name: "ProductList",
  components: {
    ProductCard
  },

  props: ["Product"],

  mounted() {
    this.$store.dispatch("getProducts");
  },
  computed: {
    Products() {
      return this.$store.state.Products;
    }
  }

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
.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: 0.7;
  position: absolute;
  width: 100%;
}
</style>
