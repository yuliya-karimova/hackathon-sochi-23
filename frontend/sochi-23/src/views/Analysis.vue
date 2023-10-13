<template>
  <div class="mx-auto max-w-screen-2xl p-8 flex flex-col gap-12">
    <!-- <Map /> -->
    <!-- <Plot /> -->
    <div class="flex w-full gap-6">
      <Card title="Екатеринбург" img="/ekaterinburg.jpg" class="flex-1" img-class="aspect-w-1 aspect-h-1" />
      <Card title="Тула" img="/tula.jpg" class="flex-1" img-class="aspect-w-1 aspect-h-1" />
      <Card title="Севастополь" img="/sevastopol.jpg" class="flex-1" img-class="aspect-w-1 aspect-h-1" />
    </div>
  </div>
</template>

<script setup lang="ts">
import Card from '../components/home/Card.vue';

// import Map from "../components/Map.vue";
// import Plot from "../components/Plot.vue";
</script>

