<template>

  <v-container class="my-5">

    <v-layout row wrap>
      <v-flex xs12 sm6 md4 lg3 v-for="product in products" :key="product.title">
        <v-hover v-slot="{ hover }">
        <v-card class="text-xs-center ma-3">
          <v-responsive>
            <v-img height="250" :src="product.image">
              <v-expand-transition>
                <div v-if="hover"
                 class="d-flex transition-fast-in-fast-out grey darken-2 v-card--reveal display-3 white--text"
                  style="height: 100%;">
                  {{ product.price }}
                </div>
              </v-expand-transition>            
            </v-img>
          </v-responsive>
          <v-card-text>
            <div class="font-weight-bold black--text text-sm-h6 text-capitalize">{{product.title}}</div>
            <div>{{ product.price }}</div>
          </v-card-text>
          <v-card-actions>
            <v-btn flat>
              <v-icon left>mdi-cart</v-icon>
              <span>add to cart</span>
            </v-btn>
          </v-card-actions>
        </v-card>
        </v-hover>
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

.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: .7;
  position: absolute;
  width: 100%;
}

</style>
