import type { APIRoute } from 'astro';

// Pre-launch: block every crawler. Flip PUBLIC_PRELAUNCH to "false" (or drop
// the variable) at launch and redeploy to open the site up.
const prelaunch = import.meta.env.PUBLIC_PRELAUNCH !== 'false';

export const GET: APIRoute = ({ site }) =>
  new Response(
    prelaunch
      ? `User-agent: *\nDisallow: /\n`
      : `User-agent: *\nAllow: /\n\nSitemap: ${new URL('sitemap-index.xml', site).href}\n`,
    { headers: { 'Content-Type': 'text/plain; charset=utf-8' } }
  );
