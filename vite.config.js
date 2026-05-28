import {defineConfig} from "vite";
import {resolve} from "path";
import { main } from "@popperjs/core";
export default defineConfig({
    base: "/static/",
    build:{
        manifest:"manifest.json",
        emptyOutDir: true,
        outDir: resolve("./mysite/mysite/static"),
        assetsDir: "",
        rollupOptions: {
            input:{
                main: resolve("./mysite/mysite/assets/js/mysite.js")
            }
        }
    },
    // Optional: Silence Sass deprecation warnings. See note below.
  css: {
     preprocessorOptions: {
        scss: {
          silenceDeprecations: [
            'import',
            'mixed-decls',
            'color-functions',
            'global-builtin',
          ],
        },
     },
  },

})