// @ts-check
import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  integrations: [react()],
  vite: {
    plugins: [tailwindcss()],
  },
  i18n: {
    defaultLocale: 'it',
    locales: ['it', 'es', 'en'],
    routing: {
      // it su "/", es su "/es/", en su "/en/"
      prefixDefaultLocale: false,
      // pagine non ancora tradotte in es/en mostrano il contenuto italiano
      fallbackType: 'rewrite',
    },
    fallback: {
      es: 'it',
      en: 'it',
    },
  },
});
