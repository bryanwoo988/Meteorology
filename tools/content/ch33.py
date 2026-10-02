"""Chapter 33 — Other models and multi-model ensembles."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch33", "num": 33, "stage": 8,
 "title": T("其他主要模型与多模型集合", "Other major models and multi-model ensembles", "Model utama lain dan ensemble pelbagai model"),
 "sources": ["OM-ENS", "OM-DOCS", "NOAA-EMC-GEFS", "METMY-TN0122", "FUN", "ESS"],
 "sections": [
 {"id": "s1", "heading": T("全世界的主要集合预报", "The world's main ensembles", "Ensemble utama dunia"), "level": "basic", "blocks": [
  P("除了 ECMWF，很多国家的气象机构也跑自己的全球模型和集合预报。美国 NOAA 的全球模型叫 {{t:gfs}}，它的集合预报叫 {{t:gefs}}；德国气象局（DWD）的叫 {{t:icon}}；英国气象局有 UKMO 的全球模型和 MOGREPS-G 集合；加拿大的是 GEM。",
    "Besides ECMWF, many national weather services run their own global models and ensembles. NOAA's global model is the {{t:gfs}}, and its ensemble the {{t:gefs}}; Germany's DWD runs {{t:icon}}; the UK Met Office has its global UKMO model and the MOGREPS-G ensemble; Canada runs GEM.",
    "Selain ECMWF, banyak perkhidmatan cuaca negara menjalankan model global dan ensemble sendiri. Model global NOAA ialah {{t:gfs}}, dan ensemblenya {{t:gefs}}; DWD Jerman menjalankan {{t:icon}}; Pejabat Met UK mempunyai model global UKMO dan ensemble MOGREPS-G; Kanada menjalankan GEM.",
    defines=["gfs", "gefs", "icon"], src=["OM-ENS", "OM-DOCS", "NOAA-EMC-GEFS"]),
  {"type": "table", "src": ["OM-ENS"],
   "caption": T("几个全球集合预报（Open-Meteo 资料表，2026 年 10 月）", "Some global ensembles (Open-Meteo data table, October 2026)", "Beberapa ensemble global (jadual data Open-Meteo, Oktober 2026)"),
   "headers": [T("集合", "Ensemble", "Ensemble"), T("机构", "Centre", "Pusat"), T("格距", "Spacing", "Jarak"), T("成员", "Members", "Ahli"), T("预报长度", "Length", "Tempoh")],
   "rows": [[T("ECMWF IFS ENS（开放资料）", "ECMWF IFS ENS (open data)", "ECMWF IFS ENS (data terbuka)"), T("ECMWF", "ECMWF", "ECMWF"), T("0.25°（约 25 km）", "0.25° (~25 km)", "0.25° (~25 km)"), T("51", "51", "51"), T("15 天", "15 days", "15 hari")],
            [T("GFS Ensemble（GEFS）", "GFS Ensemble (GEFS)", "GFS Ensemble (GEFS)"), T("NOAA（美国）", "NOAA (US)", "NOAA (AS)"), T("0.25°（约 25 km）", "0.25° (~25 km)", "0.25° (~25 km)"), T("31", "31", "31"), T("10 天", "10 days", "10 hari")],
            [T("ICON-EPS", "ICON-EPS", "ICON-EPS"), T("DWD（德国）", "DWD (Germany)", "DWD (Jerman)"), T("26 km", "26 km", "26 km"), T("40", "40", "40"), T("7.5 天", "7.5 days", "7.5 hari")],
            [T("MOGREPS-G", "MOGREPS-G", "MOGREPS-G"), T("英国气象局", "UK Met Office", "Pejabat Met UK"), T("20 km", "20 km", "20 km"), T("18", "18", "18"), T("8 天", "8 days", "8 hari")],
            [T("GEM Global Ensemble", "GEM Global Ensemble", "GEM Global Ensemble"), T("加拿大气象局", "Canadian Weather Service", "Perkhidmatan Cuaca Kanada"), T("0.25°（约 25 km）", "0.25° (~25 km)", "0.25° (~25 km)"), T("21", "21", "21"), T("16 天", "16 days", "16 hari")]]},
  N("tip", "大马气象局自己的 WRF 区域模型，起点和边界用的就是 NOAA 的 GFS（第 27 章）。",
    "MetMalaysia's own WRF regional model takes its start and boundaries from NOAA's GFS (Chapter 27).",
    "Model serantau WRF MetMalaysia sendiri mengambil titik mula dan sempadannya daripada GFS NOAA (Bab 27).",
    src=["METMY-TN0122"]),
 ]},
 {"id": "s2", "heading": T("多模型集合", "Multi-model ensembles", "Ensemble pelbagai model"), "level": "basic", "blocks": [
  P("每个模型都有自己的强项和毛病，好的预报员熟悉每个模型的习性。把几个不同机构的模型放在一起比较，叫{{t:multi-model-ensemble}}。研究显示，这样通常比只看一个模型好；先修正各模型的偏差再结合，误差还会更小。",
    "Every model has its strengths and quirks, and a good forecaster knows each one's habits. Setting several centres' models side by side is a {{t:multi-model-ensemble}}; it has been shown to beat a single model, and correcting each model's biases before combining reduces the errors further.",
    "Setiap model mempunyai kekuatan dan keanehan sendiri, dan peramal yang baik mengetahui tabiat setiap satu. Meletakkan model beberapa pusat bersebelahan ialah {{t:multi-model-ensemble}}; ia terbukti mengatasi satu model, dan membetulkan bias setiap model sebelum digabungkan mengurangkan ralat lagi.",
    defines=["multi-model-ensemble"], src=["FUN:129", "ESS:255"]),
  N("key", "练习：在 CompareCast 里选同一个地点，把 ECMWF、GFS、ICON 等模型的雨量放在一起看。它们都一样时比较可信；各说各话时，就要看集合和概率，不要只挑一个喜欢的答案。",
    "Practice: in CompareCast, pick one place and set the rain from ECMWF, GFS, ICON and others side by side. When they agree, trust rises; when each tells a different story, turn to the ensembles and probabilities rather than picking the answer you like.",
    "Latihan: dalam CompareCast, pilih satu tempat dan letakkan hujan dari ECMWF, GFS, ICON dan lain-lain bersebelahan. Apabila bersetuju, keyakinan meningkat; apabila masing-masing berbeza, beralih kepada ensemble dan kebarangkalian dan bukannya memilih jawapan yang anda suka.",
    src=["FUN:129", "ESS:257"]),
 ]},
 ]}

terms = [
 ("gfs", T("GFS", "GFS", "GFS"), T("美国 NOAA 的全球预报模型。", "NOAA's Global Forecast System.", "Sistem Ramalan Global NOAA.")),
 ("gefs", T("GEFS", "GEFS", "GEFS"), T("GFS 的集合预报，31 个成员。", "The GFS ensemble, 31 members.", "Ensemble GFS, 31 ahli.")),
 ("icon", T("ICON", "ICON", "ICON"), T("德国气象局（DWD）的模型。", "The German Weather Service's model.", "Model Perkhidmatan Cuaca Jerman.")),
 ("multi-model-ensemble", T("多模型集合", "Multi-model ensemble", "Ensemble pelbagai model"), T("把几个不同机构的模型放在一起比较或结合。", "Comparing or combining models from several centres.", "Membanding atau menggabungkan model dari beberapa pusat.")),
]

sources = [
 {"id": "OM-DOCS", "short": "Open-Meteo", "title": "Weather forecast API — data sources (national weather services, resolutions and forecast lengths)", "publisher": "Open-Meteo", "url": "https://open-meteo.com/en/docs", "accessed": "2026-10-03"},
]

quiz = [
 {"stage": 8, "chapter": "ch33", "q": T("GEFS 有几个成员？", "How many members does GEFS have?", "Berapa ahli GEFS?"),
  "options": [T("31", "31", "31"), T("51", "51", "51"), T("1", "1", "1"), T("101", "101", "101")],
  "answer": 0, "why": T("ECMWF 的 ENS 是 51 个。", "ECMWF's ENS has 51.", "ENS ECMWF ada 51.")},
 {"stage": 8, "chapter": "ch33", "q": T("几个模型各说各话时，最好怎么做？", "When the models disagree, what is best?", "Apabila model tidak bersetuju, apa yang terbaik?"),
  "options": [T("看集合和概率，不只挑一个", "Look at ensembles and probabilities, not one favourite", "Lihat ensemble dan kebarangkalian, bukan satu kegemaran"), T("挑最好听的", "Pick the nicest", "Pilih yang paling sedap didengar"), T("永远只看 GFS", "Always use GFS", "Sentiasa guna GFS"), T("不理预报", "Ignore forecasts", "Abaikan ramalan")],
  "answer": 0, "why": T("意见不一表示不确定性大。", "Disagreement means high uncertainty.", "Tidak sependapat bermaksud ketidakpastian tinggi.")},
]

write_chapter(chapter, terms, sources, quiz)
