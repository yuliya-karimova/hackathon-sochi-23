<template>
  <div>
    <Header />
    <div class="mx-auto max-w-screen-2xl p-8 flex flex-col gap-12">
      <!-- <Map /> -->
      <!-- <Plot /> -->
      <div class="flex w-full gap-6">
        <button class="flex-1" @click="currentCity = City.Yekaterinburg">
          <Card
            title="Екатеринбург"
            img="./yekaterinburg.jpg"
            img-class="aspect-w-1 aspect-h-1"
          />
        </button>
        <button class="flex-1" @click="currentCity = City.Tula">
          <Card
            title="Тула"
            img="./tula.jpg"
            img-class="aspect-w-1 aspect-h-1"
          />
        </button>
        <button class="flex-1" @click="currentCity = City.Sevastopol">
          <Card
            title="Севастополь"
            img="./sevastopol.jpg"
            img-class="aspect-w-1 aspect-h-1"
          />
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// import Plot from '../components/Plot.vue';
import { ref } from "vue";
import Card from "../components/Card.vue";
import Header from "../components/Header.vue";

enum City {
  Yekaterinburg,
  Tula,
  Sevastopol,
}

const currentCity = ref(City.Yekaterinburg);

// import Map from "../components/Map.vue";
</script>
