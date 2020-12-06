import Vue from 'vue'
import App from './App.vue'
import PortalVue from 'portal-vue'
import {BootstrapVue} from 'bootstrap-vue'
import { LayoutPlugin } from 'bootstrap-vue'
import VueRouter from 'vue-router'
import router from './router'
import Vuelidate from 'vuelidate'

Vue.use(VueRouter)
Vue.use(LayoutPlugin)
Vue.use(PortalVue)
Vue.use(BootstrapVue)
Vue.use(Vuelidate)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
