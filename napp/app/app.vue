<script setup>

</script>

<template>
  <div class="bg-gray-900">
    <div class="container mx-auto px-2">
      
      <NuxtRouteAnnouncer />
      <NuxtLoadingIndicator :color="'repeating-linear-gradient(to right,#143656 0% ,#0a4c82 100%)'" :height="6" />
      
      <NuxtLayout>
        <div class="min-h-screen flex flex-col justify-between">
          <AppHeader class=" invisible" />
          <NuxtPage class="flex-1" />
          <AppFooter class=" invisible"/>
        </div>
      </NuxtLayout>

    </div>
  </div>

</template>