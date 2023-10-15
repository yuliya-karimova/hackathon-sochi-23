<template>
  <div>
    <div class="flex items-center mx-auto max-w-screen-lg px-8 pb-12 pt-20">
      <div class="w-full sm:w-2/3 uppercase z-10">
        <div class="text-3xl sm:text-5xl">
          <div>Городская</div>
          <div>инфраструктура и</div>
          <div class="font-bold text-6xl sm:text-8xl mb-12">здоровье</div>
        </div>
        <div class="flex gap-3 md:gap-6 flex-col md:flex-row">
          <router-link
            to="/analysis"
            class="rounded-sm bg-gray-300 py-3 px-5 flex items-center justify-center text-sm sm:text-lg font-medium w-64 sm:w-auto"
          >
            Получить анализ города
          </router-link>
          <router-link
            to="/compare"
            class="rounded-sm bg-cyan-600 bg-opacity-60 py-3 px-5 flex items-center justify-center text-sm sm:text-lg font-medium w-64 sm:w-auto"
          >
            Сравнить города
          </router-link>
        </div>
      </div>
      <div class="absolute right-0 sm:static w-1/3 z-0">
        <div
          :style="`background: center / contain no-repeat url('./people/10.svg');`"
          class="aspect-w-2 aspect-h-3 -scale-x-100"
        />
      </div>
    </div>

    <div class="relative">
      <div class="relative z-10 mx-auto max-w-screen-lg px-8 py-12 sm:py-28">
        <div
          class="text-2xl sm:text-4xl text-red-600 uppercase font-bold mb-10"
        >
          Влияние городской инфраструктуры на здоровье
        </div>
        <div class="text-xl sm:text-2xl flex flex-col gap-10">
          <div>
            Добро пожаловать на наш сайт, посвященный анализу влияния
            инфраструктуры города на здоровье населения! Для наглядности вам
            будет представлена интерактивная карта, на которой отображаются
            объекты городской инфраструктуры, а также их влияние на здоровье
            населения.
          </div>
          <div class="flex flex-col gap-2">
            <div>Более 150 городов России</div>
            <div>150+ признаков инфраструктуры</div>
            <div>Глубокий статистический анализ</div>
            <div>Технологии градиентного бустинга для моделирования (ИИ)</div>
            <div>Основные факторы здоровья горожан под нашим микроскопом</div>
          </div>
          <div>
            Команда "AI Sister" провела комплексный исследовательский проект,
            целью которого является анализ городской инфраструктуры и её влияния
            на здоровье населения. Произведен детальный статистический анализ,
            позволяющий выделить ключевые факторы, влияющие на здоровье горожан.
            Для прогнозирования показателей здоровья была разработана модель на
            основе алгоритма градиентного бустинга catboost.
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
      <div
        class="flex flex-col mx-auto max-w-screen-lg px-8 py-12 xl:py-28 text-white"
      >
        <div class="flex flex-col gap-8 md:gap-8 xl:gap-12 xl:mb-24">
          <div class="text-3xl sm:text-5xl font-bold">
            Приступить к анализу!
          </div>
          <div class="flex gap-4 sm:gap-6 flex-col sm:flex-row uppercase">
            <router-link
              to="/analysis"
              class="rounded-sm h-8 bg-cyan-500 p-6 flex items-center justify-center text-lg font-medium"
            >
              Получить анализ города
            </router-link>
            <router-link
              to="/compare"
              class="rounded-sm h-8 bg-white text-cyan-900 p-6 flex items-center justify-center text-lg font-medium"
            >
              Сравнить города
            </router-link>
          </div>
        </div>

        <div class="w-full sm:w-1/3 mx-auto xl:mb-8">
          <div
            :style="`background: center / contain no-repeat url('./people/3.svg');`"
            class="aspect-w-2 aspect-h-3"
          />
        </div>

        <div class="flex flex-col md:flex-row gap-6 xl:gap-20 mb-12 xl:mb-36">
          <div class="md:w-1/2 text-5xl font-bold">
            Аналитика – ключ к успеху!
          </div>
          <div class="md:w-1/2 text-xl">
            Используя нашу платформу, вы сможете получить глубокий анализ
            городской среды и точные рекомендации по ее улучшению. Превратим
            наши города в оазисы здоровья и благополучия!
          </div>
        </div>

        <div class="grid grid-cols-3 md:grid-cols-6 gap-6 mb-12 xl:mb-36">
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
            class="aspect-w-2 aspect-h-3 hidden md:block"
          />
          <div
            :style="`background: center / contain no-repeat url('./people/8.svg');`"
            class="aspect-w-2 aspect-h-3 hidden md:block"
          />
          <div
            :style="`background: center / contain no-repeat url('./people/9.svg');`"
            class="aspect-w-2 aspect-h-3 hidden md:block"
          />
        </div>

        <div class="flex gap-6 flex-col md:flex-row mb-6">
          <div
            class="bg-white bg-opacity-10 md:w-4/6 rounded-2xl flex flex-col items-center justify-center px-12 h-52 sm:h-72 gap-4 sm:gap-8"
          >
            <div class="text-6xl sm:text-8xl font-bold">150+</div>
            <div class="text-xl text-center">
              городов использовали для построения модели машинного обучения
            </div>
          </div>
          <div
            class="bg-white bg-opacity-10 md:w-2/6 rounded-2xl flex flex-col items-center justify-center px-12 h-52 sm:h-72 gap-4 sm:gap-8"
          >
            <div
              :style="`background: center / contain no-repeat url('./people/5.svg');`"
              class="aspect-w-1 aspect-h-1 h-32 w-32 md:h-44 md:w-44 -scale-x-100"
            />
          </div>
        </div>

        <div class="flex gap-6 flex-col-reverse md:flex-row">
          <div
            class="bg-white bg-opacity-10 md:w-2/6 rounded-2xl flex flex-col items-center justify-center px-12 h-52 sm:h-72 gap-4 sm:gap-8"
          >
            <div
              :style="`background: center / contain no-repeat url('./people/8.svg');`"
              class="aspect-w-1 aspect-h-1 h-32 w-32 md:h-44 md:w-44"
            />
          </div>
          <div
            class="bg-white bg-opacity-10 md:w-4/6 rounded-2xl flex flex-col items-center justify-center px-12 h-52 sm:h-72 gap-4 sm:gap-8"
          >
            <div class="text-6xl sm:text-8xl font-bold">150+</div>
            <div class="text-xl text-center">
              факторов городской среды учтено в анализе
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- <div
      class="flex flex-col gap-12 sm:gap-20 mx-auto max-w-screen-lg px-8 py-12 sm:py-24"
    >
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
    </div> -->
    <!-- 
    <div class="bg-cyan-950">
      <div
        class="flex flex-col mx-auto max-w-screen-lg px-8 py-12 sm:py-24 text-white"
      >
        <div class="flex gap-6 flex-col lg:flex-row mb-6">
          <Card
            title="Населенный пункт"
            description="Возможность выбора населенного пункта на карте"
            img="./city.jpg"
            class="lg:w-4/6"
          />
          <Card
            title="Анализ данных"
            description="Учет множества факторов"
            img="./analysis.jpg"
            class="lg:w-2/6"
          />
        </div>

        <div class="flex gap-6 flex-col lg:flex-row">
          <Card
            title="Рекомендации"
            description="Поиск эффективных решений"
            img="./park.jpg"
            class="lg:w-2/6"
          />
          <Card
            title="Здоровье"
            description="Повышение уровня здоровья населения за счет качественного анализа"
            img="./child.jpg"
            class="lg:w-4/6"
          />
        </div>
      </div>
    </div> -->

    <div
      class="flex flex-col gap-6 sm:gap-12 mx-auto max-w-screen-lg px-8 py-12 sm:py-24"
    >
      <div class="text-3xl text-red-600 uppercase font-bold">Немного о проекте</div>
      <div
        class="flex flex-col sm:flex-row gap-12 md:gap-16 font-light justify-between"
      >
        <div class="w-full sm:w-1/3">
          <div class="text-red-600 mb-2">Как мы анализируем?</div>
          <div>
            Мы проводим глубокий статистический анализ городской инфраструктуры,
            выделяя ключевые факторы, которые влияют на здоровье горожан,
            пссихологическую обстановку, уровень жизни.
            <a href="https://docs.google.com/document/d/1MLZWv50G2NsVR8M4cSz2kHZTQl2jJ3bF/edit?usp=sharing&ouid=113982104465456762424&rtpof=true&sd=true" class="text-red-600">Отчет о проекте</a>
          </div>
        </div>
        <div class="w-full sm:w-1/3">
          <div class="text-red-600 mb-2">Какие технологии применяем?</div>
          <div>
            Применяем технологии градиентного бустинга для моделирования,
            используя алгоритм catboost, и разрабатываем веб-приложение для
            визуализации результатов.
          </div>
        </div>
        <div class="w-full sm:w-1/3">
          <div class="text-red-600 mb-2">Почему это важно?</div>
          <div>
            Это важно, потому что понимание взаимосвязи между городской средой и
            здоровьем может помочь органам местного самоуправления принимать
            обоснованные решения по улучшению жизни горожан.
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// import Card from "../components/home/Card.vue";
// import Content from "../components/home/Content.vue";
</script>
