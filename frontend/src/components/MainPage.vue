<template>
  <v-content class="pa-0 ma-0">
    <div>
      <h1 class="acapulco animate__animated animate__tada animate__delay-0.5s">
        Acapulco Design
      </h1>
      <h2 class="h2-home animate__animated animate__bounceInUp animate__delay-1s">Limited custom handmade merchendise by</h2>
    </div>

    <v-img
      class="home-background"
      max-height="900"
      src="@/assets/images/tabitha-turner--_bSa4Sn1Bs-unsplash.jpg"
    ></v-img>
    <!-- <div class="">
      <h1 class="acapulco text-center"></h1>
    </div> -->
  </v-content>
</template>
 
<script>
import { KinesisContainer, KinesisElement } from "vue-kinesis";
import Vue from "vue";

Vue.component("kinesis-container", KinesisContainer);
Vue.component("kinesis-element", KinesisElement);
export default {};
</script>


<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Sail&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Sahitya&display=swap");

.home-background {
  filter: blur(2px);
  -webkit-filter: blur(2px);
}

.acapulco {
  font-family: sail;
  z-index: 1;
  font-size: 150px;
  /* backdrop-filter: blur(4px); */
  color: #e7e7de;
  position: absolute;
  top: 30%;
  left: 10%;
  transform: translate(-50%, -50%);
  text-align: center;
  line-height: 90%;
}

.h2-home {
  font-size: 3.5rem;
  z-index: 1;
  font-family: "Sahitya", serif;
  position: absolute;
  width: 764px;
  text-align: center;
  top: 50%;
  left: 23%;
  transform: translate(-50%, -50%);
  color: #e7e7de;
  line-height: 110%;
}
</style>