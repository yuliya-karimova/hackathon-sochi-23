<template>
  <div class="relative">
    <iframe
      :src="src"
      :width="width || '100%'"
      :height="height || '500'"
      frameborder="0"
    >
    </iframe>
    <div class="absolute bottom-0 w-full h-5 bg-white"></div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  src: string;
  height?: string;
  width?: string;
  hideBottom?: boolean;
}

withDefaults(defineProps<Props>(), {
  hideBottom: true
});
</script>

