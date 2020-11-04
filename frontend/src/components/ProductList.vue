<template>
  <div>
    <v-container>
      <div v-if="products && products.length">
        <v-card
          max-width="374"
          v-for="product of products"
          v-bind:key="product.title"
        >
          <v-row wrap>
            <v-col xs12 md6>
              <v-img height="250" src=""> </v-img>
              <v-card-title>
                {{ product.title }}
              </v-card-title>
              <v-card-subtitle>
                {{ product.price }}
              </v-card-subtitle>
              <v-card-text>
                {{ product.description }}
              </v-card-text>
            </v-col>
          </v-row>
        </v-card>
      </div>
    </v-container>
    <!-- <h1>{{ product.title }}</h1> -->
  </div>
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
