<script setup>

</script>

<template>
  <div class="px-8">
    <NuxtRouteAnnouncer />
    <NuxtLayout>
      
      <div class="min-h-screen flex flex-col justify-between">
        <AppHeader />
        <NuxtPage class="flex-1" />
        <AppFooter/>
      </div>

    </NuxtLayout>
  </div>
</template>