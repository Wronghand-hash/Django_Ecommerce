 <template>
  <v-hover v-slot="{ hover }">
    <v-card height="400" width="500">
      <v-expand-transition>
        <div
          v-if="hover"
          class="d-flex transition-fast-in-fast-out green darken-2 v-card--reveal display-1 white--text"
          style="height: 100%"
        >
          <div>
          </div>
          <v-btn @click="addToCart()">Add to Cart</v-btn>
        </div>
      </v-expand-transition>
      <v-img style="height: 400px" :src="Product.image" alt />

      <div>
        <h4>
          <router-link :to="{ name: 'Product', params: { id: Product.id } }">{{
            Product.title
          }}</router-link>
        </h4>
      </div>
      <div>
        
      </div>
    </v-card>
  </v-hover>
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

v-btn{
  position: relative;
  left: 50%;
  top: 50%;
}
</style>