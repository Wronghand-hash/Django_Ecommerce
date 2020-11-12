import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";

Vue.config.productionTip = false;

// router.beforeEach((to, from, next) => {
//   if (to.matched.some((record) => record.meta.requiresLogin)) {
//     if (!store.getters.loggedIn) {
//       next({ name: "login" });
//     } else {
//       next();
//     }
//   } else {
//     next();
//   }
// });

new Vue({
  router,
  vuetify,
  store,
  render: (h) => h(App),
}).$mount("#app");
