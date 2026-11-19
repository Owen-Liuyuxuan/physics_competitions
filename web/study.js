'use strict';
(() => {
  const DATA = window.STUDY_DATA;
  if (!DATA) {
    document.getElementById('view-root').innerHTML =
      '<p class="copper-note">未找到 <code>study-data.js</code>，请先运行 <code>python3 scripts/build_study.py</code> 生成专题数据。</p>';
    return;
  }

  const STORAGE_KEY = 'physics_study_state_v1';
  const STATUS_META = {
    unstarted: { label: '未做', cls: '' },
    review: { label: '待二刷', cls: 'review' },
    hinted: { label: '提示通关', cls: 'hinted' },
    blind: { label: '独立盲解', cls: 'blind' }
  };
  const TIER_META = {
    L1: 'L1 · 复赛筑基',
    L2: 'L2 · 复赛压轴→决赛过渡',
    L3: 'L3 · 决赛核心攻坚',
    L4: 'L4 · 集训队与国际前沿'
  };

  const $ = id => document.getElementById(id);
  const byId = new Map(DATA.problems.map(p => [p.id, p]));
  const topicById = new Map(DATA.topics.map(t => [t.id, t]));
  const archById = new Map(DATA.framework.archetypes.map(a => [a.id, a]));
  const mathById = new Map(DATA.math_tools.map(m => [m.id, m]));
  const advById = new Map(DATA.advanced_models.map(a => [a.id, a]));

  // Atlas lookup lazily checks window.ATLAS (in case data.js loads right alongside or isn't present)
  let atlasMap = null;
  function getAtlasRecord(pid) {
    if (!window.ATLAS) return null;
    if (!atlasMap) {
      atlasMap = new Map();
      for (const r of [...(window.ATLAS.resources || []), ...(window.ATLAS.problems || [])]) {
        atlasMap.set(r.id, r);
      }
    }
    return atlasMap.get(pid) || null;
  }

  function loadState() {
    const empty = { statuses: {}, notes: {}, audits: {}, masteredSubtopics: {} };
    try {
      const raw = JSON.parse(localStorage.getItem(STORAGE_KEY) || 'null');
      if (!raw || typeof raw !== 'object') return empty;
      return {
        statuses: raw.statuses && typeof raw.statuses === 'object' ? raw.statuses : {},
        notes: raw.notes && typeof raw.notes === 'object' ? raw.notes : {},
        audits: raw.audits && typeof raw.audits === 'object' ? raw.audits : {},
        masteredSubtopics: raw.masteredSubtopics && typeof raw.masteredSubtopics === 'object' ? raw.masteredSubtopics : {}
      };
    } catch {
      return empty;
    }
  }

  let userState = loadState();
  function saveState() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(userState));
      updateStatStrip();
    } catch {
      toast('本地存储空间受限，建议导出备份 JSON。');
    }
  }

  function getStatus(pid) {
    return userState.statuses[pid] || 'unstarted';
  }
  function setStatus(pid, val) {
    if (val === 'unstarted') delete userState.statuses[pid];
    else userState.statuses[pid] = val;
    saveState();
  }

  const esc = s => String(s ?? '').replace(/[&<>"']/g, c => (
    { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]
  ));
  const escMath = s => String(s ?? '').replace(/[&<>]/g, c => (
    { '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]
  ));

  // Math-safe Markdown formatter: splits math spans FIRST so LaTeX subscripts/carets are never corrupted
  const MATH_SPLIT_RE = /(\$\$[\s\S]+?\$\$|\\\[[\s\S]+?\\\]|\\\([\s\S]+?\\\)|\$[^$\n]+?\$)/g;
  function mdInline(str) {
    const parts = String(str ?? '').split(MATH_SPLIT_RE);
    return parts.map((part, idx) => {
      if (idx % 2 === 1) return escMath(part);
      return esc(part)
        .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
        .replace(/`([^`]+)`/g, '<code>$1</code>');
    }).join('');
  }

  function mdParagraphs(str) {
    return String(str ?? '')
      .split(/\n{2,}/)
      .filter(Boolean)
      .map(block => `<p>${mdInline(block).replace(/\n/g, '<br>')}</p>`)
      .join('');
  }

  function mdRich(str) {
    const out = [];
    let para = [];
    let ul = [];
    let math = null;
    const flushPara = () => {
      if (para.length) {
        out.push(`<p>${mdInline(para.join('\n')).replace(/\n/g, '<br>')}</p>`);
        para = [];
      }
    };
    const flushUl = () => {
      if (ul.length) {
        out.push(`<ul>${ul.map(x => `<li>${mdInline(x)}</li>`).join('')}</ul>`);
        ul = [];
      }
    };
    for (const raw of String(str ?? '').split('\n')) {
      const t = raw.trim();
      if (math) {
        math.lines.push(raw);
        if ((math.d === '[' && t.includes('\\]')) || (math.d === '$' && t.includes('$$'))) {
          out.push(`<div class="math-block">${escMath(math.lines.join('\n'))}</div>`);
          math = null;
        }
        continue;
      }
      if (!t) {
        flushPara();
        flushUl();
        continue;
      }
      if ((t.startsWith('\\[') && !t.includes('\\]')) || (t.startsWith('$$') && t.slice(2).indexOf('$$') < 0)) {
        flushPara();
        flushUl();
        math = { d: t.startsWith('\\[') ? '[' : '$', lines: [raw] };
        continue;
      }
      if ((t.startsWith('\\[') && t.endsWith('\\]')) || (t.startsWith('$$') && t.endsWith('$$') && t.length > 4)) {
        flushPara();
        flushUl();
        out.push(`<div class="math-block">${escMath(raw)}</div>`);
        continue;
      }
      let m = t.match(/^#{2,4}\s+(.*)$/);
      if (m) {
        flushPara();
        flushUl();
        out.push(`<h4>${mdInline(m[1])}</h4>`);
        continue;
      }
      m = t.match(/^[-*•]\s+(.*)$/);
      if (m) {
        flushPara();
        ul.push(m[1]);
        continue;
      }
      m = t.match(/^(\d+[.、])\s+(.*)$/);
      if (m) {
        flushPara();
        flushUl();
        out.push(`<p class="blind-step"><strong>${esc(m[1])}</strong> ${mdInline(m[2])}</p>`);
        continue;
      }
      flushUl();
      para.push(raw);
    }
    if (math) out.push(`<div class="math-block">${escMath(math.lines.join('\n'))}</div>`);
    flushPara();
    flushUl();
    return out.join('');
  }

  let mathWaitPromise = null;
  function waitForMathJax() {
    if (window.MathJax?.typesetPromise) {
      return (window.MathJax.startup?.promise || Promise.resolve());
    }
    if (!mathWaitPromise) {
      mathWaitPromise = new Promise(resolve => {
        const start = Date.now();
        const timer = setInterval(() => {
          if (window.MathJax?.typesetPromise) {
            clearInterval(timer);
            Promise.resolve(window.MathJax.startup?.promise).then(resolve, resolve);
          } else if (Date.now() - start > 10000) {
            clearInterval(timer);
            resolve();
          }
        }, 60);
      });
    }
    return mathWaitPromise;
  }

  let mainEpoch = 0;
  let drawerEpoch = 0;
  async function typesetNode(el, isDrawer = false) {
    if (!el) return;
    const myEpoch = isDrawer ? ++drawerEpoch : ++mainEpoch;
    await waitForMathJax();
    if ((isDrawer && myEpoch !== drawerEpoch) || (!isDrawer && myEpoch !== mainEpoch)) return;
    if (window.MathJax?.typesetPromise) {
      try {
        if (window.MathJax.typesetClear) window.MathJax.typesetClear([el]);
        await window.MathJax.typesetPromise([el]);
      } catch {
        // Leave source text visible if MathJax rejects a malformed macro
      }
    }
  }

  function toast(msg) {
    const el = $('toast');
    el.textContent = msg;
    el.hidden = false;
    clearTimeout(toast._t);
    toast._t = setTimeout(() => { el.hidden = true; }, 2600);
  }

  // Inline SVG Artwork
  function workflowSVG() {
    return `<svg viewBox="0 0 980 128" width="980" height="128" role="img" aria-label="五步闭环专题备赛流程图">
      <defs>
        <marker id="wf-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#285d44"/>
        </marker>
      </defs>
      <rect x="6" y="14" width="168" height="92" rx="6" fill="#f7f5ef" stroke="#c2cbbd"/>
      <text x="20" y="38" font-size="11" font-family="monospace" fill="#285d44" font-weight="700">STEP 01</text>
      <text x="20" y="60" font-size="14" font-weight="600" fill="#1a2b26">考纲体检与微例诊断</text>
      <text x="20" y="82" font-size="11.5" fill="#5b6a63">锁定复赛→决赛盲区</text>

      <line x1="176" y1="60" x2="202" y2="60" stroke="#285d44" stroke-width="1.6" marker-end="url(#wf-arrow)"/>

      <rect x="206" y="14" width="168" height="92" rx="6" fill="#edf4f6" stroke="#b5ccd4"/>
      <text x="220" y="38" font-size="11" font-family="monospace" fill="#2e5a6b" font-weight="700">STEP 02</text>
      <text x="220" y="60" font-size="14" font-weight="600" fill="#1a2b26">数学工具前置通关</text>
      <text x="220" y="82" font-size="11.5" fill="#394b44">端图 / 复势 / 变分 / 展开</text>

      <line x1="376" y1="60" x2="402" y2="60" stroke="#285d44" stroke-width="1.6" marker-end="url(#wf-arrow)"/>

      <rect x="406" y="14" width="168" height="92" rx="6" fill="#f7f5ef" stroke="#c2cbbd"/>
      <text x="420" y="38" font-size="11" font-family="monospace" fill="#285d44" font-weight="700">STEP 03</text>
      <text x="420" y="60" font-size="14" font-weight="600" fill="#1a2b26">二级结论边界反推</text>
      <text x="420" y="82" font-size="11.5" fill="#5b6a63">绝不脱离前提死背公式</text>

      <line x1="576" y1="60" x2="602" y2="60" stroke="#285d44" stroke-width="1.6" marker-end="url(#wf-arrow)"/>

      <rect x="606" y="14" width="168" height="92" rx="6" fill="#e6efe9" stroke="#8bb19d"/>
      <text x="620" y="38" font-size="11" font-family="monospace" fill="#183d2c" font-weight="700">STEP 04</text>
      <text x="620" y="60" font-size="14" font-weight="600" fill="#1a2b26">L1→L4 防剧透盲刷</text>
      <text x="620" y="82" font-size="11.5" fill="#285d44">渐进提示 · 对照49道勘误</text>

      <line x1="776" y1="60" x2="802" y2="60" stroke="#285d44" stroke-width="1.6" marker-end="url(#wf-arrow)"/>

      <rect x="806" y="14" width="168" height="92" rx="6" fill="#faf1e8" stroke="#dfb996"/>
      <text x="820" y="38" font-size="11" font-family="monospace" fill="#a85d26" font-weight="700">STEP 05</text>
      <text x="820" y="60" font-size="14" font-weight="600" fill="#1a2b26">五维自检与二刷闭环</text>
      <text x="820" y="82" font-size="11.5" fill="#6b3813">量纲·极限·交叉·间隔复盘</text>
    </svg>`;
  }

  function topicSVG(tid) {
    const common = 'viewBox="0 0 210 135" width="210" height="135" aria-hidden="true"';
    const svgs = {
      mechanics: `<svg ${common}><line x1="20" y1="110" x2="190" y2="110" stroke="#5b6a63" stroke-width="1.4"/><path d="M55 110 A50 50 0 0 1 155 110" fill="#f0eee6" stroke="#285d44" stroke-width="1.6"/><circle cx="118" cy="60" r="10" fill="#e6efe9" stroke="#285d44" stroke-width="1.6"/><line x1="105" y1="60" x2="145" y2="38" stroke="#a85d26" stroke-width="1.4" stroke-dasharray="3 2"/><text x="16" y="24" font-size="11" fill="#5b6a63" font-family="serif" font-style="italic">I<tspan dy="3" font-size="8">P</tspan><tspan dy="-3">θ̈ + ½I′</tspan><tspan dy="3" font-size="8">P</tspan><tspan dy="-3">θ̇² + mgy′=0</tspan></text></svg>`,
      astro_relativity: `<svg ${common}><ellipse cx="95" cy="70" rx="68" ry="38" fill="none" stroke="#c2cbbd" stroke-dasharray="4 3"/><circle cx="120" cy="68" r="34" fill="none" stroke="#285d44" stroke-width="1.7"/><circle cx="105" cy="68" r="3" fill="#a85d26"/><line x1="105" y1="68" x2="152" y2="56" stroke="#2e5a6b" stroke-width="1.5"/><line x1="105" y1="68" x2="88" y2="75" stroke="#2e5a6b" stroke-width="1.5"/><text x="14" y="22" font-size="11" fill="#285d44" font-family="serif" font-style="italic">Hodograph · R<tspan dy="3" font-size="8">h</tspan><tspan dy="-3">=GM/(L/m)</tspan></text></svg>`,
      electrostatics_circuits: `<svg ${common}><line x1="105" y1="18" x2="105" y2="118" stroke="#5b6a63" stroke-width="1.8"/><circle cx="62" cy="68" r="7" fill="#a85d26"/><circle cx="148" cy="68" r="7" fill="none" stroke="#2e5a6b" stroke-width="1.6" stroke-dasharray="2 2"/><path d="M62 68 Q92 32 105 42 M62 68 Q92 104 105 94" fill="none" stroke="#285d44" stroke-width="1.3"/><text x="16" y="22" font-size="11" fill="#5b6a63" font-family="serif" font-style="italic">∇²φ = 0 · q′ = −qR/d</text></svg>`,
      magnetism_em: `<svg ${common}><ellipse cx="105" cy="75" rx="46" ry="15" fill="none" stroke="#285d44" stroke-width="2"/><path d="M72 30 Q90 70 60 112 M105 26 L105 114 M138 30 Q120 70 150 112" fill="none" stroke="#2e5a6b" stroke-width="1.3"/><text x="18" y="20" font-size="11" fill="#285d44" font-family="serif" font-style="italic">Φ<tspan dy="3" font-size="8">ext</tspan><tspan dy="-3">(z) + LI = Φ</tspan><tspan dy="3" font-size="8">0</tspan></text></svg>`,
      fluids_continua: `<svg ${common}><path d="M22 44 Q105 94 188 44" fill="none" stroke="#2e5a6b" stroke-width="1.8"/><path d="M22 68 Q105 106 188 68" fill="none" stroke="#c2cbbd" stroke-width="1.2"/><circle cx="72" cy="73" r="11" fill="#e6efe9" stroke="#285d44" stroke-width="1.5"/><circle cx="138" cy="73" r="11" fill="#e6efe9" stroke="#285d44" stroke-width="1.5"/><text x="16" y="22" font-size="11" fill="#2e5a6b" font-family="serif" font-style="italic">l<tspan dy="3" font-size="8">c</tspan><tspan dy="-3">=√(σ/ρg) · Δp=2σ/R</tspan></text></svg>`,
      thermo_stat: `<svg ${common}><line x1="30" y1="112" x2="185" y2="112" stroke="#5b6a63" stroke-width="1.3"/><line x1="30" y1="22" x2="30" y2="112" stroke="#5b6a63" stroke-width="1.3"/><path d="M44 38 Q95 96 172 104" fill="none" stroke="#2e5a6b" stroke-width="1.3" stroke-dasharray="3 2"/><path d="M48 30 L166 104" fill="none" stroke="#a85d26" stroke-width="1.8"/><circle cx="94" cy="59" r="3.5" fill="#285d44"/><circle cx="122" cy="76" r="3.5" fill="#a85d26"/><text x="58" y="24" font-size="11" fill="#5b6a63" font-family="serif" font-style="italic">C&lt;0 · F=E−TS</text></svg>`,
      optics_waves: `<svg ${common}><path d="M26 98 Q95 26 182 54" fill="none" stroke="#285d44" stroke-width="1.7"/><path d="M26 98 Q108 50 182 96" fill="none" stroke="#a85d26" stroke-width="1.4"/><line x1="22" y1="44" x2="186" y2="44" stroke="#c2cbbd" stroke-dasharray="3 2"/><text x="16" y="24" font-size="11" fill="#285d44" font-family="serif" font-style="italic">n(y)sinθ = const · δ∫nds=0</text></svg>`,
      quantum_modern: `<svg ${common}><line x1="25" y1="68" x2="185" y2="68" stroke="#c2cbbd" stroke-dasharray="3 2"/><path d="M35 28 Q105 98 175 28 M35 108 Q105 38 175 108" fill="none" stroke="#285d44" stroke-width="1.7"/><circle cx="105" cy="68" r="4" fill="#a85d26"/><text x="16" y="22" font-size="11" fill="#2e5a6b" font-family="serif" font-style="italic">E(p)=±v<tspan dy="3" font-size="8">F</tspan><tspan dy="-3">|p| · SU(2)</tspan></text></svg>`
    };
    return svgs[tid] || '';
  }

  // Router & App State
  let ui = {
    view: 'overview',
    planId: 'deep_12w',
    archId: DATA.framework.archetypes[0].id,
    topicId: DATA.topics[0].id,
    mathId: DATA.math_tools[0].id,
    advId: DATA.advanced_models[0].id,
    syllabusTopic: '',
    wb: {
      search: '',
      topic: '',
      subtopic: '',
      archetype: '',
      tier: '',
      contest: '',
      difficulty: '',
      status: '',
      onlyHl: false,
      onlyReview: false,
      sort: 'tier_asc',
      limit: 40
    },
    drawerPid: null,
    drawerTab: 'problem'
  };

  function parseHash() {
    const h = location.hash.replace(/^#/, '');
    if (!h) return;
    const p = new URLSearchParams(h);
    if (['overview', 'syllabus', 'topics', 'math', 'models', 'workbench'].includes(p.get('view'))) {
      ui.view = p.get('view');
    }
    if (topicById.has(p.get('topic'))) ui.topicId = p.get('topic');
    if (mathById.has(p.get('tool'))) ui.mathId = p.get('tool');
    if (advById.has(p.get('model'))) ui.advId = p.get('model');
    if (archById.has(p.get('arch'))) ui.archId = p.get('arch');
    if (p.has('wb_topic')) ui.wb.topic = p.get('wb_topic');
    if (p.has('wb_sub')) ui.wb.subtopic = p.get('wb_sub');
    if (p.has('wb_tier')) ui.wb.tier = p.get('wb_tier');
    if (p.has('wb_arch')) ui.wb.archetype = p.get('wb_arch');
    if (byId.has(p.get('problem'))) ui.drawerPid = p.get('problem');
  }

  function syncHash() {
    const p = new URLSearchParams({ view: ui.view });
    if (ui.view === 'topics') p.set('topic', ui.topicId);
    if (ui.view === 'math') p.set('tool', ui.mathId);
    if (ui.view === 'models') p.set('model', ui.advId);
    if (ui.view === 'syllabus') p.set('arch', ui.archId);
    if (ui.view === 'workbench') {
      if (ui.wb.topic) p.set('wb_topic', ui.wb.topic);
      if (ui.wb.subtopic) p.set('wb_sub', ui.wb.subtopic);
      if (ui.wb.tier) p.set('wb_tier', ui.wb.tier);
      if (ui.wb.archetype) p.set('wb_arch', ui.wb.archetype);
    }
    if (ui.drawerPid) p.set('problem', ui.drawerPid);
    history.replaceState(null, '', `#${p.toString()}`);
  }

  function updateStatStrip() {
    const s = DATA.stats;
    const done = DATA.problems.filter(p => ['blind', 'hinted'].includes(getStatus(p.id))).length;
    const review = DATA.problems.filter(p => getStatus(p.id) === 'review').length;
    const subDone = Object.values(userState.masteredSubtopics).filter(Boolean).length;
    $('stat-strip').innerHTML = [
      [s.total_problems, '全库独立题（2013–26）'],
      [`${s.cpho_semi} / ${s.cpho_final}`, 'CPhO 复赛 / 决赛理论'],
      [s.blind_highlight_count, '★ 盲解亮点与官方勘误'],
      [`${subDone}/44`, '子考纲自检掌握'],
      [`${done} 已解 · ${review} 待二刷`, '我的刷题进度']
    ].map(([num, label]) => `<div class="stat-cell"><strong>${esc(num)}</strong><span>${esc(label)}</span></div>`).join('');
  }

  function problemChip(pid, showTier = true) {
    const p = byId.get(pid);
    if (!p) return '';
    const title = p.title_zh || p.title;
    const st = getStatus(pid);
    const hl = p.blind_highlight ? ' ★' : '';
    const dot = st === 'blind' ? '● ' : st === 'review' ? '↻ ' : '';
    return `<button class="prob-chip" data-open-problem="${esc(pid)}" title="${esc(p.study_note)}">
      ${showTier ? `<span class="badge tier-${esc(p.tier)}">${esc(p.tier)}</span>` : ''}
      <span>${esc(dot)}${esc(p.contest)} ${esc(p.year)}${p.question ? ` Q${p.question}` : ''} · ${esc(title)}${esc(hl)}</span>
    </button>`;
  }

  function jumpToWorkbench(filters = {}) {
    ui.view = 'workbench';
    ui.wb = {
      search: '',
      topic: filters.topic || '',
      subtopic: filters.subtopic || '',
      archetype: filters.archetype || '',
      tier: filters.tier || '',
      contest: filters.contest || '',
      difficulty: filters.difficulty || '',
      status: filters.status || '',
      onlyHl: Boolean(filters.onlyHl),
      onlyReview: Boolean(filters.onlyReview),
      sort: filters.sort || 'tier_asc',
      limit: 40
    };
    renderApp();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // === VIEW 1: OVERVIEW & WORKFLOW ===
  function renderOverview() {
    const fw = DATA.framework;
    const plan = fw.study_plans.find(x => x.id === ui.planId) || fw.study_plans[0];
    return `
      <div class="section-intro">
        <p class="eyebrow">01 · STUDY SYSTEM & ROADMAP</p>
        <h2>从复赛根基到决赛及前沿模型的闭环备赛法</h2>
        <p>${mdInline(fw.meta.audience)} 本系统把题库全部 <strong>283</strong> 道独立试题按「考纲三级跃迁 × 九大解题母版 × 十大数学工具 × 十二个前沿模型」组织起来，配合防剧透逐层提示，帮助你建立真正的独立建模能力。</p>
      </div>

      <div class="editorial-note">${mdInline(fw.meta.disclaimer)}</div>

      <div class="diagram-box">${workflowSVG()}</div>

      <section class="workflow-list">
        ${fw.workflow_steps.map(st => `
          <article class="workflow-item">
            <div class="workflow-head">
              <span class="workflow-code">${esc(st.code)}</span>
              <h3>${esc(st.title)}</h3>
              <span class="workflow-dur">${esc(st.duration)}</span>
            </div>
            <p class="workflow-goal">${mdInline(st.goal)}</p>
            <ul>${st.actions.map(a => `<li>${mdInline(a)}</li>`).join('')}</ul>
            <div class="workflow-exit">过关标准：${mdInline(st.exit_criterion)}</div>
          </article>
        `).join('')}
      </section>

      <section class="monograph-section">
        <h3>分阶段自主复习路线选择 <small>点击具体周次可一键筛出对应真题集</small></h3>
        <div class="plan-switcher">
          ${fw.study_plans.map(p => `
            <button class="chip-btn ${p.id === plan.id ? 'active' : ''}" data-select-plan="${esc(p.id)}">
              <strong>${esc(p.name)}</strong> <span class="badge accent">${esc(p.badge)}</span>
            </button>
          `).join('')}
        </div>
        <div class="plan-panel">
          <div class="plan-meta">
            <div><strong>适用对象：</strong>${mdInline(plan.target)}</div>
            <div><strong>推荐每日节奏：</strong>${mdInline(plan.daily_rhythm)}</div>
          </div>
          <div class="phase-list">
            ${plan.phases.map(ph => {
              const matched = DATA.problems.filter(pr =>
                ph.recommended_filter.tiers.includes(pr.tier) &&
                ph.recommended_filter.topics.includes(pr.primary_topic)
              );
              const solved = matched.filter(pr => ['blind', 'hinted'].includes(getStatus(pr.id))).length;
              return `<div class="phase-row">
                <div>
                  <strong>${esc(ph.week)}</strong>
                  <span class="badge mono">${solved} / ${matched.length} 题已完成</span>
                </div>
                <p>${mdInline(ph.goal)}</p>
                <div class="ref-chips" style="margin-top:0;justify-content:flex-end">
                  ${ph.recommended_filter.topics.map(tid => {
                    const top = topicById.get(tid);
                    return top ? `<button class="outline-btn" data-jump-phase="${esc(tid)}" data-jump-tier="${esc(ph.recommended_filter.tiers[ph.recommended_filter.tiers.length - 1] || '')}">
                      ${esc(top.title.split('、')[0])} ↗
                    </button>` : '';
                  }).join('')}
                </div>
              </div>`;
            }).join('')}
          </div>
        </div>
      </section>

      <section class="monograph-section">
        <h3>四级备赛梯次说明（L1–L4）</h3>
        <div class="two-col">
          ${fw.tier_definitions.map(td => `
            <div class="model-block">
              <div class="model-block-head">
                <span class="badge tier-${esc(td.id)}">${esc(td.label)}</span>
                <span class="badge mono">${DATA.stats.by_tier[td.id] || 0} 题</span>
              </div>
              <p style="margin:0">${mdInline(td.summary)}</p>
            </div>
          `).join('')}
        </div>
      </section>
    `;
  }

  // === VIEW 2: SYLLABUS MATRIX & 9 ARCHETYPES ===
  function renderSyllabus() {
    const fw = DATA.framework;
    const activeArch = archById.get(ui.archId) || fw.archetypes[0];
    const filteredTopics = ui.syllabusTopic ? DATA.topics.filter(t => t.id === ui.syllabusTopic) : DATA.topics;
    return `
      <div class="section-intro">
        <p class="eyebrow">02 · SYLLABUS & 9 EXAM ARCHETYPES</p>
        <h2>复赛→决赛→大学前沿三级考纲矩阵与九大解题母版</h2>
        <p>把每条子考纲与“复赛考到哪、决赛增加什么、大学前沿如何下放”并排对照，并用九大题型母版打破章节壁垒。</p>
      </div>

      <section class="monograph-section" style="margin-top:0">
        <h3>八大专题三级能力总表 <small>勾选“已掌握”自动保存至本地进度 · 点击子专题编号筛题</small></h3>
        <div class="plan-switcher">
          <button class="chip-btn ${!ui.syllabusTopic ? 'active' : ''}" data-syl-topic="">全部八专题（44 子项）</button>
          ${DATA.topics.map(t => `
            <button class="chip-btn ${ui.syllabusTopic === t.id ? 'active' : ''}" data-syl-topic="${esc(t.id)}">
              ${esc(t.code)} · ${esc(t.title.split('、')[0])}
            </button>
          `).join('')}
        </div>
        <div class="table-scroll">
          <table class="ledger">
            <thead>
              <tr>
                <th>子专题</th>
                <th>复赛标准 (Tier A)</th>
                <th>决赛跃迁 (Tier B)</th>
                <th>大学与国际前沿 (Tier C)</th>
                <th>题数 / 自检</th>
              </tr>
            </thead>
            <tbody>
              ${filteredTopics.flatMap(t => t.syllabus_matrix.map(sub => {
                const cnt = DATA.stats.by_subtopic[sub.code] || 0;
                const checked = Boolean(userState.masteredSubtopics[sub.code]);
                return `<tr>
                  <td>
                    <button class="chip-btn" data-jump-sub="${esc(sub.code)}" data-jump-topic="${esc(t.id)}">
                      <strong>${esc(sub.code)}</strong> ${esc(sub.name)} ↗
                    </button>
                  </td>
                  <td>${mdInline(sub.tier_a_semifinal)}</td>
                  <td>${mdInline(sub.tier_b_final)}</td>
                  <td>${mdInline(sub.tier_c_frontier)}</td>
                  <td style="white-space:nowrap">
                    <div style="margin-bottom:6px"><span class="badge mono">${cnt} 题</span></div>
                    <label class="check-toggle">
                      <input type="checkbox" data-master-sub="${esc(sub.code)}" ${checked ? 'checked' : ''}> 已掌握
                    </label>
                  </td>
                </tr>`;
              })).join('')}
            </tbody>
          </table>
        </div>
      </section>

      <section class="monograph-section">
        <h3>九大跨专题高频题型母版（T1–T9） <small>考场 30 秒识破命题意图与破题套路</small></h3>
        <div class="split-layout">
          <div class="quiet-toc">
            <p class="toc-label">题型母版目录</p>
            ${fw.archetypes.map(a => `
              <button class="toc-btn ${a.id === activeArch.id ? 'active' : ''}" data-select-arch="${esc(a.id)}">
                <small><span>${esc(a.code)}</span><span>${DATA.stats.by_archetype[a.id] || 0} 题</span></small>
                <strong>${esc(a.name)}</strong>
              </button>
            `).join('')}
          </div>
          <div class="monograph">
            <div class="model-block">
              <div class="model-block-head">
                <span class="badge accent mono">${esc(activeArch.code)}</span>
                <h4 style="font-size:22px">${esc(activeArch.name)}</h4>
                <button class="solid-btn" style="margin-left:auto" data-jump-arch="${esc(activeArch.id)}">
                  在题库中筛选本母版 ${DATA.stats.by_archetype[activeArch.id] || 0} 题 ↗
                </button>
              </div>
              <p style="font-weight:500;margin:6px 0">${mdInline(activeArch.tagline)}</p>
              <p style="font-size:13px;color:var(--muted);margin:0 0 14px">${mdInline(activeArch.frequency_note)}</p>

              <h4>30 秒题眼识别信号</h4>
              <ul>${activeArch.signal_cues.map(c => `<li>${mdInline(c)}</li>`).join('')}</ul>

              <h4>五步通用拆解模板</h4>
              <ol>${activeArch.five_step_template.map(s => `<li>${mdInline(s)}</li>`).join('')}</ol>

              <div class="copper-note">
                <strong>考场失分高发区：</strong>
                <ul style="margin:6px 0 0;padding-left:18px">${activeArch.signature_traps.map(tr => `<li>${mdInline(tr)}</li>`).join('')}</ul>
              </div>

              <h4>代表标杆题例</h4>
              <div class="ref-chips">${activeArch.benchmark_problem_ids.map(pid => problemChip(pid)).join('')}</div>
            </div>
          </div>
        </div>
      </section>
    `;
  }

  // === VIEW 3: 8 TOPIC MONOGRAPHS ===
  function renderTopics() {
    const t = topicById.get(ui.topicId) || DATA.topics[0];
    const st = DATA.stats.by_topic[t.id];
    const topicProblems = DATA.problems
      .filter(p => p.primary_topic === t.id)
      .sort((a, b) => a.tier.localeCompare(b.tier) || b.year - a.year || a.id.localeCompare(b.id));

    return `
      <div class="split-layout">
        <aside class="quiet-toc" aria-label="八大专题目录">
          <p class="toc-label">专题讲义目录</p>
          ${DATA.topics.map(item => {
            const tst = DATA.stats.by_topic[item.id];
            const solved = DATA.problems.filter(p => p.primary_topic === item.id && ['blind', 'hinted'].includes(getStatus(p.id))).length;
            return `<button class="toc-btn ${item.id === t.id ? 'active' : ''}" data-select-topic="${esc(item.id)}">
              <small><span>${esc(item.code)}</span><span>${solved}/${tst.primary_total} 题</span></small>
              <strong>${esc(item.title)}</strong>
            </button>`;
          }).join('')}
        </aside>

        <article class="monograph">
          <header class="monograph-header">
            <div>
              <p class="eyebrow">${esc(t.code)} · 主属 ${st.primary_total} 题（复赛 ${st.cpho_semi} / 决赛 ${st.cpho_final} / 国际 ${st.panpho + st.physicscup + st.plancks}）· 跨专题关联 ${st.secondary_total} 题</p>
              <h2>${esc(t.title)}</h2>
              <p class="monograph-sub">${esc(t.subtitle)}</p>
              <p style="margin:0;color:var(--ink-soft)">${mdInline(t.tagline)}</p>
            </div>
            <div class="monograph-motif">${topicSVG(t.id)}</div>
          </header>

          <div class="editorial-note">
            <strong>复赛 → 决赛 → 大学模型跃迁主线：</strong>${mdInline(t.bridge_summary)}
            <div class="ref-chips" style="margin-top:10px">
              ${t.recommended_math_ids.map(mid => {
                const m = mathById.get(mid);
                return m ? `<button class="chip-btn" data-jump-math="${esc(mid)}">数学工具 ${esc(m.code)}: ${esc(m.name.split('、')[0])} ↗</button>` : '';
              }).join('')}
              ${t.recommended_adv_ids.map(aid => {
                const a = advById.get(aid);
                return a ? `<button class="chip-btn" data-jump-adv="${esc(aid)}">前沿模型 ${esc(a.code)}: ${esc(a.title.split('：')[0])} ↗</button>` : '';
              }).join('')}
            </div>
          </div>

          <section class="monograph-section">
            <h3>1. 本专题三级考纲与子专题矩阵 <small>勾选“已掌握”并可直接按子专题刷题</small></h3>
            <div class="table-scroll">
              <table class="ledger">
                <thead>
                  <tr>
                    <th>子专题</th>
                    <th>复赛根基</th>
                    <th>决赛跃迁</th>
                    <th>大学与国际前沿</th>
                    <th>自检</th>
                  </tr>
                </thead>
                <tbody>
                  ${t.syllabus_matrix.map(sub => {
                    const checked = Boolean(userState.masteredSubtopics[sub.code]);
                    return `<tr>
                      <td>
                        <button class="chip-btn" data-jump-sub="${esc(sub.code)}" data-jump-topic="${esc(t.id)}">
                          <strong>${esc(sub.code)}</strong> ${esc(sub.name)} ↗
                        </button>
                        <div style="font-size:12px;color:var(--muted);margin-top:6px">重点：${mdInline(sub.exam_focus)}</div>
                      </td>
                      <td>${mdInline(sub.tier_a_semifinal)}</td>
                      <td>${mdInline(sub.tier_b_final)}</td>
                      <td>${mdInline(sub.tier_c_frontier)}</td>
                      <td style="white-space:nowrap">
                        <div style="margin-bottom:6px"><span class="badge mono">${DATA.stats.by_subtopic[sub.code] || 0} 题</span></div>
                        <label class="check-toggle">
                          <input type="checkbox" data-master-sub="${esc(sub.code)}" ${checked ? 'checked' : ''}> 已掌握
                        </label>
                      </td>
                    </tr>`;
                  }).join('')}
                </tbody>
              </table>
            </div>
          </section>

          <section class="monograph-section">
            <h3>2. 高频核心物理模型拆解</h3>
            ${t.core_models.map(cm => `
              <div class="model-block">
                <div class="model-block-head">
                  <h4>${esc(cm.name)}</h4>
                  <span class="badge accent">${esc(cm.tier)}</span>
                </div>
                <p><strong>原型场景：</strong>${mdInline(cm.prototype)}</p>
                <p><strong>核心假设：</strong>${mdInline(cm.assumptions)}</p>
                <div class="formula-list">
                  <ul>${cm.key_equations.map(eq => `<li>${mdInline(eq)}</li>`).join('')}</ul>
                </div>
                <p><strong>复赛→决赛演化：</strong>${mdInline(cm.evolution_semi_to_final)}</p>
                <div class="ref-chips">${cm.sample_problem_ids.map(pid => problemChip(pid)).join('')}</div>
              </div>
            `).join('')}
          </section>

          <section class="monograph-section">
            <h3>3. 二级结论与解题技巧教学（附适用边界与红线）</h3>
            ${t.secondary_conclusions.map(sc => `
              <div class="conclusion-row">
                <div>
                  <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px">
                    <h4 style="margin:0">${mdInline(sc.title)}</h4>
                    <span class="badge teal">${esc(sc.source_type)}</span>
                  </div>
                  <div class="conclusion-formula">${mdInline(sc.formula)}</div>
                  <p style="margin:0;font-size:13.5px"><strong>推导骨架：</strong>${mdInline(sc.derivation_skeleton)}</p>
                </div>
                <div class="conclusion-side">
                  <p style="margin:0 0 8px"><strong>适用边界：</strong>${mdInline(sc.validity_boundaries)}</p>
                  <div class="copper-note" style="margin:0 0 10px;padding:8px 12px">
                    <strong>红线预警：</strong>${mdInline(sc.pitfall_warning)}
                  </div>
                  <div class="ref-chips">${sc.related_problem_ids.map(pid => problemChip(pid, false)).join('')}</div>
                </div>
              </div>
            `).join('')}
          </section>

          <section class="monograph-section">
            <h3>4. 诊断微例题（先自测直觉误区，再看规范推导）</h3>
            ${t.virtual_examples.map(ve => `
              <div class="ve-card" id="ve-${esc(ve.id)}">
                <div class="ve-head">
                  <h4>${mdInline(ve.title)}</h4>
                  <span class="badge teal">${esc(ve.difficulty_tag)}</span>
                </div>
                <p>${mdInline(ve.scenario)}</p>
                <details class="hint-box" style="margin-bottom:10px">
                  <summary>① 点击核对常见直觉陷阱（思考 3 分钟后再点）</summary>
                  <div class="copper-note" style="margin:0">${mdInline(ve.intuition_trap)}</div>
                </details>
                <details class="hint-box" style="margin-bottom:0">
                  <summary>② 展开完整规范推导与量纲/极限验算</summary>
                  <div class="ve-reveal" style="border-top:0;padding-top:0;margin-top:4px">
                    <ol>${ve.solution_steps.map(s => `<li>${mdInline(s)}</li>`).join('')}</ol>
                    <p class="teal-note" style="margin:0 0 10px"><strong>量纲与退化检验：</strong>${mdInline(ve.limit_dimension_check)}</p>
                    <div><strong>立即迁移至库内真题：</strong><div class="ref-chips">${ve.transfers_to_ids.map(pid => problemChip(pid)).join('')}</div></div>
                  </div>
                </details>
              </div>
            `).join('')}
          </section>

          <section class="monograph-section">
            <h3>5. 本专题高频易错点诊所</h3>
            <div class="two-col">
              ${t.topic_pitfalls.map(pit => `
                <div class="pitfall-card">
                  <h4>${mdInline(pit.title)}</h4>
                  <p style="font-size:13.5px;margin:0 0 10px">${mdInline(pit.detail)}</p>
                  <div class="ref-chips">${pit.ref_ids.map(pid => problemChip(pid, false)).join('')}</div>
                </div>
              `).join('')}
            </div>
          </section>

          <section class="monograph-section">
            <h3>6. 本专题全库真题梯次索引（${topicProblems.length} 题 · L1 → L4）</h3>
            <div class="table-scroll">
              <table class="ledger">
                <thead>
                  <tr>
                    <th>梯次 / 难度</th>
                    <th>赛事与题名</th>
                    <th>子考纲</th>
                    <th>教练学习批注（点击打开防剧透刷题抽屉）</th>
                    <th>状态</th>
                  </tr>
                </thead>
                <tbody>
                  ${topicProblems.map(p => {
                    const st = getStatus(p.id);
                    const hl = p.blind_highlight ? `<span class="badge hl" title="${esc(p.blind_highlight.note)}">★ ${esc(p.blind_highlight.kind)}</span>` : '';
                    return `<tr>
                      <td style="white-space:nowrap">
                        <span class="badge tier-${esc(p.tier)}">${esc(p.tier)}</span>
                        <span class="badge mono">${esc(p.difficulty)}</span>
                      </td>
                      <td>
                        <div><strong>${esc(p.contest)} ${esc(p.year)} ${esc(p.stage_label)}${p.question ? ` Q${p.question}` : ''}</strong> ${hl}</div>
                        <button class="prob-chip" style="margin-top:4px" data-open-problem="${esc(p.id)}">${esc(p.title_zh || p.title)} ↗</button>
                      </td>
                      <td style="white-space:nowrap"><span class="badge mono">${esc(p.subtopic)}</span></td>
                      <td style="font-size:13px">${mdInline(p.study_note)}</td>
                      <td>
                        <select class="status-select" data-status-pid="${esc(p.id)}" data-status="${esc(st)}" aria-label="题目状态">
                          ${Object.entries(STATUS_META).map(([k, v]) => `<option value="${k}" ${st === k ? 'selected' : ''}>${v.label}</option>`).join('')}
                        </select>
                      </td>
                    </tr>`;
                  }).join('')}
                </tbody>
              </table>
            </div>
          </section>
        </article>
      </div>
    `;
  }

  // === VIEW 4: MATH TOOLKIT ===
  function renderMath() {
    const m = mathById.get(ui.mathId) || DATA.math_tools[0];
    const linked = DATA.problems.filter(p => p.math_tools.includes(m.id));
    return `
      <div class="section-intro">
        <p class="eyebrow">04 · UNIVERSITY MATH TOOLKIT</p>
        <h2>竞赛核心大学数学工具箱（M-01 至 M-10）</h2>
        <p>将微积分变形、泰勒分级近似、张量动基矢、拉格朗日变分、保角映射、速度端图、重整化与四动量不变量转化为可直接上手的物理工具。</p>
      </div>

      <div class="split-layout">
        <aside class="quiet-toc" aria-label="十大数学工具目录">
          <p class="toc-label">数学工具目录</p>
          ${DATA.math_tools.map(item => `
            <button class="toc-btn ${item.id === m.id ? 'active' : ''}" data-select-math="${esc(item.id)}">
              <small><span>${esc(item.code)}</span><span>${DATA.stats.by_math[item.id] || 0} 题</span></small>
              <strong>${mdInline(item.name)}</strong>
            </button>
          `).join('')}
        </aside>

        <article class="monograph">
          <div class="model-block">
            <div class="model-block-head">
              <span class="badge teal mono">${esc(m.code)}</span>
              <span class="badge accent">${esc(m.level_tag)}</span>
            </div>
            <h2 style="font:600 26px/1.35 var(--serif);margin:6px 0 12px">${mdInline(m.name)}</h2>
            <p class="teal-note"><strong>为什么它在决赛/国际赛极其关键：</strong>${mdInline(m.why_it_matters)}</p>

            <h3>核心公式与物理含义</h3>
            ${m.core_formulas.map(cf => `
              <div class="conclusion-formula">
                <div style="font-size:13px;font-weight:600;color:var(--accent-deep)">${mdInline(cf.label)}</div>
                <div class="math-block">$$${escMath(cf.tex)}$$</div>
                <div style="font-size:13.5px;color:var(--ink-soft)">${mdInline(cf.note)}</div>
              </div>
            `).join('')}

            <h3>标准操作流程（SOP）</h3>
            <ol>${m.usage_steps.map(s => `<li>${mdInline(s)}</li>`).join('')}</ol>

            <div class="ve-card" style="margin-top:20px">
              <div class="ve-head">
                <h4>${mdInline(m.worked_mini_example.title)}</h4>
                <span class="badge teal">精讲微例</span>
              </div>
              <p><strong>问题：</strong>${mdInline(m.worked_mini_example.problem)}</p>
              <div style="background:var(--bg);padding:14px 16px;border-radius:4px">
                <strong>推导：</strong>${mdInline(m.worked_mini_example.solution)}
              </div>
            </div>

            <div class="copper-note">
              <strong>数学工具误用高发坑：</strong>
              <ul style="margin:6px 0 0;padding-left:18px">${m.common_traps.map(tr => `<li>${mdInline(tr)}</li>`).join('')}</ul>
            </div>

            <h3>精选代表题</h3>
            <div class="ref-chips">${m.featured_problem_ids.map(pid => problemChip(pid)).join('')}</div>

            <h3 style="margin-top:24px">全库应用本工具的题目（共 ${linked.length} 题）</h3>
            <div class="ref-chips">${linked.map(p => problemChip(p.id)).join('')}</div>
          </div>
        </article>
      </div>
    `;
  }

  // === VIEW 5: 12 ADVANCED MODELS ===
  function renderModels() {
    const a = advById.get(ui.advId) || DATA.advanced_models[0];
    const linked = DATA.problems.filter(p => p.advanced_models.includes(a.id));
    const allIds = [...new Set([...a.linked_problem_ids, ...linked.map(x => x.id)])];
    return `
      <div class="section-intro">
        <p class="eyebrow">05 · UNDERGRADUATE & GRADUATE SPECIAL MODELS</p>
        <h2>十二个高频本科 / 研究生下放特种物理模型（U-01 至 U-12）</h2>
        <p>当 CPhO 决赛、PanPhO、Physics Cup 与 PLANCKS 直接引入大学甚至研究生背景时，本库帮你把抽象模型翻译成清晰的高中力学/电磁/统计语言。</p>
      </div>

      <div class="split-layout">
        <aside class="quiet-toc" aria-label="十二个前沿模型目录">
          <p class="toc-label">特种模型目录</p>
          ${DATA.advanced_models.map(item => `
            <button class="toc-btn ${item.id === a.id ? 'active' : ''}" data-select-adv="${esc(item.id)}">
              <small><span>${esc(item.code)}</span><span>${esc(item.exam_probability.split('·')[0].trim())}</span></small>
              <strong>${mdInline(item.title)}</strong>
            </button>
          `).join('')}
        </aside>

        <article class="monograph">
          <div class="model-block">
            <div class="model-block-head">
              <span class="badge teal mono">${esc(a.code)}</span>
              <span class="badge accent">${esc(a.course_origin)}</span>
              <span class="badge hl">${esc(a.exam_probability)}</span>
            </div>
            <h2 style="font:600 25px/1.35 var(--serif);margin:6px 0 12px">${mdInline(a.title)}</h2>

            <div class="teal-note">
              <strong>高中物理桥梁（30 秒直觉理解）：</strong><br>${mdInline(a.plain_intuition)}
            </div>

            <h3>核心方程与推导骨架</h3>
            ${a.core_equations.map(eq => `
              <div class="conclusion-formula">
                <div style="font-size:13px;font-weight:600;color:var(--accent-deep)">${mdInline(eq.label)}</div>
                <div class="math-block">$$${escMath(eq.tex)}$$</div>
                <div style="font-size:13.5px;color:var(--ink-soft)">${mdInline(eq.note)}</div>
              </div>
            `).join('')}

            <h3>考题“脚手架”拆解规律</h3>
            <p>${mdInline(a.exam_scaffolding_pattern)}</p>

            <div class="copper-note">
              <strong>模型适用边界与失效条件：</strong>${mdInline(a.validity_limits)}
            </div>

            <h4>前置数学工具</h4>
            <div class="ref-chips" style="margin-bottom:18px">
              ${a.prerequisite_math_ids.map(mid => {
                const m = mathById.get(mid);
                return m ? `<button class="chip-btn" data-jump-math="${esc(mid)}">${esc(m.code)} · ${mdInline(m.name)} ↗</button>` : '';
              }).join('')}
            </div>

            <h4>关联真题实战入口（${allIds.length} 题）</h4>
            <div class="ref-chips">${allIds.map(pid => problemChip(pid)).join('')}</div>
          </div>
        </article>
      </div>
    `;
  }

  // === VIEW 6: 283-PROBLEM WORKBENCH & PITFALL CLINIC ===
  function filteredProblems() {
    const w = ui.wb;
    const terms = w.search.toLowerCase().trim().split(/\s+/).filter(Boolean);
    const tierOrder = { L1: 1, L2: 2, L3: 3, L4: 4 };
    const diffOrder = { D1: 1, D2: 2, D3: 3, D4: 4, D5: 5 };
    return DATA.problems.filter(p => {
      if (w.topic && p.primary_topic !== w.topic && !p.secondary_topics.includes(w.topic)) return false;
      if (w.subtopic && p.subtopic !== w.subtopic) return false;
      if (w.archetype && !p.archetypes.includes(w.archetype)) return false;
      if (w.tier && p.tier !== w.tier) return false;
      if (w.contest && p.contest !== w.contest) return false;
      if (w.difficulty && p.difficulty !== w.difficulty) return false;
      const st = getStatus(p.id);
      if (w.status && st !== w.status) return false;
      if (w.onlyHl && !p.blind_highlight) return false;
      if (w.onlyReview && st !== 'review') return false;
      if (terms.length) {
        const hay = [
          p.id, p.title, p.title_zh, p.contest, p.year, p.stage_label,
          p.primary_topic_title, p.subtopic, p.subtopic_name, p.model, p.study_note,
          ...(p.teaching_tags || []), p.blind_highlight?.kind
        ].join(' ').toLowerCase();
        if (!terms.every(t => hay.includes(t))) return false;
      }
      return true;
    }).sort((a, b) => {
      if (w.sort === 'tier_asc') return (tierOrder[a.tier] - tierOrder[b.tier]) || (b.year - a.year) || a.id.localeCompare(b.id);
      if (w.sort === 'year_desc') return (b.year - a.year) || (tierOrder[a.tier] - tierOrder[b.tier]) || a.id.localeCompare(b.id);
      if (w.sort === 'diff_desc') return (diffOrder[b.difficulty] - diffOrder[a.difficulty]) || (b.year - a.year);
      return a.id.localeCompare(b.id);
    });
  }

  function renderWorkbenchRows(visible) {
    return visible.map(p => {
      const st = getStatus(p.id);
      const hl = p.blind_highlight ? `<span class="badge hl">★ ${esc(p.blind_highlight.kind)}</span>` : '';
      return `<article class="problem-row">
        <div>
          <div class="problem-row-meta">
            <span class="badge tier-${esc(p.tier)}">${esc(p.tier)}</span>
            <span class="badge mono">${esc(p.difficulty)}</span>
            <span class="badge">${esc(p.contest)} ${esc(p.year)} · ${esc(p.stage_label)}${p.question ? ` Q${p.question}` : ''}</span>
            <span class="badge accent">${esc(p.subtopic)} · ${esc(p.primary_topic_title.split('、')[0])}</span>
            ${hl}
          </div>
          <h4><button class="prob-chip" style="border:0;background:transparent;padding:0;font:inherit" data-open-problem="${esc(p.id)}">${esc(p.title_zh || p.title)}</button></h4>
          <p class="problem-row-note">${mdInline(p.study_note)}</p>
          <div class="ref-chips">
            ${(p.teaching_tags || []).slice(0, 4).map(t => `<span class="badge">${esc(t)}</span>`).join('')}
          </div>
        </div>
        <div class="problem-row-actions">
          <select class="status-select" data-status-pid="${esc(p.id)}" data-status="${esc(st)}" aria-label="修改状态">
            ${Object.entries(STATUS_META).map(([k, v]) => `<option value="${k}" ${st === k ? 'selected' : ''}>${v.label}</option>`).join('')}
          </select>
          <button class="solid-btn" data-open-problem="${esc(p.id)}">开始盲解训练 →</button>
        </div>
      </article>`;
    }).join('') || '<div class="editorial-note">当前筛选条件下没有匹配题目，可点击「重置筛选」。</div>';
  }

  function updateWorkbenchResultsOnly() {
    const rows = filteredProblems();
    const visible = rows.slice(0, ui.wb.limit);
    const res = $('wb-results');
    const cnt = $('wb-count');
    const moreWrap = $('wb-more-wrap');
    if (!res) { renderApp(); return; }
    cnt.innerHTML = `共匹配 <strong>${rows.length}</strong> 题${rows.length > visible.length ? `（当前展示前 ${visible.length} 题）` : ''}`;
    res.innerHTML = renderWorkbenchRows(visible);
    if (rows.length > visible.length) {
      moreWrap.hidden = false;
      $('wb-more').textContent = `继续加载更多题目（剩余 ${rows.length - visible.length} 题）`;
    } else {
      moreWrap.hidden = true;
    }
    typesetNode(res, false);
  }

  function renderWorkbench() {
    const w = ui.wb;
    const rows = filteredProblems();
    const visible = rows.slice(0, w.limit);
    const allSubtopics = DATA.topics.flatMap(t => t.syllabus_matrix.map(s => ({ code: s.code, name: s.name, topic: t.id })))
      .filter(s => !w.topic || s.topic === w.topic);

    return `
      <div class="section-intro">
        <p class="eyebrow">06 · 283-PROBLEM WORKBENCH & PITFALL CLINIC</p>
        <h2>283 题多维刷题工作台、待二刷清单与易错点诊所</h2>
        <p>按八大专题、44 个子考纲、九大题型母版、L1–L4 梯次、以及 49 道「★ 盲解亮点/官方勘误」精筛题目，进度自动保存在本地浏览器。</p>
      </div>

      <section class="workbench-filters">
        <div class="search-row">
          <div class="search-input-wrap">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true" style="color:var(--accent);flex-shrink:0"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.35-4.35"/></svg>
            <input id="wb-search" type="search" value="${esc(w.search)}" placeholder="搜索题名、核心模型、学习批注、编号或输入 勘误 / 端图 / 莫比乌斯…">
            <kbd>/</kbd>
          </div>
          <button class="outline-btn" id="wb-clear">重置筛选 ↺</button>
        </div>

        <div class="filter-grid">
          <label>专题模块
            <select id="wb-topic">
              <option value="">全部八专题（含交叉）</option>
              ${DATA.topics.map(t => `<option value="${esc(t.id)}" ${w.topic === t.id ? 'selected' : ''}>${esc(t.code)} · ${esc(t.title)}</option>`).join('')}
            </select>
          </label>
          <label>子考纲
            <select id="wb-subtopic">
              <option value="">全部子考纲</option>
              ${allSubtopics.map(s => `<option value="${esc(s.code)}" ${w.subtopic === s.code ? 'selected' : ''}>${esc(s.code)} · ${esc(s.name)}</option>`).join('')}
            </select>
          </label>
          <label>题型母版
            <select id="wb-archetype">
              <option value="">全部九大母版</option>
              ${DATA.framework.archetypes.map(a => `<option value="${esc(a.id)}" ${w.archetype === a.id ? 'selected' : ''}>${esc(a.code)} · ${esc(a.name)}</option>`).join('')}
            </select>
          </label>
          <label>备赛梯次
            <select id="wb-tier">
              <option value="">全部梯次 (L1–L4)</option>
              ${Object.entries(TIER_META).map(([k, v]) => `<option value="${k}" ${w.tier === k ? 'selected' : ''}>${v}</option>`).join('')}
            </select>
          </label>
          <label>赛事来源
            <select id="wb-contest">
              <option value="">全部四大赛事</option>
              ${['CPhO', 'PanPhO', 'Physics Cup', 'PLANCKS'].map(c => `<option value="${c}" ${w.contest === c ? 'selected' : ''}>${c}</option>`).join('')}
            </select>
          </label>
          <label>原始难度
            <select id="wb-difficulty">
              <option value="">全部 (D1–D5)</option>
              ${['D1', 'D2', 'D3', 'D4', 'D5'].map(d => `<option value="${d}" ${w.difficulty === d ? 'selected' : ''}>${d}</option>`).join('')}
            </select>
          </label>
          <label>我的刷题状态
            <select id="wb-status">
              <option value="">全部状态</option>
              ${Object.entries(STATUS_META).map(([k, v]) => `<option value="${k}" ${w.status === k ? 'selected' : ''}>${v.label}</option>`).join('')}
            </select>
          </label>
          <label>排序方式
            <select id="wb-sort">
              <option value="tier_asc" ${w.sort === 'tier_asc' ? 'selected' : ''}>梯次 L1→L4（新题优先）</option>
              <option value="year_desc" ${w.sort === 'year_desc' ? 'selected' : ''}>年份从新到旧</option>
              <option value="diff_desc" ${w.sort === 'diff_desc' ? 'selected' : ''}>难度 D5→D1</option>
              <option value="id" ${w.sort === 'id' ? 'selected' : ''}>按题目 ID</option>
            </select>
          </label>
        </div>

        <div class="filter-toggles">
          <label class="check-toggle"><input type="checkbox" id="wb-hl" ${w.onlyHl ? 'checked' : ''}> 仅看 ★ 盲解亮点与官方勘误（${DATA.stats.blind_highlight_count} 题）</label>
          <label class="check-toggle"><input type="checkbox" id="wb-review" ${w.onlyReview ? 'checked' : ''}> 仅看我的「待二刷」清单</label>
          <div class="spacer">
            <button class="chip-btn" id="wb-export">导出学习进度 JSON ↓</button>
            <label class="chip-btn" style="cursor:pointer">导入进度 ↑<input type="file" id="wb-import" accept="application/json" hidden></label>
            <button class="chip-btn" id="wb-reset">清空进度</button>
          </div>
        </div>
      </section>

      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;font-size:13px;color:var(--muted)">
        <span id="wb-count">共匹配 <strong>${rows.length}</strong> 题${rows.length > visible.length ? `（当前展示前 ${visible.length} 题）` : ''}</span>
        <span>提示：点击任意题目打开 5 标签「防剧透刷题抽屉」</span>
      </div>

      <section id="wb-results">
        ${renderWorkbenchRows(visible)}
      </section>

      <div id="wb-more-wrap" style="text-align:center;margin:20px 0" ${rows.length > visible.length ? '' : 'hidden'}>
        <button class="outline-btn" id="wb-more">继续加载更多题目（剩余 ${Math.max(0, rows.length - visible.length)} 题）</button>
      </div>

      <section class="monograph-section">
        <h3>六大高频易错点诊所（跨全库 283 题提炼）</h3>
        <div class="two-col">
          ${DATA.framework.pitfall_clinics.map(pit => `
            <article class="pitfall-card">
              <h4>${mdInline(pit.title)}</h4>
              <p style="font-size:13.5px"><strong>错因机制：</strong>${mdInline(pit.mechanism)}</p>
              <ul style="font-size:13px;padding-left:18px">${pit.symptoms.map(s => `<li>${mdInline(s)}</li>`).join('')}</ul>
              <div class="copper-note" style="font-size:12.5px"><strong>自查铁律：</strong>${mdInline(pit.remedy_rule)}</div>
              <div class="ref-chips">${pit.examples.map(ex => problemChip(ex.id, false)).join('')}</div>
            </article>
          `).join('')}
        </div>
      </section>

      <section class="monograph-section">
        <h3>${esc(DATA.framework.self_audit_protocol.title)}</h3>
        <p style="color:var(--ink-soft)">${esc(DATA.framework.self_audit_protocol.subtitle)}</p>
        <div class="audit-checklist">
          ${DATA.framework.self_audit_protocol.checks.map(chk => `
            <div class="audit-item">
              <span class="badge accent">${esc(chk.name)}</span>
              <span>${mdInline(chk.detail)}</span>
            </div>
          `).join('')}
        </div>
      </section>
    `;
  }

  // === ANTI-SPOILER PROBLEM DRAWER ===
  function openDrawer(pid) {
    const p = byId.get(pid);
    if (!p) return;
    ui.drawerPid = pid;
    ui.drawerTab = 'problem';
    renderDrawer();
    $('study-drawer').showModal();
    syncHash();
  }

  function closeDrawer() {
    if ($('study-drawer').open) $('study-drawer').close();
    ui.drawerPid = null;
    drawerEpoch++;
    syncHash();
  }

  function renderAtlasImages(imgs) {
    return (imgs || []).map(im => `
      <figure class="crop-figure">
        <img loading="lazy" src="${esc(im.path)}" alt="原卷第 ${im.page} 页">
        <figcaption>原卷第 ${im.page} 页 · ${esc(im.status || '切片')}${im.original ? ` · <a href="${esc(im.original)}#page=${im.page}" target="_blank" rel="noopener">对照原始 PDF ↗</a>` : ''}</figcaption>
      </figure>
    `).join('');
  }

  function renderAtlasSolutionPages(att) {
    return (att.pages || []).map(im => `
      <figure class="crop-figure">
        <img loading="lazy" src="${esc(im.path)}" alt="${esc(att.author)} 解答第 ${im.page} 页">
        <figcaption>${esc(att.author)} · 原页 ${im.page} · <a href="${esc(att.path)}#page=${im.page}" target="_blank" rel="noopener">打开原 PDF ↗</a></figcaption>
      </figure>
    `).join('');
  }

  function renderAtlasSolutionRecord(sol) {
    if (sol.solution_attachments?.length) {
      const first = sol.solution_attachments[0];
      return `
        <div class="editorial-note" data-sol-group="${esc(sol.id)}" style="max-width:none">
          <div style="display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin-bottom:8px">
            <label><strong>切换解答作者：</strong>
              <select data-sol-switch>
                ${sol.solution_attachments.map((a, i) => `<option value="${esc(a.path)}">${i + 1}. ${esc(a.author)}</option>`).join('')}
              </select>
            </label>
            <a href="${esc(first.path)}" download class="chip-btn">下载 PDF ↓</a>
          </div>
          <div data-sol-pages>${renderAtlasSolutionPages(first)}</div>
        </div>
      `;
    }
    if (sol.reader_html) return `<article class="native-problem">${sol.reader_html}</article>`;
    if (sol.images?.length) return renderAtlasImages(sol.images);
    const pdf = (sol.files || []).find(f => f.path.endsWith('.pdf'));
    return pdf
      ? `<p><a class="outline-btn" href="${esc(pdf.path)}" target="_blank" rel="noopener">在新窗口阅读解答 PDF ↗</a></p><iframe style="width:100%;height:56vh;border:1px solid var(--line)" src="${esc(pdf.path)}"></iframe>`
      : '<p class="editorial-note">此条解答记录暂无图像或 HTML 正文，请通过上方 Atlas 链接查看原始文档。</p>';
  }

  function renderDrawer() {
    const p = byId.get(ui.drawerPid);
    if (!p) return;
    const atlas = getAtlasRecord(p.id);
    const st = getStatus(p.id);
    const topic = topicById.get(p.primary_topic);

    $('drawer-meta').textContent = `${p.contest_label} / ${p.year} / ${p.stage_label}${p.question ? ` / Q${p.question}` : ''} · ${p.subtopic} ${p.subtopic_name}`;
    $('drawer-title').textContent = p.title_zh || p.title;
    $('drawer-subtitle').textContent = p.title_zh ? p.title : '';
    $('drawer-atlas-link').href = `./index.html?view=problems&search=${encodeURIComponent(p.id)}`;
    $('drawer-tier-info').innerHTML = `<span class="badge tier-${esc(p.tier)}">${esc(p.tier)}</span> <span class="badge mono">${esc(p.difficulty)}</span> ${p.blind_highlight ? `<span class="badge hl">★ ${esc(p.blind_highlight.kind)}</span>` : ''}`;

    $('drawer-status-pills').innerHTML = Object.entries(STATUS_META).map(([k, v]) => `
      <button class="chip-btn ${st === k ? 'active' : ''}" data-drawer-status="${k}">${v.label}</button>
    `).join('');

    document.querySelectorAll('.dtab').forEach(btn => btn.classList.toggle('active', btn.dataset.dtab === ui.drawerTab));

    const body = $('drawer-body');
    if (ui.drawerTab === 'problem') {
      let html = `<div class="editorial-note" style="margin-top:0"><strong>专题定位：</strong>${esc(topic?.title || '')} · <code>${esc(p.subtopic)}</code>（${esc(p.subtopic_name)}） · 防剧透模式仅显示原题面/译文与插图，核心模型与解法请独立思考后再切换到「② 渐进提示」。</div>`;
      if (atlas?.translation_zh) {
        const figures = (atlas.reader_html || '').match(/<img\b[^>]*>/gi) || [];
        html += `<article class="native-problem">
          <div class="copper-note" style="margin-top:0">${esc(atlas.translation_zh.notice)}</div>
          ${mdParagraphs(atlas.translation_zh.body)}
          ${figures.length ? `<h4>原题附图</h4>${figures.map(img => `<figure class="crop-figure">${img}</figure>`).join('')}` : ''}
          ${atlas.images?.length ? `<details class="hint-box"><summary>展开对照原始 PDF 题面切图（${atlas.images.length} 页）</summary>${renderAtlasImages(atlas.images)}</details>` : ''}
        </article>`;
      } else if (atlas?.reader_html) {
        html += `<article class="native-problem">${atlas.reader_html}</article>`;
      } else if (atlas?.images?.length) {
        html += renderAtlasImages(atlas.images);
      } else if (atlas?.files?.find(f => f.path.endsWith('.pdf'))) {
        const pdf = atlas.files.find(f => f.path.endsWith('.pdf'));
        html += `<p><a class="outline-btn" href="${esc(pdf.path)}" target="_blank" rel="noopener">阅读原始 PDF ↗</a></p>`;
      } else {
        html += `<div class="teal-note">当前以独立讲义模式运行（未加载大体积 <code>data.js</code> 图库），请点击右上角 <strong>「在 Atlas 中查看 ↗」</strong> 阅读原卷高清切片或原题 PDF。</div>`;
      }
      body.innerHTML = html;
    } else if (ui.drawerTab === 'hints') {
      const mList = p.math_tools.map(id => mathById.get(id)?.name.split('、')[0]).filter(Boolean);
      const archList = p.archetypes.map(id => archById.get(id)?.name).filter(Boolean);
      body.innerHTML = `
        <p class="editorial-note" style="margin-top:0">建议先独立演算至少 25 分钟；确实卡死再逐层点开提示 1 → 2 → 3，保留自主破题成就感。</p>
        <details class="hint-box">
          <summary>提示 1 · 模型定位与核心抓手（剧透度：极低）</summary>
          <p><strong>所属母版：</strong>${archList.map(x => `<span class="badge accent">${esc(x)}</span>`).join(' ')}</p>
          <p><strong>核心模型：</strong>${mdInline(p.model)}</p>
          <p><strong>教练切入批注：</strong>${mdInline(p.study_note)}</p>
          <p><strong>涉及数学工具：</strong>${mList.map(x => `<span class="badge teal">${esc(x)}</span>`).join(' ')}</p>
        </details>
        <details class="hint-box">
          <summary>提示 2 · 问题关键拆解步骤（剧透度：中）</summary>
          <ol>${(p.decomposition || []).map(step => `<li>${mdInline(step)}</li>`).join('')}</ol>
        </details>
        <details class="hint-box">
          <summary>提示 3 · 本题结构难点与考场红灯陷阱（剧透度：较高）</summary>
          <h4>核心结构难点</h4>
          <ul>${(p.hard_points || []).map(x => `<li>${mdInline(x)}</li>`).join('')}</ul>
          <div class="copper-note">
            <strong>高频易错预警：</strong>
            <ul style="margin:6px 0 0;padding-left:18px">${(p.pitfalls || []).map(x => `<li>${mdInline(x)}</li>`).join('')}</ul>
          </div>
        </details>
      `;
    } else if (ui.drawerTab === 'blind') {
      const hl = p.blind_highlight
        ? `<div class="copper-note" style="margin-top:0"><strong>★ ${esc(p.blind_highlight.kind)}：</strong>${mdInline(p.blind_highlight.note)}</div>`
        : '';
      const bp = atlas?.teaching?.blind_process
        ? `<details class="hint-box" open><summary>Phase 1 完整独立盲解原始推导手稿</summary>${mdRich(atlas.teaching.blind_process)}</details>`
        : `<div class="model-block"><h4>模型主线</h4>${mdParagraphs(p.overview)}</div>`;
      body.innerHTML = `
        ${hl}
        <p style="font-size:13px;color:var(--muted)">适用水平：${esc(p.level)} · 以下为先不看答案独立盲解、再对照官方解答的教学复盘（未经人工逐题审校，以原卷为准）。</p>
        ${bp}
        <div class="model-block">
          <h4>对照参考解答差异与勘误检查</h4>
          ${mdParagraphs(p.comparison)}
        </div>
        <div class="teal-note">
          <strong>教练迁移总结：</strong>${mdParagraphs(p.takeaways)}
        </div>
      `;
    } else if (ui.drawerTab === 'solution') {
      const sols = (atlas?.solution_ids || []).map(id => getAtlasRecord(id)).filter(Boolean);
      if (sols.length) {
        body.innerHTML = sols.map(s => `<h3 style="margin-top:0">${esc(s.title)}</h3>${renderAtlasSolutionRecord(s)}`).join('');
      } else {
        body.innerHTML = `<div class="editorial-note" style="margin-top:0">${p.has_solution ? '正在连接 Atlas 解答原件，或请通过右上角「在 Atlas 中查看 ↗」打开完整原卷解答。' : '本题仓内无独立官方解答 PDF（属于 44 道无官方答案独立交叉检验题），请参考「③ 盲解推导与对比」标签页中的多方法交叉检验推导。'}</div>`;
      }
    } else if (ui.drawerTab === 'notes') {
      const savedNote = userState.notes[p.id] || '';
      const savedAudit = userState.audits[p.id] || {};
      body.innerHTML = `
        <h3 style="margin-top:0">做完本题后的 5 维自检清单</h3>
        <div class="audit-checklist">
          ${DATA.framework.self_audit_protocol.checks.map(chk => `
            <label class="audit-item">
              <input type="checkbox" data-audit-chk="${esc(chk.id)}" ${savedAudit[chk.id] ? 'checked' : ''}>
              <span><strong>${esc(chk.name)}：</strong>${mdInline(chk.detail)}</span>
            </label>
          `).join('')}
        </div>
        <h3>我的卡壳点 / 二刷复盘笔记</h3>
        <p style="font-size:13px;color:var(--muted);margin-top:0">建议只记“哪一步想偏了 / 漏了哪个守恒量或符号约定”，无需抄写完整答案过程。</p>
        <textarea class="notes-textarea" id="drawer-note-input" placeholder="记录本题暴露的知识盲区、数学卡点或自检发现…">${esc(savedNote)}</textarea>
        <div style="display:flex;gap:10px;margin-top:12px;align-items:center">
          <button class="solid-btn" id="drawer-save-note">保存笔记</button>
          <span style="font-size:12px;color:var(--muted)">自动保存于当前浏览器 localStorage</span>
        </div>
      `;
    }
    typesetNode(body, true);
  }

  // Main Render & Event Wiring
  function renderApp() {
    updateStatStrip();
    document.querySelectorAll('#primary-tabs .tab-btn').forEach(b => {
      const active = b.dataset.view === ui.view;
      b.classList.toggle('active', active);
      if (active && b.parentElement) {
        const nav = b.parentElement;
        const targetLeft = b.offsetLeft - Math.max(0, (nav.clientWidth - b.offsetWidth) / 2);
        nav.scrollTo({ left: targetLeft, behavior: 'auto' });
      }
    });
    const root = $('view-root');
    if (ui.view === 'overview') root.innerHTML = renderOverview();
    else if (ui.view === 'syllabus') root.innerHTML = renderSyllabus();
    else if (ui.view === 'topics') root.innerHTML = renderTopics();
    else if (ui.view === 'math') root.innerHTML = renderMath();
    else if (ui.view === 'models') root.innerHTML = renderModels();
    else if (ui.view === 'workbench') root.innerHTML = renderWorkbench();

    syncHash();
    typesetNode(root, false);
  }

  $('site-lead').textContent = DATA.framework.meta.subtitle;
  $('footer-disclaimer').textContent = DATA.framework.meta.disclaimer;

  $('primary-tabs').addEventListener('click', e => {
    const btn = e.target.closest('[data-view]');
    if (!btn) return;
    ui.view = btn.dataset.view;
    renderApp();
  });

  document.body.addEventListener('click', e => {
    const openBtn = e.target.closest('[data-open-problem]');
    if (openBtn) { openDrawer(openBtn.dataset.openProblem); return; }

    const planBtn = e.target.closest('[data-select-plan]');
    if (planBtn) { ui.planId = planBtn.dataset.selectPlan; renderApp(); return; }

    const archBtn = e.target.closest('[data-select-arch]');
    if (archBtn) { ui.archId = archBtn.dataset.selectArch; renderApp(); return; }

    const sylTopicBtn = e.target.closest('[data-syl-topic]');
    if (sylTopicBtn) { ui.syllabusTopic = sylTopicBtn.dataset.sylTopic; renderApp(); return; }

    const topicBtn = e.target.closest('[data-select-topic]');
    if (topicBtn) { ui.topicId = topicBtn.dataset.selectTopic; renderApp(); return; }

    const mathBtn = e.target.closest('[data-select-math]');
    if (mathBtn) { ui.mathId = mathBtn.dataset.selectMath; renderApp(); return; }

    const advBtn = e.target.closest('[data-select-adv]');
    if (advBtn) { ui.advId = advBtn.dataset.selectAdv; renderApp(); return; }

    const jMath = e.target.closest('[data-jump-math]');
    if (jMath) { ui.view = 'math'; ui.mathId = jMath.dataset.jumpMath; renderApp(); window.scrollTo({ top: 0, behavior: 'smooth' }); return; }

    const jAdv = e.target.closest('[data-jump-adv]');
    if (jAdv) { ui.view = 'models'; ui.advId = jAdv.dataset.jumpAdv; renderApp(); window.scrollTo({ top: 0, behavior: 'smooth' }); return; }

    const jPhase = e.target.closest('[data-jump-phase]');
    if (jPhase) { jumpToWorkbench({ topic: jPhase.dataset.jumpPhase, tier: jPhase.dataset.jumpTier }); return; }

    const jSub = e.target.closest('[data-jump-sub]');
    if (jSub) { jumpToWorkbench({ topic: jSub.dataset.jumpTopic, subtopic: jSub.dataset.jumpSub }); return; }

    const jArch = e.target.closest('[data-jump-arch]');
    if (jArch) { jumpToWorkbench({ archetype: jArch.dataset.jumpArch }); return; }

    if (e.target.id === 'wb-clear') { jumpToWorkbench({}); return; }
    if (e.target.id === 'wb-more') { ui.wb.limit += 40; renderApp(); return; }
    if (e.target.id === 'wb-export') {
      const blob = new Blob([JSON.stringify(userState, null, 2)], { type: 'application/json' });
      const u = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = u;
      a.download = 'physics-study-progress.json';
      a.click();
      setTimeout(() => URL.revokeObjectURL(u), 1000);
      toast('已导出个人备赛进度 JSON');
      return;
    }
    if (e.target.id === 'wb-reset') {
      if (confirm('确定清空本地刷题状态、考纲掌握勾选与复盘笔记吗？（不可撤销）')) {
        userState = { statuses: {}, notes: {}, audits: {}, masteredSubtopics: {} };
        saveState();
        renderApp();
        toast('已清空本地进度');
      }
      return;
    }

    const dStatus = e.target.closest('[data-drawer-status]');
    if (dStatus && ui.drawerPid) {
      setStatus(ui.drawerPid, dStatus.dataset.drawerStatus);
      renderDrawer();
      renderApp();
      return;
    }

    const dTab = e.target.closest('[data-dtab]');
    if (dTab && ui.drawerPid) {
      ui.drawerTab = dTab.dataset.dtab;
      renderDrawer();
      return;
    }

    if (e.target.id === 'drawer-save-note' && ui.drawerPid) {
      userState.notes[ui.drawerPid] = $('drawer-note-input').value;
      saveState();
      toast('复盘笔记已保存');
      return;
    }
  });

  document.body.addEventListener('change', e => {
    const t = e.target;
    if (t.matches('[data-master-sub]')) {
      const code = t.dataset.masterSub;
      if (t.checked) userState.masteredSubtopics[code] = true;
      else delete userState.masteredSubtopics[code];
      saveState();
      return;
    }
    if (t.matches('[data-status-pid]')) {
      setStatus(t.dataset.statusPid, t.value);
      t.dataset.status = t.value;
      return;
    }
    if (t.matches('[data-audit-chk]') && ui.drawerPid) {
      const pid = ui.drawerPid;
      userState.audits[pid] = userState.audits[pid] || {};
      userState.audits[pid][t.dataset.auditChk] = t.checked;
      saveState();
      return;
    }
    if (t.matches('[data-sol-switch]')) {
      const group = t.closest('[data-sol-group]');
      const sol = getAtlasRecord(group?.dataset.solGroup);
      const att = sol?.solution_attachments?.find(a => a.path === t.value);
      if (att) group.querySelector('[data-sol-pages]').innerHTML = renderAtlasSolutionPages(att);
      return;
    }
    if (t.id === 'wb-topic') { ui.wb.topic = t.value; ui.wb.subtopic = ''; ui.wb.limit = 40; renderApp(); return; }
    if (t.id === 'wb-subtopic') { ui.wb.subtopic = t.value; ui.wb.limit = 40; renderApp(); return; }
    if (t.id === 'wb-archetype') { ui.wb.archetype = t.value; ui.wb.limit = 40; renderApp(); return; }
    if (t.id === 'wb-tier') { ui.wb.tier = t.value; ui.wb.limit = 40; renderApp(); return; }
    if (t.id === 'wb-contest') { ui.wb.contest = t.value; ui.wb.limit = 40; renderApp(); return; }
    if (t.id === 'wb-difficulty') { ui.wb.difficulty = t.value; ui.wb.limit = 40; renderApp(); return; }
    if (t.id === 'wb-status') { ui.wb.status = t.value; ui.wb.limit = 40; renderApp(); return; }
    if (t.id === 'wb-sort') { ui.wb.sort = t.value; ui.wb.limit = 40; renderApp(); return; }
    if (t.id === 'wb-hl') { ui.wb.onlyHl = t.checked; ui.wb.limit = 40; renderApp(); return; }
    if (t.id === 'wb-review') { ui.wb.onlyReview = t.checked; ui.wb.limit = 40; renderApp(); return; }
    if (t.id === 'wb-import' && t.files?.[0]) {
      t.files[0].text().then(txt => {
        const parsed = JSON.parse(txt);
        userState = {
          statuses: parsed.statuses || {},
          notes: parsed.notes || {},
          audits: parsed.audits || {},
          masteredSubtopics: parsed.masteredSubtopics || {}
        };
        saveState();
        renderApp();
        toast('已导入学习进度 JSON');
      }).catch(() => toast('进度文件格式无效，导入失败'));
    }
  });

  document.body.addEventListener('input', e => {
    if (e.target.id === 'wb-search') {
      ui.wb.search = e.target.value;
      ui.wb.limit = 40;
      updateWorkbenchResultsOnly();
    } else if (e.target.id === 'drawer-note-input' && ui.drawerPid) {
      userState.notes[ui.drawerPid] = e.target.value;
      saveState();
    }
  });

  $('drawer-close').onclick = closeDrawer;
  $('study-drawer').addEventListener('cancel', e => {
    e.preventDefault();
    closeDrawer();
  });

  document.addEventListener('keydown', e => {
    if (e.key === '/' && !$('study-drawer').open && !/INPUT|SELECT|TEXTAREA/.test(e.target.tagName)) {
      if (ui.view !== 'workbench') {
        ui.view = 'workbench';
        renderApp();
      }
      e.preventDefault();
      $('wb-search')?.focus();
    }
  });

  parseHash();
  renderApp();
  if (ui.drawerPid) {
    openDrawer(ui.drawerPid);
  }
})();
