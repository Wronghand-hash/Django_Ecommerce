<template>
  <v-container class="my-5">
    <v-layout row wrap>
      <v-flex
        xs12
        sm6
        md4
        lg3
        v-for="product in products"
        :key="product.title"
        :product="product"
      >
        <v-hover v-slot="{ hover }">
          <v-card class="text-xs-center ma-3">
            <v-responsive>
              <v-img height="250" :src="product.image">
                <v-expand-transition>
                  <div
                    v-if="hover"
                    class="d-flex transition-fast-in-fast-out grey darken-2 v-card--reveal display-3 white--text"
                    style="height: 100%;"
                  >
                    {{ product.price }}
                  </div>
                </v-expand-transition>
              </v-img>
            </v-responsive>
            <v-card-text>
              <div
                class="font-weight-bold black--text text-sm-h6 text-capitalize"
              >
                {{ product.title }}
              </div>
              <div>{{ product.price }}</div>
            </v-card-text>
            <v-card-actions>
              <v-btn @click="addToCart">
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

export default {
  name: "productlist",
  
  props:["title"],
  data(){
    return {
      'productId': this.product.id
    }
  },
  
  mounted(){
    this.$store.dispatch('getProducts')
    this.$store.dispatch('getProduct' , this.productId);
  },
  computed: {
    products(){
      return this.$store.state.products;
    },
    product(){
      return this.$store.state.product;
    }
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
  methods:{
    addToCart(){
      this.$store.dispatch("addProductToCart", {
        product: this.product,
        quantity: 1
      })
      console.log(this.$store.state.cart);
    }
  }
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
