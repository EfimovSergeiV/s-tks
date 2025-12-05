<script setup>


</script>


<template>
  <div class="h-full content-center py-6">

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <div class="bg-gray-800 border border-gray-700 rounded-lg p-4 mb-4 h-full">
        <p class="text-white uppercase font-semibold pb-1 border-b text-right">Общая информация</p>
        <div class="grid grid-cols-1 gap-2 py-4">
          <nuxt-link class="text-gray-200 italic hover:text-white hover:mr-1 text-right transition-all">Удалённый доступ Анидеск</nuxt-link>
          <nuxt-link class="text-gray-200 italic hover:text-white hover:mr-1 text-right transition-all">Какая то информация</nuxt-link>
          <nuxt-link class="text-gray-200 italic hover:text-white hover:mr-1 text-right transition-all">Ещё какая то информация</nuxt-link>          
        </div>
      </div>
      <div class="bg-gray-800 border border-gray-700 rounded-lg p-4 h-full">
        <p class="text-white uppercase font-semibold pb-1 border-b text-right">Внутренние сервисы</p>
        <div class="grid grid-cols-1 gap-2 py-4">
          <nuxt-link class="text-gray-200 italic hover:text-white hover:mr-1 text-right transition-all">Корпоративный мессенеджер</nuxt-link>
          <nuxt-link class="text-gray-200 italic hover:text-white hover:mr-1 text-right transition-all">Корпоративная почта</nuxt-link>
          <nuxt-link :to="{ name: 'signature' }" class="text-gray-200 italic hover:text-white hover:mr-1 text-right transition-all">Генератор подписи для email</nuxt-link>      
          <nuxt-link class="text-gray-200 italic hover:text-white hover:mr-1 text-right transition-all">Корпоративный ВПН доступ</nuxt-link>          
        </div>      
      </div>
    </div>


    <div class="grid grid-cols-1 gap-4 content-center text-center text-sm md:text-base mt-8 md:mt-16">
      <p class="text-gray-300">
        «Техносвар» - это современное российское предприятие, специализирующееся в области разработки и производства электросварочного оборудования для многих отраслей промышленности. На нашем предприятии изготавливается оборудование для контактной (машины для точечной, рельефной, шовной, стыковой сварки) и дуговой сварки, трансформаторы для контактной сварки, а также другие комплектующие изделия и запасные части для электросварочного оборудования.
      </p>
      <p class="text-gray-300 hidden">
        Основными принципами работы «Технологического центра «Техносвар» является качество производимой продукции и услуг, а также решение специализированных задач в области сварочного производства.
      </p>
      <p class="text-gray-300 hidden">
        Сварочное оборудование, произведённое на нашем предприятии, не уступает по характеристикам и качеству зарубежных аналогов.
      </p>
      <p class="text-gray-300 hidden">
        Предприятие оснащено всеми необходимыми современными мощностями и оборудованием, что в свою очередь позволяет нам оперативно выполнять проекты.
      </p>
      <p class="text-gray-300 hidden">
        Специалисты предприятия идут в ногу со временем: проходят курсы по повышению квалификации, участвуют в семинарах, а также посещают специализированные выставки профильной продукции. Мы внимательно изучаем специфику потребительского рынка и оперативно реагируем на появление новых тенденций в сфере производства профессионального сварочного оборудования.
      </p>
    </div>

  </div>
</template>