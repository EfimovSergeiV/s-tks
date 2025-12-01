<template>
  <div>

    <div class="flex">
      <div class="bg-gray-800 border border-gray-700 rounded-lg p-4 w-[400px]">
        <p class="text-white uppercase font-semibold py-4">Навигация</p>

        <div class="grid grid-cols-1 gap-2">
          <nuxt-link class="text-gray-200 italic">Корпоративный мессенеджер</nuxt-link>
          <nuxt-link class="text-gray-200 italic">Корпоративная почта</nuxt-link>
          <nuxt-link :to="{ name: 'signature' }" class="text-gray-200 italic">Генератор подписи для email</nuxt-link>      
        </div>      
      </div>



    </div>



  </div>
</template>