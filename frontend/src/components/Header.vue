<template>
  <div class="mx-auto max-w-screen-2xl p-8">
    <div class=max-w-max>
      <router-link
        to="/home"
        class="text-3xl md:text-3xl text-cyan-900 cursor-pointer hover:opacity-90 uppercase flex flex-col gap-2"
      >
        <div>←</div>
        <div>назад на главную</div>
      </router-link>
    </div>
  </div>
  <!-- <div class="bg-cyan-950">
    <div class="mx-auto max-w-screen-2xl p-8 flex items-center gap-20 text-xl font-light">
      <router-link to="/home">
        <img src="/logo_white.svg" class="w-32 h-32" alt="logo" />
      </router-link>
      <router-link to="/home" v-slot="{ isActive }">
        <span :class="isActive ? '' : 'opacity-80'" class="text-white hover:opacity-100 transition duration-150 uppercase">
          Домой
        </span>
      </router-link>
      <router-link to="/analysis" v-slot="{ isActive }">
        <span :class="isActive ? '' : 'opacity-80'" class="text-white hover:opacity-100 transition duration-150 uppercase">
          Анализ
        </span>
      </router-link>
      <router-link to="/compare" v-slot="{ isActive }">
        <span :class="isActive ? '' : 'opacity-80'" class="text-white hover:opacity-100 transition duration-150 uppercase">
          Сравнение
        </span>
      </router-link>
    </div>
  </div> -->
</template>
