# PT Everywhere branding kit

PT Everywhere lets a practice brand its patient portal with a **logo**, **colors**,
and **welcome text**, so the portal reads as an extension of the clinic rather
than generic software. Everything needed for that is in this folder.

Set it in PT Everywhere under the practice or portal settings. If you cannot
find the fields, Client Care can point you at them.

## Logo files

| File | Use it for |
| --- | --- |
| `logo-horizontal-onwhite.png` | The main portal logo. Safest default: flattened onto white, so it works even where transparency is not supported. 1200 x 425. |
| `logo-horizontal-onnavy.png` | The same lockup knocked out to white on brand navy, for a dark header. |
| `logo-horizontal-transparent.png` | Full-resolution transparent version, if the upload field accepts alpha. 2500 x 885. |
| `icon-square-onwhite.png` | Square 1024 x 1024 icon (the cross and tree mark) for avatars, app tiles, or anywhere a square crop is required. |
| `icon-square-onnavy.png` | Square icon on navy. |
| `icon-transparent.png` | Transparent square mark. |

Upload the widest version the field allows. PT Everywhere will scale it down,
and starting large keeps it sharp on high-resolution screens.

## Landing background

**Use `bg-landing-1920x1080.jpg` (63 KB).** It is the right balance of
sharpness and weight for a page where most of the image sits behind a form.

| File | Size | Use it for |
| --- | --- | --- |
| `bg-landing-1920x1080.jpg` | 63 KB | **Recommended.** Desktop landing and registration. |
| `bg-landing-2560x1440.jpg` | 109 KB | Only if the portal renders on very large displays and 1080p looks soft. |
| `bg-landing-mobile-1170x2050.jpg` | 75 KB | Portrait crop, if a separate mobile background is supported. |
| `*.webp` | 20 to 34 KB | Same three images in WebP, roughly a third of the size. Use these if the upload field accepts WebP. Every current browser supports it. |

### On loading speed

The first version of these files was about four times heavier, because of the
film grain laid over the gradient. Random noise is close to worst case for JPEG:
the format is built to compress smooth areas, and grain defeats that. Dialing
the grain back to just enough to prevent banding cut the 2560 file from 268 KB
to 109 KB and the 1920 file from 152 KB to 63 KB, with no visible difference.

If the page still feels slow after swapping the file, the remaining delay is
most likely PT Everywhere's own application loading rather than the image. The
portal is a client rendered app, so the background cannot paint until its
JavaScript has booted.

Designed to sit under content rather than compete with it. The left and centre
are deliberately calm so a form has somewhere to land, and the cross and tree
mark sits quietly in the right third. White text placed anywhere on the image
measures at worst 10.9:1 contrast, comfortably past the 4.5:1 accessibility
threshold. The design rationale is in `DESIGN-PHILOSOPHY.md`.

### Light background, for the navy logo

The navy landing background is built for the white logo. Once the clinic logo
is the navy outlined version (see the logo upload section below), use the
light set instead, which is the same contour design on the brand off white:

| File | Size | Use it for |
| --- | --- | --- |
| `bg-light-1920x1080.jpg` | 58 KB | **Recommended.** Desktop landing and registration. |
| `bg-light-2560x1440.jpg` | 93 KB | Very large displays only. |
| `bg-light-mobile-1170x2050.jpg` | 65 KB | Portrait crop for a separate mobile background. |
| `*.webp` | 12 to 18 KB | Same three in WebP, if the upload accepts it. |

Navy text anywhere on the light image measures at least 10:1 contrast. The
centre and upper half are kept calm so the logo and the sign-in card have
somewhere to land, and the mark sits faint in the lower right.

## Colors

| Role | Hex | Notes |
| --- | --- | --- |
| **Header navy** | **`#011B3A`** | **The header color.** Also buttons and primary actions. Sampled from the logo. |
| Secondary slate | `#4C647A` | Accents, secondary buttons, icons. |
| Light mist | `#CED4DA` | Borders and dividers. |
| Off white | `#F5F7F9` | Section backgrounds. |

If the portal only accepts one accent color, use the primary navy `#011B3A`.
White text on that navy measures 17.2:1 contrast, which passes accessibility
standards comfortably.

## Welcome text

Keep it short. Patients read this once, while trying to get somewhere else.

**Short version, if the field is tight:**

> Welcome to Corrective Bodyworks. Book visits, complete your paperwork, follow
> your exercise program, and message your therapist, all in one place.

**Longer version, if there is room:**

> Welcome to Corrective Bodyworks Rehabilitation and Wellness.
>
> This is where you will find your upcoming appointments, your intake paperwork,
> the exercise program your therapist assigned you, and your billing. You can
> also message us directly with any question between visits.
>
> If you have any trouble getting in, call the clinic at (334) 600-2362 and we
> will sort it out.

Adjust the phone number here if it ever changes. It also lives in
`src/data/site.ts` on the website.

## Keeping the two in sync

The website and the portal should feel like one place. The site uses the same
navy and slate, the same logo, and the same voice. If the brand changes, update
both: `src/data/site.ts` and `src/styles/global.css` on the site, and the portal
settings in PT Everywhere.

## Clinic logo upload

PT Everywhere has one logo slot. It renders white-on-navy in the app header
and black-on-white on printed documents and PDFs, so a plain white logo
vanishes on paper and a plain navy logo vanishes in the header.

`logo-horizontal-outlined.png` in this folder is the navy horizontal lockup
with a thin white outline. On the navy header the outline carries the shape;
on a white page the outline disappears into the paper and the navy reads
normally. Upload it under Clinic Settings, General Information, Logo.

The alternative is to change the Header Color on the same page to a light
color, which lets the plain navy `public/logo-horizontal.png` work in both
places. Either works; the outlined file keeps the navy header.
