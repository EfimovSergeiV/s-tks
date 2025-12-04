module.exports = {
  apps: [
    {
      name: 'Portal TKS',
      port: '3000',
      exec_mode: 'cluster',
      instances:  1, /// 'max',
      script: './.output/server/index.mjs'
    }
  ]
}