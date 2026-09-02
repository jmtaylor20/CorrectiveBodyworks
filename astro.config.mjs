import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Update `site` to the production domain before launch. It drives
// canonical URLs, the sitemap, and social share tags.
export default defineConfig({
  site: 'https://www.correctivebodyworks.net',
  integrations: [sitemap()],
});
