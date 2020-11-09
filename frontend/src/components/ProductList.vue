<template>
  <v-img
    
    src="../assets/images/jean-estrella-_XOpGfUkjhs-unsplash.jpg"
    id="container"
  >
    <v-container class="my-5">
      <v-layout row wrap>
        <v-flex
          xs12
          sm6
          md4
          lg3
          v-for="product in products"
          :key="product.title"
        >
          <v-card elevation="5" color="#000814" class="text-xs-center ma-3">
            <v-responsive>
              <v-img height="250" :src="product.image"></v-img>
            </v-responsive>
            <v-card-text >
              <div id="card-text" class="subheading">{{ product.title }}</div>
              <div id="card-text">Price: ${{ product.price }}</div>
            </v-card-text>
            <v-card-actions>
              <v-btn elevation="1" color="#cca000">
                <v-icon left>mdi-cart-plus</v-icon>
                <span>add to cart</span>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-img>
</template>

<script>
import axios from "axios";

export default {
  name: "productlist",
  data() {
    return {
      products: [],
      catagory: '',
    };
  },
  created() {
    axios.get("http://127.0.0.1:8000/api/store/").then(response => {
      this.products = response.data;
    });
  },
  selectedCatagory(){
    this.catagory 
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#card-text {
  color: #f9f9f9;
}
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
