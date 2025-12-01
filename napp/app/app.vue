<script setup>

</script>

<template>
  <div class="bg-gray-900">
    <div class="container mx-auto px-8">
      <NuxtRouteAnnouncer />
      <NuxtLayout>
        
        <div class="min-h-screen flex flex-col justify-between">
          <AppHeader />
          <NuxtPage class="flex-1" />
          <AppFooter/>
        </div>

      </NuxtLayout>
    </div>
  </div>

</template>