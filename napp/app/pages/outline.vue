<script setup>
  const config = useRuntimeConfig()



</script>


<template>
  <div class="h-full content-center">
    <div class="" v-if="true">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

        <div class="bg-gray-800 border border-gray-700 rounded-lg p-4">
          <div class="grid grid-cols-1 p-1 text-center py-4">
            <p class="text-xl text-white">{{ config.public.SRC.title }}</p>
          </div>

          <div class="grid grid-cols-2 p-1">
            <p class="text-gray-100">Имя Фамилия: </p>
            <input placeholder="Иван Иванов" id="name" type="text" class="text-gray-800 p-1 pr-4 pl-4 rounded-sm text-center">
          </div>
          <div class="grid grid-cols-2 p-1">
            <p class="text-gray-100">Должность: </p>
            <input placeholder="Сотрудник" id="job" type="text" class="text-gray-800 p-1 pr-4 pl-4 rounded-sm text-center">
          </div>

          <div class="hidden">
            <a href="" target="_blank" class="text-white">Перейти по ссылке</a>
          </div>
        </div>


        <div class="text-white grid grid-cols-1 gap-4">

          <p class="text-white">{{ config.public.SRC.q }}</p> 
          <p class="text-white">{{ config.public.SRC.w }}</p>
          <p class="text-white">{{ config.public.SRC.e }}</p>
          <p class="text-white">{{ config.public.SRC.r }}</p>
          
          <div class="flex flex-wrap gap-2">
            <p class="text-white">Разработчик</p>-<a :href="config.public.SRC.t" class="text-white"> {{ config.public.SRC.y }}</a>, <a :href="config.public.SRC.t" class="text-white" target="_blank">Исходный код проекта</a>
          </div>

        </div>

      </div>


    </div>

    <div class="" v-else>

    </div>



  </div>

</template>