<template>
  <div class="rounded-2xl p-3 md:p-8" :class="cardClass || 'bg-gray-200'">
    <div class="text-xs text-center md:text-2xl uppercase font-bold pb-2">{{ title }}</div>
    <div v-if="description" class="font-light pb-2">{{ description }}</div>
    <div
      :style="`background-image: url('${img}'); background-size: cover; background-position: center;`"
      class="rounded-xl md:mt-4"
      :class="imgClass ||'h-44'"
    />
  </div>
</template>

<script setup lang="ts">
interface Props {
  title: string;
  description?: string;
  img: string;
  imgClass?: string;
  cardClass?: string
}

defineProps<Props>();
</script>
