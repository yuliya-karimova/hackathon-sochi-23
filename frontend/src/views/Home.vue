<template>
  <div>
    <div class="flex items-center mx-auto max-w-screen-lg px-8 py-20">
      <div class="w-2/3 uppercase text-5xl">
        <div>Городская</div>
        <div>инфраструктура и</div>
        <div class="font-bold text-8xl">здоровье</div>
      </div>
      <div class="w-1/3">
        <div
          :style="`background: center / contain no-repeat url('./people/10.svg');`"
          class="aspect-w-2 aspect-h-3 -scale-x-100"
        />
      </div>
    </div>

    <div class="relative">
      <div class="relative z-10 mx-auto max-w-screen-lg px-8 py-36">
        <div class="text-4xl text-red-600 uppercase font-bold mb-10">
          Влияние городской инфраструктуры на здоровье
        </div>
        <div class="text-2xl flex flex-col gap-10">
          <div>
            Добро пожаловать на наш веб-сайт, посвященный анализу влияния
            инфраструктуры города на здоровье горожан! Здесь мы изучаем
            различные факторы, такие как детские площадки, парки и освещение
            улиц, оцениваем их положительное и отрицательное влияние, чтобы
            предложить оптимальные рекомендации.
          </div>
          <div>
            На карте города будут отмечены места с позитивными и негативными
            факторами, которые могут влиять на здоровье людей. Опираясь на
            собранные данные, мы предлагаем решения по улучшению городской среды
            для повышения благополучия горожан.
          </div>
          <div>
            Цветовая гамма сайта выбрана с особым вниманием, чтобы создать
            светлую, жизнерадостную и спокойную атмосферу!
          </div>
        </div>
      </div>
      <div
        class="absolute top-0 left-0 z-0"
        style="
          width: 100%;
          height: 100%;
          background-color: transparent;
          background-image: radial-gradient(
              rgb(152, 169, 197) 1px,
              transparent 1px
            ),
            radial-gradient(rgb(152, 169, 197) 1px, rgb(255, 255, 255) 1px);
          background-position: 0 0, 30px 30px;
          background-size: 60px 60px;
          border-radius: 0;
        "
      />
    </div>

    <div class="bg-cyan-950">
      <div class="flex flex-col mx-auto max-w-screen-lg px-8 py-28 text-white">
        <div class="flex flex-col gap-12 mb-24">
          <div class="text-5xl font-bold">Приступить к анализу!</div>
          <div class="flex gap-6">
            <router-link to="/analysis"
              class="rounded-sm h-8 bg-cyan-500 p-6 flex items-center justify-center text-lg font-medium"
            >
              Получить анализ города
            </router-link>
            <router-link to="/compare"
              class="rounded-sm h-8 bg-white text-cyan-900 p-6 flex items-center justify-center text-lg font-medium"
            >
              Сравнить города
            </router-link>
          </div>
        </div>

        <div class="lg:w-1/3 mx-auto mb-8">
          <div
            :style="`background: center / contain no-repeat url('./people/3.svg');`"
            class="aspect-w-2 aspect-h-3"
          />
        </div>

        <div class="flex gap-20 mb-36">
          <div class="w-1/2 text-5xl font-bold">Аналитика – ключ к успеху!</div>
          <div class="w-1/2 text-xl">
            Используя нашу платформу, вы сможете получить глубокий анализ
            городской среды и точные рекомендации по ее улучшению. Превратим
            наши города в оазисы здоровья и благополучия!
          </div>
        </div>

        <div class="grid grid-cols-6 gap-6 mb-36">
          <div
            :style="`background: center / contain no-repeat url('./people/4.svg');`"
            class="aspect-w-2 aspect-h-3"
          />
          <div
            :style="`background: center / contain no-repeat url('./people/5.svg');`"
            class="aspect-w-2 aspect-h-3"
          />
          <div
            :style="`background: center / contain no-repeat url('./people/6.svg');`"
            class="aspect-w-2 aspect-h-3"
          />
          <div
            :style="`background: center / contain no-repeat url('./people/7.svg');`"
            class="aspect-w-2 aspect-h-3"
          />
          <div
            :style="`background: center / contain no-repeat url('./people/8.svg');`"
            class="aspect-w-2 aspect-h-3"
          />
          <div
            :style="`background: center / contain no-repeat url('./people/9.svg');`"
            class="aspect-w-2 aspect-h-3"
          />
        </div>

        <div class="flex gap-6 flex-col lg:flex-row mb-6">
          <div
            class="bg-white bg-opacity-10 lg:w-4/6 rounded-2xl flex flex-col items-center justify-center px-12 h-72 gap-8"
          >
            <div class="text-8xl font-bold">152</div>
            <div class="text-xl">
              использовали для построения модели машинного обучения
            </div>
          </div>
          <div
            class="bg-white bg-opacity-10 lg:w-2/6 rounded-2xl flex flex-col items-center justify-center px-12 h-72 gap-8"
          >
            <div
              :style="`background: center / contain no-repeat url('./people/5.svg');`"
              class="aspect-w-1 aspect-h-1 h-44 w-full -scale-x-100"
            />
          </div>
        </div>

        <div class="flex gap-6 flex-col lg:flex-row">
          <div
            class="bg-white bg-opacity-10 lg:w-2/6 rounded-2xl flex flex-col items-center justify-center px-12 h-72 gap-8"
          >
            <div
              :style="`background: center / contain no-repeat url('./people/8.svg');`"
              class="aspect-w-1 aspect-h-1 h-44 w-full"
            />
          </div>
          <div
            class="bg-white bg-opacity-10 lg:w-4/6 rounded-2xl flex flex-col items-center justify-center px-12 h-72 gap-8"
          >
            <div class="text-8xl font-bold">150</div>
            <div class="text-xl">факторов городской среды учтено в анализе</div>
          </div>
        </div>
      </div>
    </div>

    <div class="flex flex-col gap-20 mx-auto max-w-screen-lg px-8 py-24">
      <Content
        title="Изучите влияние факторов городской среды"
        description="Мы анализируем, как факторы городской среды влияют на здоровье населения, пссихологическую обстановку, уровень жизни"
        img="./sport.jpg"
        textAlign="right"
      />
      <Content
        title="Населенный пункт"
        description="Возможность выбора населенного пункта на карте"
        img="./night.jpg"
        textAlign="left"
      />
    </div>

    <div class="bg-cyan-950">
      <div class="flex flex-col mx-auto max-w-screen-lg px-8 py-28 text-white">
        <div class="flex gap-6 flex-col lg:flex-row mb-6">
          <Card
            title="Населенный пункт"
            description="Возможность выбора населенного пункта на карте"
            img="./city.jpg"
            class="lg:w-4/6"
            cardClass="bg-white bg-opacity-10"
          />
          <Card
            title="Анализ данных"
            description="Учет множества факторов"
            img="./analysis.jpg"
            class="lg:w-2/6"
            cardClass="bg-white bg-opacity-10"
          />
        </div>

        <div class="flex gap-6 flex-col lg:flex-row">
          <Card
            title="Рекомендации"
            description="Поиск эффективных решений"
            img="./park.jpg"
            class="lg:w-2/6"
            cardClass="bg-white bg-opacity-10"
          />
          <Card
            title="Здоровье"
            description="Повышение уровня здоровья населения за счет качественного анализа"
            img="./child.jpg"
            class="lg:w-4/6"
            cardClass="bg-white bg-opacity-10"
          />
        </div>
      </div>
    </div>

    <div class="flex flex-col gap-12 mx-auto max-w-screen-lg px-8 py-20">
      <div class="text-3xl text-red-600 uppercase font-bold">Немного о нас</div>
      <div class="flex flex-col md:flex-row gap-20 font-light justify-between">
        <div class="md:w-1/3">
          <div class="text-red-600 mb-2">Почему мы этим занимаемся?</div>
          <div>
            Мы анализируем, как факторы городской среды влияют на здоровье
            населения, пссихологическую обстановку, уровень жизни. Повышение
            уровня здоровья населения за счет качественного анализа
          </div>
        </div>
        <div class="md:w-1/3">
          <div class="text-red-600 mb-2">Как мы анализируем?</div>
          <div>
            Мы анализируем, как факторы городской среды влияют на здоровье
            населения, пссихологическую обстановку, уровень жизни. Повышение
            уровня здоровья населения за счет качественного анализа
          </div>
        </div>
        <div class="md:w-1/3">
          <div class="text-red-600 mb-2">Какие технологии применяем?</div>
          <div>
            Мы анализируем, как факторы городской среды влияют на здоровье
            населения, пссихологическую обстановку, уровень жизни. Повышение
            уровня здоровья населения за счет качественного анализа
          </div>
        </div>
      </div>
    </div>
    <div class="flex flex-col gap-8 items-center justify-center mx-auto max-w-screen-lg px-8 pt-8 pb-20">
      <div class="h-44">
        <div
        :style="`background: center / contain no-repeat url('./logo_dark.svg');`"
        class="aspect-w-1 aspect-h-1 h-44 w-44"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Card from "../components/Card.vue";
import Content from "../components/Content.vue";
</script>
