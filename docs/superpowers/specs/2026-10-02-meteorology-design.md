# 气象学 · Meteorology — 设计 Spec

**日期：** 2026-10-02
**作者：** Bryan Woo
**状态：** 待审阅

---

## 1. 目的

给气象学小白的一本**离线、三语、可以动手玩的气象学入门**。从"大气是什么"一路学到"ECMWF 的 51 个集合成员在算什么"、"Windy 每个图层是什么意思"，并且用马来西亚的天气做例子。

**给谁用：** 对天气有兴趣、但没有气象背景的人——园区管理人员、农业从业者、学生、家人朋友。主要在马来西亚，语言是中文、英文、马来文混用。

**成功的样子：**

1. 一个完全不懂气象的人，按顺序读完 10 个阶段以后，打开 Windy，每个图层都知道是什么、在 App 第几章学过。
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

14. **学习路线与进度**：10 个阶段，每章可标"已读"，首页显示每阶段进度。
15. **名词弹窗**：正文中的名词可点，弹出一句话定义＋"在第 N 章详细讲"。
16. **"本章新名词"框**：每章开头列 3–6 个本章首次定义的名词。
17. **常见误解框**：`note` 的一种（`kind: "myth"`）。
18. **名词闪卡**：按阶段抽卡，正面名词、背面定义。
19. **自测题**：每阶段一套（8–12 题），答完显示对错和解释，记录最好成绩。
20. **°C ⇄ °F 换算**：两个输入框互相联动。
21. **蒲福风级表**。
22. **互动图表**：24 个（§7）。

---

## 5. 内容大纲：10 个阶段、36 章

排序原则：**每一章只用前面已定义的名词**（由 linter 强制，§6.3）。

| # | 阶段 | 章 | 重点 | 主要来源 | 互动 |
|---|---|---|---|---|---|
| 1 | 1 认识大气 | 气象学是什么 | 天气与气候、气象要素、农业气象学、气象机构（WMO、MetMalaysia、JMA、ECMWF、NOAA、ASMC） | PAM 1–2, ESS 1 | |
| 2 | | 大气层 | 成分、分层、臭氧层与 UV 指数 | PAM 1, ESS 1, ESS 14 | W1 |
| 3 | 2 能量与温度 | 太阳辐射与能量平衡 | 辐射定律、直接/散射辐射、能量平衡、温室效应、四季 | PAM 3, ESS 2 | W2, W3 |
| 4 | | 气温 | 影响因素、日变化与年变化、"2 米气温" | PAM 4, ESS 3 | W4 |
| 5 | 3 水在大气中 | 湿度 | 相对湿度、露点、湿球温度、热压力 | PAM 6, ESS 4 | W5 |
| 6 | | 凝结、雾与云 | 低/中/高云、WMO 云分类、云底、云顶、能见度 | PAM 6, ESS 4 | W6 |
| 7 | | 大气稳定度与降水 | 直减率、热泡、CAPE 概念、冻结高度、降水类型、水循环（预告 Skew-T） | PAM 7, ESS 5 | W7 |
| 8 | | 天空的颜色 | 蓝天、晚霞、彩虹、日晕 | ESS 15 | |
| 9 | 4 空气怎样流动 | 气压与风 | 气压梯度力、科里奥利力、高低压、平均风与阵风、蒲福风级、海陆风、山谷风 | PAM 5, ESS 6–7 | W8 |
| 10 | | 高空大气 | 气压层：850 / 700 / 500 / 250 hPa 各看什么；急流；晴空湍流 | ESS 6–7, FUN 1 | W9 |
| 11 | | 全球环流 | Hadley / Ferrel / 极地环流圈、信风、ITCZ、Walker 环流 | PAM 5, ESS 7, FUN 6 | W10 |
| 12 | | 气团、锋面与风暴 | 气团、锋面、雷暴、雷电安全、热带气旋（为何赤道附近少台风） | ESS 8, 10, 11；雷电：官方 | |
| 13 | 5 海洋与气候 | 海洋与天气 | 海温、洋流、风浪与涌浪、潮汐与潮流、风暴潮 | ESS 7, 11；Windy；MetMalaysia | W11 |
| 14 | | MJO、ENSO 与 IOD | 厄尔尼诺 / 拉尼娜、ONI 指数、MJO、IOD、遥相关、对马来西亚雨量的影响 | ESS 7, FUN 6；NOAA CPC；MetMalaysia | W12 |
| 15 | | 气候与气候变化 | Köppen 分类、气候平均值与距平、全球变暖、对农业的影响 | PAM 14, ESS 12–13 | |
| 16 | 6 马来西亚的天气 | 马来西亚的季风 | 西南季风、东北季风、季风转换期、寒潮（cold surge）、东海岸雨季 | MetMalaysia | W13 |
| 17 | | 每天的天气规律 | **午后阵雨的完整解释**（总结 §5.1 主线）、季风转换期西海岸午后雷雨最多、苏门答腊飑线（凌晨到早上）、海陆风 | MetMalaysia RP04/2025 等 | W24 |
| 18 | | 天气预警 | 连续降雨 Waspada / Buruk / Bahaya、强风大浪、雷暴预警、CAP 格式；看到预警园里要做什么 | MetMalaysia | |
| 19 | | 洪水与干旱 | 季风水灾、闪电水灾、干旱类型、干旱期农业措施 | PAM 9；MetMalaysia | |
| 20 | | 霾与空气质量 | API 等级、ASMC 火点、泥炭地火、厄尔尼诺 + 西南季风；CO、粉尘、SO₂ | ESS 14；DOE；ASMC | W14 |
| 21 | 7 观测 | 地面观测站与仪器 | 观测站等级、选址与布置；温度计、干湿球、雨量筒、蒸发皿、风速风向仪、气压计、日照计、自动气象站 | PAM 15–23 | |
| 22 | | 高空与海洋观测 | 探空气球、AMDAR 飞机资料、浮标与 Argo | ESS 1, 9；FUN 3 | |
| 23 | | 卫星 | 同步与极轨轨道；卫星全家福（Himawari-9、FY-4、GK-2A、INSAT、Meteosat、GOES、NOAA-20/21、MetOp、Terra/Aqua、GPM、Sentinel-1/2）；可见光、红外线、水汽图 | ESS 9；JMA 等官方 | W15, W16 |
| 24 | | 雷达与闪电定位 | 雷达原理、dBZ、多普勒、双偏振、太空雷达 GPM、SAR；闪电定位网（含 Blitzortung）；MetMalaysia 雷达网 | ESS 5, 10；MetMalaysia | W17 |
| 25 | | Skew-T 探空图 | 怎样读：气温线、露点线、LCL、CAPE、逆温层 | TERM；NOAA NWS | W18 |
| 26 | 8 预报与模型 | 天气图 | 站点模型、天气符号、等压线、等高线、流线 | PAM 24, ESS 附录 C, FUN 4 | W19 |
| 27 | | 数值天气预报怎样运作 | 网格与分辨率、数据同化（含卫星资料）、参数化、时间步长、全球模型与区域模型 | FUN 5, ESS 9 | W20 |
| 28 | | 混沌与集合预报 | 蝴蝶效应、control / perturbed 成员、集合平均、离散度、概率 | ESS 9, FUN 5；ECMWF | W21 |
| 29 | | 主要模型 | ECMWF IFS（HRES、ENS 51 成员、9 km）、AIFS；GFS、GEFS（31 成员、约 25 km）；ICON、UKMO、GEM；对照表 | ECMWF、NOAA EMC、DWD、Met Office、ECCC 官方 | |
| 30 | | 再分析与季节预报 | ERA5 是什么、ENSO 展望怎样看、延伸期预报 | ECMWF、NOAA CPC | |
| 31 | | 看懂天气 App | 降雨概率、UTC 与马来西亚时间（00/06/12/18 UTC = 8am/2pm/8pm/2am MYT）、meteogram、airgram、为什么不同 App 不一样、预报准确度随天数下降 → 链接 CompareCast | ESS 9；Windy；ECMWF | W22 |
| 32 | | Windy 图层导读 | 每个 Windy 图层：是什么、在第几章学、点击跳回 | Windy 官方 | |
| 33 | 9 用在农业上 | 天气与作物 | 天气对生长、发育、产量的影响；农业气象服务 | PAM 2, 10 | |
| 34 | | 蒸散与作物需水 | 蒸发与蒸散、ET₀（Penman-Monteith）、土壤湿度、水分距平 | PAM 18；FAO-56 | W23 |
| 35 | | 微气象与小气候 | 小气候、遮荫、防风林、覆盖物、人工改善小气候 | PAM 11 | |
| 36 | | 遥感与作物模型 | 遥感原理、植被指数 NDVI（链接 NDVI App）、作物模型 | PAM 12–13 | |

### 5.1 主线案例：午后阵雨

马来西亚最常见的天气是"早上晴、下午雷阵雨"。把它当成一条贯穿全书的主线：每学到一个新概念，就回头解释午后阵雨多一层。读者会在 10 个章节里反复遇到它，最后在第 17 章拼成完整的答案。

| 章 | 学到的概念 | 对午后阵雨的解释 |
|---|---|---|
| 4 气温 | 气温日变化 | 太阳把地面越晒越热，最高温出现在午后，不在正午 |
| 5 湿度 | 露点、水汽 | 马来西亚空气很湿，早上的露点就很高，"燃料"充足 |
| 7 稳定度与降水 | 热泡、对流、CAPE | 地面热空气像热气球一样往上冲，到 LCL 开始成云，CAPE 越大冲得越高 |
| 9 气压与风 | 海风 | 下午海风吹进内陆，和对面来的海风或山风相撞，空气被迫上升 |
| 12 雷暴 | 雷暴生命史 | 积云 → 积雨云 → 下雨打雷 → 消散，通常一两个小时 |
| **17 每天的天气规律** | **总结** | 全部拼起来；为什么季风转换期（4–5 月、10–11 月）西海岸午后雷雨最多 |
| 23 卫星 | 红外线图像 | 中午后云顶迅速变冷变高，在 Himawari 图上看得到云"长出来" |
| 24 雷达 | dBZ | 雷达图上下午突然冒出一块块黄红色 |
| 25 Skew-T | 早上的探空 | 早上看探空图就能判断下午会不会有雷雨 |
| 31 看懂天气 App | 降雨概率 | 为什么 App 常显示"下午 60% 下雨"，但雨只下在城市的一部分 |

**W24（第 17 章）"午后阵雨的一天"**：拖动时间轴 6am → 8pm，同一张剖面图依次显示：太阳加热地面 → 热泡上升 → 海风吹入 → 积云长高 → 积雨云下雨 → 傍晚消散。剖面图是示意图；图下方附一条吉隆坡"每小时平均雨量"的真实曲线，数据来源优先找 MetMalaysia 或卫星降雨资料（GPM IMERG）。找不到可靠的逐时数据就只放示意图，不放数字。

### 5.2 "怎样才算下雨"

读者常问的问题，分散放在四个地方：

| 章 | 内容 |
|---|---|
| 6 凝结与云 | 常见误解框：乌云不是水汽（水汽看不见），而是小水滴和冰晶；云滴太小掉不下来，要长大约百万倍体积才成雨滴；雨在半空蒸发掉叫"雨幡"（virga） |
| 7 降水 | 微量（trace）与"可测量降水" |
| 15 气候 | 对照表："雨日"的门槛因机构和用途不同：0.2 mm（*Terminology* 所载国际惯例）、1 mm（WMO 气候平均值 / ETCCDI 湿日）、2.5 mm（印度气象局 IMD 的 rainy day）；MetMalaysia 的降雨强度分级（核对原始出处后才写） |
| 31 看懂天气 App | 降雨概率的定义（以美国 NWS 为例：某一点在时段内出现 ≥ 0.25 mm 的概率，ESS 表 9.1）；模型网格平均的意思；不同 App 自定"显示下雨图标"的门槛 |

**工具页**（不算章）：名词词典、名词闪卡、自测题、°C ⇄ °F、蒲福风级、资料来源、分享。

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
│   ├── widgets/               每个互动图表一个模块（W1–W23）
│   ├── physics.js             纯函数：饱和水汽压、露点、湿球、LCL、绝热线、CAPE、日长、ET₀、dBZ↔雨量、单位换算
│   ├── search.js              三语搜索
│   ├── quiz.js                自测题与闪卡
│   ├── share.js               分享面板
│   ├── qrcode.js              离线 QR 编码器（沿用 OilPalmWiki 已验证版本）
│   ├── updatelogic.js         判断是否有新版、何时套用（沿用 CompareCast）
│   └── swpolicy.js            请求的缓存规则（可单元测试）
├── data/
│   ├── index.json             阶段、章节清单、UI 字串
│   ├── ch01.json … ch36.json  三语章节内容
│   ├── terms.json             名词表
│   ├── quiz.json              自测题与闪卡
│   ├── sources.json           来源登记
│   ├── releases.json          三语更新说明
│   └── series/*.json          互动图表用的真实数据（附来源）
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

| ID | 章 | 互动 | 数据或公式来源 |
|---|---|---|---|
| W1 | 2 | 拖动高度 → 气温、气压、所在层 | 标准大气（ESS 附录 E） |
| W2 | 3 | 选纬度和日期 → 日长、正午太阳高度 | 太阳赤纬与日长公式 |
| W3 | 3 | 点能量平衡图上的箭头 → 各项百分比 | ESS 2 |
| W4 | 4 | 吉隆坡某晴天与某阴天的逐时气温，滑动读值 | ERA5（Open-Meteo Archive） |
| W5 | 5 | 拖动气温和湿度 → 饱和水汽量、露点、湿球温度、热压力等级 | Magnus 公式、Stull (2011) 湿球公式 |
| W6 | 6 | 点云图 → 云名、高度、会不会下雨 | WMO 云分类 |
| W7 | 7 | 气块上升：拖动起始温度和露点 → 干绝热上升、到 LCL 后湿绝热 | 干绝热 9.8 °C/km、湿绝热数值积分 |
| W8 | 9 | 拖动气压差和纬度 → 风速与偏转方向 | 地转风关系 |
| W9 | 10 | 点 850 / 700 / 500 / 250 hPa → 大约高度、该层看什么 | 标准大气 + ESS 6 |
| W10 | 11 | 拖动月份 → ITCZ 大致位置（示意图） | ESS 7 |
| W11 | 13 | 拖动月相 → 大潮与小潮 | 潮汐原理 |
| W12 | 14 | 切换厄尔尼诺 / 正常 / 拉尼娜 → Walker 环流示意；下方 ONI 历史曲线可滑动读值 | 示意 + NOAA CPC ONI 真实数据 |
| W13 | 16 | 拖动月份 → 盛行风向与各区月雨量 | MetMalaysia；若找不到公开逐月数据，用 ERA5 气候平均并标明 |
| W14 | 20 | 点 API 等级 → 健康建议 | DOE |
| W15 | 23 | 点地球上一个经度 → 哪几颗同步卫星看得到 | 各卫星运营机构公布的定点经度 |
| W16 | 23 | 同一片云切换可见光 / 红外线 / 水汽（示意图） | ESS 9 |
| W17 | 24 | 点 dBZ 色阶 → 约多少 mm/h | Marshall-Palmer 关系 Z = 200R^1.6 |
| W18 | 25 | 拖动气温线与露点线 → LCL、CAPE、会不会有雷雨 | 同 W7 的公式 |
| W19 | 26 | 点站点模型上的符号 → 意思 | ESS 附录 C |
| W20 | 27 | 切换网格 9 / 25 / 100 km → 雷雨云和地形能"看到"多少（示意图） | 示意 |
| W21 | 28 | 51 条集合成员线，拖动预报天数看越来越分散 | Lorenz-63 模型现场计算，**明确标示是演示，不是真实预报** |
| W22 | 31 | 读一张 meteogram：滑动读逐时温度、雨量、风 | ERA5（Open-Meteo Archive）某一真实日期 |
| W23 | 34 | 拖动气温、湿度、风速、日照 → ET₀（mm/天） | FAO-56 Penman-Monteith |
| W24 | 17 | 午后阵雨的一天：拖动时间轴 6am → 8pm，看加热、热泡、海风、积云、下雨、消散（§5.1） | 示意图 + 吉隆坡逐时平均雨量（MetMalaysia 或 GPM IMERG；找不到就不放数字） |

所有图表：

- SVG，有 `viewBox`，随视窗和字级缩放；颜色用 CSS token，换主题不用重画。
- 有 `<title>` / `<desc>`，并附隐藏的数据表，方便读屏软件。
- 手机上用 Pointer Events，支持拖动和点击；键盘可用方向键调整。
- 每个图下方注明数据或公式来源；示意图标示"示意图"。

---

## 8. 版面与互动

- **首页**：App 名称、10 个阶段卡片（显示进度）、"继续上次阅读"。
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
4. 预计全部预缓存约 2–3 MB（36 章 JSON + SVG + icon），首次打开在 Wi-Fi 下几秒内完成。Info 页显示"已可离线使用"或"尚未完成"。

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
| `node tools/fetch-series.mjs` | 从 Open-Meteo Archive、NOAA CPC 抓图表用的真实数据，写进 `data/series/`，含来源与抓取日期 |
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
5. 按阶段 1 → 10 写内容，每阶段同时完成该阶段的互动图表、名词、自测题，并核对来源。
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

1. GitHub repo 名用 `Meteorology` 可以吗？（决定网址和二维码）
