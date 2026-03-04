<script setup>
  const config = useRuntimeConfig()

  const secret = ref("")
  const credentials = ref({
    ip: "Появиться после ввода секретного слова",
    key: "Появиться после ввода секретного слова",
  })


  const checkSecret = async () => {
    const data = await $fetch(`${config.public.baseURL}/srvc/credentials/`, {
      method: 'POST',
      body: {
        service_name: "rudesk",
        service_secret: secret.value
      },
    })
    console.log(data)
    credentials.value = data
  }


</script>



<template>
  <div class="grid grid-cols-1 gap-4">

    <div class="grid grid-cols-1 gap-6 mt-6 py-10 border border-gray-300/20 p-4 rounded-md">
      <div class="">
        <p class="text-gray-300 text-xl">RustDesk - это приложение для удаленного рабочего стола с открытым исходным кодом</p>
      </div>


      <div class="">
        <div class="flex flex-wrap justify-start gap-4">
          <a href="https://github.com/rustdesk/rustdesk/releases/download/1.4.5/rustdesk-1.4.5-x86_64.exe" class="text-white font-semibold bg-blue-500 hover:bg-blue-600 px-4 py-2 rounded-md">Скачать для Windows</a>
          <a href="https://github.com/rustdesk/rustdesk/releases/tag/1.4.5" class="text-white font-semibold bg-blue-500 hover:bg-blue-600 px-4 py-2 rounded-md" target="blank">Все клиенты на Github</a>
        </div>
      </div>
    </div>




    <div class="py-6 border border-gray-300/20 p-4 rounded-md">
      <p class="text-white text-xl">Подключение к серверу:</p>

      <div class="grid grid-cols-3 gap-4 py-4">

        <div class="grid grid-cols-1 gap-2">
          <div class=""><img src="/desk/1.png" /></div>
          <div class="">
            <p class="text-white">
              1. В правом верхнем углу жамкаем на бургер (☰)
            </p>
          </div>
        </div>

        <div class="grid grid-cols-1 gap-2">
          <div class=""><img src="/desk/2.png" /></div>
          <div class="">
            <p class="text-white">
              2. Идём в настройки сети, жамкаем ID/Ретранслятор
            </p>
          </div>
        </div>

        <div class="grid grid-cols-1 gap-2">
          <div class=""><img src="/desk/3.png" /></div>
          <div class="">
            <p class="text-white">
              3. В Сервер ID и Ретранслятор вбиваем айпишник, а в Key ключик полученные ниже
            </p>
          </div>
         
        </div>


      </div>

      <div class="flex justify-end gap-2">
        <input v-model="secret" type="text" id="qwe" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block dark:bg-gray-700 dark:border-gray-700 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Секретное слово">
        <button @click="checkSecret()" class="text-white font-semibold bg-blue-500 hover:bg-blue-600 px-4 py-2 rounded-md">Введи и жамкни мня</button> 
      </div>
      <div class="flex justify-end gap-2 mt-4">
        <p class="text-white">Сервер ID и Ретранслятор: <span class="bg-gray-300/30 px-2 py-0.5">{{ credentials.ip }}</span></p>
        <p class="text-white">Key: <span class="bg-gray-300/30 px-2 py-0.5">{{ credentials.key }}</span></p>
      </div>


    </div>


    <div class="py-6 border border-gray-300/20 p-4 rounded-md">
      <p class="text-white text-xl">Безопасность:</p>

      <div class="grid grid-cols-3 gap-4 py-4">

        <div class="grid grid-cols-1 gap-2">
          <div class=""><img src="/desk/4.png" /></div>
          <div class="">
            <p class="text-red-500 text-sm">
              Для секьюрности лучше отключить одноразовый пароль и задать постоянный (желательно что то посложнее qwerty1234)
            </p>
            <p class="text-white mt-0.5">
              4. Открываем вкладку безопасность, жамкаем на "Использовать постоянный пароль" и на "Установить постоянный пароль"
            </p>
          </div>
        </div>

        <div class="grid grid-cols-1 gap-2">
          <div class=""><img src="/desk/5.png" /></div>
          <div class="">
            <p class="text-white">
              5. Вбиваем свой сложный придуманный пароль и жамкаем ОКЕ
            </p>
          </div>
        </div>

        <div class="flex h-full items-center justify-center">

          <div class="">
            <p class="text-white text-xl font-semibold ">
              6. Радуемся, пользуемся
            </p>
          </div>
        </div>

      </div>


    </div>


    <div class="py-2 flex justify-end">

      <a href="https://github.com/rustdesk" class="text-sm text-gray-300 hover:text-white" target="blank">Исходный код RustDesk на Github</a>

    </div>






  </div>
</template>