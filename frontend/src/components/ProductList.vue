<template>
  <div>
    <div v-if="products && products.length">
      <div v-for="product of products" v-bind:key="product.title">
        <h1>{{ product.title }}</h1>
      </div>
    </div>
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
    },
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
