import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { buildIndex, search, normalise } from '../js/search.js';

const read = f => JSON.parse(readFileSync(new URL(`../data/${f}.json`, import.meta.url), 'utf8'));
const index = buildIndex([read('ch05')], read('terms'));

test('a Chinese query finds the chapter, titled in the reading language', () => {
  const hits = search(index, '露点', 'ms');
  assert.ok(hits.length > 0);
  assert.ok(hits.some(h => h.route.startsWith('#/ch/ch05')));
  assert.ok(hits.every(h => !/[一-鿿]/.test(h.title)), `titles not in Malay: ${hits.map(h => h.title)}`);
});
test('Latin search ignores case and accents', () => {
  assert.ok(search(index, 'DEW POINT', 'en').length > 0);
  assert.equal(normalise('Évaporation'), 'evaporation');
});
test('all words must match', () => {
  assert.ok(search(index, 'dew point', 'en').length > 0);
  assert.equal(search(index, 'dew zebra', 'en').length, 0);
});
test('term markup is searchable by what the reader sees', () => {
  assert.ok(search(index, 'Takat embun', 'ms').some(h => h.route.startsWith('#/ch/ch05')));
});
test('snippets contain no raw markup', () => {
  for (const h of search(index, 'vapour', 'en')) assert.ok(!h.snippet.includes('{{'), h.snippet);
});
test('empty query returns nothing', () => assert.deepEqual(search(index, '  ', 'en'), []));
