import Vue from 'vue'
import App from './App.vue'
import PortalVue from 'portal-vue'
import {BootstrapVue} from 'bootstrap-vue'
import { LayoutPlugin } from 'bootstrap-vue'
import VueRouter from 'vue-router'
import router from './router'
import store from './store'
import Vuelidate from 'vuelidate'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)
Vue.use(VueRouter)
Vue.use(LayoutPlugin)
Vue.use(PortalVue)
Vue.use(BootstrapVue)
Vue.use(Vuelidate)

Vue.config.productionTip = false


new Vue({
    render: h => h(App),
    store,
    router,
    axios
}).$mount('#app')
