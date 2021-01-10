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
import AddNewOffersLands from './components/AddNewOffersLands'
import AddNewOfferHouse from './components/AddNewOfferHouse'
import AddNewOfferFlat from './components/AddNewOfferFlat'
import AddNewReqFlat from './components/AddNewReqFlat'
import AddNewReqLand from './components/AddNewReqLand'
import AddNewReqHouse from './components/AddNewReqHouse'

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
			path: '/AddNewOffersLands',
			component: AddNewOffersLands
		},
		{
			path: '/AddNewOfferHouse',
			component: AddNewOfferHouse
		},
		{
			path: '/AddNewOfferFlat',
			component: AddNewOfferFlat
		},
		{
			path: '/AddNewReqFlat',
			component: AddNewReqFlat
		},
		{
			path: '/AddNewReqLand',
			component: AddNewReqLand
		},
		{
			path: '/AddNewReqHouse',
			component: AddNewReqHouse
		}
	],
	// Удаление хэша
	mode: 'history'
})