# Print collateral

Physician-facing pieces for referral outreach. Built from the same brand system
as the website: navy `#011B3A`, slate `#4C647A`, Barlow Condensed over
Source Sans 3, with both faces embedded in the PDFs so they print correctly
anywhere.

| File | Size | Use |
| --- | --- | --- |
| `referral-pad.pdf` | 5.5 x 8.5 in | Prescription pad. Print in pads of 50 or 100, glued at the top edge. |
| `physician-flyer.pdf` | 8.5 x 11 in | Leave-behind one sheet for physician offices. |
| `card-jeff.pdf` | 3.5 x 2 in trim | Business card. Page 1 front, page 2 back. |
| `card-cameron.pdf` | 3.5 x 2 in trim | Same card for Cameron. |

The pad and flyer are exactly one page each. Verified: content height matches
page height, so neither spills a blank second sheet at the printer. Each card
file is two pages, front then back, which is what most printers expect.

### Business card bleed

The card PDFs are **3.75 x 2.25 in, which is 3.5 x 2 in trim plus .125 in of
bleed on all four edges.** Tell the printer the artwork already includes bleed.
There are no crop marks, which is what most online printers want; if yours asks
for marks, say so and they can be added.

All card content sits at least .155 in inside the trim line. The navy stripe on
the front runs off the left edge on purpose: it is .2 in wide in the artwork so
that .075 in of it survives after .125 in is cut away. Do not narrow it, or the
cutter removes it entirely.

## The official logo

These pieces should carry the full lockup, the one that reads
**CORRECTIVE BODYWORKS / REHABILITATION & WELLNESS**, rather than the two line
mark used in the website header.

`logo-full.png` and `logo-full-white.png` are in this folder and every piece
uses them. The source arrived with a clean alpha channel, so it is used as
delivered rather than re-keyed; the ink samples as exactly `#011B3A` and
`#4C647A`.

`build.py` places the logo narrower when the full lockup is present, because it
is three lines and stands taller at any given width. Without that reduction the
referral pad ran four pixels onto a second page.

### Tagline size

The REHABILITATION & WELLNESS line is 13 percent of the lockup's height, so at
the placed widths it renders at roughly:

| Piece | Placed width | Tagline cap height |
| --- | --- | --- |
| Physician flyer | 2.15 in | 8.6 pt |
| Referral pad | 1.32 in | 5.3 pt |
| Business card | 1.26 in | 5.0 pt |

Five points is small but normal for a logo tagline, which registers as part of
the mark rather than being read. On the pad the full clinic name also appears
in the footer at a readable size. On the business card it does not, so if that
line matters there, either enlarge the card logo (which tightens the gap above
the name) or use the two line mark on cards only by removing the two logo-full
files and rebuilding.

## Before printing

Fax is **(334) 625-6578**, set on all four pieces. It appears prominently on the
referral pad, since fax is how most physician offices will actually send one.

There is deliberately **no website address** on either piece. correctiverehab.com
currently serves an under construction placeholder, and sending a physician to a
dead page is worse than omitting the URL. Add it once the site is live, which
means a reprint, so consider printing a smaller first run.

## Claims that need Jeff's sign off

Both pieces state **"We contact every referral within one business day."** That is
the single most persuasive line for a referring physician and the easiest to
break. He has to be able to honor it, including on days he is treating and the
phone goes to voicemail.

The flyer also claims prompt new patient access without naming a number of days.
If he can commit to something specific, such as seen within 48 hours, that is far
stronger and worth adding.

## Regenerating

```
python3 print/build.py     # writes every HTML file next to itself
node print/topdf.mjs print/referral-pad.html     print/referral-pad.pdf     5.5in  8.5in
node print/topdf.mjs print/physician-flyer.html  print/physician-flyer.pdf  8.5in  11in
node print/topdf.mjs print/card-jeff.html        print/card-jeff.pdf        3.75in 2.25in
node print/topdf.mjs print/card-cameron.html     print/card-cameron.pdf     3.75in 2.25in
```

`topdf.mjs` needs playwright available. Verify page counts afterwards: the pad
and flyer must be one page, each card two.

`fonts.css` holds the base64 embedded font faces. Regenerate it only if the
brand typefaces change.

## Printing notes

The pad and flyer are designed for standard digital printing with no bleed: all
content sits within a safe margin and no artwork runs to the paper edge. That
keeps cost down and lets a local shop or an online printer handle them without
special setup. The business cards do use bleed, as described above.

The PDFs are RGB, which every digital printer accepts. If a shop asks for CMYK
they can convert on their end; expect the navy to shift very slightly, which is
normal and will be consistent across all four pieces.
