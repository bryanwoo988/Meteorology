"""Chapter 40 — Evapotranspiration and crop water."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch40", "num": 40, "stage": 9,
 "title": T("蒸散与作物需水", "Evapotranspiration and crop water", "Sejatpeluhan dan air tanaman"),
 "sources": ["FAO56", "PAM", "TERM", "ERA5-OM", "WINDY-OVERLAYS"],
 "sections": [
 {"id": "s1", "heading": T("蒸发、蒸腾和蒸散", "Evaporation, transpiration and evapotranspiration", "Penyejatan, transpirasi dan sejatpeluhan"), "level": "basic", "blocks": [
  P("水从土壤表面变成水汽跑掉是蒸发（第 5 章）；水从作物叶片的气孔散到空气里叫{{t:transpiration}}。两者加起来叫{{t:evapotranspiration}}。影响它的因素包括辐射、气温、风速、湿度、地表性质和地表有多少水。",
    "Water leaving the soil surface as vapour is evaporation (Chapter 5); water escaping from a crop's leaves through the stomata is {{t:transpiration}}. The two together are {{t:evapotranspiration}}. It depends on radiation, temperature, wind, humidity, the nature of the surface and how much water it holds.",
    "Air yang meninggalkan permukaan tanah sebagai wap ialah penyejatan (Bab 5); air yang keluar dari daun tanaman melalui stomata ialah {{t:transpiration}}. Kedua-duanya bersama ialah {{t:evapotranspiration}}. Ia bergantung pada sinaran, suhu, angin, kelembapan, sifat permukaan dan jumlah air yang ada.",
    defines=["transpiration", "evapotranspiration"], src=["FAO56", "PAM:146", "TERM:116"]),
 ]},
 {"id": "s2", "heading": T("ET₀：参考蒸散", "ET₀: reference evapotranspiration", "ET₀: sejatpeluhan rujukan"), "level": "basic", "blocks": [
  P("不同作物用水不同，所以先定一个标准：一片假想的、长得很好、水分充足、完全盖住地面的草地，高 0.12 米。这片草地的蒸散量叫{{t:et0}}，只由天气决定。FAO 推荐用 Penman–Monteith 公式从气象资料计算，单位是每天几毫米。",
    "Different crops use different amounts, so a standard comes first: an imaginary, extensive surface of green, well-watered grass 0.12 m tall that fully shades the ground. Its evapotranspiration is the {{t:et0}}, set by the weather alone. FAO recommends the Penman–Monteith equation to compute it from weather data, in millimetres a day.",
    "Tanaman berlainan menggunakan jumlah air berlainan, jadi piawai ditetapkan dahulu: permukaan rumput hijau khayalan yang luas, cukup air, setinggi 0.12 m dan meliputi tanah sepenuhnya. Sejatpeluhannya ialah {{t:et0}}, ditentukan oleh cuaca sahaja. FAO mengesyorkan persamaan Penman–Monteith untuk mengiranya daripada data cuaca, dalam milimeter sehari.",
    defines=["et0"], src=["FAO56"]),
  {"type": "widget", "id": "W23"},
  P("某种作物的用水，再乘上{{t:crop-coefficient}}：ETc = Kc × ET₀。Kc 由作物本身决定，而且从播种到收割会改变。",
    "A particular crop's water use is ET₀ times its {{t:crop-coefficient}}: ETc = Kc × ET₀. Kc depends on the crop and changes from sowing to harvest.",
    "Penggunaan air sesuatu tanaman ialah ET₀ didarab dengan {{t:crop-coefficient}}nya: ETc = Kc × ET₀. Kc bergantung pada tanaman dan berubah dari menyemai hingga menuai.",
    defines=["crop-coefficient"], src=["FAO56", "TERM:72"]),
 ]},
 {"id": "s3", "heading": T("雨量减去蒸散：吉隆坡 2025 年", "Rain minus evapotranspiration: Kuala Lumpur 2025", "Hujan tolak sejatpeluhan: Kuala Lumpur 2025"), "level": "basic", "blocks": [
  {"type": "chart", "src": ["ERA5-OM"], "chart": {"kind": "line", "series_file": "kl-et0-2025",
    "title": T("吉隆坡 2025 年：每月雨量和 ET₀", "Kuala Lumpur, 2025: monthly rain and ET₀", "Kuala Lumpur, 2025: hujan dan ET₀ bulanan"),
    "x": {"col": "month", "label": T("月份", "Month", "Bulan"), "format": "month"},
    "y": {"label": T("毫米", "Millimetres", "Milimeter"), "unit": "mm"},
    "series": [{"col": "rain", "name": T("雨量", "Rain", "Hujan"), "color": "rain"},
               {"col": "et0", "name": T("ET₀", "ET₀", "ET₀"), "color": "sun"}]}},
  P("一年加起来，吉隆坡 2025 年下了约 2,800 毫米雨，ET₀ 约 1,440 毫米，雨比蒸散多。但月份之间差很多：7 月 ET₀ 约 146 毫米，雨只有约 55 毫米，是缺水的月份；4 月和 11 月雨量超过 400 毫米，远多于蒸散。",
    "Over the year Kuala Lumpur had about 2,800 mm of rain in 2025 against an ET₀ of about 1,440 mm — more rain than evapotranspiration. Months differ widely, though: July's ET₀ was about 146 mm against only about 55 mm of rain, a water-short month, while April and November each had over 400 mm, far above evapotranspiration.",
    "Sepanjang tahun Kuala Lumpur menerima kira-kira 2,800 mm hujan pada 2025 berbanding ET₀ kira-kira 1,440 mm — lebih banyak hujan daripada sejatpeluhan. Namun bulan berbeza dengan ketara: ET₀ Julai kira-kira 146 mm berbanding hanya kira-kira 55 mm hujan, bulan kekurangan air, manakala April dan November masing-masing melebihi 400 mm, jauh di atas sejatpeluhan.",
    src=["ERA5-OM"]),
 ]},
 {"id": "s4", "heading": T("土壤湿度和水分距平", "Soil moisture and its anomaly", "Lembapan tanah dan anomalinya"), "level": "basic", "blocks": [
  P("Windy 的{{t:soil-moisture}}图层显示作物可用的水，以百分比表示：0 % 是凋萎点，100 % 是田间持水量；低于 50 % 时植物开始受水分限制，低于 30 % 时大多数植物会出现明显的缺水症状。另一个图层“水分距平”，则是和 1961–2010 年同期的平常水量比较，负数表示比平常少。",
    "Windy's {{t:soil-moisture}} layer shows the water available to plants as a percentage: 0 % is the wilting point and 100 % field capacity; below 50 % plants start to be limited by water, and below 30 % most show clear signs of stress. Its ‘moisture anomaly’ layer compares the water with the usual amount for the time of year in 1961–2010; negative means less than usual.",
    "Lapisan {{t:soil-moisture}} Windy menunjukkan air yang tersedia untuk tumbuhan sebagai peratusan: 0 % ialah takat layu dan 100 % kapasiti ladang; di bawah 50 % tumbuhan mula dihadkan oleh air, dan di bawah 30 % kebanyakannya menunjukkan tanda tekanan yang jelas. Lapisan ‘anomali lembapan’nya membandingkan air dengan jumlah biasa bagi masa itu dalam 1961–2010; negatif bermaksud kurang daripada biasa.",
    defines=["soil-moisture"], src=["WINDY-OVERLAYS"]),
 ]},
 ]}

terms = [
 ("transpiration", T("蒸腾", "Transpiration", "Transpirasi"), T("水从植物叶片的气孔散到空气中。", "Water lost to the air through a plant's stomata.", "Air yang hilang ke udara melalui stomata tumbuhan.")),
 ("evapotranspiration", T("蒸散", "Evapotranspiration", "Sejatpeluhan"), T("蒸发加蒸腾。", "Evaporation plus transpiration.", "Penyejatan ditambah transpirasi.")),
 ("et0", T("ET₀（参考蒸散量）", "ET₀ (reference evapotranspiration)", "ET₀ (sejatpeluhan rujukan)"), T("标准草地的蒸散，只由天气决定，单位毫米/天。", "Evapotranspiration of a standard grass surface, set by weather alone, in mm per day.", "Sejatpeluhan permukaan rumput piawai, ditentukan cuaca sahaja, dalam mm sehari.")),
 ("crop-coefficient", T("作物系数（Kc）", "Crop coefficient (Kc)", "Pekali tanaman (Kc)"), T("把 ET₀ 换算成某种作物用水的乘数：ETc = Kc × ET₀。", "The multiplier turning ET₀ into a crop's use: ETc = Kc × ET₀.", "Pengganda yang menukar ET₀ kepada penggunaan tanaman: ETc = Kc × ET₀.")),
 ("soil-moisture", T("土壤湿度", "Soil moisture", "Lembapan tanah"), T("土壤里作物可用的水；0 % 凋萎，100 % 田间持水量。", "Water in the soil available to plants; 0 % wilting point, 100 % field capacity.", "Air dalam tanah tersedia untuk tumbuhan; 0 % takat layu, 100 % kapasiti ladang.")),
]

sources = [
 {"id": "FAO56", "short": "FAO-56", "title": "Crop evapotranspiration — Guidelines for computing crop water requirements (FAO Irrigation and Drainage Paper 56)", "publisher": "R. G. Allen, L. S. Pereira, D. Raes and M. Smith, FAO, 1998", "url": "https://www.fao.org/4/x0490e/x0490e00.htm", "accessed": "2026-10-03"},
]

quiz = [
 {"stage": 9, "chapter": "ch40", "q": T("ET₀ 是什么的蒸散？", "ET₀ is the evapotranspiration of…", "ET₀ ialah sejatpeluhan…"),
  "options": [T("一片标准的、水分充足的草地", "A standard, well-watered grass surface", "Permukaan rumput piawai yang cukup air"), T("你种的作物", "Your own crop", "Tanaman anda"), T("一个水池", "A pond", "Sebuah kolam"), T("沙漠", "A desert", "Gurun")],
  "answer": 0, "why": T("再乘上作物系数 Kc，才是某种作物的用水。", "Multiply by the crop coefficient for a given crop.", "Darab dengan pekali tanaman bagi tanaman tertentu.")},
 {"stage": 9, "chapter": "ch40", "q": T("吉隆坡 2025 年哪个月最缺水？", "Which month of 2025 was most water-short in Kuala Lumpur?", "Bulan mana pada 2025 paling kekurangan air di Kuala Lumpur?"),
  "options": [T("7 月", "July", "Julai"), T("4 月", "April", "April"), T("11 月", "November", "November"), T("12 月", "December", "Disember")],
  "answer": 0, "why": T("ET₀ 约 146 毫米，雨只有约 55 毫米。", "ET₀ about 146 mm against only about 55 mm of rain.", "ET₀ kira-kira 146 mm berbanding hanya kira-kira 55 mm hujan.")},
]

write_chapter(chapter, terms, sources, quiz)
