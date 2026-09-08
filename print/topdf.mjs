import { chromium } from 'playwright';
const [src, pdf, w, h, png] = process.argv.slice(2);
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const p = await b.newPage();
await p.goto('file://' + src, { waitUntil: 'load' });
await p.evaluate(() => document.fonts.ready);
await p.waitForTimeout(800);
await p.pdf({ path: pdf, width: w, height: h, printBackground: true,
              margin: { top: '0', bottom: '0', left: '0', right: '0' } });
if (png) {
  await p.setViewportSize({ width: Math.round(parseFloat(w) * 96), height: Math.round(parseFloat(h) * 96) });
  await p.screenshot({ path: png });
}
await b.close();
console.log('pdf written');
