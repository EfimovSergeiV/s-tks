<template>
  <div class="h-full content-center py-6">

    <div class="grid grid-cols-3 gap-4">
      <div class="bg-gray-800 border border-gray-700 rounded-lg p-4">
        <p class="text-white uppercase font-semibold pb-0.5 border-b">Навигация</p>

        <div class="grid grid-cols-1 gap-2 py-4">
          <nuxt-link class="text-gray-200 italic hover:text-white hover:ml-1 transition-all">Корпоративный мессенеджер</nuxt-link>
          <nuxt-link class="text-gray-200 italic hover:text-white hover:ml-1 transition-all">Корпоративная почта</nuxt-link>
          <nuxt-link :to="{ name: 'signature' }" class="text-gray-200 italic hover:text-white hover:ml-1 transition-all">Генератор подписи для email</nuxt-link>      
        </div>      
      </div>
    </div>

  </div>
</template>