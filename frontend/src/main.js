import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import store from "./store"
import VueKinesis from 'vue-kinesis'
import 'animate.css'




Vue.config.productionTip = false;

Vue.use(VueKinesis)

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount("#app");
