import { defineConfig } from '@playwright/test';

export default defineConfig({
    webServer: {
        command: 'pnpm run build && pnpm run preview',
        port: 4321,
        timeout: 120 * 1000,
    },
    use: {
        baseURL: 'http://localhost:4321/',
    },

    testDir: 'playwright'
});