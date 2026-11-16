# Physics Atlas · 物理竞赛资料库与单题训练系统

面向校内物理竞赛学习与教学研究小范围使用的题库与解析平台，整理 **CPhO（全国中学生物理竞赛）**、**PanPhO（泛珠三角物理奥林匹克）**、**Physics Cup** 与 **PLANCKS**（2019–2026）的已有原件、逐题切分图、英文题目中文辅助译文及逐题教学拆解。

---

## 访问与部署方针

- **GitHub Pages（校内便捷访问）**：通过 [pages.yml](.github/workflows/pages.yml) 直接构建并部署完整内部版（`sites/internal/dist`）页面与静态资源，包含原题图像/原生图文、PDF 原件下载、中文辅助译文、参考解答及全套教学分析与盲解流程，供校内小范围学习使用。
- **GPT Sites 保持原有双站隔离政策**：
  - [公开索引站](https://owen-physics-atlas.owenyxliu.chatgpt.site)：仅发布白名单元数据、物理标签与官方来源入口（对应 `docs/` 与 `sites/public/dist`），不含原题、解答、PDF 或切片。
  - [内部资料库](https://owen-physics-library.owenyxliu.chatgpt.site)：保持仅限本人登录访问的保护策略。

---

## 内容概览与单题训练功能

当前归档 **145 条来源记录**，拆分并整理 **174 道独立题目**：

| 竞赛 | 涵盖年份与场次 | 单题数 | 参考解答配对 | 特色说明 |
| --- | --- | ---: | ---: | --- |
| **CPhO** | 2020–2021 复赛 / 决赛理论 | 28 | 28 | 全套官方解答切片，高清原卷对照 |
| **PanPhO** | 2019–2026 综合卷二 | 16 | 15 | 科研背景多步骤建模，含 2024 Q1 错配说明 |
| **Physics Cup** | 2019–2026 | 41 | 36 | 原生网页 + 本地 MathJax 公式重排，配中文译文 |
| **PLANCKS** | 2019–2026 预赛 / 决赛 | 89 | 59 | 11 套原卷完整切分，均配中文辅助译文 |

### 网页端核心使用方式

1. **多维检索与按模型找题**：
   - 在「逐题探索」中可按**竞赛、年份、物理类型、受控领域、方法/易错主题、难度（D1–D5）**联合筛选，并支持按难度排序。
   - 搜索框支持检索**中英文题名、核心物理模型、细粒度教学标签**，也可直接输入 `盲解更优` 或 `官方笔误` 筛选带有独立盲解亮点的题目。
2. **单题阅读器四标签页**：
   - **中文译文**（Physics Cup 与 PLANCKS 共 130 题）：AI 辅助中文题面 + 原卷插图，可一键展开原题图像对照核验。
   - **原题阅读 / 参考解答**：保留 PDF 原卷高清切图（附原页坐标与原件 SHA-256 校验）或按作者切换的参赛者解答原页。
   - **教学拆解 · 易错分析**：全库 174 题均采用两阶段分析流程（先仅看原题独立盲解，再对照参考解答），包含：
     - **模型主线与问题拆解**；
     - **完整 Phase 1 盲解原始推导流程**（默认展开，展示不看答案时的完整破题与演算过程，并对 24 道**盲解路径更优或纠出官方印刷/计算笔误**的题目给出专门标注）；
     - **参考解答对照、核心难点、高频易错点与教练迁移总结**（综合总结见 [TEACHING_ANALYSIS_SUMMARY.md](notes/TEACHING_ANALYSIS_SUMMARY.md)）。

---

## 使用边界与免责声明

- **AI 内容核验提醒**：全部中文译文、物理标签、`D1–D5` 难度评级、教学拆解、盲解过程及对官方解答的笔误判断均由 AI 生成，**未经人工逐题审校**；所有公式、边界条件与定量结果请以原卷 PDF / 原图为准。
- **版权声明**：收录的竞赛试题与官方/获奖解答版权归原竞赛主办方及原作者所有；部分赛事官网限制公开再分发。本仓库及 GitHub Pages 部署仅用于校内教学与竞赛备赛小范围研究参考，请勿用于商业用途或公开传播。

---

## 开发者须知

### 目录结构

```text
originals/                 原始 PDF 与采集原件（保留版权，不修改）
derived/                   从 PDF 切分渲染的题目与解答单页图像
catalog/
  extended-resources.json  来源索引、URL 与原件校验信息
  questions.json           逐题切分坐标、解答关联
  translations/            英文题目中文辅助译文源文件 (*.zh.md)
  teaching-batches/        分批次结构化教学拆解 JSON
  teaching-analysis.json   合并后的全库教学数据（含盲解流程）
notes/
  TEACHING_ANALYSIS_SUMMARY.md  174 题难点与易错点综合报告
  problems/batch-*.md      分批次两阶段解析笔记
web/                       共用静态前端与本地 MathJax bundle
docs/                      GPT 公开站同步目录（受 PUBLIC_KEYS 白名单隔离）
scripts/                   采集、切分、合并、构建与隔离检查脚本
```

`sites/` 与 `output/` 不提交至 Git（`.gitignore` 排除，保留 GPT Sites 部署目录与本地凭据隔离）。

### 本地构建与全量校验

依赖 Python 3.10+（`pymupdf`、`beautifulsoup4`、`requests`）及 Node.js：

```bash
python3 scripts/merge_teaching.py      # 合并教学数据与完整盲解流程
python3 scripts/build_sites.py         # 构建 sites/public/dist、sites/internal/dist 与 docs/
python3 scripts/check_sites.py         # 校验文件哈希、切片与前端约束
python3 scripts/check_translations.py  # 校验译文、PLANCKS 切分与公私隔离
python3 scripts/check_public_release.py # 校验 docs/ 公开发布白名单
node --check web/app.js
```

本地预览可在仓库根目录启动 `python3 -m http.server -d sites/internal/dist --bind 127.0.0.1 8080`；向 `main` 分支推送后，GitHub Actions（[pages.yml](.github/workflows/pages.yml)）会自动执行上述构建与全部检查，并将 `sites/internal/dist` 部署至 GitHub Pages。
