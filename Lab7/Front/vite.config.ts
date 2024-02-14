import {defineConfig} from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
    plugins: [react()],
    server: {
        proxy: {
            "/api/": { // Временный костыль, пока эти запросы не передут на норм path
                target: "http://localhost:8000/",
                changeOrigin: true,
                secure: false,
            },
        }
    }
})
