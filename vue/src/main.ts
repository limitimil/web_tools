import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
// global use packages
import iview from 'iview';
import axios from 'axios';
import VueAxios from 'vue-axios';

Vue.config.productionTip = false;
Vue.use(iview);
axios.defaults.baseURL = 'http://localhost:5000/';
Vue.use(VueAxios, axios);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
