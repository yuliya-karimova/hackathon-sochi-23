<template>
  <div class="flex flex-col gap-2">
    <input
      ref="input"
      type="text"
      v-model="search"
      :placeholder="placeholder"
      class="border-2 rounded-md px-4 py-2"
      @input="filterCities"
      @click="isExpanded = !isExpanded"
    />
    <div
      ref="optionsList"
      v-if="isExpanded"
      class="border-2 rounded-md py-2 flex flex-col gap-1 max-h-44 overflow-y-auto"
    >
      <button
        v-for="option in filteredValues"
        :key="option.id"
        class="text-left px-4 py-1 hover:bg-gray-200"
        :class="selectedValueId === option.id && 'bg-gray-100'"
        @click="onSelect(option)"
      >
        {{ option.name }}
      </button>
      <div v-if="!filteredValues.length" class="px-4 py-1 text-gray-500">
        Извините, ничего не нашлось
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref, watch } from "vue";
import { onClickOutside } from "@vueuse/core";
import { Option } from "../../models/main";

interface Props {
  options?: Option[];
  placeholder?: string;
  isExpandedInitial?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
  options: () => [],
  placeholder: "Поиск...",
  isExpandedInitial: false
});

const search = ref("");
const filteredValues = ref<Option[]>([]);
const selectedValueId = ref<number | null>(null);
const isExpanded = ref(false);
const optionsList = ref<HTMLDivElement | null>(null);
const searchInput = ref<HTMLInputElement | null>(null);

onMounted(() => {
  filteredValues.value = props.options;
  isExpanded.value = props.isExpandedInitial;
});

const emit = defineEmits(["update"]);

const onSelect = (option: Option) => {
  selectedValueId.value = option.id;
  isExpanded.value = false;
  search.value = option.name;
  emit("update", option.id);
};

const filterCities = () => {
  isExpanded.value = true;

  if (search.value) {
    filteredValues.value = props.options.filter((option) =>
      option.name.toLowerCase().includes(search.value.toLowerCase())
    );
  } else {
    filteredValues.value = props.options;
  }
};

onClickOutside(optionsList, () => (isExpanded.value = false), {
  ignore: [searchInput],
});

watch(
  () => props.options,
  (newValue) => {
    filteredValues.value = newValue;
  }
);

watch(
  () => props.isExpandedInitial,
  (newValue) => {
    isExpanded.value = newValue;
  }
);
</script>
