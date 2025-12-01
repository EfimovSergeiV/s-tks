<script setup>
  const config = useRuntimeConfig()


  const signatureCode = ref(null)
  const userData = ref(
    {
      "name": null,
      "family": null
    }
  )

  const getSignatureCode = async () => {
    const res = await fetch(`${ config.public.baseURL }/srvc/signature/`)
    signatureCode.value = await res.text()
  }


  const copyToClipboard = async () => {
    try {
      const blob = new Blob([signatureCode.value], { type: "text/html" })

      const item = new ClipboardItem({
        "text/html": blob
      })

      await navigator.clipboard.write([item])

      alert("Подпись скопированна в бефер обмена, теперь её можно вставить в почтовый клиент")
    } catch (err) {
      console.error("Ошибка копирования:", err)
      alert("Не удалось скопировать HTML")
    }
  }

  const previewFrame = ref(null)
  watch(signatureCode, (html) => {
    if (previewFrame.value) {
      const doc = previewFrame.value.contentDocument
      doc.open()
      doc.write(html)
      doc.close()
    }
  })

</script>


<template>
  <div class="h-full content-center py-6">



    <div class="flex items-center justify-between gap-8 py-4">
      <div class="">

      </div>
      <div class="">
        <div class="">
          <nuxt-link :to="{ name: 'index' }" class="text-gray-50">Вернуться на главную</nuxt-link>
        </div>
      </div>
    </div>


    <div class="grid grid-cols-1 md:grid-cols-2 items-center justify-center gap-4">
      <div class="">

        <div class="flex flex-wrap items-center justify-start gap-x-6 gap-y-2  py-2">
          <div class="">
            <div class="flex gap-4 items-center">
              <label for="country" class="block text-sm/6 font-medium text-gray-100">Выбрать шаблон</label>
              <div class="mt-2 grid grid-cols-1">
                <select id="country" name="country" autocomplete="country-name" class="appearance-none rounded-md bg-gray-700 py-1.5 pr-8 pl-3 text-base text-gray-100 outline-1 -outline-offset-1 outline-white *:bg-gray-500 focus:outline-1 focus:-outline-offset-1 focus:outline-gray-500 sm:text-sm/6">
                  <option>Базовый шаблон</option>
                  <option>Canada</option>
                  <option>Mexico</option>
                </select>
              </div>
            </div>
          </div>
          <div class="">
            <div class="flex gap-4 items-center">
              <label for="country" class="block text-sm/6 font-medium text-gray-100">Заполнить из списка</label>
              <div class="mt-2 grid grid-cols-1">
                <select id="country" name="country" autocomplete="country-name" class="appearance-none rounded-md bg-gray-700 py-1.5 pr-8 pl-3 text-base text-gray-100 outline-1 -outline-offset-1 outline-white *:bg-gray-500 focus:outline-1 focus:-outline-offset-1 focus:outline-gray-500 sm:text-sm/6">
                  <option>Не выбрано</option>
                  <option>Canada</option>
                  <option>Mexico</option>
                </select>
              </div>
            </div>
          </div>
        </div>

        <div class="bg-gray-800 border border-gray-700 rounded-lg p-4">

          <div class="grid grid-cols-1 p-1 text-center py-4">
            <p class="text-xl text-white">Генератор подписи для email</p>
          </div>
      
          <div>
              <div class="grid grid-cols-2 p-1">
                <p class="text-gray-100">Имя Фамилия: </p>
                <input placeholder="Иван Иванов" id="name" type="text"  class="text-gray-800 p-1 pr-4 pl-4 rounded-sm text-center">
              </div>
              <div class="grid grid-cols-2 p-1">
                <p class="text-gray-100">Должность: </p>
                <input placeholder="Сотрудник" id="job" type="text" class="text-gray-800 p-1 pr-4 pl-4 rounded-sm text-center">
              </div>
              <div class="grid grid-cols-2 p-1">
                <p class="text-gray-100">Рабочий: </p>
                <input placeholder="+7 (8112) 75 52 13" type="text" value="+7 (8112) 72 52 13" class="text-gray-800 p-1 pr-4 pl-4 rounded-sm text-center">
              </div>
              <div class="grid grid-cols-2 p-1">
                <p class="text-gray-100">Мобильный: </p>
                <input placeholder="+7 (012) 345 67 89" id="private" type="text" class="text-gray-800 p-1 pr-4 pl-4 rounded-sm text-center">
              </div>

              <div class="grid grid-cols-1 p-1 mt-6 text-right">
                <small class="text-gray-100">* Оставить пустыми, если совпадает с мобильным телефоном</small>
              </div>              
              <div class="grid grid-cols-2 p-1">
                <p class="text-gray-100">WhatsApp: </p>
                <input placeholder="+7 (012) 345 67 89" id="private" type="text" class="text-gray-800 p-1 pr-4 pl-4 rounded-sm text-center">
              </div>
              <div class="grid grid-cols-2 p-1">
                <p class="text-gray-100">Телеграмм: </p>
                <input placeholder="+7 (012) 345 67 89" id="private" type="text" class="text-gray-800 p-1 pr-4 pl-4 rounded-sm text-center">
              </div>

              <div class="py-4 mt-4">
                <div class="flex flex-wrap gap-4 items-center justify-center">
                  <button @click="getSignatureCode()" class="rounded-sm bg-sky-500 px-10 py-2 text-base text-gray-50 font-semibold shadow-sm hover:bg-sky-800 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-1 transition-all">Сгенерировать подпись</button>
                  <button @click="copyToClipboard()" class="rounded-sm bg-sky-500 px-10 py-2 text-base text-gray-50 font-semibold shadow-sm hover:bg-sky-800 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-1 transition-all">Скопировать в буфер обмена</button>      
                </div>          
              </div>

            </div>  
        </div>
      </div>

      <div class="">
        <div class="grid grid-cols-1 gap-4">
          <p class="text-gray-50">Предварительный просмотр</p>
          <iframe
            ref="previewFrame"
            class="w-full h-[400px] border border-gray-500 bg-white"
          ></iframe>
        </div>        
      </div>

    </div>

    <div class="flex flex-wrap items-center justify-end gap-6 mt-4">
      <div class="">
        <div class="mt-1 mb-1 text-white">
          <p>Настройка подписи в браузере</p>
        </div>
        <div class="">
          <video width="400" height="300" controls="controls" class="rounded-sm">
            <source src="https://api.glsvar.ru/files/signature.mp4" type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
            Тег video не поддерживается вашим браузером. 
            <a href="video/duel.mp4">Скачайте видео</a>
          </video>              
        </div>
      </div>
      <div class="">
        <div class="mt-1 mb-1 text-white">
          <p>Настройка подписи в The Bat</p>
        </div>
        <div class="">
          <video width="400" height="300" controls="controls" class="rounded-sm">
            <source src="https://api.glsvar.ru/files/batmanual.mp4" type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
            Тег video не поддерживается вашим браузером. 
            <a href="video/duel.mp4">Скачайте видео</a>
          </video>              
        </div>
      </div>
    </div>


  </div>
</template>