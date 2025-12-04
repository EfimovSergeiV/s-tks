import cfg from "./conf"

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  
  app: {
    pageTransition: { name: 'page', mode: 'out-in' },
  },

  modules: [
    '@nuxt/image',
    '@nuxtjs/tailwindcss',
  ],

  runtimeConfig: {
    public: {
      baseURL: cfg.BASE_URL, ///"http://127.0.0.1:8000",
    },
  },

  css: [
    '~/assets/css/main.css',
  ]
})