 <template>
  <v-card height="400" width="500">
    <v-img style="height: 400px" :src="Product.image" alt />
    <div>
      <h4>
        <router-link :to="{ name: 'Product', params: { id: Product.id } }">{{
          Product.title
        }}</router-link>
      </h4>
      <strong>${{ Product.price }}</strong>
      <p>{{ Product.description }}</p>
    </div>
    <div>
      <button @click="addToCart()">Add to Cart</button>
    </div>
  </v-card>
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
    },
  },
  methods: {
    addToCart() {
      this.$store.dispatch("addProductToCart", {
        Product: this.Product,
        quantity: 1,
      });
      console.log(this.$store.state.Product);
    },
  },
};
</script>

<style scoped>
v-img {
  height: 200px;
  width: 200px;
}
</style>