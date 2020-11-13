<template>
  <v-container>
    <v-card>
    <div >
      <div >
        <v-img :src="Product.image" alt />
        <div>
          <h4>
            <router-link
              :to="{ name: 'product', params: { id: Product.id } }"
              >{{ Product.title }}</router-link
            >
          </h4>
          <strong>${{ Product.price }}</strong>
          <p>{{ Product.description }}</p>
        </div>
        <div>
          <button @click="addToCart()">
            Add to Cart
          </button>
        </div>
      </div>
    </div>
    </v-card>
  </v-container>
</template>



<script>

export default {
  props: ["Product"],
  
  mounted() {
    this.$store.dispatch("getProduct", this.id);
  },
  computed: {
    product() {
      return this.$store.state.Product;
    }
  },
  methods: {
    addToCart() {
      this.$store.dispatch("addProductToCart", {
        Product: this.Product,
        quantity: 1
      });
      console.log(this.$store.state.Product);
    }
  }
};
</script>