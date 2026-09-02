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

| File | Use it for |
| --- | --- |
| `bg-landing-2560x1440.jpg` | Primary. Wide desktop landing or login background, 16:9. |
| `bg-landing-1920x1080.jpg` | Same image at 1080p, if there is an upload size limit. |
| `bg-landing-mobile-1170x2050.jpg` | Portrait crop, if the portal takes a separate mobile background. |

Designed to sit under content rather than compete with it. The left and centre
are deliberately calm so a login card or welcome panel has somewhere to land,
and the cross and tree mark sits quietly in the right third. White text placed
anywhere on the image measures at worst 10.9:1 contrast, comfortably past the
4.5:1 accessibility threshold, so overlaid copy stays readable wherever the
portal decides to put it.

If the portal crops rather than letterboxes, it will crop toward the centre,
which keeps the composition intact. The design rationale is in
`DESIGN-PHILOSOPHY.md`.

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
> If you have any trouble getting in, call the clinic at (334) 319-1684 and we
> will sort it out.

Adjust the phone number here if it ever changes. It also lives in
`src/data/site.ts` on the website.

## Keeping the two in sync

The website and the portal should feel like one place. The site uses the same
navy and slate, the same logo, and the same voice. If the brand changes, update
both: `src/data/site.ts` and `src/styles/global.css` on the site, and the portal
settings in PT Everywhere.
