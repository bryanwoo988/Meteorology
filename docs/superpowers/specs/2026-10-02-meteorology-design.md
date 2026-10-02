# 气象学 · Meteorology — 设计 Spec

**日期：** 2026-10-02
**作者：** Bryan Woo
**状态：** 已确认（2026-10-02）。界面要求：专业、干净。

---

## 1. 目的

给气象学小白的一本**离线、三语、可以动手玩的气象学入门**。从"大气是什么"一路学到"ECMWF 的 51 个集合成员在算什么"、"Windy 每个图层是什么意思"，并且用马来西亚的天气做例子。

**给谁用：** 对天气有兴趣、但没有气象背景的人——园区管理人员、农业从业者、学生、家人朋友。主要在马来西亚，语言是中文、英文、马来文混用。

**成功的样子：**

1. 一个完全不懂气象的人，按顺序读完 9 个阶段以后，打开 Windy，每个图层都知道是什么、在 App 第几章学过。
2. 看到 MetMalaysia 发的"Buruk"橙色预警，知道代表什么、园里要做什么。
3. 站在没有信号的园区里，也能打开 App 查"露点"是什么意思。

**不是什么：** 不是任何一本教科书的翻版（见 §2），也不是天气预报 App（实时预报交给 CompareCast）。

---

## 2. 资料来源与版权

### 2.1 参考书（全部是商业书，只作参考，不复制）

| 代号 | 书 | 用途 |
|---|---|---|
| PAM | Mote & Sahu, *Principles of Agricultural Meteorology*, Scientific Publishers (India) | **主书**。原理、农业气象、观测仪器 |
| ESS | Ahrens, *Essentials of Meteorology*, 6th ed., Cengage, 2010 | 辅助。云、稳定度、风暴、气候、卫星雷达、预报 |
| FUN | *Fundamentals of Meteorology*（编著本） | 辅助。数值预报、ENSO、MJO、Walker 环流 |
| TERM | *Terminology on Agricultural Meteorology and Agronomy* | 词典与名词定义 |
| LEC | Thaer O. Roomi, *Lectures on Meteorology* | 自测题的出题参考 |
| — | *Understanding Meteorology*（扫描版，无文字层） | **不用** |

| 书里的东西 | 用不用 | 原因 |
|---|---|---|
| 事实、数据、公式、物理定律 | 用 | 事实不受版权保护 |
| 文字 | 不用 | 全部用自己的话重写 |
| 图片、照片、扫描图表 | 不用 | 受版权保护；改成根据数据重画的 SVG |
| 书末选择题 | 不照抄 | 只作出题方向参考，题目自己写 |

参考书 PDF 在 `.gitignore` 里，**永远不上传**。

### 2.2 书以外的资料（必须有官方来源，不乱造）

马来西亚内容、模型现况、卫星、Windy 图层，书里没有或已过时，只用下列官方或一手来源：

| 主题 | 来源 |
|---|---|
| 马来西亚季风、预警、雷达、飑线、气候 | MetMalaysia（met.gov.my）及其研究报告 |
| 空气污染指数 API | 马来西亚环境局 DOE |
| 霾、火点 | ASEAN Specialised Meteorological Centre（ASMC） |
| ECMWF IFS / ENS / AIFS | ecmwf.int |
| GFS / GEFS、ENSO 指数（ONI）、MJO | NOAA EMC、NOAA CPC、NOAA NWS |
| Himawari | JMA 气象卫星中心 |
| 其他卫星 | EUMETSAT、NOAA NESDIS、NASA、ESA、CMA、KMA |
| Skew-T 读图 | NOAA NWS 教学资料 |
| 雷电安全 | MetMalaysia / WMO / NOAA NWS |
| 蒸散 ET₀ | FAO Irrigation and Drainage Paper 56 |
| Windy 图层与模型 | Windy 官方说明（community.windy.com） |
| 历史天气数据（给互动图表用） | ERA5 再分析，经 Open-Meteo Archive API 取得 |

**规则：**

1. 每一条书以外的事实都要有来源 id，挂在段落上；来源 id 必须存在于 `data/sources.json`，含网址和查阅日期。
2. 写之前先打开来源网页核对，核对记录写进 `docs/sources-log.md`（哪一句、哪个网址、哪天查的）。
3. 找不到可靠来源的说法，**不写**。宁可少一段，也不编。
4. 互动图表里的数据也一样：用真实数据（附来源），或明确标示为"示意图"。示意图只能用来表达原理，不能放假的数字。

### 2.3 App icon

`icon.png`（书本 + 云 + 太阳 + 温度计）是 Bryan 付费购买授权的 Flaticon 图标，可直接使用，不需要在 App 里注明作者。

---

## 3. 名称与识别

| 语言 | 名称 | 代码 |
|---|---|---|
| 中文 | 气象学 | `zh` |
| English | Meteorology | `en` |
| Bahasa Melayu | Meteorology | `ms` |

调色盘取自 `icon.png`：

| Token | 色值（实作时从图取样确认） | 来自 |
|---|---|---|
| `sky` | 深蓝 | 外框线、书本 |
| `cloud` | 浅蓝白 | 云 |
| `sun` | 黄 | 太阳 |
| `mercury` | 珊瑚红 | 温度计 |
| `page` | 淡蓝 | 书页 |

深色模式另配一组同色系 token。

发布网址（`APP_URL`）：`https://bryanwoo988.github.io/Meteorology/`（GitHub repo 名 `Meteorology`）。

---

## 4. 功能清单（Bryan 的 PWA 标准，全部要有）

1. **离线**：Service Worker 安装时预缓存整个 App。没有"部分离线"。
2. **第一次打开先选语言**：三个选项各用自己的语言标示，**默认 English**；选过就记住。分享进来的深层链接选完语言后仍然跳到原本的位置。
3. **三语一个按钮**：之后头部按钮循环 中 → EN → BM → 中，原地重绘，保留阅读位置。
4. **浅色 / 深色**：跟随系统 → 浅色 → 深色 → 跟随系统；首帧前套用，不闪白。
5. **阅读模式 AAA**：100% → 115% → 130% → 150%；图表文字一起放大；130% 以上改单栏。
6. **搜索**：三种语言同时搜，包括词典；结果用当前语言显示。
7. **Info 页**："Apps created by Bryan Woo"、资料来源、图标来源、离线状态、版本号。
8. **分享**：二维码（离线生成）、"分享"按钮（`navigator.share`，弹出系统分享到 WhatsApp 等）、"复制链接"。
9. **自动更新**：push 就是发布。不用手改版本号、不用清缓存（§9）。
10. **更新说明弹窗**：更新后弹出"已更新到 vX.Y.Z"＋三语改动说明。每次发布都要写。
11. **Splash screen 与 icon**：用脚本从 `icon.png` 生成全部尺寸（含 maskable、iOS 启动图）。
12. **WhatsApp 预览**：`og:` 标签用绝对网址，配 og-image。
13. **省电**：除了 splash screen，没有自动播放的背景动画。互动图表只在用户操作时动。遵守 `prefers-reduced-motion`。

本 App 额外的学习功能：

14. **学习路线与进度**：9 个阶段，每章可标"已读"，首页显示每阶段进度。
15. **名词弹窗**：正文中的名词可点，弹出一句话定义＋"在第 N 章详细讲"。
16. **"本章新名词"框**：每章开头列 3–6 个本章首次定义的名词。
17. **常见误解框**：`note` 的一种（`kind: "myth"`）。
18. **名词闪卡**：按阶段抽卡，正面名词、背面定义。
19. **自测题**：每阶段一套（8–12 题），答完显示对错和解释，记录最好成绩。
20. **°C ⇄ °F 换算**：两个输入框互相联动。
21. **蒲福风级表**。
22. **互动图表**：27 个（§7）。
23. **基础 / 进阶**：每章默认只显示基础内容；公式和细节放进可展开的"进阶"框。
24. **缩写表**：ECMWF、IFS、ENS、CAPE、LCL、MJO……三语，可搜索。
26. **数据卡片与数据目录**：模型和数据章节附真实数据样本、参数表、直接链接（见大纲"数据卡片"）。外部链接标 ↗，离线时提示需要网络。
25. **名词地图**：互动图显示名词之间的先后关系，点一个名词看要先懂哪些。

---

## 5. 内容大纲

完整大纲见 **[2026-10-02-meteorology-outline.md](2026-10-02-meteorology-outline.md)**：9 个阶段、42 章，每章列出本章新名词、内容、来源和互动图表；包括"午后阵雨"主线（10 章）与"怎样才算下雨"。

大纲是内容的唯一依据；这份 spec 只管功能与架构。

---

## 6. 架构

沿用 OilPalmWiki 已验证的做法：**静态 PWA，无打包工具、无 npm 依赖、无 CDN**。所有文件都从本仓库提供。

```
Meteorology/
├── index.html                 单页，所有视图
├── manifest.webmanifest
├── sw.js                      预缓存全部（由 tools/build-sw.mjs 生成清单与 cache 名）
├── css/app.css                token、主题、字级、版面
├── js/
│   ├── app.js                 启动、hash 路由、视图组装（唯一接线的模块）
│   ├── config.js              APP_URL
│   ├── prefs.js               语言 / 主题 / 字级 / 进度 持久化
│   ├── i18n.js                语言循环、UI 字串、pick({zh,en,ms})
│   ├── content.js             读取章节 JSON、渲染 block
│   ├── terms.js               名词表、弹窗、"本章新名词"
│   ├── charts.js              声明式数据图表（可滑动读值）
│   ├── maps.js                地图底图（世界 / 东南亚 / 可转地球）＋数据图层
│   ├── widgets/               每个互动图表一个模块（W1–W27）
│   ├── physics.js             纯函数：饱和水汽压、露点、湿球、LCL、绝热线、CAPE、日长、ET₀、dBZ↔雨量、单位换算
│   ├── search.js              三语搜索
│   ├── quiz.js                自测题与闪卡
│   ├── share.js               分享面板
│   ├── qrcode.js              离线 QR 编码器（沿用 OilPalmWiki 已验证版本）
│   ├── updatelogic.js         判断是否有新版、何时套用（沿用 CompareCast）
│   └── swpolicy.js            请求的缓存规则（可单元测试）
├── data/
│   ├── index.json             阶段、章节清单、UI 字串
│   ├── ch01.json … ch42.json  三语章节内容
│   ├── terms.json             名词表
│   ├── quiz.json              自测题与闪卡
│   ├── sources.json           来源登记
│   ├── releases.json          三语更新说明
│   ├── series/*.json          互动图表用的真实数据（附来源）
│   └── maps/*.json            简化后的海岸线、国界，以及海温等网格数据（附来源）
├── icons/                     icon、maskable、iOS 启动图、og-image
├── tools/                     见 §11
├── tests/
└── docs/
```

### 6.1 模块边界

- `physics.js` 只放纯函数，不碰 DOM——这是最容易算错、也最好测试的部分。
- `widgets/*` 每个模块输出 `mount(el, opts)`，只依赖 `physics.js`、`i18n.pick` 和 CSS token；不 fetch（数据由 `content.js` 传入）。
- `charts.js` 只做声明式图表，返回 `<svg>`。
- `terms.js` 不知道路由；`content.js` 不知道路由；`app.js` 是唯一把它们接起来的地方。

### 6.2 内容模型

沿用 OilPalmWiki 的 block 格式（`p`、`list`、`keyval`、`table`、`chart`、`figure`、`note`），加上：

- `dataset`：`{ "type": "dataset", "id": "ecmwf-ens" }`，卡片内容存在 `data/datasets.json`
- `widget`：`{ "type": "widget", "id": "W7", "opts": {…} }`
- `note.kind` 增加 `myth`（常见误解）
- 段落里的名词标记：`{{t:dew-point}}`，渲染成可点的名词；`{{t:dew-point|露点温度}}` 可换显示文字
- 来源标记：block 上的 `"src": ["metmalaysia-monsoon", "PAM:8"]`

`terms.json`：

```json
{ "id": "dew-point",
  "name": { "zh": "露点", "en": "Dew point", "ms": "Takat embun" },
  "short": { "zh": "…一句话…", "en": "…", "ms": "…" },
  "chapter": 5,
  "see": ["relative-humidity"] }
```

马来文名词优先用 MetMalaysia 与 DBP 的通行用法。

### 6.3 Linter（`tools/lint-content.mjs`，CI 必过）

1. 每个可见字串都有 `zh` / `en` / `ms`，缺一个就失败。
2. **名词顺序**：第 N 章用到的名词，定义章必须 ≤ N；同一章内，必须在定义段落之后才能用。
3. 每个 `src` 都能在 `sources.json` 找到；阶段 6（马来西亚）每一段都必须有来源。
4. 每个 `widget` id 都有对应模块；每个 `series` 数据文件都有 `source` 字段。
5. 表格行列数一致、图表 series 长度和类别一致、引用的文件存在。
6. 每个章节至少有一题自测题。

---

## 7. 互动图表

用户说要"用手去动它"：所有图表都可以拖、点、滑；读数显示在图表下方固定的读数栏，不用悬浮提示（手指会挡住）。

**两种类型：**

- **数据图表**（`charts.js`）：柱状、折线、表格式图。手指在图上滑动，读数栏显示该点的值。
- **互动模拟**（`widgets/`）：拖动参数，图即时重算。计算全部来自 `physics.js` 的公式，公式来源写在图下方。

27 个互动图表的清单和数据来源见大纲最后的"互动图表总表"；13 个地图图示见大纲的"地图图示"。

**地图：** `maps.js` 提供三种底图——世界（Equal Earth 投影）、东南亚、可以拖动旋转的地球（正射投影）。海岸线和国界来自 Natural Earth（公有领域），由 `tools/build-maps.py` 简化成 SVG 路径，随 App 预缓存，离线可用。数据图层（海温、距平、气候分区）事先缩成小网格存成 JSON，每个文件都有 `source` 和日期；示意图层标示"示意图"。底图和图层颜色都用 CSS token。

所有图表：

- SVG，有 `viewBox`，随视窗和字级缩放；颜色用 CSS token，换主题不用重画。
- 有 `<title>` / `<desc>`，并附隐藏的数据表，方便读屏软件。
- 手机上用 Pointer Events，支持拖动和点击；键盘可用方向键调整。
- 每个图下方注明数据或公式来源；示意图标示"示意图"。

---

## 8. 版面与互动

- **首页**：App 名称、9 个阶段卡片（显示进度）、"继续上次阅读"。
- **阶段页**：该阶段的章节列表＋自测入口。
- **章节页**：本章新名词框 → 正文 → 本章来源 → 上一章 / 下一章 / 标记已读。
- **头部按钮**：语言、主题、AAA、搜索、更多（工具、Info、分享）。
- **名词弹窗**：底部抽屉，点外面或下滑关闭；"详细讲"跳到定义章节。
- 手机宽度优先设计（375 px），平板以上目录固定在左侧。

---

## 9. 离线与更新

结合两套已在用的做法：

1. **CI 生成预缓存清单**（沿用 OilPalmWiki）：`tools/build-sw.mjs` 列出所有要缓存的文件，cache 名取所有文件内容的 hash。任何文件改了，cache 名就会变。
2. **页面检查新版**（沿用 CompareCast 的 `updatelogic.js`）：打开时、回到前台时、使用中每 15 分钟，用 HEAD 请求比对 `index.html` 的 `Last-Modified`。
   - 刚打开 → 直接更新；
   - 正在阅读 → 底部出现提示条，用户自己按；
   - 在后台 → 等回到前台再处理；
   - 同一版本 10 分钟内只自动重载一次，避免循环。
3. **更新说明弹窗**：`data/releases.json` 存每一版的三语说明；更新后显示上次看过的版本之后的所有说明（最多 4 条）。
4. 预计全部预缓存约 2–3 MB（42 章 JSON + SVG + icon），首次打开在 Wi-Fi 下几秒内完成。Info 页显示"已可离线使用"或"尚未完成"。

---

## 10. Icon 与 splash

`tools/make-icons.py` 从 `icon.png` 生成：192 / 512、maskable 192 / 512、apple-touch-icon、favicon、iOS 启动图各尺寸、og-image（1200×630 与 方形）。

`icon.png` 只有 512×512，作为 splash 与 og-image 足够，但不放大超过原尺寸使用。

---

## 11. 工具与测试

| 命令 | 作用 |
|---|---|
| `python3 tools/serve.py` | 本地开发服务器（no-store、HTTP/1.1、正确 MIME） |
| `node tools/lint-content.mjs` | §6.3 全部检查 |
| `node tools/build-sw.mjs` | 生成预缓存清单与 cache 名 |
| `node --test tests/*.test.js` | `physics.js`、`updatelogic.js`、`swpolicy.js`、`i18n.js` 单元测试，以及 sw 行为测试 |
| `venv/bin/python tools/build-maps.py` | 从 Natural Earth 生成简化底图；把海温等数据缩成小网格写进 `data/maps/` |
| `node tools/fetch-series.mjs` | 从 Open-Meteo Archive、NOAA CPC 抓图表用的真实数据，写进 `data/series/`，含来源与抓取日期 |
| `node tools/check-links.mjs` | 检查所有外部链接是否仍然有效（每周由 CI 排程执行，失效只提醒、不阻挡发布） |
| `venv/bin/python tools/verify-qr.py` | 用 zxing-cpp 解码 App 生成的二维码，确认等于 `APP_URL` |
| `tests/index.html` | 浏览器测试页：语言选择、路由、名词弹窗、图表挂载、搜索、自测 |

**物理公式要对照已知值测试**，例如：

- 20 °C、相对湿度 50% 的露点约 9.3 °C；
- 标准大气 500 hPa 约 5.6 km；
- FAO-56 书中的 ET₀ 算例；
- Stull 湿球公式的原文示例（20 °C、50% → 约 13.7 °C）。

**手机宽度实测**：每完成一个阶段，在浏览器 375 px 宽度下检查版面和每个互动图表的拖动。

`.github/workflows/deploy.yml`：lint → 生成 sw → 跑测试 → 只发布 App 需要的文件（不发布 tools、docs、References）。

---

## 12. 开发顺序

1. 资产：生成 icon、splash、og-image，取色定 token。
2. 框架：路由、语言选择、语言循环、主题、AAA、Info、分享、更新机制、离线——用第 5 章（湿度）一章真实内容跑通，在手机宽度下检查。
3. `physics.js` + 测试，再做 W5 作为第一个互动图表，确定 widget 模式。
4. 名词系统与 linter（名词顺序检查）。
5. 按阶段 1 → 9 写内容，每阶段同时完成该阶段的互动图表、名词、自测题，并核对来源。
6. 搜索、闪卡、词典、°C ⇄ °F、蒲福风级。
7. 全部完成后：全站复查（三语、来源、离线、更新、二维码），部署到 GitHub Pages，在真机上确认。

---

## 13. 不做的事

- 实时天气预报、地图、推送通知（那是 CompareCast 的工作）。
- 用户账号、云端同步。
- 复制任何参考书的文字、图片或题目。
- 背景动画（splash 除外）。
- *Understanding Meteorology*（扫描版）的 OCR。

---

## 14. 待确认

（无。repo 名默认 `Meteorology`，要改只需改 `js/config.js` 的 `APP_URL` 并重新生成 `qr.svg`。）
