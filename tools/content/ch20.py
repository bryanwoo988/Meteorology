"""Chapter 20 — Haze and air quality."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch20", "num": 20, "stage": 6,
 "title": T("烟霾与空气质量", "Haze and air quality", "Jerebu dan kualiti udara"),
 "sources": ["ESS", "TERM", "ASMC", "ASMC-HOME", "ASMC-HOTSPOT", "DOE-API", "MET-ENSO-STATUS", "NEWS-VIBES-2026", "NEWS-FMT-2026"],
 "sections": [
 {"id": "s1", "heading": T("跨境烟霾", "Transboundary haze", "Jerebu rentas sempadan"), "level": "basic", "blocks": [
  P("第 6 章讲过：空气里有很多微粒时，远处的东西会变得模糊，这就是霾。在东南亚，最严重的霾常常来自森林和泥炭地着火冒出的烟。烟被风从一个国家吹到另一个国家，叫{{t:transboundary-haze}}。",
    "Chapter 6 described haze: when the air is full of tiny particles, distant things blur. In South-East Asia the worst haze usually comes from the smoke of forest and peatland fires. When the wind carries that smoke from one country into another, it is {{t:transboundary-haze}}.",
    "Bab 6 menerangkan jerebu: apabila udara penuh dengan zarah halus, benda yang jauh menjadi kabur. Di Asia Tenggara jerebu paling teruk biasanya datang daripada asap kebakaran hutan dan tanah gambut. Apabila angin membawa asap itu dari satu negara ke negara lain, ia ialah {{t:transboundary-haze}}.",
    defines=["transboundary-haze"], src=["ESS:97", "ASMC", "NEWS-VIBES-2026"]),
  P("{{t:peat}}是大部分没有分解、或只分解了一点的植物残体，在长期积水的地方堆积而成的土壤。大马气象局提醒：长期干旱会增加森林和泥炭地火灾，引起烟霾。",
    "{{t:peat}} is soil made mostly of plant remains that have not decomposed, or only slightly, built up where the ground stays waterlogged. MetMalaysia warns that long dry spells raise the risk of forest and peatland fires and of the haze they bring.",
    "{{t:peat}} ialah tanah yang kebanyakannya terdiri daripada sisa tumbuhan yang tidak reput, atau hanya sedikit reput, terkumpul di tempat yang sentiasa bertakung air. MetMalaysia mengingatkan bahawa tempoh kering yang panjang meningkatkan risiko kebakaran hutan dan tanah gambut serta jerebu yang dibawanya.",
    defines=["peat"], src=["TERM:255", "NEWS-VIBES-2026"]),
  {"type": "map", "id": "M12", "src": ["ASMC-HOME"]},
  P("西南季风期间，低空的风主要从东南或西南吹来，这正是东盟南部的旱季。2026 年 10 月 2 日查阅的 ASMC 区域烟霾情况说：苏门答腊南部和加里曼丹东南部有成群的火点，砂拉越部分地区出现跨境的中到浓烟霾。",
    "During the south-west monsoon the low-level winds blow mainly from the south-east or south-west, and it is the dry season of the southern ASEAN region. ASMC's regional haze situation, as read on 2 October 2026, noted clusters of hotspots in southern Sumatra and south-eastern Kalimantan, and moderate to dense transboundary smoke haze over parts of Sarawak.",
    "Semasa monsun barat daya angin aras rendah bertiup terutamanya dari tenggara atau barat daya, dan ia musim kering rantau ASEAN selatan. Situasi jerebu serantau ASMC, seperti dibaca pada 2 Oktober 2026, mencatat kelompok titik panas di selatan Sumatera dan tenggara Kalimantan, serta jerebu asap rentas sempadan sederhana hingga tebal di sebahagian Sarawak.",
    src=["ASMC-HOME"]),
 ]},
 {"id": "s2", "heading": T("为什么厄尔尼诺年霾特别严重", "Why El Niño years bring worse haze", "Mengapa tahun El Niño membawa jerebu lebih teruk"), "level": "basic", "blocks": [
  P("第 14 章讲过，厄尔尼诺让东南亚偏干。大马气象局 2026 年 9 月的 ENSO 状态说：非常强的厄尔尼诺常常和严重的烟霾一起出现，“就像我们现在正在经历的”；这次烟霾预计会持续到 2026 年 10 月。",
    "Chapter 14 showed that El Niño tends to dry South-East Asia. MetMalaysia's ENSO status of September 2026 says a very strong El Niño is often linked with serious haze, ‘as we are experiencing now’, and expected the haze to last until October 2026.",
    "Bab 14 menunjukkan El Niño cenderung mengeringkan Asia Tenggara. Status ENSO MetMalaysia pada September 2026 menyatakan El Niño yang sangat kuat sering dikaitkan dengan cuaca berjerebu yang serius ‘sebagaimana yang sedang kita alami ketika ini’, dan menjangkakan jerebu berterusan sehingga Oktober 2026.",
    src=["MET-ENSO-STATUS"]),
  N("key", "厄尔尼诺 + 西南季风的旱季 = 泥炭地更干、更容易着火，而风又正好把烟吹向马来西亚。",
    "El Niño plus the south-west monsoon's dry season means drier peat that burns more easily — and winds that carry the smoke towards Malaysia.",
    "El Niño ditambah musim kering monsun barat daya bermakna gambut lebih kering dan mudah terbakar — serta angin yang membawa asap ke arah Malaysia.",
    src=["MET-ENSO-STATUS", "ASMC-HOME", "NEWS-VIBES-2026"]),
 ]},
 {"id": "s3", "heading": T("卫星怎样找火点", "How satellites find fires", "Bagaimana satelit mencari kebakaran"), "level": "basic", "blocks": [
  P("着火的地面会放出特别强的中红外辐射。卫星的火点算法把每个像元和一组门槛、以及周围的像元比较，判断是不是着火；被判定为着火的像元，就是一个{{t:hotspot}}。ASMC 2019 年起用 NOAA-20 卫星的资料数火点。",
    "Burning ground gives off unusually strong mid-infrared radiation. A satellite fire algorithm compares each pixel with a set of thresholds and with the pixels around it to decide whether it is on fire; a pixel flagged as fire is a {{t:hotspot}}. Since 2019 ASMC has counted hotspots from the NOAA-20 satellite.",
    "Tanah yang terbakar memancarkan sinaran inframerah tengah yang luar biasa kuat. Algoritma kebakaran satelit membandingkan setiap piksel dengan set ambang dan dengan piksel di sekelilingnya untuk menentukan sama ada ia terbakar; piksel yang ditandakan sebagai kebakaran ialah {{t:hotspot}}. Sejak 2019 ASMC mengira titik panas daripada satelit NOAA-20.",
    defines=["hotspot"], src=["ASMC-HOTSPOT"]),
  {"type": "chart", "src": ["ASMC-HOTSPOT"], "chart": {"kind": "line", "series_file": "asmc-hotspots-2026",
    "title": T("每天的火点数，2026 年 7–9 月", "Hotspots a day, July–September 2026", "Titik panas sehari, Julai–September 2026"),
    "x": {"col": "date", "label": T("日期", "Date", "Tarikh"), "format": "date"},
    "y": {"label": T("火点", "Hotspots", "Titik panas"), "unit": ""},
    "series": [{"col": "kalimantan", "name": T("加里曼丹", "Kalimantan", "Kalimantan"), "color": "mercury"},
               {"col": "sumatra", "name": T("苏门答腊", "Sumatra", "Sumatera"), "color": "sun"},
               {"col": "malaysia", "name": T("马来西亚", "Malaysia", "Malaysia"), "color": "sky"}]}},
  P("这三个月里，加里曼丹每天的火点最多在 8 月 28 日达到 1,734 个，苏门答腊在 9 月 16 日达到 387 个；马来西亚（半岛加沙巴、砂拉越）三个月加起来只有 419 个。马来西亚的霾，大部分是从外面吹进来的。",
    "Over these three months Kalimantan's daily count peaked at 1,734 on 28 August and Sumatra's at 387 on 16 September; Malaysia — the Peninsula plus Sabah and Sarawak — had only 419 in all three months together. Most of Malaysia's haze is blown in from outside.",
    "Dalam tiga bulan ini kiraan harian Kalimantan memuncak pada 1,734 pada 28 Ogos dan Sumatera pada 387 pada 16 September; Malaysia — Semenanjung serta Sabah dan Sarawak — hanya mempunyai 419 bagi ketiga-tiga bulan bersama. Kebanyakan jerebu Malaysia ditiup masuk dari luar.",
    src=["ASMC-HOTSPOT"]),
  N("warn", "火点不一定是真的火：天然气燃烧塔、发电厂也会被当成火点。反过来，云太多、火在树冠下面、火太小或太短，卫星都可能看不到。所以多云的日子，火点少不代表火少。",
    "A hotspot is not always a fire: gas flares and power plants can show up too. And the satellite can miss fires under cloud, under the forest canopy, or ones that are too small or too brief. On a cloudy day, few hotspots do not mean few fires.",
    "Titik panas tidak semestinya kebakaran: suar gas dan loji janakuasa juga boleh muncul. Dan satelit boleh terlepas kebakaran di bawah awan, di bawah kanopi hutan, atau yang terlalu kecil atau singkat. Pada hari berawan, sedikit titik panas tidak bermakna sedikit kebakaran.",
    src=["ASMC-HOTSPOT"]),
  {"type": "dataset", "id": "asmc-hotspots", "src": ["ASMC-HOTSPOT"]},
 ]},
 {"id": "s4", "heading": T("空气污染指数（API）", "The Air Pollutant Index (API)", "Indeks Pencemar Udara (IPU)"), "level": "basic", "blocks": [
  P("马来西亚环境局（DOE）用{{t:api}}报告空气质量。它由六种污染物算出：二氧化硫、二氧化氮、一氧化碳、地面臭氧、PM10 和 {{t:pm25}}。每种污染物先按自己的时间平均（例如 PM2.5 和 PM10 用 24 小时平均），换算成一个分指数；六个分指数里最高的那个，就是 API。",
    "Malaysia's Department of Environment (DOE) reports air quality as the {{t:api}}. It is worked out from six pollutants: sulphur dioxide, nitrogen dioxide, carbon monoxide, ground-level ozone, PM10 and {{t:pm25}}. Each pollutant is averaged over its own period (24 hours for PM2.5 and PM10, for example) and turned into a sub-index; the highest of the six sub-indices is the API.",
    "Jabatan Alam Sekitar (JAS) melaporkan kualiti udara sebagai {{t:api}}. Ia dikira daripada enam bahan pencemar: sulfur dioksida, nitrogen dioksida, karbon monoksida, ozon aras tanah, PM10 dan {{t:pm25}}. Setiap pencemar dipuratakan mengikut tempohnya sendiri (24 jam bagi PM2.5 dan PM10, contohnya) dan ditukar kepada sub-indeks; sub-indeks tertinggi daripada enam itu ialah IPU.",
    defines=["api", "pm25"], src=["DOE-API"]),
  N("key", "平常和有霾的时候，决定 API 读数的通常是微粒（PM2.5、PM10），因为它们是最主要的污染物。PM2.5 从 2017 年起算进 API。",
    "Most of the time, and especially in haze, the API reading is set by particulate matter (PM2.5 and PM10), the dominant pollutant. PM2.5 has been part of the API since 2017.",
    "Kebanyakan masa, terutamanya semasa jerebu, bacaan IPU ditentukan oleh habuk halus (PM2.5 dan PM10), pencemar yang dominan. PM2.5 menjadi sebahagian daripada IPU sejak 2017.",
    src=["DOE-API"]),
  {"type": "widget", "id": "W14", "src": ["DOE-API"]},
  P("2026 年 10 月 2 日下午 3 点 20 分，全国已经没有“不健康”的读数：哥打京那巴鲁 34、林梦 38 属于“良好”，其他地方都是“中等”，例如蕉赖（Cheras）96。",
    "At 3.20 pm on 2 October 2026 no area in the country was ‘unhealthy’: Kota Kinabalu (34) and Limbang (38) were ‘good’ and the rest ‘moderate’, such as Cheras at 96.",
    "Pada jam 3.20 petang 2 Oktober 2026 tiada kawasan di negara ini yang ‘tidak sihat’: Kota Kinabalu (34) dan Limbang (38) ‘baik’ dan selebihnya ‘sederhana’, seperti Cheras pada 96.",
    src=["NEWS-FMT-2026"]),
  {"type": "dataset", "id": "doe-apims", "src": ["DOE-API"]},
 ]},
 ]}

terms = [
 ("transboundary-haze", T("跨境烟霾", "Transboundary haze", "Jerebu rentas sempadan"), T("森林和泥炭地火灾的烟被风从一个国家吹到另一个国家。", "Smoke from forest and peatland fires carried by the wind from one country into another.", "Asap kebakaran hutan dan tanah gambut dibawa angin dari satu negara ke negara lain.")),
 ("peat", T("泥炭（泥炭地）", "Peat", "Gambut"), T("大部分没分解的植物残体在积水处堆成的土壤；干了很容易着火、冒烟。", "Soil of barely decomposed plant remains built up in waterlogged ground.", "Tanah daripada sisa tumbuhan yang hampir tidak reput, terkumpul di tanah bertakung air.")),
 ("hotspot", T("火点", "Hotspot", "Titik panas"), T("卫星判定可能在着火的像元。", "A satellite pixel flagged as a possible fire.", "Piksel satelit yang ditandakan sebagai kemungkinan kebakaran.")),
 ("api", T("空气污染指数（API）", "Air Pollutant Index (API)", "Indeks Pencemar Udara (IPU)"), T("六种污染物分指数里最高的一个；0–50 良好，101–200 不健康，300 以上危险。", "The highest of six pollutant sub-indices; 0–50 good, 101–200 unhealthy, above 300 hazardous.", "Sub-indeks tertinggi daripada enam pencemar; 0–50 baik, 101–200 tidak sihat, melebihi 300 berbahaya.")),
 ("pm25", T("PM2.5", "PM2.5", "PM2.5"), T("直径小于 2.5 微米的细微粒，霾的主要成分之一。", "Fine particles smaller than 2.5 micrometres across.", "Zarah halus bersaiz kurang daripada 2.5 mikrometer.")),
]

sources = [
 {"id": "ASMC-HOTSPOT", "short": "ASMC", "title": "Daily hotspot count and FAQ (fire detection algorithm)", "publisher": "ASEAN Specialised Meteorological Centre", "url": "https://asmc.asean.org/asmc-haze-hotspot-daily-new/", "accessed": "2026-10-02"},
 {"id": "DOE-API", "short": "DOE", "title": "Pengiraan Indeks Pencemar Udara (IPU) / Air Pollutant Index (API) calculation", "publisher": "Jabatan Alam Sekitar Malaysia", "url": "https://www.doe.gov.my/wp-content/uploads/2021/09/API_Calculation.pdf", "accessed": "2026-10-02"},
 {"id": "NEWS-VIBES-2026", "short": "The Vibes", "title": "El Nino to bring drier weather, higher temperatures and greater haze risk in Malaysia (quoting MetMalaysia's director-general), 30 September 2026", "publisher": "The Vibes", "url": "https://www.thevibes.com/index.php/articles/news/127819/el-nino-to-bring-drier-weather-higher-temperatures-and-greater-haze-risk-in-malaysia", "accessed": "2026-10-02"},
 {"id": "NEWS-FMT-2026", "short": "FMT", "title": "Haze clears further, no unhealthy API readings, 2 October 2026", "publisher": "Free Malaysia Today", "url": "https://www.freemalaysiatoday.com/category/nation/2026/10/02/haze-clears-further-no-unhealthy-api-readings", "accessed": "2026-10-02"},
]

datasets = [
 {"id": "asmc-hotspots", "name": "ASMC daily hotspot count", "provider": "ASEAN Specialised Meteorological Centre",
  "what": T("每天每个地区的火点数，可选白天或夜间、高中低可信度；本章的火点图就是用它画的。", "Daily hotspot counts by region, by day or night and by confidence level. This chapter's hotspot chart is drawn from it.", "Kiraan titik panas harian mengikut rantau, siang atau malam dan tahap keyakinan. Carta titik panas bab ini dilukis daripadanya."),
  "resolution": T("按地区计数", "Counts by region", "Kiraan mengikut rantau"), "update": T("每天", "Daily", "Harian"), "format": "JSON (web page)",
  "licence": {"text": "© ASMC", "url": "https://asmc.asean.org/"},
  "params": [{"raw": "Sumatra, Kalimantan, P_Malaysia, SabahSarawak …", "meaning": T("该地区当天的火点数", "Hotspots in that region that day", "Titik panas di rantau itu pada hari tersebut"), "unit": T("个", "count", "bilangan"), "chapter": 20},
             {"raw": "daynight, conf", "meaning": T("白天/夜间；可信度（High、Medium、Low）", "Day or night; confidence (High, Medium, Low)", "Siang atau malam; keyakinan (High, Medium, Low)"), "unit": "—", "chapter": 20}],
  "sample": {"columns": ["date", "Sumatra", "Kalimantan", "P_Malaysia", "SabahSarawak"], "rows": [["2026-09-28", "84", "161", "1", "0"], ["2026-09-29", "191", "327", "0", "1"], ["2026-09-30", "47", "227", "0", "10"]], "source": "ASMC daily hotspot count, NOAA-20, daytime, high confidence", "fetched": "2026-10-02"},
  "links": [
   {"level": "view", "label": T("ASMC 每日火点页面", "ASMC daily hotspot page", "Halaman titik panas harian ASMC"), "url": "https://asmc.asean.org/asmc-haze-hotspot-daily-new/"},
   {"level": "try", "label": T("区域烟霾情况地图", "Regional haze situation map", "Peta situasi jerebu serantau"), "url": "https://asmc.asean.org/home/"},
   {"level": "pro", "label": T("NASA FIRMS 全球火点数据", "NASA FIRMS global fire data", "Data kebakaran global NASA FIRMS"), "url": "https://firms.modaps.eosdis.nasa.gov/"}]},
 {"id": "doe-apims", "name": "APIMS (Air Pollutant Index Management System)", "provider": "Department of Environment Malaysia",
  "what": T("全国空气质量监测站每小时的 API 读数。", "Hourly API readings from the national air-quality stations.", "Bacaan IPU setiap jam dari stesen kualiti udara seluruh negara."),
  "resolution": T("按监测站", "By station", "Mengikut stesen"), "update": T("每小时", "Hourly", "Setiap jam"), "format": T("网页、手机应用", "Web page, app", "Laman web, aplikasi"),
  "licence": {"text": "© Jabatan Alam Sekitar", "url": "https://eqms.doe.gov.my/APIMS/main"},
  "params": [{"raw": "API / IPU", "meaning": T("六种污染物分指数中最高的一个", "Highest of the six pollutant sub-indices", "Sub-indeks tertinggi daripada enam pencemar"), "unit": "—", "chapter": 20}],
  "sample": {"columns": ["Station", "API", "Status"], "rows": [["Kota Kinabalu", "34", "Good"], ["Cheras", "96", "Moderate"], ["Seri Manjung", "96", "Moderate"]], "source": "APIMS readings at 3.20 pm, 2 Oct 2026, as reported by Free Malaysia Today", "fetched": "2026-10-02"},
  "links": [
   {"level": "view", "label": T("APIMS 官方网站", "APIMS official site", "Laman rasmi APIMS"), "url": "https://eqms.doe.gov.my/APIMS/main"},
   {"level": "pro", "label": T("API 计算方法（PDF）", "How the API is calculated (PDF)", "Cara IPU dikira (PDF)"), "url": "https://www.doe.gov.my/wp-content/uploads/2021/09/API_Calculation.pdf"}]},
]

quiz = [
 {"stage": 6, "chapter": "ch20", "q": T("API 是怎样决定的？", "How is the API value decided?", "Bagaimana nilai IPU ditentukan?"),
  "options": [T("取六个污染物分指数中最高的一个", "The highest of six pollutant sub-indices", "Sub-indeks tertinggi daripada enam pencemar"), T("六个分指数的平均", "The average of the six", "Purata enam"), T("只看 PM10", "PM10 only", "PM10 sahaja"), T("看能见度", "Visibility", "Ketampakan")],
  "answer": 0, "why": T("有霾时通常是微粒的分指数最高。", "In haze it is usually the particulate sub-index.", "Semasa jerebu biasanya sub-indeks habuk halus.")},
 {"stage": 6, "chapter": "ch20", "q": T("API 150 属于哪一级？", "API 150 is in which band?", "IPU 150 dalam tahap mana?"),
  "options": [T("不健康", "Unhealthy", "Tidak sihat"), T("良好", "Good", "Baik"), T("中等", "Moderate", "Sederhana"), T("危险", "Hazardous", "Merbahaya")],
  "answer": 0, "why": T("101–200 是不健康。", "101–200 is unhealthy.", "101–200 ialah tidak sihat.")},
 {"stage": 6, "chapter": "ch20", "q": T("多云的日子火点很少，可以说明火很少吗？", "Few hotspots on a cloudy day: does that mean few fires?", "Sedikit titik panas pada hari berawan: adakah itu bermakna sedikit kebakaran?"),
  "options": [T("不一定，云会挡住卫星", "Not necessarily: cloud hides fires from the satellite", "Tidak semestinya: awan melindungi kebakaran daripada satelit"), T("一定是", "Yes, always", "Ya, sentiasa"), T("火点和火无关", "Hotspots have nothing to do with fire", "Titik panas tiada kaitan dengan kebakaran"), T("卫星晚上看不到", "Satellites cannot see at night", "Satelit tidak dapat melihat pada waktu malam")],
  "answer": 0, "why": T("云、树冠和小火都可能让卫星漏掉火点。", "Cloud, canopy and small fires can all be missed.", "Awan, kanopi dan kebakaran kecil semuanya boleh terlepas.")},
]

write_chapter(chapter, terms, sources, quiz, datasets)
