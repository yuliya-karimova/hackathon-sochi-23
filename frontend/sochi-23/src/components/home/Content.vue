<template>
  <div class="flex gap-12 items-center" :class="textAlign === 'right' && 'flex-row-reverse'">
    <div class="w-1/2">
      <div class="text-2xl uppercase font-bold pb-2">{{ title }}</div>
      <div class="pb-6 font-light">{{ description }}</div>
    </div>
    <div class="w-1/2">
      <div
        class="aspect-w-1 aspect-h-1 rounded-2xl"
        :style="`background-image: url('${img}'); background-size: cover; background-position: center;`"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  title: string;
  description: string;
  img: string;
  textAlign: "left" | "right";
}

defineProps<Props>();
</script>
