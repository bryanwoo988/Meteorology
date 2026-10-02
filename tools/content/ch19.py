"""Chapter 19 — Floods and drought."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch19", "num": 19, "stage": 6,
 "title": T("洪水与干旱", "Floods and drought", "Banjir dan kemarau"),
 "sources": ["MET-PHEN", "TERM", "PAM", "MET-DROUGHT", "MET-ENSO-STATUS"],
 "sections": [
 {"id": "s1", "heading": T("季风水灾", "Monsoon floods", "Banjir monsun"), "level": "basic", "blocks": [
  P("东北季风带来的大雨，常常在半岛东海岸的吉兰丹、登嘉楼、彭亨和柔佛东部，以及砂拉越和沙巴造成大范围的水灾。这种跟着季风来的水灾，叫{{t:monsoon-flood}}。",
    "The heavy rain of the north-east monsoon often causes widespread floods in Kelantan, Terengganu, Pahang and East Johor on the Peninsula's east coast, and in Sarawak and Sabah. Floods that come with the monsoon are {{t:monsoon-flood}}s.",
    "Hujan lebat monsun timur laut sering menyebabkan banjir meluas di Kelantan, Terengganu, Pahang dan Johor Timur di pantai timur Semenanjung, serta di Sarawak dan Sabah. Banjir yang datang bersama monsun ialah {{t:monsoon-flood}}.",
    defines=["monsoon-flood"], src=["MET-PHEN"]),
  {"type": "map", "id": "M11", "src": ["MET-PHEN"]},
  N("key", "季风水灾来自连续的大雨，这正是第 18 章连续降雨预警要提醒的情况。",
    "Monsoon floods come from continuous heavy rain — exactly what the continuous-rain warnings of Chapter 18 are for.",
    "Banjir monsun datang daripada hujan lebat berterusan — tepat seperti yang diberi amaran oleh amaran hujan berterusan Bab 18.",
    src=["MET-PHEN", "MET-WARN-RAIN"]),
 ]},
 {"id": "s2", "heading": T("闪电水灾", "Flash floods", "Banjir kilat"), "level": "basic", "blocks": [
  P("{{t:flash-flood}}是水涨得快、退得也快、几乎没有预先警告的水灾，通常由突然的大雨造成。马来西亚的雷雨和飑线带来的大雨，常在低洼和排水差的地方造成闪电水灾，在山区还可能引起土崩。",
    "A {{t:flash-flood}} rises and falls quickly with little or no warning, usually after a sudden downpour. The heavy rain of Malaysia's thunderstorms and squall lines often flash-floods low-lying and poorly drained places, and can set off landslides in the hills.",
    "{{t:flash-flood}} naik dan surut dengan cepat dengan sedikit atau tiada amaran, biasanya selepas hujan lebat mendadak. Hujan lebat ribut petir dan garis badai di Malaysia sering menyebabkan banjir kilat di kawasan rendah dan bersaliran lemah, dan boleh mencetuskan tanah runtuh di kawasan bukit.",
    defines=["flash-flood"], src=["TERM:129", "MET-PHEN"]),
  N("warn", "闪电水灾不需要下几天的雨，一场雷雨就够了。看到雷暴预警（每小时超过 20 毫米）就要留意。",
    "A flash flood needs no days of rain; one thunderstorm is enough. Take note whenever a thunderstorm warning (over 20 mm an hour) is issued.",
    "Banjir kilat tidak memerlukan hujan berhari-hari; satu ribut petir sudah cukup. Beri perhatian setiap kali amaran ribut petir (melebihi 20 mm sejam) dikeluarkan.",
    src=["MET-PHEN", "MET-WARN-TS"]),
 ]},
 {"id": "s3", "heading": T("干旱的种类", "Kinds of drought", "Jenis kemarau"), "level": "basic", "blocks": [
  P("干旱是缺水的一种气候异常：可用的水不够满足需要。它来得慢，很难说哪一天开始，但影响又久又广。按影响的对象，可以分成三种：",
    "Drought is a climatic anomaly of moisture shortage: the water available falls short of the water needed. It creeps in — it is hard to say on which day it begins — but its effects last long and spread wide. By what it affects, there are three kinds:",
    "Kemarau ialah anomali iklim kekurangan lembapan: air yang ada tidak mencukupi untuk keperluan. Ia datang perlahan — sukar untuk menentukan hari ia bermula — tetapi kesannya lama dan meluas. Mengikut apa yang terjejas, terdapat tiga jenis:",
    src=["PAM:95-97"]),
  L(("{{t:meteorological-drought}}：大范围的雨量明显低于平常", "{{t:meteorological-drought}}: rainfall well below normal over a wide area", "{{t:meteorological-drought}}: hujan jauh di bawah normal di kawasan yang luas"),
    ("{{t:hydrological-drought}}：气象干旱拖得太久，河流、水库和湖泊的水变少甚至干涸", "{{t:hydrological-drought}}: a meteorological drought lasts so long that rivers, reservoirs and lakes run low or dry", "{{t:hydrological-drought}}: kemarau meteorologi berlarutan sehingga sungai, takungan dan tasik menyusut atau kering"),
    ("{{t:agricultural-drought}}：作物在一季里得不到足够的土壤水分", "{{t:agricultural-drought}}: a crop does not get enough soil moisture during its season", "{{t:agricultural-drought}}: tanaman tidak mendapat lembapan tanah yang mencukupi sepanjang musimnya"),
    defines=["meteorological-drought", "hydrological-drought", "agricultural-drought"], src=["PAM:97"]),
 ]},
 {"id": "s4", "heading": T("马来西亚怎样监测干旱", "How Malaysia monitors drought", "Bagaimana Malaysia memantau kemarau"), "level": "basic", "blocks": [
  P("大马气象局每月用{{t:spi}}监测 40 个主要气象站。SPI 在 −0.99 到 0.99 之间是正常；负数表示雨量比正常少，越负越干。",
    "Each month MetMalaysia checks its 40 principal stations with the {{t:spi}}. Between −0.99 and 0.99 the SPI is normal; a negative value means less rain than normal, and the more negative, the drier.",
    "Setiap bulan MetMalaysia memantau 40 stesen utamanya dengan {{t:spi}}. SPI antara −0.99 dan 0.99 adalah normal; nilai negatif bermaksud hujan kurang daripada normal, dan semakin negatif, semakin kering.",
    defines=["spi"], src=["MET-DROUGHT"]),
  {"type": "table", "src": ["MET-DROUGHT"],
   "caption": T("SPI 的等级", "SPI scale", "Skala SPI"),
   "headers": [T("SPI", "SPI", "SPI"), T("等级", "Category", "Kategori")],
   "rows": [[T("2.0 或以上", "2.0 or more", "2.0 dan ke atas"), T("极湿", "Extremely wet", "Terlalu lembap")],
            [T("1.5 到 1.99", "1.5 to 1.99", "1.5 ke 1.99"), T("很湿", "Very wet", "Sangat lembap")],
            [T("1.0 到 1.49", "1.0 to 1.49", "1.0 ke 1.49"), T("中等湿", "Moderately wet", "Sederhana lembap")],
            [T("−0.99 到 0.99", "−0.99 to 0.99", "−0.99 ke 0.99"), T("正常", "Normal", "Normal")],
            [T("−1.0 到 −1.49", "−1.0 to −1.49", "−1.0 ke −1.49"), T("中等干", "Moderately dry", "Sederhana kering")],
            [T("−1.5 到 −1.99", "−1.5 to −1.99", "−1.5 ke −1.99"), T("很干", "Very dry", "Sangat kering")],
            [T("−2.0 或以下", "−2.0 or less", "−2.0 atau kurang"), T("极干", "Extremely dry", "Terlalu kering")]]},
  P("只看 SPI 还不够：要宣布气象干旱，还要看最近 3 个月和/或 6 个月的累积雨量比正常少了多少。例如第一级 Waspada：最近 3 个月（或 6 个月）的雨量比正常少 35 % 以上，而且最新一个月的 SPI 低于 −1.5。2026 年 7 月的报告里，淡马鲁（Temerloh）和纳闽（Labuan）属于“很干”，但没有一个站达到气象干旱的状态。",
    "The SPI alone is not enough: declaring a meteorological drought also looks at how far the total rain of the last 3 and/or 6 months has fallen below normal. The first level, Waspada, for example, needs the last 3 (or 6) months' rain more than 35 % below normal and the latest month's SPI below −1.5. In the July 2026 report Temerloh and Labuan were ‘very dry’, but no station had reached meteorological-drought status.",
    "SPI sahaja tidak mencukupi: pengisytiharan kemarau meteorologi juga melihat sejauh mana jumlah hujan 3 dan/atau 6 bulan terkini jatuh di bawah normal. Peringkat pertama, Waspada, contohnya, memerlukan hujan 3 (atau 6) bulan terkini lebih daripada 35 % di bawah normal dan SPI bulan terkini di bawah −1.5. Dalam laporan Julai 2026 Temerloh dan Labuan berada pada skala ‘sangat kering’, tetapi tiada stesen yang mencapai status kemarau meteorologi.",
    src=["MET-DROUGHT"]),
  {"type": "dataset", "id": "metmy-spi", "src": ["MET-DROUGHT"]},
  N("warn", "大马气象局 2026 年 9 月 15 日的 ENSO 状态说：厄尔尼诺目前是中等强度，预计持续到 2027 年 5 月，年底几乎肯定会变得非常强；东北季风结束后，2027 年 1 月到 5 月预计会有极端干热的天气。",
    "MetMalaysia's ENSO status of 15 September 2026 says El Niño is now moderate, is expected to last until May 2027 and is almost certain to become very strong by the end of the year; extreme hot, dry weather is expected from the end of the north-east monsoon, January to May 2027.",
    "Status ENSO MetMalaysia pada 15 September 2026 menyatakan El Niño kini pada tahap sederhana, dijangka berterusan sehingga Mei 2027 dan hampir pasti mencapai tahap sangat kuat menjelang akhir tahun; cuaca kering dan panas ekstrem dijangka bermula penghujung monsun timur laut, Januari hingga Mei 2027.",
    src=["MET-ENSO-STATUS"]),
 ]},
 {"id": "s5", "heading": T("干旱时农业可以做什么", "What farming can do in a drought", "Apa yang boleh dilakukan pertanian semasa kemarau"), "level": "basic", "blocks": [
  L(("选用耐旱的作物和种子", "Choose drought-resistant crops and seeds", "Pilih tanaman dan benih tahan kemarau"),
    ("在雨多的时候集雨、蓄水", "Harvest and store water when the rains are heavy", "Tuai dan simpan air ketika hujan lebat"),
    ("做好保水和水土保持", "Conserve soil moisture and protect the soil", "Pelihara lembapan tanah dan lindungi tanah"),
    ("除草，减少和作物抢水", "Remove weeds that compete for water", "Buang rumpai yang bersaing untuk air"),
    ("种防风林、设挡风屏障", "Plant shelterbelts and windbreaks", "Tanam tali pelindung dan penghadang angin"),
    ("覆盖地面（mulching），减少蒸发", "Mulch the ground to cut evaporation", "Sungkup tanah untuk mengurangkan penyejatan"),
    src=["PAM:98"]),
 ]},
 ]}

terms = [
 ("monsoon-flood", T("季风水灾", "Monsoon flood", "Banjir monsun"), T("东北季风的大雨造成的大范围水灾。", "Widespread flooding from the heavy rain of the north-east monsoon.", "Banjir meluas akibat hujan lebat monsun timur laut.")),
 ("flash-flood", T("闪电水灾", "Flash flood", "Banjir kilat"), T("突然的大雨造成、涨得快退得快、几乎没有预警的水灾。", "A flood that rises and falls fast with little warning, after a sudden downpour.", "Banjir yang naik dan surut cepat dengan sedikit amaran, selepas hujan lebat mendadak.")),
 ("meteorological-drought", T("气象干旱", "Meteorological drought", "Kemarau meteorologi"), T("大范围的雨量明显低于平常。", "Rainfall well below normal over a wide area.", "Hujan jauh di bawah normal di kawasan luas.")),
 ("hydrological-drought", T("水文干旱", "Hydrological drought", "Kemarau hidrologi"), T("气象干旱拖久了，河流、水库和湖泊缺水。", "A long meteorological drought that drains rivers, reservoirs and lakes.", "Kemarau meteorologi yang lama sehingga sungai, takungan dan tasik kekurangan air.")),
 ("agricultural-drought", T("农业干旱", "Agricultural drought", "Kemarau pertanian"), T("作物在生长季里土壤水分不足。", "Too little soil moisture for a crop during its season.", "Lembapan tanah tidak mencukupi untuk tanaman sepanjang musimnya.")),
 ("spi", T("标准化降水指数（SPI）", "Standardized Precipitation Index (SPI)", "Indeks Kerpasan Piawai (SPI)"), T("干旱监测用的指数；负数表示雨量比正常少，−1.5 以下“很干”。", "A drought-monitoring index; negative means less rain than normal, below −1.5 ‘very dry’.", "Indeks pemantauan kemarau; negatif bermaksud hujan kurang daripada normal, di bawah −1.5 ‘sangat kering’.")),
]

sources = [
 {"id": "MET-DROUGHT", "short": "MetMalaysia", "title": "Laporan pemantauan kemarau, Julai 2026 (Indeks Kerpasan Piawai)", "publisher": "Jabatan Meteorologi Malaysia", "url": "https://www.met.gov.my/data/climate/kemarau.pdf", "accessed": "2026-10-02"},
 {"id": "MET-ENSO-STATUS", "short": "MetMalaysia", "title": "Status El Niño Southern Oscillation (ENSO), kemas kini 15 September 2026", "publisher": "Jabatan Meteorologi Malaysia", "url": "https://www.met.gov.my/data/climate/status_elnino.pdf", "accessed": "2026-10-02"},
]

datasets = [
 {"id": "metmy-spi", "name": "MetMalaysia SPI drought monitoring", "provider": "Malaysian Meteorological Department",
  "what": T("每月一份报告：40 个主要气象站 1 到 6 个月的 SPI，以及干旱等级。", "A monthly report: 1- to 6-month SPI for 40 principal stations, and the drought level.", "Laporan bulanan: SPI 1 hingga 6 bulan bagi 40 stesen utama, dan tahap kemarau."),
  "resolution": T("40 个气象站", "40 stations", "40 stesen"), "update": T("每月", "Monthly", "Bulanan"), "format": "PDF",
  "licence": {"text": "© Jabatan Meteorologi Malaysia", "url": "https://www.met.gov.my/"},
  "params": [{"raw": "SPI 1bulan … 6bulan", "meaning": T("最近 1 到 6 个月的标准化降水指数", "SPI over the last 1 to 6 months", "SPI bagi 1 hingga 6 bulan terkini"), "unit": "—", "chapter": 19},
             {"raw": "No Stn", "meaning": T("气象站编号", "Station number", "Nombor stesen"), "unit": "—", "chapter": 19}],
  "sample": {"columns": ["No Stn", "Nama Stesen", "Lat", "Lon", "SPI 1bulan", "SPI 3bulan", "SPI 6bulan"],
   "rows": [["48653", "TEMERLOH", "3.47", "102.38", "-1.65", "0.17", "-0.58"], ["96465", "LABUAN", "5.30", "115.25", "-1.54", "-0.17", "-0.89"], ["48665", "MELAKA", "2.27", "102.25", "2.53", "2.03", "1.61"]],
   "source": "Laporan Pemantauan Kemarau Julai 2026, Jadual 1", "fetched": "2026-10-02"},
  "links": [
   {"level": "view", "label": T("最新干旱监测报告（PDF）", "Latest drought report (PDF)", "Laporan kemarau terkini (PDF)"), "url": "https://www.met.gov.my/data/climate/kemarau.pdf"},
   {"level": "try", "label": T("最新 ENSO 状态（PDF）", "Latest ENSO status (PDF)", "Status ENSO terkini (PDF)"), "url": "https://www.met.gov.my/data/climate/status_elnino.pdf"}]},
]

quiz = [
 {"stage": 6, "chapter": "ch19", "q": T("闪电水灾和季风水灾最大的不同是什么？", "What most separates a flash flood from a monsoon flood?", "Apakah perbezaan utama banjir kilat dan banjir monsun?"),
  "options": [T("闪电水灾来得快、退得快，一场大雨就够", "A flash flood comes and goes fast; one downpour is enough", "Banjir kilat datang dan surut cepat; satu hujan lebat sudah cukup"), T("闪电水灾只在东海岸", "Flash floods happen only on the east coast", "Banjir kilat hanya di pantai timur"), T("季风水灾没有雨", "Monsoon floods need no rain", "Banjir monsun tidak memerlukan hujan"), T("两者完全一样", "They are the same", "Kedua-duanya sama")],
  "answer": 0, "why": T("季风水灾来自东北季风连续的大雨。", "Monsoon floods come from the north-east monsoon's continuous heavy rain.", "Banjir monsun datang daripada hujan lebat berterusan monsun timur laut.")},
 {"stage": 6, "chapter": "ch19", "q": T("河流和水库干涸，是哪一种干旱？", "Rivers and reservoirs running dry: which drought?", "Sungai dan takungan kering: kemarau jenis apa?"),
  "options": [T("水文干旱", "Hydrological", "Hidrologi"), T("气象干旱", "Meteorological", "Meteorologi"), T("农业干旱", "Agricultural", "Pertanian"), T("都不是", "None", "Tiada")],
  "answer": 0, "why": T("气象干旱拖久了，就变成水文干旱。", "A long meteorological drought becomes a hydrological one.", "Kemarau meteorologi yang lama menjadi kemarau hidrologi.")},
 {"stage": 6, "chapter": "ch19", "q": T("某站 SPI 是 −1.65，属于哪个等级？", "A station's SPI is −1.65. Which category?", "SPI sebuah stesen ialah −1.65. Kategori mana?"),
  "options": [T("很干", "Very dry", "Sangat kering"), T("正常", "Normal", "Normal"), T("极湿", "Extremely wet", "Terlalu lembap"), T("中等湿", "Moderately wet", "Sederhana lembap")],
  "answer": 0, "why": T("−1.5 到 −1.99 是“很干”。", "−1.5 to −1.99 is ‘very dry’.", "−1.5 hingga −1.99 ialah ‘sangat kering’.")},
]

write_chapter(chapter, terms, sources, quiz, datasets)
