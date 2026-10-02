"""Chapter 31 — Reanalysis and seasonal forecasts."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch31", "num": 31, "stage": 8,
 "title": T("再分析与季节预报", "Reanalysis and seasonal forecasts", "Analisis semula dan ramalan bermusim"),
 "sources": ["CDS-ERA5", "ERA5-OM", "ECMWF-SEASONAL", "NOAA-CPC-DISC", "MET-ENSO-STATUS"],
 "sections": [
 {"id": "s1", "heading": T("ERA5：把过去重新算一遍", "ERA5: recomputing the past", "ERA5: mengira semula masa lalu"), "level": "basic", "blocks": [
  P("{{t:reanalysis}}用和天气预报一样的数据同化方法（第 27 章），把过去几十年的观测重新喂进同一个模型，算出一套完整、前后一致的历史天气。它不用赶着发布，所以有时间收集更多观测，也能用改进过的旧资料。ERA5 是 ECMWF 第五代再分析，从 1940 年到现在、逐时，还附有 10 个成员的不确定性估计。",
    "A {{t:reanalysis}} uses the same data assimilation as forecasting (Chapter 27), feeding decades of past observations into one model to produce a complete, consistent record of past weather. It has no deadline, so it can gather more observations and use improved versions of old ones. ERA5, ECMWF's fifth-generation reanalysis, runs from 1940 to the present, hourly, with a 10-member estimate of its uncertainty.",
    "{{t:reanalysis}} menggunakan asimilasi data yang sama seperti ramalan (Bab 27), memasukkan cerapan berdekad-dekad ke dalam satu model untuk menghasilkan rekod cuaca lalu yang lengkap dan konsisten. Ia tiada tarikh akhir, jadi ia boleh mengumpul lebih banyak cerapan dan menggunakan versi lama yang diperbaiki. ERA5, analisis semula generasi kelima ECMWF, dari 1940 hingga kini, setiap jam, dengan anggaran ketidakpastian 10 ahli.",
    defines=["reanalysis"], src=["CDS-ERA5"]),
  P("这本书很多吉隆坡的图表（第 4、5、15、16、35 章）都用 ERA5。它的好处是任何地点、任何时间都有资料；限制是它代表约 25 公里一格的平均，而不是一个雨量计，所以局部的大雨和小雨日的次数都会和气象站不同（第 15 章）。",
    "Many of this book's Kuala Lumpur charts (Chapters 4, 5, 15, 16 and 35) use ERA5. Its strength is data for any place at any time; its limit is that it represents an average over a box about 25 km across, not a rain gauge, so local downpours and the count of light-rain days differ from a station's (Chapter 15).",
    "Banyak carta Kuala Lumpur dalam buku ini (Bab 4, 5, 15, 16 dan 35) menggunakan ERA5. Kekuatannya ialah data untuk mana-mana tempat pada bila-bila masa; hadnya ialah ia mewakili purata kotak kira-kira 25 km, bukan tolok hujan, jadi hujan lebat setempat dan kiraan hari hujan renyai berbeza daripada stesen (Bab 15).",
    src=["ERA5-OM", "CDS-ERA5"]),
 ]},
 {"id": "s2", "heading": T("季节预报和 ENSO 展望", "Seasonal forecasts and the ENSO outlook", "Ramalan bermusim dan tinjauan ENSO"), "level": "basic", "blocks": [
  P("{{t:seasonal-forecast}}不预报哪一天下雨，而是预报未来几个月平均起来比平常偏高、正常还是偏低的概率。它靠的是变化很慢的东西，最重要的就是厄尔尼诺和拉尼娜。ECMWF 的 SEAS5 每月发布一次，51 个成员，预报到 7 个月。",
    "A {{t:seasonal-forecast}} does not say which day it will rain; it gives the chances that the coming months, on average, will be above, near or below normal. It relies on things that change slowly — above all El Niño and La Niña. ECMWF's SEAS5 is issued monthly with 51 members, out to 7 months.",
    "{{t:seasonal-forecast}} tidak menyatakan hari mana hujan akan turun; ia memberi peluang bahawa bulan-bulan akan datang, secara purata, di atas, hampir atau di bawah normal. Ia bergantung pada perkara yang berubah perlahan — terutamanya El Niño dan La Niña. SEAS5 ECMWF dikeluarkan setiap bulan dengan 51 ahli, hingga 7 bulan.",
    defines=["seasonal-forecast"], src=["ECMWF-SEASONAL"]),
  P("美国 NOAA 气候预测中心每月第二个星期四左右发布 {{t:enso-outlook}}。2026 年 9 月 10 日那一期的状态是“厄尔尼诺警报（El Niño Advisory）”，说厄尔尼诺正在加强，北半球秋冬（2026–27）出现非常强事件的机会超过 90 %；Niño 3.4 区 8 月的距平是 +1.8 °C。",
    "The US NOAA Climate Prediction Center issues its monthly {{t:enso-outlook}}. The issue of 10 September 2026 carried the status ‘El Niño Advisory’: El Niño is strengthening, with a greater than 90 % chance of a very strong event during the northern autumn and winter 2026–27; the Niño 3.4 anomaly for August was +1.8 °C.",
    "Pusat Ramalan Iklim NOAA AS mengeluarkan {{t:enso-outlook}} bulanan. Keluaran 10 September 2026 membawa status ‘El Niño Advisory’: El Niño sedang menguat, dengan peluang lebih 90 % bagi peristiwa sangat kuat semasa musim luruh dan sejuk utara 2026–27; anomali Niño 3.4 bagi Ogos ialah +1.8 °C.",
    defines=["enso-outlook"], src=["NOAA-CPC-DISC"]),
  N("key", "把它和第 14、19 章连起来：大马气象局 9 月 15 日的 ENSO 状态预计厄尔尼诺持续到 2027 年 5 月，东北季风结束后（2027 年 1–5 月）可能有极端干热的天气。季节预报就是用来提前准备这种情况的。",
    "Link this to Chapters 14 and 19: MetMalaysia's ENSO status of 15 September expects El Niño to last until May 2027, with extreme hot, dry weather possible after the north-east monsoon, January to May 2027. Seasonal forecasts exist to prepare for exactly this.",
    "Kaitkan ini dengan Bab 14 dan 19: status ENSO MetMalaysia pada 15 September menjangkakan El Niño berterusan hingga Mei 2027, dengan cuaca kering dan panas ekstrem mungkin selepas monsun timur laut, Januari hingga Mei 2027. Ramalan bermusim wujud untuk bersedia bagi keadaan sebegini.",
    src=["MET-ENSO-STATUS"]),
 ]},
 ]}

terms = [
 ("reanalysis", T("再分析", "Reanalysis", "Analisis semula"), T("用同一个模型和数据同化，把过去几十年的天气重新算一遍。", "Recomputing decades of past weather with one model and data assimilation.", "Mengira semula cuaca berdekad-dekad dengan satu model dan asimilasi data.")),
 ("seasonal-forecast", T("季节预报", "Seasonal forecast", "Ramalan bermusim"), T("预报未来几个月平均偏高、正常或偏低的概率。", "Chances that the coming months average above, near or below normal.", "Peluang bulan-bulan akan datang berpurata di atas, hampir atau di bawah normal.")),
 ("enso-outlook", T("ENSO 展望", "ENSO outlook", "Tinjauan ENSO"), T("NOAA 等机构每月发布的厄尔尼诺/拉尼娜现况和概率预报。", "The monthly status and probability forecast of El Niño/La Niña from NOAA and others.", "Status dan ramalan kebarangkalian El Niño/La Niña bulanan daripada NOAA dan lain-lain.")),
]

sources = [
 {"id": "NOAA-CPC-DISC", "short": "NOAA CPC", "title": "ENSO Diagnostic Discussion, 10 September 2026", "publisher": "NOAA Climate Prediction Center", "url": "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml", "accessed": "2026-10-03"},
]

quiz = [
 {"stage": 8, "chapter": "ch31", "q": T("再分析和天气预报最大的不同是什么？", "What most separates a reanalysis from a forecast?", "Apakah perbezaan utama analisis semula dan ramalan?"),
  "options": [T("再分析重算过去，没有发布的期限", "A reanalysis recomputes the past with no deadline", "Analisis semula mengira semula masa lalu tanpa tarikh akhir"), T("再分析预报未来 46 天", "It forecasts 46 days ahead", "Ia meramal 46 hari"), T("再分析不用模型", "It uses no model", "Ia tidak menggunakan model"), T("再分析只用雷达", "It uses only radar", "Ia hanya menggunakan radar")],
  "answer": 0, "why": T("它用同样的同化方法，但有更多时间收集观测。", "Same assimilation, more time to gather observations.", "Asimilasi sama, lebih masa untuk mengumpul cerapan.")},
 {"stage": 8, "chapter": "ch31", "q": T("季节预报会告诉你什么？", "What does a seasonal forecast tell you?", "Apakah yang diberitahu oleh ramalan bermusim?"),
  "options": [T("未来几个月偏干或偏湿的概率", "The chances of the coming months being drier or wetter", "Peluang bulan-bulan akan datang lebih kering atau basah"), T("下个星期三会不会下雨", "Whether next Wednesday is wet", "Sama ada Rabu depan hujan"), T("明天几点下雨", "What time it rains tomorrow", "Pukul berapa hujan esok"), T("今天的风速", "Today's wind speed", "Kelajuan angin hari ini")],
  "answer": 0, "why": T("它说的是几个月平均的倾向，不是哪一天。", "It speaks of months on average, not days.", "Ia tentang purata bulanan, bukan hari.")},
]

write_chapter(chapter, terms, sources, quiz)
