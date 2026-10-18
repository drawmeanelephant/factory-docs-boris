const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

const source = fs.readFileSync(
  path.join(__dirname, '../themes/factory/assets/js/factory.js'), 'utf8'
);
const searchClient = source.slice(source.indexOf('  // 9. Language-Scoped'));
assert.ok(searchClient.startsWith('  // 9. Language-Scoped'));

class Element {
  constructor(tag = 'div') {
    this.tagName = tag;
    this.children = [];
    this.listeners = {};
    this.hidden = true;
    this.value = '';
    this.textContent = '';
  }
  addEventListener(name, listener) { this.listeners[name] = listener; }
  appendChild(child) { this.children.push(child); }
  setAttribute(name, value) { this[name] = value; }
  set innerHTML(value) {
    assert.equal(value, '');
    this.children = [];
  }
}

function section(text, code = '', heading = '') {
  return { level: 2, heading, fragment: 'section', text, code };
}

function index(documents) {
  return { format: 'boris-rendered-search-index', schema_version: 1, documents };
}

function response(body, ok = true) {
  return { ok, json: async () => body };
}

function createClient(body, options = {}) {
  const input = new Element('input');
  const results = new Element();
  const document = new Element();
  document.getElementById = id => ({
    'boris-ui-search-input': input,
    'boris-ui-search-results': results
  })[id];
  document.createElement = tag => new Element(tag);
  const requests = [];
  const fetch = url => {
    requests.push(url);
    return options.fetch ? options.fetch(url) : Promise.resolve(response(body));
  };
  vm.runInNewContext('(function () {' + searchClient, {
    document, fetch, isJp: options.isJp || false,
    rootPrefix: options.rootPrefix || ''
  });
  const flush = () => new Promise(resolve => setImmediate(resolve));
  return {
    input, results, requests,
    async query(value) {
      input.value = value;
      input.listeners.input();
      await flush();
    },
    async escape() {
      document.listeners.keydown({ key: 'Escape' });
      await flush();
    },
    flush,
    hits: () => results.children.filter(child => child.className === 'factory-search-hit')
  };
}

const documents = [
  {
    path: 'benchmarks/boris-migration-report.html',
    title: 'Boris Migration & Benchmark Report',
    sections: [section('Local compile speed and validation timings.')]
  },
  {
    path: 'cli/getting-started/quickstart.html',
    title: 'Quickstart',
    sections: [section('Install the CLI.', 'sudo apt-get install xdg-utils')]
  },
  {
    path: 'jp/cli/getting-started/quickstart.html',
    title: 'クイックスタート',
    sections: [section('インストール手順', 'sudo apt-get install xdg-utils')]
  }
];

test('finds the report by title and links from a nested page', async () => {
  const client = createClient(index(documents), { rootPrefix: '../../' });
  await client.query('benchmark report');
  const hit = client.hits()[0];
  assert.equal(hit.children[0].textContent, documents[0].title);
  assert.equal(hit.href, '../../benchmarks/boris-migration-report.html');
  assert.equal(hit.children[1].textContent, 'benchmarks/boris-migration-report');
  assert.equal(new URL(hit.href, 'https://example.com/docs/cli/getting-started/quickstart.html').pathname,
    '/docs/benchmarks/boris-migration-report.html');
  assert.equal(client.requests[0], '../../_boris/search/search-index.json');
});

test('searches prose, headings, paths, and code with useful snippets', async () => {
  const extra = {
    path: 'reference/special-route.html', title: 'Reference',
    sections: [section('General introduction.'), section('Details.', '', 'Distinctive heading')]
  };
  const client = createClient(index([...documents, extra]));
  await client.query('compile speed');
  assert.equal(client.hits()[0].children[2].textContent.includes('compile speed'), true);
  await client.query('xdg-utils');
  assert.equal(client.hits().length, 1);
  assert.match(client.hits()[0].children[2].textContent, /xdg-utils/);
  await client.query('distinctive');
  assert.match(client.hits()[0].children[2].textContent, /Distinctive heading/);
  await client.query('special-route');
  assert.equal(client.hits()[0].href, extra.path);
});

test('filters both languages using canonical paths', async () => {
  const jp = createClient(index(documents), { isJp: true, rootPrefix: '../../../' });
  await jp.query('クイックスタート');
  assert.equal(jp.hits().length, 1);
  assert.equal(jp.hits()[0].href, '../../../jp/cli/getting-started/quickstart.html');
  await jp.query('xdg-utils');
  assert.equal(jp.hits().length, 1);
  assert.match(jp.hits()[0].href, /jp\//);
  const en = createClient(index(documents));
  await en.query('クイックスタート');
  assert.equal(en.hits().length, 0);
});

test('ranks title matches before body matches and caps results', async () => {
  const many = Array.from({ length: 15 }, (_, i) => ({
    path: `reference/page-${i}.html`, title: 'Other page', sections: [section('boris')]
  }));
  const client = createClient(index([...many, documents[0]]));
  await client.query('BORIS');
  assert.equal(client.hits().length, 12);
  assert.equal(client.hits()[0].children[0].textContent, documents[0].title);
});

test('encodes path segments and renders indexed text without HTML injection', async () => {
  const client = createClient(index([{
    path: 'reference/日本語&tips.html', title: '<img src=x onerror=alert(1)>',
    sections: [section('Example')]
  }]));
  await client.query('example');
  assert.equal(client.hits()[0].href, 'reference/%E6%97%A5%E6%9C%AC%E8%AA%9E%26tips.html');
  assert.equal(client.hits()[0].children[0].textContent, '<img src=x onerror=alert(1)>');
  assert.equal(client.hits()[0].children[0].children.length, 0);
});

test('shows empty and no-match states, and hides cleared queries', async () => {
  const empty = createClient(index([]));
  await empty.query('missing');
  assert.equal(empty.results.children[0].textContent, 'No matching pages found.');
  assert.equal(empty.results.hidden, false);
  await empty.query('  ');
  assert.equal(empty.results.hidden, true);
  assert.equal(empty.results.children.length, 0);
});

test('rejects unsupported or malformed indexes rather than using partial results', async () => {
  const badSection = { ...documents[0], sections: [{ ...section('text'), level: '2' }] };
  const invalid = [
    { ...index(documents), format: 'wrong' },
    { ...index(documents), schema_version: 2 },
    { ...index(documents), documents: {} },
    index([documents[0], { ...documents[1], title: null }]),
    index([badSection]),
    ...['../secret.html', '/absolute.html', 'nested//page.html', 'page.html#fragment',
      'page.html?query', 'nested\\page.html', 'page.txt'].map(p =>
      index([{ ...documents[0], path: p }]))
  ];
  for (const body of invalid) {
    const client = createClient(body);
    await client.query('boris');
    assert.equal(client.hits().length, 0);
    assert.match(client.results.children[0].textContent, /could not be loaded/);
  }
});

test('reports load errors and retries on subsequent input', async () => {
  let attempts = 0;
  const client = createClient(null, {
    fetch: async () => ++attempts === 1 ? response(null, false) : response(index(documents))
  });
  await client.query('boris');
  assert.match(client.results.children[0].textContent, /Type again to retry/);
  await client.query('boris');
  assert.equal(client.hits().length, 1);
  assert.equal(attempts, 2);
  const failed = createClient(null, { isJp: true, fetch: async () => { throw new Error('offline'); } });
  await failed.query('anything');
  assert.match(failed.results.children[0].textContent, /検索を読み込めませんでした/);
});

test('does not reopen cleared or dismissed searches when loading finishes', async () => {
  for (const dismiss of ['clear', 'escape']) {
    let finish;
    const client = createClient(null, { fetch: () => new Promise(resolve => { finish = resolve; }) });
    await client.query('boris');
    if (dismiss === 'clear') await client.query('');
    else await client.escape();
    finish(response(index(documents)));
    await client.flush();
    assert.equal(client.results.hidden, true);
    assert.equal(client.hits().length, 0);
  }
});

test('uses the latest query and fetches the index only once', async () => {
  let finish;
  const client = createClient(null, { fetch: () => new Promise(resolve => { finish = resolve; }) });
  await client.query('boris');
  await client.query('quickstart');
  finish(response(index(documents)));
  await client.flush();
  assert.equal(client.hits().length, 1);
  assert.equal(client.hits()[0].children[0].textContent, 'Quickstart');
  assert.equal(client.requests.length, 1);
});
