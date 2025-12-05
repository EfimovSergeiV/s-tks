<script setup>




</script>


<template>
  <div class="text-white">

    <div class="bg-gray-800 border border-gray-700 rounded-lg p-4">

      <div class="grid grid-cols-1 p-1 text-center py-4">
        <p class="text-xl text-white">Получить доступ в мессенджер</p>
      </div>

      <div class="flex flex-wrap gap-2">
        <div><p>Получить ссылку для регистрации</p></div>
        <div><p>Отправить приглашение на email</p></div>
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






  </div>
</template>
