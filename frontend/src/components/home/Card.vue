<template>
  <div class="bg-gray-100 rounded-2xl p-8">
    <div class="text-2xl uppercase font-bold pb-2">{{ title }}</div>
    <div v-if="description" class="font-light pb-2">{{ description }}</div>
    <div
      :style="`background-image: url('${img}'); background-size: cover; background-position: center;`"
      class="rounded-xl mt-4"
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
}

defineProps<Props>();
</script>
