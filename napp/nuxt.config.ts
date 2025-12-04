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
      baseURL: cfg.BASE_URL,
    },
  },

  css: [
    '~/assets/css/main.css',
  ]
})