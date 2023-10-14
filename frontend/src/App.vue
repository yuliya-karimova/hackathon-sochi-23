<template>
  <div>
    <router-view />
    <Footer />
    <button
      class="bg-amber-500 text-cyan-950 font-bold rounded-full fixed bottom-10 right-10 h-14 w-14 text-4xl flex items-center justify-center pb-1 hover:pb-3 duration-150"
      @click="scrollToTop"
    >
      <div>🠕</div>
    </button>
  </div>
</template>

<script setup lang="ts">
import Footer from "./components/Footer.vue";

const scrollToTop = () => {
  scroll({
    top: 0,
    behavior: "smooth",
  });
};
</script>
