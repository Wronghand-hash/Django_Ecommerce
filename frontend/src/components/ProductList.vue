<template>
  <v-container class="my-5">

    <v-layout row wrap>
      <v-flex xs12 sm6 md4 lg3 v-for="product in products" :key="product.title">
        <v-card class="text-xs-center ma-3">
          <v-responsive>
            <v-img height="250" :src="product.image"></v-img>
          </v-responsive>
          <v-card-text>
            <div class="subheading">{{product.title}}</div>
            <div>{{ product.price }}</div>
          </v-card-text>
          <v-card-actions>
            <v-btn flat>
              <v-icon left>mdi-cart</v-icon>
              <span>add to cart</span>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>

  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "productlist",
  data() {
    return {
      products: []
    };
  },
  created() {
    axios.get("http://127.0.0.1:8000/api/store/").then(response => {
      this.products = response.data;
    });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
