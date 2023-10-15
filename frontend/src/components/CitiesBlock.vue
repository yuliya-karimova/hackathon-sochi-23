<template>
  <div class="flex flex-col gap-12">
    <div class="grid grid-cols-3 w-full gap-3 md:gap-6">
      <button @click="onSelectCity(MainCities.Yekaterinburg)">
        <Card
          title="Екатеринбург"
          img="./yekaterinburg.jpg"
          img-class="aspect-w-1 aspect-h-1"
          :cardClass="
            currentCityId === MainCities.Yekaterinburg
              ? 'bg-cyan-600 bg-opacity-30'
              : ''
          "
        />
      </button>
      <button @click="onSelectCity(MainCities.Tula)">
        <Card
          title="Тула"
          img="./tula.jpg"
          img-class="aspect-w-1 aspect-h-1"
          :cardClass="
            currentCityId === MainCities.Tula ? 'bg-cyan-600 bg-opacity-30' : ''
          "
        />
      </button>
      <button @click="onSelectCity(MainCities.Sevastopol)">
        <Card
          title="Севастополь"
          img="./sevastopol.jpg"
          img-class="aspect-w-1 aspect-h-1"
          :cardClass="
            currentCityId === MainCities.Sevastopol
              ? 'bg-cyan-600 bg-opacity-30'
              : ''
          "
        />
      </button>
    </div>
    <div class="flex flex-col lg:flex-row gap-6">
      <div class="lg:w-1/2">
        <div class="text-xl sm:text-2xl font-semibold">
          Расширенный список городов
        </div>
        <div class="text-sm mb-4 font-light text-gray-800">
          Выберите город из списка
        </div>
        <div class="max-w-sm">
          <BaseSelect
            placeholder="Поиск города"
            :options="CityList"
            @update="onSelectCity"
          />
        </div>
      </div>
      <div
        class="lg:w-1/2"
        :class="
          isSelectedMainCity || currentDistrictId
            ? ''
            : 'pointer-events-none opacity-25'
        "
      >
        <div class="text-xl sm:text-2xl font-semibold">Список районов</div>
        <div class="text-sm mb-4 font-light text-gray-800">
          Список районов доступен для трех городов
        </div>
        <div class="max-w-sm">
          <BaseSelect
            placeholder="Поиск района"
            :options="districtList"
            :is-expanded-initial="isDistrictsOpen"
            @update="onSelectDistrict"
          />
        </div>
      </div>
    </div>

    <div v-if="currentObjectId" class="flex flex-col gap-6 pt-10">
      <div class="text-xl sm:text-2xl font-semibold">Результаты анализа</div>
      <div class="flex flex-col md:flex-row gap-6">
        <div class="flex-1">
          <div>
            <BaseIframe
              :src="`./data/map/${currentObjectId}.html`"
              width="100%"
              height="500"
            />
            <div class="flex flex-col gap-2">
              <div class="flex gap-2">
                <div class="h-6 w-6 rounded-full bg-sky-300"></div>
                <div>
                  Голубые объекты - нейтральные (школы, университеты и т.д.)
                </div>
              </div>
              <div class="flex gap-2">
                <div class="h-6 w-6 rounded-full bg-green-500"></div>
                <div>
                  Зеленые объекты - положительные (парки, спорт площадки и т.д.)
                </div>
              </div>
              <div class="flex gap-2">
                <div class="h-6 w-6 rounded-full bg-red-600"></div>
                <div>
                  Красные объекты - отрицательные (табачные лавки, алкгольные и
                  т.д.)
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="md:w-1/3">
          <div
            :style="`background: top center / contain no-repeat url('./data/plot/${currentObjectId}.jpg');`"
            class="aspect-w-2 aspect-h-3"
          />
        </div>
      </div>
      <div class="text-xl sm:text-2xl font-semibold">Расшифровка анализа</div>
      <div v-html="text"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, nextTick, ref } from "vue";
import Card from "../components/analysis/Card.vue";
import {
  CityList,
  YekaterinburgDistrictList,
  TulaDistrictList,
  SevastopolDistrictList,
} from "../cities.ts";
import BaseSelect from "../components/base/BaseSelect.vue";
import BaseIframe from "../components/base/BaseIframe.vue";

const MainCities = {
  Yekaterinburg: 35,
  Tula: 132,
  Sevastopol: undefined,
};

const mainCitiesIds = Object.values(MainCities).map((id) =>
  id === undefined ? id : Number(id)
);

const currentCityId = ref<number | null | undefined>(null);
const currentDistrictId = ref<number | null>(null);
const currentObjectId = ref<number | null | undefined>(null);
const text = ref("");
const isDistrictsOpen = ref(false);

const onSelectCity = async (id?: number) => {
  currentCityId.value = id;
  currentObjectId.value = id;
  currentDistrictId.value = null;

  if (currentObjectId.value) {
    await loadText(currentObjectId.value);
  }

  if (isSelectedMainCity.value) {
    isDistrictsOpen.value = false;
    await nextTick();
    isDistrictsOpen.value = true;
  } else {
    isDistrictsOpen.value = false;
  }
};

const onSelectDistrict = async (id: number) => {
  currentDistrictId.value = id;
  currentObjectId.value = id;

  if (currentObjectId.value) {
    await loadText(currentObjectId.value);
  }
};

const isSelectedMainCity = computed(() => {
  return currentCityId.value !== null
    ? mainCitiesIds.includes(currentCityId.value)
    : false;
});

const districtList = computed(() => {
  if (isSelectedMainCity.value !== null) {
    if (currentCityId.value === MainCities.Yekaterinburg) {
      return YekaterinburgDistrictList;
    } else if (currentCityId.value === MainCities.Tula) {
      return TulaDistrictList;
    } else {
      return SevastopolDistrictList;
    }
  }
  return [];
});

const loadText = async (id: number) => {
  try {
    const response = await fetch(`./data/text/${id}.txt`);
    if (!response.ok) {
      throw new Error("Ошибка сети при попытке загрузить файл.");
    }
    const fileText = await response.text();
    text.value = fileText.replace(/\n/g, "<br>");
  } catch (error) {
    console.error("Произошла ошибка при чтении файла:", error);
  }
};
</script>
