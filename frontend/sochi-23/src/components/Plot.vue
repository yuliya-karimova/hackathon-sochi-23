<template>
    <!-- <iframe src="/shap_plot.html" width="100%" height="500" frameborder="0"></iframe> -->
    <div class="relative">
      <iframe src="./map_with_features.html" width="100%" height="500" frameborder="0">
      </iframe>
      <div class="absolute bottom-0 w-full h-5 bg-white"></div>
    </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';

onMounted(() => {
  // Ваш код для инициализации графика
});
</script>

<style>
.leaflet-control-attribution {
  display: none;
}
</style>