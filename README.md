# Corrective Bodyworks: Rehabilitation & Wellness

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

All copy and business details are data-driven. You should rarely need to touch
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
- [ ] Have a clinician review the FAQ answers on `/services/` for accuracy
- [ ] Add social profile URLs in `src/data/site.ts` → `social`


## Writing style

No em dashes or en dashes anywhere, including in code comments. Use a comma, a
colon, parentheses, a new sentence, or the word "to" for ranges. Regular hyphens
in compound words are fine.

`npm run check:dashes` enforces this and runs automatically as part of
`npm run build`, so a stray dash fails the build rather than reaching the site.

## PT Everywhere

PT Everywhere does have an Open API, but it is **not** the right tool for this
public marketing site:

- It is not public. Documentation is free to subscribers but must be requested
  from PT Everywhere Client Care, and is not self-service.
- It is a back-office API. It exposes appointment types, visit recency,
  birthdays and financials, aimed at business intelligence, accounting and
  marketing automation.
- It carries PHI and authenticates through AWS Cognito. Credentials that reach
  protected health information must never sit in a static site's client-side
  code, and any such integration needs a server-side component and a signed BAA.

What belongs on this site instead is a **link out** to the practice's own PT
Everywhere patient booking and portal pages, which is the normal pattern.

### Where these links live in the dashboard

**Settings > Clinic Settings > Online Settings.**

That page holds the self-registration link, the notification recipients for new
self-registrations, and the Enable Patient Self-Scheduling toggle. The URL shown
there matches the one wired into `src/data/site.ts`, so the dashboard is the
place to confirm it after any change.

PT Everywhere's in-app assistant claims a **Portal Subdomain** section exists
on this page, giving a URL like `correctivebodyworks.pteverywhere.com`. As of
the last check that section is not present, and the evidence says the feature
does not exist:

- The section is absent from the page the assistant named.
- PT Everywhere's own documentation states patient sign in is
  `app.pteverywhere.com` or the mobile app, with no per practice URL.
- The pricing page never mentions it.
- No clinic subdomain found anywhere resolves in DNS. There is no wildcard
  record on `pteverywhere.com`, so a configured subdomain would resolve.
  Only company subdomains exist: `app`, `help`, `wp`, `lp`.
- PHYT Collective, a large PT Everywhere practice, uses a path based portal
  URL rather than a subdomain.

Treat the assistant's answers about URLs and settings as unverified. It has
given several confident, specific and wrong answers on this topic.

Existing patients sign in at the shared `app.pteverywhere.com`, which is what
the site links to and works correctly. If a human at
support@pteverywhere.com ever confirms a practice specific URL, put it in
`portal.login` in `src/data/site.ts`.

Verification method, should one be offered: run
`getent hosts <name>.pteverywhere.com`. Because there is no wildcard DNS, a
real subdomain resolves and a nonexistent one returns nothing. This is the
only PT Everywhere URL that can be verified without a browser, since their
path based URLs return an identical page whether or not they exist.

### Wiring it up

Set either value in `src/data/site.ts` under `booking`:

```ts
booking: {
  url: 'https://...',        // public self-booking link
  portalUrl: 'https://...',  // existing-patient login
  label: 'Request an Appointment',
},
```

Every call to action across the site switches over automatically, and external
links get `target="_blank"` plus `rel="noopener noreferrer"`. Leave a value
empty and it degrades gracefully: booking buttons fall back to `/contact/` and
the portal link stays hidden. No other file needs to change.

If a real API integration is wanted later (syncing appointments or patient
data), that is a separate server-side project, not a change to this site.
