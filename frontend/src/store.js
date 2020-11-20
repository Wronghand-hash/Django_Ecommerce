 import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);
export default new Vuex.Store({ 
  state: {
    accessToken: null,
    refreshToken: null,
    Products: [],
    Product: null,
    Cart: [], 
  },
  mutations: {
    setProducts(state, Products){
      state.Products = Products;
    },
    setProduct(state, Product){
      state.Product = Product;
    },
    updateStorage(state, { access, refresh }) {
      state.accessToken = access;
      state.refreshToken = refresh;
    },
    destroyToken(state){
      state.accessToken = null
      state.refreshToken = null
    },
    AddToCart(state, {Product, quantity}){

      let productInCart = state.Cart.find(item =>{
        return item.Product.id == Product.id
      })

      if(productInCart){
        productInCart.quantity += quantity
        return;
      }

      state.Cart.push({
        Product,
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
      axios.get("http://127.0.0.1:8000/api/store/")
      .then(response => {
        commit('setProducts', response.data)
      })
    },
    addProductToCart({commit}, {Product , quantity}){
      commit('AddToCart', {Product, quantity})
    },
    getProduct({commit}, ProductId){
      axios.get(`http://127.0.0.1/api/store/${ProductId}/`)
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
  getters:{
    cartItemCount(state){
      return state.Cart.length
    },
    cartTotal(state){
      let total = 0;

      state.Cart.forEach(item => {
        total += item.Product.price * item.quantity
      });
      return total
    }
  }
})
