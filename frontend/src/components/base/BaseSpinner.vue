<template>
  <svg
    :class="[sizes[props.size], props.animate && 'animate-spin']"
    viewBox="0 0 24 24"
    fill="none"
    @animationiteration="emit('animation-iteration')"
  >
    <circle
      class="opacity-25"
      cx="12"
      cy="12"
      r="10"
      stroke="currentColor"
      stroke-width="4"
    />
    <path
      class="opacity-75"
      fill="currentColor"
      d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
    />
  </svg>
</template>

<script setup lang="ts">
const sizes = {
  xs: 'h-4 w-4',
  sm: 'h-5 w-5',
  md: 'h-6 w-6',
  lg: 'h-8 w-8',
  xl: 'h-10 w-10',
  none: '',
}
interface Props {
  size?: keyof typeof sizes
  animate?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  size: 'md',
  animate: true,
})
const emit = defineEmits<{
  (e: 'animation-iteration'): void
}>()
</script>
