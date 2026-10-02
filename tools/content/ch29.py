"""Chapter 29 — Getting to know ECMWF."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch29", "num": 29, "stage": 8,
 "title": T("认识 ECMWF", "Getting to know ECMWF", "Mengenali ECMWF"),
 "sources": ["ECMWF-WHO", "CAMS-ABOUT", "ECMWF-MEDIUM", "ECMWF-SUBSEAS", "ECMWF-SEASONAL", "ECMWF-AIFS", "ECMWF-OPEN", "CDS-ERA5", "GLOFAS", "FUN"],
 "sections": [
 {"id": "s1", "heading": T("ECMWF 是什么", "What ECMWF is", "Apakah ECMWF"), "level": "basic", "blocks": [
  P("{{t:ecmwf}}（欧洲中期天气预报中心）在 1975 年成立，是一个独立的政府间组织，由 35 个国家支持，在英国 Reading、意大利 Bologna 和德国 Bonn 都有据点。它既是研究机构，也是全天候运作的预报中心，把数值预报交给成员国的气象局使用。ECMWF 和美国 NCEP 从 1992 年起率先把集合预报用在日常预报上。",
    "{{t:ecmwf}}, the European Centre for Medium-Range Weather Forecasts, was founded in 1975: an independent intergovernmental organisation supported by 35 states, with sites in Reading (UK), Bologna (Italy) and Bonn (Germany). It is both a research institute and a 24/7 operational service, producing numerical forecasts for its member states' weather services. With the US NCEP, ECMWF pioneered operational ensemble forecasts from 1992.",
    "{{t:ecmwf}}, Pusat Ramalan Cuaca Jarak Sederhana Eropah, ditubuhkan pada 1975: organisasi antara kerajaan bebas yang disokong oleh 35 negara, dengan tapak di Reading (UK), Bologna (Itali) dan Bonn (Jerman). Ia institut penyelidikan dan juga perkhidmatan operasi 24/7, menghasilkan ramalan berangka untuk perkhidmatan cuaca negara anggotanya. Bersama NCEP AS, ECMWF mempelopori ramalan ensemble operasi dari 1992.",
    defines=["ecmwf"], src=["ECMWF-WHO", "CAMS-ABOUT", "FUN:128"]),
  P("它的预报模型叫{{t:ifs}}（综合预报系统）。中期预报每天从 00 和 12 UTC 的初始场各跑一次，另有从 06 和 18 UTC 出发的较短补充预报。换成马来西亚时间：00 UTC 是早上 8 点、06 UTC 是下午 2 点、12 UTC 是晚上 8 点、18 UTC 是凌晨 2 点；预报要过几个小时才发布。",
    "Its forecasting model is the {{t:ifs}}, the Integrated Forecasting System. Medium-range forecasts start from 00 and 12 UTC each day, with shorter supplementary runs from 06 and 18 UTC. In Malaysian time, 00 UTC is 8 am, 06 UTC 2 pm, 12 UTC 8 pm and 18 UTC 2 am; the forecasts become available a few hours later.",
    "Model ramalannya ialah {{t:ifs}}, Sistem Ramalan Bersepadu. Ramalan jarak sederhana bermula dari 00 dan 12 UTC setiap hari, dengan larian tambahan lebih pendek dari 06 dan 18 UTC. Dalam waktu Malaysia, 00 UTC ialah 8 pagi, 06 UTC 2 petang, 12 UTC 8 malam dan 18 UTC 2 pagi; ramalan tersedia beberapa jam kemudian.",
    defines=["ifs"], src=["ECMWF-MEDIUM"]),
 ]},
 {"id": "s2", "heading": T("产品家族：从几天到几个月", "The product family: days to months", "Keluarga produk: hari hingga bulan"), "level": "basic", "blocks": [
  {"type": "widget", "id": "W25"},
  L(("{{t:ens}}：51 个成员、约 9 公里，预报到 15 天", "{{t:ens}}: 51 members at about 9 km, out to 15 days", "{{t:ens}}: 51 ahli pada kira-kira 9 km, hingga 15 hari"),
    ("次季节预报：每天一次、约 36 公里，预报到 46 天，看每星期比平常偏暖偏湿还是偏冷偏干", "Sub-seasonal: daily at about 36 km to 46 days, showing whether each week is warmer, wetter, cooler or drier than normal", "Sub-musim: harian pada kira-kira 36 km hingga 46 hari, menunjukkan sama ada setiap minggu lebih panas, basah, sejuk atau kering daripada biasa"),
    ("{{t:seas5}} 季节预报：每月一次、51 个成员、约 36 公里，预报到 7 个月；每三个月再延长到 13 个月", "{{t:seas5}} seasonal: monthly, 51 members at about 36 km, out to 7 months; every three months extended to 13 months", "Bermusim {{t:seas5}}: bulanan, 51 ahli pada kira-kira 36 km, hingga 7 bulan; setiap tiga bulan dilanjutkan ke 13 bulan"),
    ("ERA5 再分析：1940 年到现在，逐时（第 31 章）", "ERA5 reanalysis: 1940 to the present, hourly (Chapter 31)", "Analisis semula ERA5: 1940 hingga kini, setiap jam (Bab 31)"),
    ("{{t:cams}}：空气污染、气溶胶和温室气体的资料与预报", "{{t:cams}}: information and forecasts of air pollution, aerosols and greenhouse gases", "{{t:cams}}: maklumat dan ramalan pencemaran udara, aerosol dan gas rumah hijau"),
    ("{{t:glofas}}：把 ECMWF 的集合预报喂进水文模型，预报河流流量到 30 天", "{{t:glofas}}: ECMWF ensemble forecasts fed into a hydrological model to forecast river flow out to 30 days", "{{t:glofas}}: ramalan ensemble ECMWF dimasukkan ke model hidrologi untuk meramal aliran sungai hingga 30 hari"),
    ("AIFS：ECMWF 的人工智能模型，2025 年起正式运作（第 32 章）", "AIFS: ECMWF's artificial-intelligence model, operational since 2025 (Chapter 32)", "AIFS: model kecerdasan buatan ECMWF, beroperasi sejak 2025 (Bab 32)"),
    defines=["ens", "seas5", "cams", "glofas"], src=["ECMWF-MEDIUM", "ECMWF-SUBSEAS", "ECMWF-SEASONAL", "CDS-ERA5", "CAMS-ABOUT", "GLOFAS", "ECMWF-AIFS"]),
 ]},
 {"id": "s3", "heading": T("开放数据", "Open data", "Data terbuka"), "level": "basic", "blocks": [
  P("ECMWF 把一部分即时预报资料（IFS 和 AIFS）免费公开，使用 CC BY 4.0 授权：可以转载，也可以商业使用，只要注明出处。这就是 Open-Meteo、Windy 之类的网站能免费显示 ECMWF 预报的原因；本书第 30 章的吉隆坡 EPSgram 用的也是这批开放资料。",
    "ECMWF makes a subset of its real-time forecast data, from both IFS and AIFS, free and open under the CC BY 4.0 licence: it may be redistributed and used commercially as long as it is credited. That is why sites such as Open-Meteo and Windy can show ECMWF forecasts free of charge — and the Kuala Lumpur EPSgram in Chapter 30 uses these open data too.",
    "ECMWF menjadikan sebahagian data ramalan masa nyatanya, dari IFS dan AIFS, percuma dan terbuka di bawah lesen CC BY 4.0: ia boleh diedarkan semula dan digunakan secara komersial asalkan dikreditkan. Itulah sebabnya laman seperti Open-Meteo dan Windy boleh memaparkan ramalan ECMWF secara percuma — dan EPSgram Kuala Lumpur dalam Bab 30 juga menggunakan data terbuka ini.",
    src=["ECMWF-OPEN"]),
  {"type": "dataset", "id": "ecmwf-open"},
 ]},
 ]}

terms = [
 ("ecmwf", T("ECMWF（欧洲中期天气预报中心）", "ECMWF", "ECMWF"), T("1975 年成立的欧洲政府间预报中心，以中期和集合预报闻名。", "The European intergovernmental forecast centre founded in 1975, known for medium-range and ensemble forecasts.", "Pusat ramalan antara kerajaan Eropah yang ditubuhkan 1975, terkenal dengan ramalan jarak sederhana dan ensemble.")),
 ("ifs", T("IFS（综合预报系统）", "IFS (Integrated Forecasting System)", "IFS (Sistem Ramalan Bersepadu)"), T("ECMWF 的物理数值预报模型。", "ECMWF's physics-based forecast model.", "Model ramalan berasaskan fizik ECMWF.")),
 ("ens", T("ENS（ECMWF 集合预报）", "ENS (ECMWF ensemble)", "ENS (ensemble ECMWF)"), T("ECMWF 的 51 成员、约 9 公里、15 天集合预报。", "ECMWF's 51-member, ~9 km, 15-day ensemble.", "Ensemble ECMWF 51 ahli, ~9 km, 15 hari.")),
 ("seas5", T("SEAS5 季节预报", "SEAS5", "SEAS5"), T("ECMWF 的季节预报系统，每月一次、到 7 个月。", "ECMWF's seasonal forecast system: monthly, to 7 months.", "Sistem ramalan bermusim ECMWF: bulanan, hingga 7 bulan.")),
 ("cams", T("CAMS（哥白尼大气监测服务）", "CAMS", "CAMS"), T("由 ECMWF 运作，提供空气污染、气溶胶和温室气体资料与预报。", "Run by ECMWF: air pollution, aerosol and greenhouse-gas data and forecasts.", "Dikendalikan ECMWF: data dan ramalan pencemaran udara, aerosol dan gas rumah hijau.")),
 ("glofas", T("GloFAS（全球洪水预警系统）", "GloFAS", "GloFAS"), T("用 ECMWF 集合预报推算河流流量，预报到 30 天。", "River-flow forecasts to 30 days driven by ECMWF ensembles.", "Ramalan aliran sungai hingga 30 hari dipacu ensemble ECMWF.")),
]

sources = [
 {"id": "CAMS-ABOUT", "short": "Copernicus CAMS", "title": "About the Copernicus Atmosphere Monitoring Service", "publisher": "Copernicus / ECMWF", "url": "https://atmosphere.copernicus.eu/about-us", "accessed": "2026-10-03"},
 {"id": "ECMWF-SUBSEAS", "short": "ECMWF", "title": "Sub-seasonal-range forecasts", "publisher": "European Centre for Medium-Range Weather Forecasts", "url": "https://www.ecmwf.int/en/forecasts/documentation-and-support/extended-range-forecasts", "accessed": "2026-10-03"},
 {"id": "ECMWF-SEASONAL", "short": "ECMWF", "title": "Seasonal forecasts", "publisher": "European Centre for Medium-Range Weather Forecasts", "url": "https://www.ecmwf.int/en/forecasts/documentation-and-support/long-range", "accessed": "2026-10-03"},
 {"id": "ECMWF-AIFS", "short": "ECMWF", "title": "AIFS Machine Learning data", "publisher": "European Centre for Medium-Range Weather Forecasts", "url": "https://www.ecmwf.int/en/forecasts/dataset/aifs-machine-learning-data", "accessed": "2026-10-03"},
 {"id": "ECMWF-OPEN", "short": "ECMWF", "title": "Open data (IFS and AIFS real-time subset, CC BY 4.0)", "publisher": "European Centre for Medium-Range Weather Forecasts", "url": "https://www.ecmwf.int/en/forecasts/datasets/open-data", "accessed": "2026-10-03"},
 {"id": "GLOFAS", "short": "Copernicus EWDS", "title": "River discharge and related forecasted data by the Global Flood Awareness System", "publisher": "Copernicus Emergency Management Service", "url": "https://ewds.climate.copernicus.eu/datasets/cems-glofas-forecast", "accessed": "2026-10-03"},
]

datasets = [
 {"id": "ecmwf-open", "name": "ECMWF open data (IFS and AIFS)", "provider": "ECMWF",
  "what": T("ECMWF 免费公开的一部分即时预报：IFS 中期预报（control 和集合）、AIFS 的单一和集合预报，0.25° 网格，GRIB2 档案。", "The free subset of ECMWF's real-time forecasts — IFS medium-range control and ensemble, AIFS single and ensemble — on a 0.25° grid as GRIB2 files.", "Subset percuma ramalan masa nyata ECMWF — kawalan dan ensemble jarak sederhana IFS, AIFS tunggal dan ensemble — pada grid 0.25° sebagai fail GRIB2."),
  "resolution": "0.25°", "update": T("每天 4 次（00、06、12、18 UTC）", "Four times a day (00, 06, 12, 18 UTC)", "Empat kali sehari (00, 06, 12, 18 UTC)"), "format": "GRIB2",
  "licence": {"text": "CC BY 4.0 + ECMWF Terms of Use", "url": "https://www.ecmwf.int/en/forecasts/datasets/open-data"},
  "params": [{"raw": "2t", "meaning": T("2 米气温", "2 m temperature", "Suhu 2 m"), "unit": "K", "chapter": 4},
             {"raw": "tp", "meaning": T("累积总降水", "Total precipitation (accumulated)", "Jumlah kerpasan (terkumpul)"), "unit": "m", "chapter": 30},
             {"raw": "10u / 10v", "meaning": T("10 米风的东西、南北分量", "10 m wind components (east, north)", "Komponen angin 10 m (timur, utara)"), "unit": "m/s", "chapter": 9}],
  "sample": {"columns": ["date", "member", "tmax (°C)", "rain (mm)"], "rows": [["2026-10-03", "control", "32.0", "8.1"], ["2026-10-03", "member 1", "31.5", "2.7"], ["2026-10-03", "member 2", "31.2", "5.4"]], "source": "ENS for Kuala Lumpur via Open-Meteo, daily values computed from hourly data", "fetched": "2026-10-03"},
  "links": [
   {"level": "view", "label": T("ECMWF 预报图（opencharts）", "ECMWF forecast charts (opencharts)", "Carta ramalan ECMWF (opencharts)"), "url": "https://charts.ecmwf.int/"},
   {"level": "try", "label": T("用 Open-Meteo 取吉隆坡的 51 个成员（JSON）", "Fetch Kuala Lumpur's 51 members via Open-Meteo (JSON)", "Ambil 51 ahli Kuala Lumpur melalui Open-Meteo (JSON)"), "url": "https://ensemble-api.open-meteo.com/v1/ensemble?latitude=3.139&longitude=101.6869&hourly=temperature_2m,precipitation&models=ecmwf_ifs025&forecast_days=15&timezone=Asia%2FKuala_Lumpur"},
   {"level": "pro", "label": T("ECMWF 开放数据说明", "ECMWF open-data page", "Halaman data terbuka ECMWF"), "url": "https://www.ecmwf.int/en/forecasts/datasets/open-data",
    "note": T("用 Python 的 ecmwf-opendata 套件下载 GRIB2。", "Download GRIB2 with the Python package ecmwf-opendata.", "Muat turun GRIB2 dengan pakej Python ecmwf-opendata.")}]},
]

quiz = [
 {"stage": 8, "chapter": "ch29", "q": T("ECMWF 12 UTC 的预报，起点是马来西亚几点？", "ECMWF's 12 UTC run starts at what time in Malaysia?", "Larian 12 UTC ECMWF bermula pada pukul berapa di Malaysia?"),
  "options": [T("晚上 8 点", "8 pm", "8 malam"), T("中午 12 点", "Noon", "Tengah hari"), T("早上 4 点", "4 am", "4 pagi"), T("下午 2 点", "2 pm", "2 petang")],
  "answer": 0, "why": T("马来西亚比 UTC 快 8 小时。", "Malaysia is UTC+8.", "Malaysia ialah UTC+8.")},
 {"stage": 8, "chapter": "ch29", "q": T("想知道未来 3 个月会不会比平常干，看哪个产品？", "To see whether the next 3 months will be drier than normal, which product?", "Untuk melihat sama ada 3 bulan akan datang lebih kering daripada biasa, produk mana?"),
  "options": [T("SEAS5 季节预报", "SEAS5 seasonal forecast", "Ramalan bermusim SEAS5"), T("雷达", "Radar", "Radar"), T("ENS 第 1 天", "ENS day 1", "ENS hari 1"), T("ERA5", "ERA5", "ERA5")],
  "answer": 0, "why": T("季节预报给的是偏高、正常、偏低的概率。", "Seasonal forecasts give chances of above, near or below normal.", "Ramalan bermusim memberi peluang di atas, hampir atau di bawah normal.")},
 {"stage": 8, "chapter": "ch29", "q": T("为什么 Windy 可以免费显示 ECMWF 的预报？", "Why can Windy show ECMWF forecasts free?", "Mengapa Windy boleh memaparkan ramalan ECMWF secara percuma?"),
  "options": [T("ECMWF 用 CC BY 4.0 开放了一部分资料", "ECMWF opened a subset under CC BY 4.0", "ECMWF membuka subset di bawah CC BY 4.0"), T("Windy 自己跑 ECMWF 模型", "Windy runs the ECMWF model itself", "Windy menjalankan model ECMWF sendiri"), T("资料是偷来的", "It is pirated", "Ia cetak rompak"), T("ECMWF 属于 Windy", "ECMWF belongs to Windy", "ECMWF milik Windy")],
  "answer": 0, "why": T("开放资料可以转载和商业使用，只要注明出处。", "Open data may be reused, even commercially, with credit.", "Data terbuka boleh digunakan semula, termasuk komersial, dengan kredit.")},
]

write_chapter(chapter, terms, sources, quiz, datasets)
