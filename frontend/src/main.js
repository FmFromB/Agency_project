import Vue from 'vue'
import App from './App.vue'
import PortalVue from 'portal-vue'
import {BootstrapVue} from 'bootstrap-vue'
import { LayoutPlugin } from 'bootstrap-vue'
import VueRouter from 'vue-router'
import router from './router'
import store from './store'
import Vuelidate from 'vuelidate'
import firebase from "firebase/app"
import firebaseConfig from './config/firebase'

Vue.use(firebase)
Vue.use(VueRouter)
Vue.use(LayoutPlugin)
Vue.use(PortalVue)
Vue.use(BootstrapVue)
Vue.use(Vuelidate)

Vue.config.productionTip = false

firebase.initializeApp(firebaseConfig);

new Vue({
    render: h => h(App),
    store,
    router,
}).$mount('#app')
