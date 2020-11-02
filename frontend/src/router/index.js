import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import productlist from "../components/ProductList.vue"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/productslist",
    name: "productlist",
    component: productlist
  }
];

const router = new VueRouter({
  routes
});

export default router;
