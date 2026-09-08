# Print collateral

Physician-facing pieces for referral outreach. Built from the same brand system
as the website: navy `#011B3A`, slate `#4C647A`, Barlow Condensed over
Source Sans 3, with both faces embedded in the PDFs so they print correctly
anywhere.

| File | Size | Use |
| --- | --- | --- |
| `referral-pad.pdf` | 5.5 x 8.5 in | Prescription pad. Print in pads of 50 or 100, glued at the top edge. |
| `physician-flyer.pdf` | 8.5 x 11 in | Leave-behind one sheet for physician offices. |

Both are exactly one page. Verified: content height matches page height, so
neither spills a blank second sheet at the printer.

## Before printing

Two placeholders are marked in red as `[FAX]` and must be replaced:

- **Fax number.** A referral pad without a fax is close to useless, since fax is
  still how most physician offices send referrals. PT Everywhere has fax
  management built in, so there may already be a number on the account.

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
python3 print/build.py            # writes the HTML
node print/topdf.mjs print/referral-pad.html print/referral-pad.pdf 5.5in 8.5in
node print/topdf.mjs print/physician-flyer.html print/physician-flyer.pdf 8.5in 11in
```

`fonts.css` holds the base64 embedded font faces. Regenerate it only if the
brand typefaces change.

## Printing notes

Both are designed for standard digital printing with no bleed: all content sits
within a safe margin, and there is no artwork running to the paper edge. That
keeps cost down and lets a local shop or an online printer handle it without
special setup. Two ink colors plus black on white stock.
