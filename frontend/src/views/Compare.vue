<template>
  <div>
    <Header />

    <div
      class="mx-auto max-w-screen-2xl px-8 md:pt-4 pb-8"
    >
      <div class="hidden 2xl:grid 2xl:grid-cols-2 gap-20">
        <CitiesBlock />
        <CitiesBlock />
      </div>
      <div class="2xl:hidden">
        Пожалуйста, пользуйтесь этой страницей только на больших экранах (больше 1500)
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import CitiesBlock from "../components/CitiesBlock.vue";
import Header from "../components/Header.vue";
</script>
