/* Inline markup inside content strings.

   {{t:dew-point}}         a tappable glossary term, shown by its name
   {{t:lcl|cloud base}}    the same, with different visible words

   Pure: the renderer and the content linter both use it. */

const RE = /\{\{t:([a-z0-9-]+)(?:\|([^}]*))?\}\}/g;

export function parseInline(str) {
  const out = [];
  let last = 0;
  for (const m of String(str ?? '').matchAll(RE)) {
    if (m.index > last) out.push({ text: str.slice(last, m.index) });
    out.push(m[2] === undefined ? { term: m[1] } : { term: m[1], label: m[2] });
    last = m.index + m[0].length;
  }
  if (last < String(str ?? '').length) out.push({ text: str.slice(last) });
  return out;
}

export function termIds(str) {
  return [...String(str ?? '').matchAll(RE)].map(m => m[1]);
}
