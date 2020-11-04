<template>
  <div class="home">
    <div>
      <v-img max-height=900 src="@/assets/images/jean-estrella-_XOpGfUkjhs-unsplash.jpg"></v-img>
      <!-- <v-img class="van-pic" absolute right max-height=700 max-width=400 src="@/assets/images/tyler-nix-6mze64HRU2Q-unsplash.jpg" ></v-img> -->
    </div>
    <div class="right-pic">
    </div>
    <div>
      <productlist></productlist>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import productlist from "@/components/ProductList.vue";

export default {
  name: "Home",
  components: {
    productlist
  }
};
</script>

<style scoped>
  .van-pic {
    position: absolute;
  }
</style>