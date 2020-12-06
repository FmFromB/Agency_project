<template>
  <div class="slider">
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      controls=""
      indicators=""
      background="#ababab"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=52">
        <h1>Text</h1>
      </b-carousel-slide>
      <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=54">
        <h1>Text</h1>
      </b-carousel-slide>
      <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=58">
        <h1>Text</h1>
      </b-carousel-slide>
      <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=60">
        <h1>Text</h1>
      </b-carousel-slide>
    </b-carousel>
  </div>
</template>

<script>
  
</script>