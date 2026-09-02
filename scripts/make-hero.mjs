// Crops a source photo to the hero's 4:5 portrait and writes an optimised JPEG.
//   node scripts/make-hero.mjs <source> [focusX]
// focusX is where the subject sits horizontally, 0 to 1, default 0.55.
import { execFileSync } from 'node:child_process';
const [src, focus = '0.55'] = process.argv.slice(2);
if (!src) { console.error('usage: node scripts/make-hero.mjs <source> [focusX]'); process.exit(1); }
execFileSync('python3', ['-c', `
import sys
from PIL import Image
src, focus = sys.argv[1], float(sys.argv[2])
im = Image.open(src).convert('RGB')
w, h = im.size
tw = int(h * 0.8)                      # 4:5 portrait
if tw <= w:
    x0 = max(0, min(w - tw, int(w * focus) - tw // 2))
    box = (x0, 0, x0 + tw, h)
else:                                   # source is already tall
    th = int(w / 0.8)
    y0 = max(0, min(h - th, 0))
    box = (0, y0, w, y0 + th)
out = im.crop(box).resize((900, 1125), Image.LANCZOS)
out.save('public/jeff-hero.jpg', 'JPEG', quality=84, optimize=True, progressive=True)
print('wrote public/jeff-hero.jpg from', src, 'crop', box)
`, src, focus], { stdio: 'inherit' });
