import scope from "astro-scope";
// @ts-check
import { defineConfig } from "astro/config";

export default defineConfig({
    integrations: [scope()],
});
