"""Chapter 36 — A real event, step by step: December 2021."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch36", "num": 36, "stage": 8,
 "title": T("真实事件复盘：2021 年 12 月大雨", "A real event, step by step: December 2021", "Peristiwa sebenar, langkah demi langkah: Disember 2021"),
 "sources": ["METMY-NEM2122", "ERA5-OM", "MET-WARN-RAIN"],
 "sections": [
 {"id": "s1", "heading": T("发生了什么", "What happened", "Apa yang berlaku"), "level": "basic", "blocks": [
  P("这一章只用大马气象局的官方检讨报告（2021/2022 东北季风检讨，研究报告 1/2024），把 2021 年 12 月 16 到 18 日的大雨从头看一遍，每一步都标出用到哪一章的知识。",
    "This chapter uses only MetMalaysia's official review of the 2021/2022 north-east monsoon (Research Publication 1/2024) to walk through the heavy rain of 16–18 December 2021, marking which chapter each step draws on.",
    "Bab ini hanya menggunakan kajian semula rasmi MetMalaysia bagi monsun timur laut 2021/2022 (Penerbitan Penyelidikan 1/2024) untuk menelusuri hujan lebat 16–18 Disember 2021, menandakan bab mana yang digunakan setiap langkah.",
    src=["METMY-NEM2122"]),
  L(("12 月 16 日：一股季风潮（第 16 章）开始。东海岸雨很大，吉兰丹、登嘉楼、彭亨连续下大雨。季风槽从菲律宾斜到苏门答腊，东北风在槽里汇合（第 9、26 章）。", "16 December: a monsoon surge (Chapter 16) begins. Heavy rain falls on the east coast, prolonged in Kelantan, Terengganu and Pahang. The monsoon trough slants from the Philippines to Sumatra, and the north-east winds converge in it (Chapters 9 and 26).", "16 Disember: luruan monsun (Bab 16) bermula. Hujan lebat di pantai timur, berpanjangan di Kelantan, Terengganu dan Pahang. Palung monsun condong dari Filipina ke Sumatera, dan angin timur laut menumpu di dalamnya (Bab 9 dan 26)."),
    ("12 月 17 日：台风雷伊（Rai）穿过巴拉望进入南中国海后加强（第 12 章）。下游的风分成两支，一支进入半岛，和从苏门答腊来的西风汇合，在马六甲海峡一带带来大雨。", "17 December: Typhoon Rai strengthens after crossing Palawan into the South China Sea (Chapter 12). Downstream the winds split; one branch enters the Peninsula and converges with westerlies from Sumatra, bringing heavy rain around the Strait of Malacca.", "17 Disember: Taufan Rai menguat selepas melintasi Palawan ke Laut China Selatan (Bab 12). Di hilir angin berpecah; satu cabang memasuki Semenanjung dan menumpu dengan angin barat dari Sumatera, membawa hujan lebat di sekitar Selat Melaka."),
    ("12 月 18 日：雷伊在接近越南时意外地重新增强。东北风深入半岛，和西南风汇合，马六甲海峡一带继续下大雨。", "18 December: Rai unexpectedly re-intensifies as it nears Vietnam. North-east winds push deep into the Peninsula and meet south-west winds, keeping the heavy rain going around the Strait of Malacca.", "18 Disember: Rai menguat semula secara tidak dijangka apabila menghampiri Vietnam. Angin timur laut menembusi jauh ke Semenanjung dan bertemu angin barat daya, meneruskan hujan lebat di sekitar Selat Melaka."),
    ("12 月 19 日：台风减弱，南中国海风速减慢，季风潮结束。", "19 December: the typhoon weakens, the winds over the South China Sea slacken, and the surge ends.", "19 Disember: taufan melemah, angin di Laut China Selatan menjadi perlahan, dan luruan berakhir."),
    src=["METMY-NEM2122"]),
  {"type": "table", "src": ["METMY-NEM2122"],
   "caption": T("气象站的日雨量（大马气象局检讨报告表 4）", "Daily rain at principal stations (MetMalaysia review, Table 4)", "Hujan harian di stesen utama (kajian semula MetMalaysia, Jadual 4)"),
   "headers": [T("日期", "Date", "Tarikh"), T("气象站", "Station", "Stesen"), T("雨量", "Rain", "Hujan")],
   "rows": [[T("12 月 17 日", "17 Dec", "17 Dis"), T("吉隆坡国际机场（雪兰莪）", "KLIA (Selangor)", "KLIA (Selangor)"), T("188 毫米", "188 mm", "188 mm")],
            [T("12 月 17 日", "17 Dec", "17 Dis"), T("关丹（彭亨）", "Kuantan (Pahang)", "Kuantan (Pahang)"), T("261 毫米", "261 mm", "261 mm")],
            [T("12 月 18 日", "18 Dec", "18 Dis"), T("关丹（彭亨）", "Kuantan (Pahang)", "Kuantan (Pahang)"), T("339 毫米", "339 mm", "339 mm")],
            [T("12 月 18 日", "18 Dec", "18 Dis"), T("梳邦（雪兰莪）", "Subang (Selangor)", "Subang (Selangor)"), T("253 毫米", "253 mm", "253 mm")],
            [T("12 月 18 日", "18 Dec", "18 Dis"), T("八打灵再也（雪兰莪）", "Petaling Jaya (Selangor)", "Petaling Jaya (Selangor)"), T("201 毫米", "201 mm", "201 mm")]]},
  N("key", "对照第 18 章的预警标准：24 小时超过 250 毫米就是最高级 Bahaya；梳邦和关丹的一天雨量都超过这个门槛。",
    "Compare Chapter 18's warning criteria: over 250 mm in 24 hours is the top level, Bahaya — and both Subang and Kuantan passed that in a single day.",
    "Bandingkan kriteria amaran Bab 18: lebih 250 mm dalam 24 jam ialah peringkat tertinggi, Bahaya — dan kedua-dua Subang dan Kuantan melepasinya dalam satu hari.",
    src=["MET-WARN-RAIN", "METMY-NEM2122"]),
 ]},
 {"id": "s2", "heading": T("格子平均和雨量计", "Grid averages and gauges", "Purata grid dan tolok"), "level": "basic", "blocks": [
  {"type": "chart", "src": ["ERA5-OM"], "chart": {"kind": "line", "series_file": "dec2021-era5",
    "title": T("ERA5 的日雨量，2021 年 12 月 10–25 日", "ERA5 daily rain, 10–25 December 2021", "Hujan harian ERA5, 10–25 Disember 2021"),
    "x": {"col": "date", "label": T("日期", "Date", "Tarikh"), "format": "date"},
    "y": {"label": T("雨量", "Rain", "Hujan"), "unit": "mm"},
    "series": [{"col": "subang", "name": T("梳邦格子", "Subang box", "Kotak Subang"), "color": "sky"},
               {"col": "kuantan", "name": T("关丹格子", "Kuantan box", "Kotak Kuantan"), "color": "mercury"}]}},
  P("再分析 ERA5 抓到了同一段大雨，但数字小得多：12 月 18 日梳邦的格子只有约 69 毫米，气象站是 253 毫米；关丹格子 18 日约 43 毫米，最大值反而出现在 19 日（约 141 毫米），而气象站 18 日就有 339 毫米。原因就是第 15、31 章说的：一格约 25 公里的平均，会把局部的极端大雨抹平；每天从几点算起，也可能不一样。",
    "The ERA5 reanalysis catches the same spell but with much smaller numbers: on 18 December the Subang box has about 69 mm against the station's 253 mm; the Kuantan box has about 43 mm on the 18th and peaks only on the 19th (about 141 mm), while the station had 339 mm on the 18th. That is Chapters 15 and 31 at work: an average over a box about 25 km across smooths away local extremes, and the hour at which a 'day' starts may also differ.",
    "Analisis semula ERA5 menangkap tempoh yang sama tetapi dengan nombor jauh lebih kecil: pada 18 Disember kotak Subang kira-kira 69 mm berbanding 253 mm di stesen; kotak Kuantan kira-kira 43 mm pada 18hb dan hanya memuncak pada 19hb (kira-kira 141 mm), manakala stesen mencatat 339 mm pada 18hb. Itulah Bab 15 dan 31: purata kotak kira-kira 25 km melicinkan ekstrem setempat, dan jam bermulanya 'hari' juga mungkin berbeza.",
    src=["ERA5-OM", "METMY-NEM2122"]),
  N("tip", "复盘一次事件时，可以照这个顺序：卫星（第 23 章）看云系，雷达（第 24 章）看雨区移动，ECMWF 的集合预报（第 30 章）看事前有几成成员预报大雨，最后对照气象局的预警（第 18 章）和雨量站。",
    "To review any event, follow this order: satellite (Chapter 23) for the cloud systems, radar (Chapter 24) for how the rain moved, ECMWF's ensemble (Chapter 30) for how many members foresaw heavy rain, and finally MetMalaysia's warnings (Chapter 18) and the gauges.",
    "Untuk mengkaji semula mana-mana peristiwa, ikut susunan ini: satelit (Bab 23) untuk sistem awan, radar (Bab 24) untuk pergerakan hujan, ensemble ECMWF (Bab 30) untuk berapa ahli menjangka hujan lebat, dan akhirnya amaran MetMalaysia (Bab 18) dan tolok.",
    src=["METMY-NEM2122"]),
 ]},
 ]}

quiz = [
 {"stage": 8, "chapter": "ch36", "q": T("2021 年 12 月 18 日马六甲海峡一带大雨，报告怎样解释？", "How does the review explain the heavy rain around the Strait of Malacca on 18 Dec 2021?", "Bagaimana kajian semula menerangkan hujan lebat di Selat Melaka pada 18 Dis 2021?"),
  "options": [T("东北风深入半岛，和西南风汇合", "North-east winds met south-west winds over the Peninsula", "Angin timur laut bertemu angin barat daya di Semenanjung"), T("一条苏门答腊飑线", "A single Sumatras", "Satu Sumatras"), T("热浪", "A heat wave", "Gelombang haba"), T("烟霾", "Haze", "Jerebu")],
  "answer": 0, "why": T("季风潮加上台风雷伊，让风在海峡一带汇合。", "The surge and Typhoon Rai brought converging winds over the strait.", "Luruan dan Taufan Rai membawa angin menumpu di atas selat.")},
 {"stage": 8, "chapter": "ch36", "q": T("为什么 ERA5 的格子雨量比气象站小很多？", "Why is ERA5's box rain so much less than the station's?", "Mengapa hujan kotak ERA5 jauh kurang daripada stesen?"),
  "options": [T("25 公里格子的平均把局部极端值抹平", "A 25 km box average smooths local extremes", "Purata kotak 25 km melicinkan ekstrem setempat"), T("气象站坏了", "The station broke", "Stesen rosak"), T("ERA5 不算雨", "ERA5 has no rain", "ERA5 tiada hujan"), T("那天没下雨", "It did not rain", "Tidak hujan")],
  "answer": 0, "why": T("格子平均不是雨量计。", "A box average is not a gauge.", "Purata kotak bukan tolok.")},
]

write_chapter(chapter, [], [], quiz)
