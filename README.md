# Corrective Bodyworks — Rehabilitation & Wellness

Marketing site for Corrective Bodyworks, LLC (Notasulga, AL), built with
[Astro](https://astro.build) and deployed as a static site.

## Getting started

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # static output → dist/
npm run preview  # serve the production build locally
```

## Where the content lives

All copy and business details are data-driven — you should rarely need to touch
a page component to make an edit.

| File | Contains |
| --- | --- |
| `src/data/site.ts` | Address, phone, email, hours, booking URLs, nav |
| `src/data/team.ts` | Staff bios, credentials, focus areas, photos |
| `src/data/services.ts` | Service list and the "what makes us different" points |
| `src/styles/global.css` | Design tokens (brand colors, type, spacing) |

Brand palette is sampled from the logo: navy `#011b3a`, slate `#4c647a`,
mist `#ced4da`.

## Pre-launch mode

The site ships **closed to search engines**. While `PUBLIC_PRELAUNCH` is unset
or anything other than `"false"`:

- every page renders `<meta name="robots" content="noindex, nofollow, …">`
- `/robots.txt` serves `Disallow: /`
- `netlify.toml` sends an `X-Robots-Tag: noindex, nofollow` header

### Going live

1. Set `PUBLIC_PRELAUNCH=false` in the Netlify environment variables.
2. Delete the `X-Robots-Tag` line from `netlify.toml`.
3. Remove the site's password protection in Netlify
   (**Site settings → Access & security → Visitor access**).
4. Point `site:` in `astro.config.mjs` at the real production domain.
5. Redeploy, then submit the sitemap in Google Search Console.

## Still to do before launch

- [ ] Add staff headshots to `public/team/` and set the `photo` field in `src/data/team.ts`
- [ ] Confirm clinic hours in `src/data/site.ts` (currently placeholder)
- [ ] Confirm the public email address in `src/data/site.ts`
- [ ] Wire up PT Everywhere booking + patient portal (`src/data/site.ts` → `booking`)
- [ ] Have a clinician review the FAQ answers on `/services/` for accuracy
- [ ] Add social profile URLs in `src/data/site.ts` → `social`
