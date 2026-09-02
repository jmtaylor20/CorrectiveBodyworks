// House style: no em dash (U+2014) or en dash (U+2013) anywhere, including comments
// and generated output. Use a comma, colon, parentheses, a new sentence, or
// the word "to" for ranges. Regular hyphens in compound words are fine.
import { readdirSync, statSync, readFileSync } from 'node:fs';
import { join, extname } from 'node:path';

const ROOTS = ['src', 'scripts', 'brand'];
const FILES = ['README.md', 'astro.config.mjs', 'netlify.toml'];
const EXT = new Set(['.astro', '.ts', '.js', '.mjs', '.css', '.md', '.html', '.toml', '.json']);
const BAD = /[\u2014\u2013]/g;

const walk = dir => {
  let out = [];
  for (const e of readdirSync(dir)) {
    const p = join(dir, e);
    if (statSync(p).isDirectory()) out = out.concat(walk(p));
    else if (EXT.has(extname(p))) out.push(p);
  }
  return out;
};

const targets = [...ROOTS.flatMap(r => { try { return walk(r); } catch { return []; } }), ...FILES];
const hits = [];

for (const file of targets) {
  let text;
  try { text = readFileSync(file, 'utf8'); } catch { continue; }
  text.split('\n').forEach((line, i) => {
    if (BAD.test(line)) {
      BAD.lastIndex = 0;
      hits.push(`${file}:${i + 1}: ${line.trim().slice(0, 100)}`);
    }
  });
}

if (hits.length) {
  console.error(`\n✗ Found ${hits.length} em/en dash(es). House style forbids them.\n`);
  hits.forEach(h => console.error('  ' + h));
  console.error('\n  Use a comma, a colon, parentheses, a new sentence, or "to" for ranges.\n');
  process.exit(1);
}
console.log('✓ no em or en dashes found');
