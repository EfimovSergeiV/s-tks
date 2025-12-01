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
  <div class="">
    <p class="">Генератор подписи для email</p>

    <div class="">
      <nuxt-link :to="{ name: 'index' }">Вернуться</nuxt-link>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">




      <div class="grid grid-cols-1 gap-4">
        <p class="text-red-500">{{ userData }}</p>

        <div class="">
          <div class="flex flex-wrap gap-4">
            <div class="">
              <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-900 dark:text-gray-400">Имя</label>
              <div class="relative">
                <div class="flex absolute inset-y-0 left-0 items-center pl-2 pointer-events-none">
                  <p class="mdi mdi-24px mdi-account"></p>
                </div>
                <input v-model="userData.name" type="text" id="person" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-700 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Иван">
              </div>
            </div>
            <div class="">
              <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-900 dark:text-gray-400">Фамилия</label>
              <div class="relative">
                <div class="flex absolute inset-y-0 left-0 items-center pl-2 pointer-events-none">
                  <p class="mdi mdi-24px mdi-account"></p>
                </div>
                <input v-model="userData.family" type="text" id="person" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-700 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Иванов">
              </div>
            </div>
          </div>
          <div class="flex flex-wrap gap-4">
            <div class="">
              <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-900 dark:text-gray-400">Имя</label>
              <div class="relative">
                <div class="flex absolute inset-y-0 left-0 items-center pl-2 pointer-events-none">
                  <p class="mdi mdi-24px mdi-account"></p>
                </div>
                <input v-model="userData.name" type="text" id="person" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-700 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Иван">
              </div>
            </div>
            <div class="">
              <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-900 dark:text-gray-400">Фамилия</label>
              <div class="relative">
                <div class="flex absolute inset-y-0 left-0 items-center pl-2 pointer-events-none">
                  <p class="mdi mdi-24px mdi-account"></p>
                </div>
                <input v-model="userData.family" type="text" id="person" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-700 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Иванов">
              </div>
            </div>
          </div>
        </div>

        <div class="flex flex-wrap gap-4">
          <button @click="getSignatureCode()" class="bg-blue-500 px-4 py-2 text-gray-100 font-semibold rounded-sm">Сгенерировать подпись</button>
          <button @click="copyToClipboard()" class="bg-blue-500 px-4 py-2 text-gray-100 font-semibold rounded-sm">Скопировать в буфер обмена</button>      
        </div>
        
      </div>

      <div class="">
        <div class="grid grid-cols-1 gap-4">
          <p class="">Предварительный просмотр</p>
          <iframe
            ref="previewFrame"
            class="w-full h-64 border"
          ></iframe>
        </div>        
      </div>

    </div>

  </div>
</template>