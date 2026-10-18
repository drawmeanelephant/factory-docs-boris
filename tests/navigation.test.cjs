const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

const source = fs.readFileSync(
  path.join(__dirname, '../themes/factory/assets/js/factory.js'), 'utf8'
);
const start = source.indexOf('  // 2. Canonical URL & Route Map');
const end = source.indexOf('  // 3. Interactive Language Switcher');
assert.ok(start !== -1 && end > start);
const routes = [
  'index', 'welcome/index', 'cli/getting-started/quickstart',
  'jp/index', 'jp/welcome/index', 'jp/cli/getting-started/quickstart'
];

function routeClient(currentId, basePath = '') {
  const page = currentId + '.html';
  const canonical = 'https://example.com' + basePath + '/' + page;
  const links = routes.map(id => ({
    textContent: id,
    parentElement: {},
    getAttribute(name) {
      if (name === 'href') return path.posix.relative(path.posix.dirname(page), id + '.html');
      if (name === 'aria-current') return id === currentId ? 'page' : null;
      return null;
    }
  }));
  const document = {
    documentElement: { setAttribute() {} },
    querySelector(selector) {
      if (selector === 'link[rel="canonical"]') return { getAttribute: () => canonical };
      if (selector === '.site-nav') return { querySelectorAll: () => links };
      return null;
    }
  };
  const depth = currentId.split('/').length - 1;
  return vm.runInNewContext(
    '(function () {' + source.slice(start, end) +
    '; return { currentId, isJp, routeMap, routeHref, hrefToPageId }; })()',
    { document, URL, rootPrefix: '../'.repeat(depth), window: { location: { href: canonical } } }
  );
}

for (const basePath of ['', '/factory-docs-boris']) {
  test(`navigation and locale IDs exclude the deployment prefix "${basePath}"`, () => {
    for (const currentId of routes) {
      const client = routeClient(currentId, basePath);
      assert.equal(client.currentId, currentId);
      assert.equal(client.isJp, currentId.startsWith('jp/'));
      assert.deepEqual(Object.keys(client.routeMap), routes);
      const target = currentId.startsWith('jp/') ? 'welcome/index' : 'jp/welcome/index';
      const actual = new URL(client.routeHref(target),
        'https://example.com' + basePath + '/' + currentId + '.html');
      assert.equal(actual.pathname, basePath + '/' + target + '.html');
    }
  });
}

test('ignores navigation paths outside the configured publication root', () => {
  const client = routeClient('cli/getting-started/quickstart', '/factory-docs-boris');
  assert.equal(client.hrefToPageId('https://example.com/other/index.html'), '');
});
