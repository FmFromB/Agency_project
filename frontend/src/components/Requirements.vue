<template>
  <div class="requirements">
    <div class="offers_text">
      <h1>запросы</h1>
    </div>
    <b-card-group deck="">
      <b-card img-src="floor.png" img-alt="Image" img-top="">
        <router-link class="a" tag="b-card-title" :to="'/NewReqFlats'">Квартиры</router-link>
      </b-card>
      <b-card img-src="house.png" img-alt="Image" img-top="">
        <router-link class="a" tag="b-card-title" :to="'/NewReqHouses'">Дома</router-link>
      </b-card>
      <b-card img-src="ground.png" img-alt="Image" img-top="">
        <router-link class="a" tag="b-card-title" :to="'/NewReqLands'">Земли</router-link>
      </b-card>
    </b-card-group>
    <div>
      <router-link class="offer_button" tag="b-button" :to="'/RegistrateReq'">Оставить запрос</router-link>
    </div>
  </div>
</template>

<script>
 export default{
 
 }
</script>