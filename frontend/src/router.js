import VueRouter from 'vue-router'
import Home from './components/Home'
import Offers from './components/Offers'
import Requirements from './components/Requirements'
import Registration from './components/Registration'
import Enterance from './components/Enterance'


export default new VueRouter({
	routes: [
		{
			path: '',
			component: Home
		},
		{
			path: '/Offers',
			component: Offers
		},
		{
			path: '/Requirements',
			component: Requirements
		},
		{
			path: '/Requirements',
			component: Requirements
		},
		{
			path: '/Registration',
			component: Registration
		},
		{
			path: '/Enterance',
			component: Enterance
		}
	],
	// Отключение хэша
	mode: 'history'
})