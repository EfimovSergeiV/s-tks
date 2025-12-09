import cfg from "./conf"

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-12-05',
  devtools: { enabled: true },
  ssr: true, /// true or false
  app: {
    head: {
      title: 'Внутренние сервисы Техносвар КС',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'format-detection', content: 'telephone=yes' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.png' }
      ],
    },


    pageTransition: { name: 'page', mode: 'out-in' },
  },

  modules: [
    '@nuxt/image',
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt',
  ],

  runtimeConfig: {
    public: {
      baseURL: cfg.BASE_URL,
      SRC: cfg.SRC,
    },
  },

  css: [
    '~/assets/css/main.css',
  ]
})