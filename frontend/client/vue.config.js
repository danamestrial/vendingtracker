const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  transpileDependencies: true,
});

module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'https://127.0.0.1:5000',
        changeOrigin: true,
      },
    },
  },
};
