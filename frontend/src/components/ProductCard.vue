 <template>
  <!-- <v-hover v-slot="{ hover }"> -->
  <!-- <v-card height="400" width="500">
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
    </v-card> -->
  <v-card color="#03045e" class="mx-5" max-width="500">
    <v-img :src="Product.image" height="300px" width="400px"></v-img>

    <v-card-title>
      <h3 class="white--text">
      {{ Product.title }}
      </h3>
    </v-card-title>

    <v-card-subtitle class="white--text">
      {{ Product.price }}
    </v-card-subtitle>

    <v-card-actions>
      <v-btn color="#fcf876" text> Detail </v-btn>

      <v-spacer></v-spacer>

      <v-btn color="#fcf876" icon @click="show = !show">
        <v-icon>{{ show ? "mdi-chevron-up" : "mdi-chevron-down" }}</v-icon>
      </v-btn>
      <v-btn color="#fcf876" @click="addToCart()">Add to Cart</v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text class="white--text">
          {{Product.description}}
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
  <!-- </v-hover> -->
</template>



<script>
export default {
  props: ["Product"],

  data(){
    return{
      show: false
    }
  },

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

v-btn {
  position: relative;
  left: 50%;
  top: 50%;
}
v-card{
  border: 1px solid yellow;
}
</style>