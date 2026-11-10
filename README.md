# Physics Atlas · 物理竞赛资料库

更新：2026-11-10。收录全国中学生物理竞赛、泛珠三角物理奥林匹克、Physics Cup、PLANCKS 的已有可用资料，目标范围 2019—2026。年份范围不代表每个竞赛每年都已收齐。

## GitHub：私有源码与公开索引分开

源码仓库：[Owen-Liuyuxuan/physics_competitions](https://github.com/Owen-Liuyuxuan/physics_competitions)。本仓库包含个人研究原件，必须保持私有；不要为了启用 Pages 而改成公开仓库。

- `docs/` 是唯一允许部署到 GitHub Pages 的目录，仅含5个公开索引文件。
- `.github/workflows/pages.yml` 先执行 `scripts/check_public_release.py`，再上传 `docs/`，绝不上传仓库根目录、`originals/`、`derived/` 或内部发行包。
- `sites/` 和 `output/` 不进入 GitHub；原有托管站点身份、Git历史与部署凭据均不上传。
- 私有仓库不等于私有 Pages。内部资料库继续使用原有的本人登录保护，不迁移到公开 Pages。
- GitHub Free 通常不支持从私有仓库启用 Pages；以 GitHub 实际返回的权限/套餐结果为准，不自动改变仓库可见性。
- 2026-11-10 实际启用结果：GitHub API 返回 HTTP 422，当前套餐不支持本私有仓库的 Pages。因此目前没有 GitHub Pages 在线地址；上面的两个已有托管地址继续使用。
- Actions 默认只检查公开发行包，不部署。若之后升级到支持私有仓库 Pages 的套餐，请在仓库 Settings → Pages 启用 GitHub Actions，并设置 Actions 仓库变量 `ENABLE_PAGES=true`，再手动运行工作流。不要将内部发行目录用于 Pages。

## 两个严格分离的站点

已发布：[公开索引](https://owen-physics-atlas.owenyxliu.chatgpt.site) · [内部资料库（仅本人登录）](https://owen-physics-library.owenyxliu.chatgpt.site)。内部站的根页面与原始 PDF 均已进行未登录访问拦截检查。

- `sites/public/dist/`：公开元数据、分类、官方来源入口；不包含原题、解答、PDF、切片、内部站地址。
- `sites/internal/dist/`：个人研究用资料。原件真实下载，PDF 原图逐题阅读，网页题面保留附图和 TeX 公式排版。部署时必须保持 owner-private。
- `web/`：共用界面源码。无笔记系统、无 PDF 纯文本提取页、无本地存储功能。

公开发布依赖字段白名单与独立资产目录，不依赖隐藏按钮。内部站的整个站点和静态资源必须受到托管平台访问控制保护。不要将内部目录上传到公开静态托管。

## 当前内容与边界

- 145 条已有可用来源记录；95 道独立题目索引；46 条逐题解答记录；445 张原有切片。
- 内部发行包含 200 个去重原始文件。另将31题的93份 Physics Cup 解答PDF渲染为392张完整原页图，按作者切换；不展示成绩表、奖金、获奖评述或投稿说明。
- 2019 Physics Cup旧站解答链接未通过TLS证书校验，暂不显示这5条解答；之前误归入解答的题目/提示文件不再以解答展示。原始来源页存档保留在私有目录，未修改下载原件。
- 竞赛显示标签采用中文；去掉自动“数学工具”标签与筛选，避免低质量标签干扰阅读。
- 逐题覆盖：CPhO 28 题、泛珠综合卷二 16 题、Physics Cup 41 题、PLANCKS 2024 共10题。其他已有 PDF 目前直接阅读整卷，尚未全部切分。
- 全国赛2022—2026的第三方待核验入口、没有原件的记录和仅有DOC的记录不进入网页；研究目录中的历史查找记录仍保留。
- PLANCKS 原生资料为 PDF：保留原版公式排印与附图；Physics Cup 原生网页保留图文、转换其 TeX 标记，使用本地 MathJax 3.2.2 SVG 排版，不依赖外部 CDN。
- 所有自动切分均标记待复核；边界、题解配对与物理结论是不同的核验层次。不声称已完成所有题目的独立分析。难度暂未逐题评级，分类标签是关键词初筛。
- 泛珠2024卷二：官网所链解答Q1标题“引力波测量中的误差估计”与题面Q1“时空变介电常数”不一致，故不自动配对。

## 数据与来源溯源

```text
catalog/
  extended-resources.json   原件记录、URL、SHA-256、私有网页图文
  questions.json           题号、原文内部提取、页码、裁切矩形、解答关联
  crop-review-queue.json   尚未适配的整卷（仅维护用，不显示占位）
originals/                 不修改的下载原件
derived/questions/         从 PDF 渲染的切片
web/                       页面与本地数学排版资源
sites/public/              公开发布目录及独立站点身份
sites/internal/            私有发布目录及独立站点身份
scripts/                   收集、切分、构建与隔离检查
output/                    发布包与视觉验收截图
```

原件保留版权；泛珠官网明确限制转载，内部文件不得未经许可再公开分发。网页只展示可用资料；原件保留在本地不代表授权公开。

## 可重复构建

依赖 Python3.10+、requests、beautifulsoup4、pymupdf；Node 用于语法检查与发布工具。MathJax bundle 首次从固定版本下载并本地托管。

```bash
python3 physics-library/scripts/collect_extended.py
python3 physics-library/scripts/collect_web_readers.py
python3 physics-library/scripts/clean_physicscup_solutions.py
python3 physics-library/scripts/render_solution_pages.py
python3 physics-library/scripts/build_questions.py
python3 physics-library/scripts/build_sites.py
python3 physics-library/scripts/check_sites.py
python3 physics-library/scripts/check_public_release.py
node --check physics-library/web/app.js
```

`build_sites.py` 会清理内部生成目录中已不再引用的文件副本，包括旧纯文本快照；不会删除 `originals/` 中的原件。不要往生成目录手工放资料。

本地预览可从 `physics-library/sites` 启动 HTTP 服务器，分别访问 `public/dist/` 与 `internal/dist/`。本地预览没有登录保护，应仅绑定127.0.0.1。发布凭据不写入文件，不提交到 Git。

## 相关研究材料

- [同类竞赛地图](competitions.md)
- [原始官方目录与核验记录](catalog/official-resources.md)
- [全国赛补充查找记录（不进入网页）](catalog/cpho-2022-2026.md)

工作区原有第37届复赛教学网页和 `wuli_fusai.pdf` 未修改，其解答没有因本次收集而被自动认定为已验证。
