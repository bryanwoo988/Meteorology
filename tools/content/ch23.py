"""Chapter 23 — Weather satellites."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch23", "num": 23, "stage": 7,
 "title": T("气象卫星", "Weather satellites", "Satelit cuaca"),
 "sources": ["ESS", "TERM", "WMO-OSCAR", "NASA-GPM-DPR", "ESA-S1", "JMA-AHI", "AWS-HIMAWARI", "NASA-WORLDVIEW"],
 "sections": [
 {"id": "s1", "heading": T("两种轨道", "Two kinds of orbit", "Dua jenis orbit"), "level": "basic", "blocks": [
  P("{{t:geostationary-satellite}}在赤道上空约 36,000 公里，绕地球的速度和地球自转一样，所以一直停在同一个地点上方，可以不停地看同一片地区，几分钟拍一张，接成动画就能看云怎样移动、长大或消散。",
    "A {{t:geostationary-satellite}} sits about 36,000 km above the equator, circling at the same rate as the Earth spins, so it stays over one spot and watches the same region non-stop; images every few minutes, run as an animation, show clouds moving, growing and dying.",
    "{{t:geostationary-satellite}} berada kira-kira 36,000 km di atas khatulistiwa, mengorbit pada kadar yang sama dengan putaran bumi, jadi ia kekal di atas satu tempat dan memerhati kawasan yang sama tanpa henti; imej setiap beberapa minit, dimainkan sebagai animasi, menunjukkan awan bergerak, tumbuh dan hilang.",
    defines=["geostationary-satellite"], src=["ESS:250", "TERM:133"]),
  P("{{t:polar-satellite}}低得多（约 700–850 公里），每一圈都经过南北极附近；地球在下面自转，每一圈扫到的地方都比上一圈偏西，最后扫遍全球。它看得比较清楚，也能看清同步卫星斜着看、变形很厉害的高纬度地区。",
    "A {{t:polar-satellite}} flies much lower, about 700–850 km, passing near both poles on every orbit; as the Earth turns beneath it each pass lies further west than the last, until it has covered the whole globe. It sees in sharper detail, including the high latitudes that a geostationary satellite views at a distorting low angle.",
    "{{t:polar-satellite}} terbang jauh lebih rendah, kira-kira 700–850 km, melalui berhampiran kedua-dua kutub pada setiap orbit; apabila bumi berputar di bawahnya setiap laluan terletak lebih ke barat, sehingga meliputi seluruh dunia. Ia melihat dengan lebih terperinci, termasuk latitud tinggi yang dilihat satelit geopegun pada sudut rendah yang mengherotkan.",
    defines=["polar-satellite"], src=["ESS:250-251", "WMO-OSCAR"]),
 ]},
 {"id": "s2", "heading": T("卫星全家福", "The family of satellites", "Keluarga satelit"), "level": "basic", "blocks": [
  {"type": "widget", "id": "W15"},
  P("看马来西亚最常用的是日本的 Himawari-9，停在东经 140.7°，从吉隆坡看它在天空约 45° 高。韩国的 GEO-KOMPSAT-2A（128.2°E）、中国的风云四号和印度的 INSAT 也看得到马来西亚。WMO 的资料显示，停在东经 105° 的 FY-4B，主成像仪在 2026 年 7 月 30 日故障。",
    "For Malaysia the workhorse is Japan's Himawari-9, parked at 140.7°E and about 45° up in the sky from Kuala Lumpur. Korea's GEO-KOMPSAT-2A (128.2°E), China's Fengyun-4 satellites and India's INSATs can also see Malaysia. WMO records show that FY-4B, at 105°E, lost its main imager on 30 July 2026.",
    "Bagi Malaysia, satelit utama ialah Himawari-9 Jepun, ditempatkan pada 140.7°T dan kira-kira 45° tinggi di langit dari Kuala Lumpur. GEO-KOMPSAT-2A Korea (128.2°T), satelit Fengyun-4 China dan INSAT India juga dapat melihat Malaysia. Rekod WMO menunjukkan FY-4B, pada 105°T, kehilangan pengimej utamanya pada 30 Julai 2026.",
    src=["WMO-OSCAR"]),
  {"type": "table", "src": ["WMO-OSCAR", "ESS:251", "NASA-GPM-DPR", "ESA-S1", "NASA-WORLDVIEW"],
   "caption": T("几颗常用的极轨卫星（WMO OSCAR）", "Some polar orbiters in daily use (WMO OSCAR)", "Beberapa satelit orbit kutub yang biasa digunakan (WMO OSCAR)"),
   "headers": [T("卫星", "Satellite", "Satelit"), T("机构", "Agency", "Agensi"), T("高度", "Height", "Ketinggian"), T("看什么", "Best known for", "Terkenal kerana")],
   "rows": [[T("NOAA-20、NOAA-21", "NOAA-20, NOAA-21", "NOAA-20, NOAA-21"), T("NOAA、NASA", "NOAA, NASA", "NOAA, NASA"), T("824 公里", "824 km", "824 km"), T("温度和湿度探测，喂进预报模型", "Temperature and moisture soundings for forecast models", "Profil suhu dan lembapan untuk model ramalan")],
            [T("MetOp-B、MetOp-C", "MetOp-B, MetOp-C", "MetOp-B, MetOp-C"), T("EUMETSAT", "EUMETSAT", "EUMETSAT"), T("约 830 公里", "about 830 km", "kira-kira 830 km"), T("上午轨道的探测", "Morning-orbit soundings", "Profil orbit pagi")],
            [T("Terra、Aqua", "Terra, Aqua", "Terra, Aqua"), T("NASA", "NASA", "NASA"), T("705 公里", "705 km", "705 km"), T("MODIS 真彩色图、火点", "MODIS true-colour images, fires", "Imej warna sebenar MODIS, kebakaran")],
            [T("GPM 核心卫星", "GPM Core Observatory", "Balai Cerap Teras GPM"), T("NASA、JAXA", "NASA, JAXA", "NASA, JAXA"), T("442 公里", "442 km", "442 km"), T("太空中的降雨雷达", "A rain radar in space", "Radar hujan di angkasa")],
            [T("Sentinel-1C、Sentinel-2B/2C", "Sentinel-1C, Sentinel-2B/2C", "Sentinel-1C, Sentinel-2B/2C"), T("ESA", "ESA", "ESA"), T("693 / 786 公里", "693 / 786 km", "693 / 786 km"), T("雷达成像（穿云）、地面细节", "Radar imaging through cloud; fine ground detail", "Pengimejan radar menembusi awan; perincian darat")]]},
 ]},
 {"id": "s3", "heading": T("三种卫星图像", "Three kinds of satellite image", "Tiga jenis imej satelit"), "level": "basic", "blocks": [
  P("卫星的仪器分很多{{t:spectral-band}}，每个波段看一种光。Himawari-9 的成像仪有 16 个波段，每 10 分钟拍一次全圆盘。最常用的是三种：",
    "Satellite instruments look in many {{t:spectral-band}}s, each seeing one kind of light. Himawari-9's imager has 16 bands and scans the full disc every 10 minutes. Three kinds of image are used most:",
    "Peralatan satelit melihat dalam banyak {{t:spectral-band}}, setiap satu melihat satu jenis cahaya. Pengimej Himawari-9 mempunyai 16 jalur dan mengimbas cakera penuh setiap 10 minit. Tiga jenis imej paling banyak digunakan:",
    defines=["spectral-band"], src=["JMA-AHI"]),
  L(("{{t:visible-image}}（例如 Himawari 第 3 波段，0.64 微米）：看反射的阳光。厚云亮、薄云暗，但高云低云分不出来；晚上不能用", "{{t:visible-image}} (e.g. Himawari band 3, 0.64 µm): reflected sunlight. Thick cloud bright, thin cloud dim, but high and low cloud look alike; useless at night", "{{t:visible-image}} (cth. jalur Himawari 3, 0.64 µm): cahaya matahari dipantul. Awan tebal terang, awan nipis malap, tetapi awan tinggi dan rendah kelihatan sama; tidak berguna pada waktu malam"),
    ("{{t:infrared-image}}（例如第 13 波段，10.4 微米）：看温度。云顶越高越冷越白，低云灰色；白天晚上都能用", "{{t:infrared-image}} (e.g. band 13, 10.4 µm): temperature. The higher and colder the top, the whiter; low cloud grey; works day and night", "{{t:infrared-image}} (cth. jalur 13, 10.4 µm): suhu. Semakin tinggi dan sejuk puncak, semakin putih; awan rendah kelabu; berfungsi siang dan malam"),
    ("{{t:water-vapour-image}}（例如第 8 波段，6.2 微米）：看中高层的水汽。湿的地方亮、干的地方暗，能看到没有云的气流和急流", "{{t:water-vapour-image}} (e.g. band 8, 6.2 µm): moisture in the middle and upper air. Moist areas bright, dry areas dark, showing flow and jet streams even where there is no cloud", "{{t:water-vapour-image}} (cth. jalur 8, 6.2 µm): lembapan di udara tengah dan atas. Kawasan lembap terang, kering gelap, menunjukkan aliran dan aliran jet walaupun tiada awan"),
    defines=["visible-image", "infrared-image", "water-vapour-image"], src=["ESS:251-253", "JMA-AHI"]),
  {"type": "widget", "id": "W16"},
  N("tip", "午后阵雨在卫星上：在 Himawari 的红外线动画里，中午以后马来西亚上空会冒出一团团越来越白（越来越高、越冷）的云顶，傍晚后又慢慢散掉。",
    "Afternoon showers from space: on a Himawari infrared animation, after noon you can watch cloud tops pop up over Malaysia and turn whiter — higher and colder — then fade away after dusk.",
    "Hujan petang dari angkasa: pada animasi inframerah Himawari, selepas tengah hari anda boleh melihat puncak awan muncul di atas Malaysia dan menjadi lebih putih — lebih tinggi dan sejuk — kemudian pudar selepas senja.",
    src=["ESS:251", "ESS:352"]),
  P("卫星不只是拍照片。新一代的探测仪能量出各高度的温度和湿度，这些资料会喂进电脑预报模型——第 27 章会讲。",
    "Satellites do more than take pictures. Modern sounders measure temperature and moisture at different heights, and those data are fed into computer forecast models — the subject of Chapter 27.",
    "Satelit bukan sekadar mengambil gambar. Penduga moden mengukur suhu dan lembapan pada pelbagai ketinggian, dan data itu dimasukkan ke dalam model ramalan komputer — topik Bab 27.",
    src=["ESS:251", "ESS:256"]),
  {"type": "dataset", "id": "himawari-aws"},
  {"type": "dataset", "id": "nasa-worldview"},
 ]},
 ]}

terms = [
 ("geostationary-satellite", T("同步卫星", "Geostationary satellite", "Satelit geopegun"), T("在赤道上空约 36,000 公里、一直停在同一点上方的卫星。", "A satellite about 36,000 km above the equator that stays over one spot.", "Satelit kira-kira 36,000 km di atas khatulistiwa yang kekal di atas satu tempat.")),
 ("polar-satellite", T("极轨卫星", "Polar-orbiting satellite", "Satelit orbit kutub"), T("低轨道、每圈经过两极附近、逐渐扫遍全球的卫星。", "A low satellite passing near both poles each orbit, covering the globe in strips.", "Satelit rendah yang melalui berhampiran kedua-dua kutub setiap orbit, meliputi dunia secara berjalur.")),
 ("spectral-band", T("波段", "Spectral band", "Jalur spektrum"), T("卫星仪器看的一段特定波长的光。", "The particular range of wavelengths an instrument channel sees.", "Julat panjang gelombang tertentu yang dilihat oleh satu saluran alat.")),
 ("visible-image", T("可见光图像", "Visible image", "Imej cahaya nampak"), T("拍反射阳光的卫星图；厚云亮，晚上不能用。", "A satellite image of reflected sunlight; thick cloud bright; no use at night.", "Imej satelit cahaya matahari dipantul; awan tebal terang; tidak berguna pada waktu malam.")),
 ("infrared-image", T("红外线图像", "Infrared image", "Imej inframerah"), T("按温度显示的卫星图；高而冷的云顶最白。", "A satellite image of temperature; high, cold tops whitest.", "Imej satelit suhu; puncak tinggi dan sejuk paling putih.")),
 ("water-vapour-image", T("水汽图像", "Water-vapour image", "Imej wap air"), T("显示中高层水汽的卫星图；湿亮干暗。", "A satellite image of middle- and upper-level moisture; moist bright, dry dark.", "Imej satelit lembapan aras tengah dan atas; lembap terang, kering gelap.")),
]

sources = [
 {"id": "WMO-OSCAR", "short": "WMO OSCAR", "title": "OSCAR/Space — satellite pages (orbit, longitude, status), checked 2 Oct 2026", "publisher": "World Meteorological Organization", "url": "https://space.oscar.wmo.int/satellites", "accessed": "2026-10-02"},
 {"id": "NASA-GPM-DPR", "short": "NASA GPM", "title": "GPM Dual-frequency Precipitation Radar (DPR)", "publisher": "NASA Global Precipitation Measurement", "url": "https://gpm.nasa.gov/missions/GPM/DPR", "accessed": "2026-10-02"},
 {"id": "ESA-S1", "short": "Copernicus", "title": "Sentinel-1: all-weather, day-and-night radar imagery", "publisher": "ESA / Copernicus", "url": "https://sentinels.copernicus.eu/copernicus/sentinel-1", "accessed": "2026-10-02"},
 {"id": "JMA-AHI", "short": "JMA", "title": "Himawari-8/9 Advanced Himawari Imager (AHI): bands and observation schedule", "publisher": "Japan Meteorological Agency, Meteorological Satellite Center", "url": "https://www.data.jma.go.jp/mscweb/en/himawari89/space_segment/spsg_ahi.html", "accessed": "2026-10-02"},
 {"id": "AWS-HIMAWARI", "short": "AWS Open Data", "title": "JMA Himawari-8/9 on the Registry of Open Data on AWS", "publisher": "NOAA Open Data Dissemination / Amazon Web Services", "url": "https://registry.opendata.aws/noaa-himawari/", "accessed": "2026-10-02"},
 {"id": "NASA-WORLDVIEW", "short": "NASA Worldview", "title": "NASA Worldview — interactive satellite imagery", "publisher": "NASA Earth Science Data Systems", "url": "https://worldview.earthdata.nasa.gov/", "accessed": "2026-10-02"},
]

datasets = [
 {"id": "himawari-aws", "name": "Himawari-9 AHI full disk (AWS)", "provider": "JMA, distributed by NOAA on AWS",
  "what": T("Himawari-9 每 10 分钟一次的全圆盘原始资料，16 个波段，每个波段切成 10 段。", "Himawari-9's raw full-disc data every 10 minutes: 16 bands, each cut into 10 segments.", "Data mentah cakera penuh Himawari-9 setiap 10 minit: 16 jalur, setiap satu dipotong kepada 10 segmen."),
  "resolution": "0.5–2 km", "update": T("每 10 分钟", "Every 10 minutes", "Setiap 10 minit"), "format": "Himawari Standard Data (.DAT.bz2)",
  "licence": {"text": "Open data; JMA and NOAA request attribution", "url": "https://registry.opendata.aws/noaa-himawari/"},
  "params": [{"raw": "B03", "meaning": T("第 3 波段，0.64 微米可见光，0.5 公里", "Band 3, 0.64 µm visible, 0.5 km", "Jalur 3, 0.64 µm nampak, 0.5 km"), "unit": "—", "chapter": 23},
             {"raw": "B08", "meaning": T("第 8 波段，6.2 微米水汽", "Band 8, 6.2 µm water vapour", "Jalur 8, 6.2 µm wap air"), "unit": "—", "chapter": 23},
             {"raw": "B13", "meaning": T("第 13 波段，10.4 微米红外线", "Band 13, 10.4 µm infrared", "Jalur 13, 10.4 µm inframerah"), "unit": "—", "chapter": 23}],
  "sample": {"columns": ["Key", "Size (bytes)"], "rows": [["AHI-L1b-FLDK/2026/10/01/0300/HS_H09_20261001_0300_B01_FLDK_R10_S0110.DAT.bz2", "4245260"], ["AHI-L1b-FLDK/2026/10/01/0300/HS_H09_20261001_0300_B01_FLDK_R10_S0210.DAT.bz2", "7642134"]], "source": "Bucket listing of noaa-himawari9 (03:00 UTC = 11 am in Malaysia)", "fetched": "2026-10-02"},
  "links": [
   {"level": "view", "label": T("JMA 卫星图像（网页）", "JMA satellite imagery (web)", "Imej satelit JMA (web)"), "url": "https://www.data.jma.go.jp/mscweb/data/himawari/index.html"},
   {"level": "try", "label": T("在浏览器里列出档案", "List the files in a browser", "Senaraikan fail dalam pelayar"), "url": "https://noaa-himawari9.s3.amazonaws.com/?list-type=2&prefix=AHI-L1b-FLDK/2026/10/01/0300/&max-keys=20"},
   {"level": "pro", "label": T("AWS 开放数据说明", "AWS open-data page", "Halaman data terbuka AWS"), "url": "https://registry.opendata.aws/noaa-himawari/",
    "note": T("用 Python 的 satpy 读 .DAT 档案。", "Read the .DAT files with Python's satpy.", "Baca fail .DAT dengan satpy Python.")}]},
 {"id": "nasa-worldview", "name": "NASA Worldview", "provider": "NASA",
  "what": T("在浏览器里看全球卫星图层：真彩色、火点、云、气溶胶等，可以选日期，不用下载。", "Browse global satellite layers in a web page — true colour, fires, clouds, aerosols and more — for any date, with no download.", "Layari lapisan satelit global dalam laman web — warna sebenar, kebakaran, awan, aerosol dan banyak lagi — bagi sebarang tarikh, tanpa muat turun."),
  "resolution": "250 m – 2 km", "update": T("每天", "Daily", "Harian"), "format": T("网页地图（可导出图片）", "Web map (export as image)", "Peta web (eksport imej)"),
  "licence": {"text": "NASA open data", "url": "https://worldview.earthdata.nasa.gov/"},
  "params": [{"raw": "MODIS / VIIRS Corrected Reflectance", "meaning": T("真彩色图像", "True-colour imagery", "Imej warna sebenar"), "unit": "—", "chapter": 23}],
  "sample": {"columns": ["Layer", "Satellite"], "rows": [["Corrected Reflectance (True Color)", "Terra / Aqua (MODIS)"], ["Thermal Anomalies and Fires (375m, VIIRS)", "NOAA-20 / NOAA-21"]], "source": "NASA GIBS layer list behind Worldview", "fetched": "2026-10-02"},
  "links": [
   {"level": "view", "label": T("打开 Worldview", "Open Worldview", "Buka Worldview"), "url": "https://worldview.earthdata.nasa.gov/"}]},
]

quiz = [
 {"stage": 7, "chapter": "ch23", "q": T("晚上要看云，应该用哪一种图像？", "To see cloud at night, which image?", "Untuk melihat awan pada waktu malam, imej mana?"),
  "options": [T("红外线", "Infrared", "Inframerah"), T("可见光", "Visible", "Cahaya nampak"), T("真彩色", "True colour", "Warna sebenar"), T("都不行", "None", "Tiada")],
  "answer": 0, "why": T("红外线看温度，不需要阳光。", "Infrared sees temperature and needs no sunlight.", "Inframerah melihat suhu dan tidak memerlukan cahaya matahari.")},
 {"stage": 7, "chapter": "ch23", "q": T("在红外线图上，哪一种云最白？", "Which cloud is whitest on an infrared image?", "Awan manakah paling putih pada imej inframerah?"),
  "options": [T("又高又冷的雷雨云顶", "A high, cold thunderstorm top", "Puncak ribut petir yang tinggi dan sejuk"), T("低积云", "Low cumulus", "Kumulus rendah"), T("雾", "Fog", "Kabus"), T("没有云的海面", "Clear sea", "Laut tanpa awan")],
  "answer": 0, "why": T("越冷显示越白。", "The colder, the whiter.", "Semakin sejuk, semakin putih.")},
 {"stage": 7, "chapter": "ch23", "q": T("Himawari-9 多久拍一次全圆盘？", "How often does Himawari-9 scan the full disc?", "Berapa kerap Himawari-9 mengimbas cakera penuh?"),
  "options": [T("每 10 分钟", "Every 10 minutes", "Setiap 10 minit"), T("每天一次", "Once a day", "Sekali sehari"), T("每小时", "Every hour", "Setiap jam"), T("每星期", "Every week", "Setiap minggu")],
  "answer": 0, "why": T("所以可以做成动画看云的变化。", "Which is why it can be animated.", "Itulah sebabnya ia boleh dianimasikan.")},
]

write_chapter(chapter, terms, sources, quiz, datasets)
