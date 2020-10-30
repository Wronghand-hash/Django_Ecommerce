<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
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
