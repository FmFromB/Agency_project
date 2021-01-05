<template>
  <div class="offers">
    <div class="offers_text">
      <h1>предложения</h1>
    </div>
    <b-card-group deck="">
      <b-card img-src="floor.png" img-alt="Image" img-top="">
        <router-link class="a" tag="b-card-title" :to="'/NewOffersFlats'">Квартиры</router-link>
      </b-card>
      <b-card img-src="house.png" img-alt="Image" img-top="">
        <router-link class="a" tag="b-card-title" :to="'/NewOffersHouses'">Дома</router-link>
      </b-card>
      <b-card img-src="ground.png" img-alt="Image" img-top="">
        <router-link class="a" tag="b-card-title" :to="'/NewOffersLands'">Земли</router-link>
      </b-card>
    </b-card-group>
    <div>
      <router-link class="offer_button" tag="b-button" :to="'/RegistrateOffer'">Оставить предложение</router-link>
    </div>
  </div>
</template>

<script>
 export default{
 
 }
</script>