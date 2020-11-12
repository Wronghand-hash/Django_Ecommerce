import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

const getAPI = axios.create({
  baseURL: "http://127.0.0.1:8000",
  timeout: 1000,
});

Vue.use(Vuex);
export default new Vuex.Store({
  state: {
    accessToken: null,
    refreshToken: null,
    products: [],
    product: null,
    cart: [], 
  },
  mutations: {
    setProducts(state, products){
      state.products = products;
    },
    setProduct(state, product){
      state.product = product;
    },
    updateStorage(state, { access, refresh }) {
      state.accessToken = access;
      state.refreshToken = refresh;
    },
    destroyToken(state){
      state.accessToken = null
      state.refreshToken = null
    },
    AddToCart(state, {product, quantity}){
      state.cart.push({
        product,
        quantity
      })
    }
  },
  // getters: {
  //   loggedIn(state) {
  //     return state.accessToken != null;
  //   },
  // },
  actions: {
    getProducts({commit}){
      getAPI.get("/api/store/")
      .then(response => {
        commit('setProducts', response.data)
      })
    },
    addProductToCart({commit}, {product , quantity}){
      commit('AddToCart', {product, quantity})
    },
    getProduct({commit}, productId){
      getAPI.get(`/api/store/${productId}/`)
      .then(response => {
        commit('setProduct', response.data)
      })
    }
    // userLogout(context){
    //   if(context.getters.loggedIn){
    //     context.commit('destroyToken')
    //   }
    // },
    // userLogin(context, usercredentials) {
    //   return new Promise((resolve) => {
    //     getAPI
    //       .post("/api/token/", {
    //         username: usercredentials.username,
    //         password: usercredentials.password,
    //       })
    //       .then((response) => {
    //         context.commit("updateStorage", {
    //           access: response.data.access,
    //           refresh: response.data.refresh,
    //         });
    //         resolve();
    //       });
    //   });
    // },
  },
});
