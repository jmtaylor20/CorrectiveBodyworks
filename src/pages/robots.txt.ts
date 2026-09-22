import type { APIRoute } from 'astro';

// The site is live and open to crawlers. Set PUBLIC_PRELAUNCH to "true" to
// block them again on a build that should stay out of search results.
const prelaunch = import.meta.env.PUBLIC_PRELAUNCH === 'true';

export const GET: APIRoute = ({ site }) =>
  new Response(
    prelaunch
      ? `User-agent: *\nDisallow: /\n`
      : `User-agent: *\nAllow: /\n\nSitemap: ${new URL('sitemap-index.xml', site).href}\n`,
    { headers: { 'Content-Type': 'text/plain; charset=utf-8' } }
  );
