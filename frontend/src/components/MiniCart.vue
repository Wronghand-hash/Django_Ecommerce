<template>
  <v-container>
    <v-card color="grey">
      <v-card-title>Shopping Cart</v-card-title>
      <v-card-title>total:{{cartItemCount }}</v-card-title>
      <v-card-text>
        <div v-for="item in Cart" :key="item.Product.id">
          <div>
            <strong>{{ item.Product.title }}</strong>
            <br />
            {{ item.quantity }} x ${{ item.Product.price }}
          </div>
        </div>
      </v-card-text>
      <v-spacer></v-spacer>
      <v-card-action>
          <div class="subheading">Total Price: ${{ cartTotal}}</div>
      </v-card-action>
    </v-card>
  </v-container>
</template>

<script>
export default {
  computed: {
    Cart() {
      return this.$store.state.Cart;
    },
    cartItemCount(){
        return this.$store.getters.cartItemCount;
    },
    cartTotal(){
        return this.$store.getters.cartTotal
    }
  },
};
</script>