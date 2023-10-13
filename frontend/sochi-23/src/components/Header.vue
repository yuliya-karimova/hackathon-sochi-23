<template>
  <div class="bg-cyan-600">
    <div class="mx-auto max-w-screen-2xl p-8 flex items-center gap-20 text-xl font-light">
      <router-link to="/">
        <img src="/logo_white.svg" class="w-32 h-32" alt="logo" />
      </router-link>
      <router-link to="/analysis" v-slot="{ isActive }">
        <span :class="isActive ? '' : 'opacity-80'" class="text-white hover:opacity-100 transition duration-150 uppercase">
          Проанализировать населенный пункт
        </span>
      </router-link>
      <router-link to="/compare" v-slot="{ isActive }">
        <span :class="isActive ? '' : 'opacity-80'" class="text-white hover:opacity-100 transition duration-150 uppercase">
          Сравнить населенные пункты
        </span>
      </router-link>
    </div>
  </div>
</template>
