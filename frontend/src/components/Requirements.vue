<template>
  <div class="requirements">
    <div class="offers_text">
      <h1>запросы</h1>
    </div>
    <b-card-group deck="">
        <b-card img-src="floor.png" img-alt="Image" img-top="">
            <router-link class="a" tag="b-card-title" :to="'/NewReqFlats'">Квартиры</router-link>
            <router-link class="a" tag="b-button-light" :to="'/AddNewReqFlat'">Добавить запрос</router-link>
        </b-card>
      <b-card img-src="house.png" img-alt="Image" img-top="">
          <router-link class="a" tag="b-card-title" :to="'/NewReqHouses'">Дома</router-link>
          <router-link class="a" tag="b-button-light" :to="'/AddNewReqHouse'">Добавить запрос</router-link>
      </b-card>
      <b-card img-src="ground.png" img-alt="Image" img-top="">
          <router-link class="a" tag="b-card-title" :to="'/NewReqLands'">Земли</router-link>
          <router-link class="a" tag="b-button-light" :to="'/AddNewReqLand'">Добавить запрос</router-link>
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
 export default{
 
 }
</script>