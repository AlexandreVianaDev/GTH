import { defineConfig } from "vite";

export default defineConfig({
  resolve: {
    alias: {
      "@emotion/styled": "@emotion/styled",
      "@emotion/react": "@emotion/react",
    },
  },
  server: {
    host: "0.0.0.0", // Permite conexões externas
    port: 3000, // Porta padrão
  },
});
