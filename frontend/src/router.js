import VueRouter from 'vue-router'
import Home from './components/Home'
import Offers from './components/Offers'
import Requirements from './components/Requirements'
import Registration from './components/Registration'
import Enterance from './components/Enterance'
import NewOffersFlats from './components/NewOffersFlats'
import NewOffersHouses from './components/NewOffersHouses'
import NewOffersLands from './components/NewOffersLands'
import NewReqFlats from './components/NewReqFlats'
import NewReqHouses from './components/NewReqHouses'
import NewReqLands from './components/NewReqLands'
import RegistrateOffer from './components/RegistrateOffer'
import RegistrateReq from './components/RegistrateReq'

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
		},
		{
			path: '/NewOffersFlats',
			component: NewOffersFlats
		},
		{
			path: '/NewOffersHouses',
			component: NewOffersHouses
		},
		{
			path: '/NewOffersLands',
			component: NewOffersLands
		},
		{
			path: '/NewReqFlats',
			component: NewReqFlats
		},
		{
			path: '/NewReqHouses',
			component: NewReqHouses
		},
		{
			path: '/NewReqLands',
			component: NewReqLands
		},
		{
			path: '/RegistrateOffer',
			component: RegistrateOffer
		},
		{
			path: '/RegistrateReq',
			component: RegistrateReq
		}
	],
	// Удаление хэша
	mode: 'history'
})