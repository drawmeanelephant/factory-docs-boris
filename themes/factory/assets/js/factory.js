(function () {
  var scripts = document.getElementsByTagName('script');
  var rootPrefix = '';
  for (var s = 0; s < scripts.length; s++) {
    var src = scripts[s].getAttribute('src') || '';
    var idx = src.indexOf('assets/js/factory.js');
    if (idx !== -1) {
      rootPrefix = src.slice(0, idx);
      break;
    }
  }

  // Mintlify docs.json navigation structure for EN and JP
  var NAV_SPEC = {
    en: {
      tabs: [
        { key: 'docs', label: 'Docs', entry: 'welcome/index' },
        { key: 'guides', label: 'Guides', entry: 'guides/power-user/setup-checklist' },
        { key: 'changelog', label: 'Changelog', entry: 'changelog/release-notes' },
        { key: 'benchmarks', label: 'Benchmarks', entry: 'benchmarks/boris-migration-report' },
        { key: 'api-reference', label: 'API Reference', entry: 'api-reference/index' }
      ],
      topbarLinks: [
        { id: 'models', label: 'Available Models' },
        { id: 'enterprise/index', label: 'Enterprise' }
      ],
      sections: {
        docs: [
          {
            group: 'Start Here',
            pages: ['welcome/index', 'models']
          },
          {
            group: 'Platform',
            pages: [
              {
                group: 'Droid CLI',
                pages: ['cli/getting-started/overview', 'cli/getting-started/quickstart']
              },
              {
                group: 'Factory App',
                pages: ['web/getting-started/overview', 'web/getting-started/quickstart']
              },
              'web/factory-router',
              'cli/droid-exec/overview',
              {
                group: 'Droid Computers',
                pages: ['cli/features/droid-computers', 'cli/features/droid-computers-byom']
              },
              'web/machine-connection/cloud-templates/index'
            ]
          },
          {
            group: 'Capabilities',
            pages: [
              {
                group: 'Agent Readiness',
                pages: [
                  'web/agent-readiness/overview',
                  'cli/features/readiness-report',
                  'web/agent-readiness/dashboard'
                ]
              },
              {
                group: 'Factory Missions',
                pages: [
                  'features/missions/overview',
                  'features/missions/planning',
                  'cli/features/missions/running-cli',
                  'web/missions',
                  'features/missions/troubleshooting',
                  'features/missions/reference'
                ]
              },
              'web/software-factory',
              'web/automations',
              {
                group: 'AutoWiki',
                pages: [
                  'cli/features/wiki/overview',
                  'cli/features/wiki/generate',
                  'cli/features/wiki/web-viewer',
                  'cli/features/wiki/auto-refresh'
                ]
              },
              'guides/droid-exec/code-review',
              'cli/features/code-review',
              'cli/features/incident-response',
              'enterprise/security-review',
              'cli/features/droid-control',
              'guides/skills/automated-qa',
              'cli/account/droid-shield'
            ]
          },
          {
            group: 'Configure & Extend',
            pages: [
              'cli/user-guides/auto-run',
              'cli/configuration/sandbox',
              'cli/configuration/settings',
              'cli/configuration/agents-md',
              'cli/configuration/skills',
              'cli/configuration/mcp',
              'cli/configuration/custom-droids',
              'cli/configuration/hooks-guide',
              'cli/configuration/custom-slash-commands',
              'cli/configuration/plugins',
              'cli/configuration/mixed-models',
              {
                group: 'Bring Your Own Key',
                pages: [
                  'cli/byok/overview',
                  'cli/byok/baseten',
                  'cli/byok/deepinfra',
                  'cli/byok/fireworks',
                  'cli/byok/google-gemini',
                  'cli/byok/groq',
                  'cli/byok/huggingface',
                  'cli/byok/lm-studio',
                  'cli/byok/ollama',
                  'cli/byok/openai-anthropic',
                  'cli/byok/openrouter'
                ]
              }
            ]
          },
          {
            group: 'Integrations',
            pages: [
              'integrations/ide-integrations',
              'integrations/jetbrains',
              'integrations/zed',
              'integrations/linear',
              'integrations/slack',
              'onboarding/integrating-with-your-engineering-system/gitlab-self-hosted',
              'onboarding/integrating-with-your-engineering-system/github-enterprise-server'
            ]
          },
          {
            group: 'Enterprise',
            pages: [
              'enterprise/index',
              {
                group: 'Security',
                pages: [
                  'cli/account/security',
                  'cli/account/droid-shield-plus',
                  'enterprise/privacy-and-data-flows',
                  'enterprise/llm-safety-and-agent-controls'
                ]
              },
              {
                group: 'Identity & Governance',
                pages: [
                  'enterprise/identity-and-access',
                  'enterprise/identity-sso-and-scim',
                  'enterprise/service-accounts',
                  'enterprise/hierarchical-settings-and-org-control'
                ]
              },
              {
                group: 'Architecture & Deployment',
                pages: [
                  'enterprise/network-and-deployment',
                  'enterprise/eu-deployment',
                  'enterprise/models-llm-gateways-and-integrations',
                  'enterprise/enterprise-plugin-registry',
                  'enterprise/github-integration-security'
                ]
              },
              {
                group: 'Analytics & Compliance',
                pages: [
                  'enterprise/usage-cost-and-analytics',
                  'enterprise/telemetry-export',
                  'enterprise/compliance-audit-and-monitoring',
                  'enterprise/audit-log'
                ]
              }
            ]
          },
          {
            group: 'Using Droid',
            pages: [
              'cli/getting-started/common-use-cases',
              'cli/getting-started/how-to-talk-to-a-droid',
              'cli/getting-started/video-walkthrough',
              {
                group: 'Advanced Usage',
                pages: [
                  'cli/user-guides/become-a-power-user',
                  'cli/user-guides/specification-mode',
                  'cli/user-guides/implementing-large-features'
                ]
              }
            ]
          },
          {
            group: 'Reference',
            pages: [
              'reference/cli-reference',
              'reference/hooks-reference',
              'reference/analytics-api',
              'reference/readiness-reports-api'
            ]
          }
        ],
        guides: [
          {
            group: 'Power User',
            pages: [
              'guides/power-user/setup-checklist',
              'guides/power-user/memory-management',
              'guides/power-user/rules-conventions',
              'guides/power-user/prompt-crafting',
              'guides/power-user/token-efficiency',
              'guides/power-user/evaluating-context-compression'
            ]
          },
          {
            group: 'Building',
            pages: [
              'guides/building/building-plugins',
              'guides/building/droid-exec-tutorial'
            ]
          },
          {
            group: 'Skills',
            pages: [
              'guides/skills/frontend-ui-integration',
              'guides/skills/service-integration',
              'guides/skills/data-querying',
              'guides/skills/internal-tools',
              'guides/skills/vibe-coding',
              'guides/skills/ai-data-analyst',
              'guides/skills/product-management',
              'guides/skills/browser'
            ]
          },
          {
            group: 'Hooks',
            pages: [
              'guides/hooks/auto-formatting',
              'guides/hooks/code-validation',
              'guides/hooks/documentation-sync',
              'guides/hooks/git-workflows',
              'guides/hooks/logging-analytics',
              'guides/hooks/notifications',
              'guides/hooks/session-automation',
              'guides/hooks/testing-automation'
            ]
          },
          {
            group: 'Droid Exec (Headless)',
            pages: [
              'guides/droid-exec/refactor-imports',
              'guides/droid-exec/refactor-error-messages',
              'guides/droid-exec/refactor-fix-lint',
              'guides/droid-exec/document-automation',
              'guides/droid-exec/github-actions',
              'guides/building/droid-vps-setup'
            ]
          }
        ],
        changelog: [
          {
            group: 'Changelog',
            pages: [
              'changelog/release-notes',
              'changelog/1-10',
              'changelog/1-9',
              'changelog/1-8'
            ]
          }
        ],
        benchmarks: [
          {
            group: 'Benchmarks',
            pages: [
              'benchmarks/boris-migration-report',
              'benchmarks/terminal-bench',
              'benchmarks/nextjs-eval',
              'benchmarks/agent-arena',
              'benchmarks/review-benchmark',
              'benchmarks/legacy-bench'
            ]
          }
        ]
      }
    },
    jp: {
      tabs: [
        { key: 'docs', label: 'ドキュメント', entry: 'jp/welcome/index' },
        { key: 'guides', label: 'ガイド', entry: 'jp/guides/power-user/setup-checklist' },
        { key: 'changelog', label: '変更履歴', entry: 'jp/changelog/release-notes' },
        { key: 'benchmarks', label: 'ベンチマーク', entry: 'jp/benchmarks/terminal-bench' },
        { key: 'api-reference', label: 'APIリファレンス', entry: 'jp/api-reference/index' }
      ],
      topbarLinks: [
        { id: 'jp/models', label: '利用可能なモデル' },
        { id: 'jp/enterprise/index', label: 'エンタープライズ' }
      ],
      sections: {
        docs: [
          {
            group: 'ようこそ',
            pages: [
              'jp/welcome/index',
              {
                group: 'CLI',
                pages: [
                  'jp/cli/getting-started/overview',
                  'jp/cli/getting-started/quickstart',
                  {
                    group: '設定',
                    pages: [
                      'jp/cli/configuration/agents-md',
                      'jp/cli/configuration/settings',
                      {
                        group: '独自キーの使用',
                        pages: [
                          'jp/cli/byok/overview',
                          'jp/cli/byok/baseten',
                          'jp/cli/byok/deepinfra',
                          'jp/cli/byok/fireworks',
                          'jp/cli/byok/google-gemini',
                          'jp/cli/byok/groq',
                          'jp/cli/byok/huggingface',
                          'jp/cli/byok/ollama',
                          'jp/cli/byok/openai-anthropic',
                          'jp/cli/byok/openrouter'
                        ]
                      }
                    ]
                  },
                  {
                    group: 'アカウント',
                    pages: [
                      'jp/cli/account/security',
                      'jp/cli/account/droid-shield',
                      'jp/cli/account/droid-shield-plus'
                    ]
                  }
                ]
              },
              {
                group: 'アプリ',
                pages: [
                  'jp/web/getting-started/overview',
                  'jp/web/getting-started/quickstart'
                ]
              },
              'jp/models'
            ]
          },
          {
            group: 'インテグレーション',
            pages: [
              'jp/integrations/ide-integrations',
              'jp/integrations/jetbrains',
              'jp/integrations/zed',
              'jp/integrations/linear',
              'jp/integrations/slack'
            ]
          },
          {
            group: '機能',
            pages: [
              {
                group: 'エージェント準備状況',
                pages: [
                  'jp/web/agent-readiness/overview',
                  'jp/cli/features/readiness-report',
                  'jp/web/agent-readiness/dashboard',
                  'jp/reference/readiness-reports-api'
                ]
              },
              {
                group: 'Factory Missions',
                pages: [
                  'jp/features/missions/overview',
                  'jp/features/missions/planning',
                  'jp/cli/features/missions/running-cli',
                  'jp/web/missions',
                  'jp/features/missions/troubleshooting',
                  'jp/features/missions/reference'
                ]
              },
              'jp/guides/droid-exec/code-review',
              'jp/cli/features/code-review',
              'jp/cli/features/droid-control',
              'jp/cli/features/droid-computers',
              'jp/cli/features/droid-computers-byom',
              'jp/web/machine-connection/cloud-templates/index',
              'jp/guides/skills/automated-qa',
              'jp/cli/configuration/plugins',
              'jp/cli/configuration/custom-slash-commands',
              'jp/cli/configuration/custom-droids',
              'jp/cli/configuration/skills',
              'jp/cli/configuration/mixed-models',
              'jp/cli/configuration/mcp',
              'jp/cli/configuration/hooks-guide',
              'jp/cli/droid-exec/overview'
            ]
          },
          {
            group: 'リファレンス',
            pages: [
              'jp/reference/cli-reference',
              'jp/reference/hooks-reference'
            ]
          },
          {
            group: 'エンタープライズ',
            pages: [
              'jp/enterprise/index',
              {
                group: 'アーキテクチャとデプロイ',
                pages: [
                  'jp/enterprise/network-and-deployment',
                  'jp/enterprise/models-llm-gateways-and-integrations'
                ]
              },
              {
                group: 'セキュリティとガバナンス',
                pages: [
                  'jp/enterprise/identity-and-access',
                  'jp/enterprise/identity-sso-and-scim',
                  'jp/enterprise/privacy-and-data-flows',
                  'jp/enterprise/llm-safety-and-agent-controls',
                  'jp/enterprise/hierarchical-settings-and-org-control',
                  'jp/enterprise/enterprise-plugin-registry',
                  'jp/enterprise/compliance-audit-and-monitoring',
                  'jp/enterprise/github-integration-security'
                ]
              },
              {
                group: '分析と運用',
                pages: [
                  'jp/enterprise/usage-cost-and-analytics',
                  'jp/enterprise/telemetry-export',
                  'jp/reference/analytics-api'
                ]
              }
            ]
          },
          {
            group: 'リソース',
            pages: [
              {
                group: 'リソース',
                pages: [
                  'jp/cli/getting-started/video-walkthrough',
                  'jp/cli/getting-started/how-to-talk-to-a-droid',
                  'jp/cli/getting-started/common-use-cases'
                ]
              },
              {
                group: 'ユーザーガイド',
                pages: [
                  'jp/cli/user-guides/become-a-power-user',
                  'jp/cli/user-guides/specification-mode',
                  'jp/cli/user-guides/auto-run',
                  'jp/cli/user-guides/choosing-your-model',
                  'jp/cli/user-guides/implementing-large-features'
                ]
              }
            ]
          }
        ],
        guides: [
          {
            group: 'パワーユーザー',
            pages: [
              'jp/guides/power-user/setup-checklist',
              'jp/guides/power-user/memory-management',
              'jp/guides/power-user/rules-conventions',
              'jp/guides/power-user/prompt-crafting',
              'jp/guides/power-user/token-efficiency',
              'jp/guides/power-user/evaluating-context-compression'
            ]
          },
          {
            group: '構築',
            pages: [
              'jp/guides/building/building-plugins',
              'jp/guides/building/droid-exec-tutorial',
              'jp/guides/building/droid-vps-setup'
            ]
          },
          {
            group: 'スキル',
            pages: [
              'jp/guides/skills/frontend-ui-integration',
              'jp/guides/skills/service-integration',
              'jp/guides/skills/data-querying',
              'jp/guides/skills/internal-tools',
              'jp/guides/skills/vibe-coding',
              'jp/guides/skills/ai-data-analyst',
              'jp/guides/skills/product-management',
              'jp/guides/skills/browser'
            ]
          },
          {
            group: 'フック',
            pages: [
              'jp/guides/hooks/auto-formatting',
              'jp/guides/hooks/code-validation',
              'jp/guides/hooks/documentation-sync',
              'jp/guides/hooks/git-workflows',
              'jp/guides/hooks/logging-analytics',
              'jp/guides/hooks/notifications',
              'jp/guides/hooks/session-automation',
              'jp/guides/hooks/testing-automation'
            ]
          },
          {
            group: 'Droid Exec（ヘッドレス）',
            pages: [
              'jp/guides/droid-exec/refactor-imports',
              'jp/guides/droid-exec/refactor-error-messages',
              'jp/guides/droid-exec/refactor-fix-lint',
              'jp/guides/droid-exec/document-automation',
              'jp/guides/droid-exec/github-actions'
            ]
          }
        ],
        changelog: [
          {
            group: '変更履歴',
            pages: [
              'jp/changelog/release-notes',
              'jp/changelog/1-10',
              'jp/changelog/1-9',
              'jp/changelog/1-8'
            ]
          }
        ],
        benchmarks: [
          {
            group: 'ベンチマーク',
            pages: [
              'jp/benchmarks/terminal-bench',
              'jp/benchmarks/nextjs-eval',
              'jp/benchmarks/agent-arena',
              'jp/benchmarks/review-benchmark',
              'jp/benchmarks/legacy-bench'
            ]
          }
        ]
      }
    }
  };

  // 1. Theme toggle
  var savedTheme = null;
  try {
    savedTheme = localStorage.getItem('factory-docs-theme');
  } catch (e) {}
  if (savedTheme === 'light' || savedTheme === 'dark') {
    document.documentElement.setAttribute('data-theme', savedTheme);
  }
  var themeBtn = document.getElementById('boris-ui-theme-toggle');
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var cur = document.documentElement.getAttribute('data-theme') || 'dark';
      var next = cur === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      try {
        localStorage.setItem('factory-docs-theme', next);
      } catch (e) {}
    });
  }

  // 2. Canonical URL & Route Map from Boris <nav class="site-nav">
  var canonicalEl = document.querySelector('link[rel="canonical"]');
  var canonicalBase = (canonicalEl && canonicalEl.getAttribute('href')) || window.location.href;
  var siteRootPath = new URL(rootPrefix || './', canonicalBase).pathname;

  function hrefToPageId(href) {
    if (!href) return '';
    try {
      var u = new URL(href, canonicalBase);
      if (u.pathname.indexOf(siteRootPath) !== 0) return '';
      return u.pathname.slice(siteRootPath.length).replace(/\.html$/, '');
    } catch (e) {
      return '';
    }
  }

  function routeHref(pageId) {
    if (routeMap[pageId] && routeMap[pageId].href) {
      return routeMap[pageId].href;
    }
    return rootPrefix + pageId + '.html';
  }

  var siteNav = document.querySelector('.site-nav');
  var routeMap = {};
  var currentId = hrefToPageId(canonicalBase);

  if (siteNav) {
    var rawLinks = siteNav.querySelectorAll('a');
    for (var i = 0; i < rawLinks.length; i++) {
      var a = rawLinks[i];
      var pid = hrefToPageId(a.getAttribute('href'));
      if (!pid) continue;
      routeMap[pid] = {
        id: pid,
        href: a.getAttribute('href'),
        title: (a.textContent || '').trim(),
        li: a.parentElement
      };
      if (a.getAttribute('aria-current') === 'page') {
        currentId = pid;
      }
    }
  }

  var isJp = (currentId === 'jp/index' || currentId.indexOf('jp/') === 0);
  var langKey = isJp ? 'jp' : 'en';
  document.documentElement.setAttribute('lang', isJp ? 'ja' : 'en');

  // 3. Interactive Language Switcher Dropdown (English <-> 日本語)
  var langBadge = document.getElementById('boris-ui-lang-badge');
  var langLabel = document.getElementById('boris-ui-lang-label');
  var langMenu = document.getElementById('boris-ui-lang-menu');
  var langEnLink = document.getElementById('boris-ui-lang-en');
  var langJpLink = document.getElementById('boris-ui-lang-jp');
  var langSwitcher = document.getElementById('boris-ui-lang-switcher');

  var enTargetId = 'welcome/index';
  var jpTargetId = 'jp/welcome/index';

  if (isJp) {
    jpTargetId = currentId;
    var stripped = (currentId === 'jp/index') ? 'welcome/index' : currentId.replace(/^jp\//, '');
    if (routeMap[stripped]) {
      enTargetId = stripped;
    } else if (routeMap['index']) {
      enTargetId = 'welcome/index';
    }
  } else {
    enTargetId = currentId;
    var candidateJp = (currentId === 'index') ? 'jp/welcome/index' : ('jp/' + currentId);
    if (routeMap[candidateJp]) {
      jpTargetId = candidateJp;
    } else if (currentId.indexOf('benchmarks/') === 0 && routeMap['jp/benchmarks/terminal-bench']) {
      jpTargetId = 'jp/benchmarks/terminal-bench';
    } else if (currentId.indexOf('enterprise/') === 0 && routeMap['jp/enterprise/index']) {
      jpTargetId = 'jp/enterprise/index';
    } else if (currentId.indexOf('onboarding/') === 0 && routeMap['jp/integrations/ide-integrations']) {
      jpTargetId = 'jp/integrations/ide-integrations';
    } else {
      jpTargetId = 'jp/welcome/index';
    }
  }

  if (langLabel) {
    langLabel.textContent = isJp ? '日本語' : 'English';
  } else if (langBadge) {
    langBadge.textContent = isJp ? '日本語 ▾' : 'English ▾';
  }

  if (langEnLink) {
    langEnLink.setAttribute('href', routeHref(enTargetId));
    langEnLink.classList.toggle('is-active', !isJp);
    langEnLink.setAttribute('aria-selected', !isJp ? 'true' : 'false');
  }
  if (langJpLink) {
    langJpLink.setAttribute('href', routeHref(jpTargetId));
    langJpLink.classList.toggle('is-active', isJp);
    langJpLink.setAttribute('aria-selected', isJp ? 'true' : 'false');
  }

  if (langBadge && langMenu) {
    langBadge.addEventListener('click', function (e) {
      e.stopPropagation();
      var isOpen = !langMenu.hidden;
      langMenu.hidden = isOpen;
      langBadge.setAttribute('aria-expanded', isOpen ? 'false' : 'true');
    });
    document.addEventListener('click', function (e) {
      if (!langMenu.hidden && langSwitcher && !langSwitcher.contains(e.target)) {
        langMenu.hidden = true;
        langBadge.setAttribute('aria-expanded', 'false');
      }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !langMenu.hidden) {
        langMenu.hidden = true;
        langBadge.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // 4. Localize Brand Link, Topbar Quick Links, Search Placeholder, and TOC Heading
  var brandLink = document.getElementById('boris-ui-brand-link');
  if (brandLink) {
    brandLink.setAttribute('href', routeHref(isJp ? 'jp/welcome/index' : 'welcome/index'));
  }

  var topbarLinksContainer = document.getElementById('boris-ui-topbar-links');
  if (topbarLinksContainer) {
    var tbSpec = NAV_SPEC[langKey].topbarLinks;
    var tbAnchors = topbarLinksContainer.querySelectorAll('.factory-topbar-link');
    for (var tbl = 0; tbl < tbAnchors.length && tbl < tbSpec.length; tbl++) {
      tbAnchors[tbl].textContent = tbSpec[tbl].label;
      tbAnchors[tbl].setAttribute('href', routeHref(tbSpec[tbl].id));
    }
  }

  var tocHeading = document.getElementById('boris-ui-toc-heading');
  if (tocHeading && isJp) {
    tocHeading.textContent = '≡ このページの内容';
  }

  // 5. Determine Active Top Tab & Wire Up Top Tabs
  function treeContainsPage(items, targetId) {
    for (var i = 0; i < items.length; i++) {
      var item = items[i];
      if (typeof item === 'string') {
        if (item === targetId) return true;
      } else if (item && item.pages) {
        if (treeContainsPage(item.pages, targetId)) return true;
      }
    }
    return false;
  }

  var relNoLang = isJp ? currentId.replace(/^jp\//, '') : currentId;
  var activeSection = 'docs';
  var langSections = NAV_SPEC[langKey].sections;

  if (relNoLang.indexOf('api-reference/') === 0 || relNoLang === 'api-reference') {
    activeSection = 'api-reference';
  } else if (relNoLang.indexOf('benchmarks/') === 0 || relNoLang === 'benchmarks') {
    activeSection = 'benchmarks';
  } else if (relNoLang.indexOf('changelog/') === 0 || relNoLang === 'changelog') {
    activeSection = 'changelog';
  } else if (treeContainsPage(langSections.docs, currentId)) {
    activeSection = 'docs';
  } else if (treeContainsPage(langSections.guides, currentId) || relNoLang.indexOf('guides/') === 0) {
    activeSection = 'guides';
  }

  var tabSpecList = NAV_SPEC[langKey].tabs;
  var tabSpecMap = {};
  for (var ts = 0; ts < tabSpecList.length; ts++) {
    tabSpecMap[tabSpecList[ts].key] = tabSpecList[ts];
  }

  var topTabs = document.querySelectorAll('.factory-top-tab');
  for (var t = 0; t < topTabs.length; t++) {
    var tabEl = topTabs[t];
    var sec = tabEl.getAttribute('data-tab-section');
    var spec = tabSpecMap[sec];
    if (spec) {
      tabEl.textContent = spec.label;
      tabEl.setAttribute('href', routeHref(spec.entry));
    }
    tabEl.classList.toggle('is-active', sec === activeSection);
  }

  // 6. Build Single-Language, Section-Scoped Sidebar Navigation
  var effectiveCurrentId = (currentId === 'index')
    ? 'welcome/index'
    : (currentId === 'jp/index' ? 'jp/welcome/index' : currentId);

  function renderNavItems(items, ulEl) {
    for (var i = 0; i < items.length; i++) {
      var item = items[i];
      if (typeof item === 'string') {
        var info = routeMap[item];
        if (!info) continue;
        var li = document.createElement('li');
        li.className = 'site-nav__satellite';
        var a = document.createElement('a');
        a.setAttribute('href', info.href);
        a.textContent = info.title.replace(/\s*\(JP\)$/, '');
        var isCurrent = (item === effectiveCurrentId);
        if (isCurrent) {
          a.classList.add('is-active');
          a.setAttribute('aria-current', 'page');
        }
        li.appendChild(a);
        ulEl.appendChild(li);
      } else if (item && item.group && item.pages) {
        var subLi = document.createElement('li');
        subLi.className = 'site-nav__subgroup-item';
        var details = document.createElement('details');
        details.className = 'factory-nav-subgroup';
        details.open = treeContainsPage(item.pages, effectiveCurrentId);
        var summary = document.createElement('summary');
        summary.className = 'factory-nav-subgroup-title';
        var titleSpan = document.createElement('span');
        titleSpan.textContent = item.group;
        var caretSpan = document.createElement('span');
        caretSpan.className = 'factory-nav-subgroup-caret';
        caretSpan.setAttribute('aria-hidden', 'true');
        caretSpan.textContent = '▸';
        summary.appendChild(titleSpan);
        summary.appendChild(caretSpan);
        details.appendChild(summary);
        var innerUl = document.createElement('ul');
        renderNavItems(item.pages, innerUl);
        details.appendChild(innerUl);
        subLi.appendChild(details);
        ulEl.appendChild(subLi);
      }
    }
  }

  if (siteNav) {
    var newRootUl = document.createElement('ul');
    newRootUl.className = 'factory-nav-root';

    if (activeSection === 'api-reference') {
      var apiIndexId = isJp ? 'jp/api-reference/index' : 'api-reference/index';
      var apiPrefix = isJp ? 'jp/api-reference/' : 'api-reference/';

      // Overview link
      if (routeMap[apiIndexId]) {
        var ovHdrLi = document.createElement('li');
        var ovHdr = document.createElement('div');
        ovHdr.className = 'factory-nav-group-header';
        ovHdr.textContent = isJp ? '概要' : 'Overview';
        ovHdrLi.appendChild(ovHdr);
        var ovUl = document.createElement('ul');
        var ovItemLi = document.createElement('li');
        var ovA = document.createElement('a');
        ovA.setAttribute('href', routeMap[apiIndexId].href);
        ovA.textContent = isJp ? 'Factory 公開APIリファレンス' : 'Factory Public API Reference';
        if (currentId === apiIndexId) {
          ovA.classList.add('is-active');
          ovA.setAttribute('aria-current', 'page');
        }
        ovItemLi.appendChild(ovA);
        ovUl.appendChild(ovItemLi);
        ovHdrLi.appendChild(ovUl);
        newRootUl.appendChild(ovHdrLi);
      }

      // Collect API tag hubs (e.g. api-reference/sessions/index) and their endpoints
      var apiHubLi = routeMap[apiIndexId] ? routeMap[apiIndexId].li : null;
      var apiTagUl = apiHubLi ? apiHubLi.querySelector(':scope > ul') : null;
      if (apiTagUl) {
        var tagLis = apiTagUl.children;
        for (var tg = 0; tg < tagLis.length; tg++) {
          var tLi = tagLis[tg];
          var tLink = tLi.querySelector(':scope > a');
          var tChildUl = tLi.querySelector(':scope > ul');
          if (!tLink) continue;
          var tPid = hrefToPageId(tLink.getAttribute('href'));
          if (tPid.indexOf(apiPrefix) !== 0) continue;

          var groupLi = document.createElement('li');
          var hdr = document.createElement('div');
          hdr.className = 'factory-nav-group-header';
          hdr.textContent = (tLink.textContent || '').replace(/\s*\(JP\)$/, '');
          groupLi.appendChild(hdr);

          var epUl = document.createElement('ul');
          if (tChildUl) {
            var epLis = tChildUl.children;
            for (var ep = 0; ep < epLis.length; ep++) {
              var epA = epLis[ep].querySelector(':scope > a');
              if (!epA) continue;
              var epPid = hrefToPageId(epA.getAttribute('href'));
              var itemLi = document.createElement('li');
              var itemA = document.createElement('a');
              itemA.setAttribute('href', epA.getAttribute('href'));
              itemA.textContent = epA.textContent;
              if (epPid === currentId) {
                itemA.classList.add('is-active');
                itemA.setAttribute('aria-current', 'page');
              }
              itemLi.appendChild(itemA);
              epUl.appendChild(itemLi);
            }
          }
          groupLi.appendChild(epUl);
          newRootUl.appendChild(groupLi);
        }
      }
    } else {
      var groups = langSections[activeSection] || langSections.docs;
      for (var g = 0; g < groups.length; g++) {
        var grp = groups[g];
        var gLi = document.createElement('li');
        gLi.className = 'factory-nav-group';
        var gHdr = document.createElement('div');
        gHdr.className = 'factory-nav-group-header';
        gHdr.textContent = grp.group;
        gLi.appendChild(gHdr);

        var gUl = document.createElement('ul');
        renderNavItems(grp.pages, gUl);
        gLi.appendChild(gUl);
        newRootUl.appendChild(gLi);
      }
    }

    siteNav.innerHTML = '';
    siteNav.appendChild(newRootUl);

    var activeEl = siteNav.querySelector('a.is-active');
    var sidebarContainer = document.getElementById('boris-ui-sidebar');
    if (activeEl && sidebarContainer) {
      sidebarContainer.scrollTop = Math.max(0, activeEl.offsetTop - (sidebarContainer.clientHeight / 3));
    }

    // Update page eyebrow to match the active Mintlify sidebar group/subgroup
    var eyebrowEl = document.querySelector('.factory-eyebrow .breadcrumbs');
    if (eyebrowEl && activeEl) {
      var parentDetails = activeEl.closest('details.factory-nav-subgroup');
      var parentGroup = activeEl.closest('li.factory-nav-group');
      var eyebrowText = '';
      if (parentDetails) {
        var sumSpan = parentDetails.querySelector(':scope > summary > span');
        if (sumSpan) eyebrowText = sumSpan.textContent.trim();
      } else if (parentGroup) {
        var grpHdr = parentGroup.querySelector(':scope > .factory-nav-group-header');
        if (grpHdr) eyebrowText = grpHdr.textContent.trim();
      }
      if (eyebrowText) {
        eyebrowEl.textContent = eyebrowText;
      } else {
        var bcLinks = eyebrowEl.querySelectorAll('a');
        for (var bci = 0; bci < bcLinks.length; bci++) {
          bcLinks[bci].textContent = bcLinks[bci].textContent.replace(/\s*\(JP\)$/, '');
        }
      }
    }
  }

  // 7. Copy Page Button
  var copyBtns = document.querySelectorAll('.factory-copy-page-btn');
  for (var cb = 0; cb < copyBtns.length; cb++) {
    copyBtns[cb].addEventListener('click', function () {
      var btn = this;
      var article = document.querySelector('.factory-article');
      var text = article ? article.innerText : document.body.innerText;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () {
          var orig = btn.textContent;
          btn.textContent = isJp ? 'コピー完了 ✓' : 'Copied ✓';
          setTimeout(function () { btn.textContent = orig; }, 1600);
        });
      }
    });
  }

  // 8. CodeGroup Interactive Tabs
  var codeGroups = document.querySelectorAll('.factory-codegroup');
  for (var cg = 0; cg < codeGroups.length; cg++) {
    (function (group) {
      var tabs = group.querySelectorAll('.factory-codegroup-tab');
      var panels = group.querySelectorAll('.factory-codegroup-panel');
      for (var k = 0; k < tabs.length; k++) {
        tabs[k].addEventListener('click', function () {
          var targetIdx = this.getAttribute('data-tab-idx');
          for (var x = 0; x < tabs.length; x++) {
            tabs[x].classList.toggle('is-active', tabs[x].getAttribute('data-tab-idx') === targetIdx);
          }
          for (var y = 0; y < panels.length; y++) {
            panels[y].classList.toggle('is-active', panels[y].getAttribute('data-panel-idx') === targetIdx);
          }
        });
      }
    })(codeGroups[cg]);
  }

  // 9. Language-Scoped Boris Search Index Client
  var searchInput = document.getElementById('boris-ui-search-input');
  var searchResults = document.getElementById('boris-ui-search-results');
  var searchIndexPromise = null;
  var searchRequest = 0;

  if (searchInput && isJp) {
    searchInput.setAttribute('placeholder', 'ドキュメントを検索...');
  }

  function prepareSearchIndex(index) {
    if (!index || index.format !== 'boris-rendered-search-index' ||
        index.schema_version !== 1 || !Array.isArray(index.documents)) {
      throw new Error('Unsupported search index');
    }
    return index.documents.map(function (doc) {
      if (!doc || typeof doc.path !== 'string' || !doc.path.endsWith('.html') ||
          /[\\?#\u0000-\u0020\u007f]/.test(doc.path) ||
          doc.path.split('/').some(function (part) { return !part || part === '.' || part === '..'; }) ||
          typeof doc.title !== 'string' || !Array.isArray(doc.sections)) {
        throw new Error('Invalid search document');
      }
      var sections = doc.sections.map(function (section) {
        if (!section || !Number.isInteger(section.level) || section.level < 0 || section.level > 6 ||
            typeof section.heading !== 'string' || typeof section.fragment !== 'string' ||
            typeof section.text !== 'string' || typeof section.code !== 'string') {
          throw new Error('Invalid search section');
        }
        return [section.heading, section.text, section.code].filter(Boolean).join(' ');
      });
      return {
        path: doc.path,
        title: doc.title,
        titleLower: doc.title.toLowerCase(),
        pathLower: doc.path.toLowerCase(),
        isJp: doc.path.indexOf('jp/') === 0,
        sections: sections,
        textLower: sections.join(' ').toLowerCase()
      };
    });
  }

  function loadSearchIndex() {
    if (!searchIndexPromise) {
      searchIndexPromise = fetch(rootPrefix + '_boris/search/search-index.json')
        .then(function (r) {
          if (!r.ok) throw new Error('Search index request failed');
          return r.json();
        })
        .then(prepareSearchIndex)
        .catch(function (error) {
          searchIndexPromise = null;
          throw error;
        });
    }
    return searchIndexPromise;
  }

  function showSearchMessage(message) {
    searchResults.innerHTML = '';
    var notice = document.createElement('div');
    notice.className = 'factory-search-hit-snippet';
    notice.textContent = message;
    searchResults.appendChild(notice);
    searchResults.hidden = false;
  }

  function searchSnippet(doc, terms) {
    var bestSection = '';
    var bestScore = -1;
    for (var i = 0; i < doc.sections.length; i++) {
      var section = doc.sections[i];
      var lower = section.toLowerCase();
      var score = terms.filter(function (term) { return lower.indexOf(term) !== -1; }).length;
      if (section && score > bestScore) {
        bestSection = section;
        bestScore = score;
      }
    }
    var firstMatch = bestSection.length;
    var snippetLower = bestSection.toLowerCase();
    for (var t = 0; t < terms.length; t++) {
      var match = snippetLower.indexOf(terms[t]);
      if (match !== -1) firstMatch = Math.min(firstMatch, match);
    }
    var start = Math.max(0, firstMatch === bestSection.length ? 0 : firstMatch - 45);
    return (start ? '…' : '') + bestSection.slice(start, start + 180) +
      (bestSection.length > start + 180 ? '…' : '');
  }

  if (searchInput && searchResults) {
    document.addEventListener('keydown', function (e) {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        searchInput.focus();
      } else if (e.key === '/' && document.activeElement !== searchInput) {
        e.preventDefault();
        searchInput.focus();
      } else if (e.key === 'Escape') {
        searchRequest++;
        searchResults.hidden = true;
      }
    });

    searchInput.addEventListener('input', function () {
      var request = ++searchRequest;
      var q = searchInput.value.trim().toLowerCase();
      if (!q) {
        searchResults.hidden = true;
        searchResults.innerHTML = '';
        return;
      }
      loadSearchIndex().then(function (documents) {
        if (request !== searchRequest) return;
        var terms = q.split(/\s+/);
        var scored = [];
        for (var i = 0; i < documents.length; i++) {
          var doc = documents[i];
          if (doc.isJp !== isJp) continue;

          var score = 0;
          var matchedAll = true;
          for (var t = 0; t < terms.length; t++) {
            var term = terms[t];
            if (!term) continue;
            var inTitle = doc.titleLower.indexOf(term) !== -1;
            var inPath = doc.pathLower.indexOf(term) !== -1;
            var inText = doc.textLower.indexOf(term) !== -1;
            if (!inTitle && !inPath && !inText) {
              matchedAll = false;
              break;
            }
            if (inTitle) score += 10;
            if (inPath) score += 6;
            if (inText) score += 2;
          }
          if (matchedAll && score > 0) {
            scored.push({ doc: doc, score: score });
          }
        }
        scored.sort(function (a, b) { return b.score - a.score; });
        var top = scored.slice(0, 12);
        searchResults.innerHTML = '';
        if (top.length === 0) {
          showSearchMessage(isJp ? '一致するページが見つかりませんでした。' : 'No matching pages found.');
        } else {
          for (var j = 0; j < top.length; j++) {
            var d = top[j].doc;
            var link = document.createElement('a');
            link.className = 'factory-search-hit';
            link.href = rootPrefix + d.path.split('/').map(encodeURIComponent).join('/');
            var tEl = document.createElement('div');
            tEl.className = 'factory-search-hit-title';
            tEl.textContent = d.title;
            var idEl = document.createElement('div');
            idEl.className = 'factory-search-hit-id';
            idEl.textContent = d.path.replace(/\.html$/, '');
            var sEl = document.createElement('div');
            sEl.className = 'factory-search-hit-snippet';
            sEl.textContent = searchSnippet(d, terms);
            link.appendChild(tEl);
            link.appendChild(idEl);
            link.appendChild(sEl);
            searchResults.appendChild(link);
          }
        }
        searchResults.hidden = false;
      }).catch(function () {
        if (request !== searchRequest) return;
        showSearchMessage(isJp
          ? '検索を読み込めませんでした。もう一度入力してお試しください。'
          : 'Search could not be loaded. Type again to retry.');
      });
    });
  }
})();
