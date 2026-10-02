"""Chapter 35 — Reading weather apps."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch35", "num": 35, "stage": 8,
 "title": T("看懂天气 App", "Reading weather apps", "Membaca aplikasi cuaca"),
 "sources": ["ESS", "FUN", "ERA5-OM", "ECMWF-MEDIUM", "COMPARECAST"],
 "sections": [
 {"id": "s1", "heading": T("“60 % 下雨”是什么意思", "What ‘60 % chance of rain’ means", "Apakah maksud ‘60 % peluang hujan’"), "level": "basic", "blocks": [
  P("{{t:pop}}不是“六成地方会下雨”，也不是“会下六成的时间”。美国气象局的定义是：预报区里任何一个地点（例如你家）下到可量雨量（0.01 英寸，约 0.25 毫米）以上的机会是 60 %。换个说法：同样的预报出现 10 次，你家应该有 6 次下雨。",
    "A {{t:pop}} of 60 % does not mean ‘rain over 60 % of the area’ or ‘rain for 60 % of the time’. In the US National Weather Service's definition it is a 60 % chance that any given spot in the forecast area — your house, say — gets measurable rain, at least 0.01 inch (about 0.25 mm). Put another way: if the same forecast were issued ten times, it should rain at your house on six.",
    "{{t:pop}} 60 % tidak bermaksud ‘hujan di 60 % kawasan’ atau ‘hujan selama 60 % masa’. Mengikut takrif Perkhidmatan Cuaca Kebangsaan AS, ia peluang 60 % bahawa mana-mana tempat dalam kawasan ramalan — rumah anda, contohnya — menerima hujan yang boleh diukur, sekurang-kurangnya 0.01 inci (kira-kira 0.25 mm). Dalam kata lain: jika ramalan yang sama dikeluarkan sepuluh kali, rumah anda patut hujan enam kali.",
    defines=["pop"], src=["ESS:259"]),
  N("key", "可是阵雨不一样。同一本书的注解说：如果是阵雨，百分比指的是预计会被阵雨淋到的面积。所以“下午 60 % 阵雨”常常是城里一部分地方下大雨、另一部分一滴都没有——这正是午后对流的样子（第 17 章）。",
    "Showers are different, though. The same source notes that for showers the percentage refers to the area expected to be hit. So ‘60 % showers this afternoon’ often means a downpour over part of the city and not a drop over another — exactly how afternoon convection behaves (Chapter 17).",
    "Hujan lebat setempat berbeza. Sumber yang sama mencatat bahawa bagi hujan lebat peratusan merujuk kepada kawasan yang dijangka terkena. Jadi ‘60 % hujan petang ini’ sering bermaksud hujan lebat di sebahagian bandar dan tiada setitik di bahagian lain — tepat seperti perolakan petang (Bab 17).",
    src=["ESS:259"]),
  P("模型给的雨量是整个格子的平均（第 27 章），不是你家门口那一点。App 把它画成一朵云或一个雨滴，中间还经过了各自的处理；不同 App 用的模型和处理方法不同，同一天的说法当然也会不一样。",
    "A model's rainfall is the average over a whole grid box (Chapter 27), not the spot outside your door. An app turns it into a cloud or raindrop icon after its own processing, and different apps use different models and methods — so on the same day they will naturally disagree.",
    "Hujan model ialah purata seluruh kotak grid (Bab 27), bukan tempat di depan pintu anda. Aplikasi menukarnya menjadi ikon awan atau titisan selepas pemprosesan sendiri, dan aplikasi berlainan menggunakan model dan kaedah berlainan — jadi pada hari yang sama ia tentu tidak sependapat.",
    src=["ESS:254-256"]),
 ]},
 {"id": "s2", "heading": T("UTC 和马来西亚时间", "UTC and Malaysian time", "UTC dan waktu Malaysia"), "level": "basic", "blocks": [
  P("模型和天气图都用{{t:utc}}（协调世界时）。{{t:myt}}（马来西亚时间）比 UTC 快 8 小时：",
    "Models and charts use {{t:utc}}, Coordinated Universal Time. {{t:myt}}, Malaysian time, is 8 hours ahead of it:",
    "Model dan carta menggunakan {{t:utc}}, Waktu Universal Berkoordinat. {{t:myt}}, waktu Malaysia, 8 jam lebih awal daripadanya:",
    defines=["utc", "myt"], src=["ECMWF-MEDIUM", "METMY-TN0122"]),
  L(("00 UTC = 早上 8 点", "00 UTC = 8 am", "00 UTC = 8 pagi"), ("06 UTC = 下午 2 点", "06 UTC = 2 pm", "06 UTC = 2 petang"), ("12 UTC = 晚上 8 点", "12 UTC = 8 pm", "12 UTC = 8 malam"), ("18 UTC = 凌晨 2 点", "18 UTC = 2 am", "18 UTC = 2 pagi"),
    src=["METMY-TN0122"]),
 ]},
 {"id": "s3", "heading": T("Meteogram：一个地点的一天", "The meteogram: one place, one day", "Meteogram: satu tempat, satu hari"), "level": "basic", "blocks": [
  P("{{t:meteogram}}把一个地点的气温、雨量、风等随时间画在一起。下面是吉隆坡 2025 年 6 月 16 日的真实逐时资料（ERA5）：中午 12 点升到 32 °C，下午 1 点开始下雨，气温跟着往下掉——一个典型的午后阵雨天。拖动图表读每个钟头。",
    "A {{t:meteogram}} plots one place's temperature, rain, wind and more against time. Below are real hourly data (ERA5) for Kuala Lumpur on 16 June 2025: 32 °C at noon, rain from 1 pm, and the temperature dropping with it — a textbook afternoon-shower day. Drag across the chart to read each hour.",
    "{{t:meteogram}} memplot suhu, hujan, angin dan lain-lain bagi satu tempat melawan masa. Di bawah ialah data setiap jam sebenar (ERA5) bagi Kuala Lumpur pada 16 Jun 2025: 32 °C pada tengah hari, hujan dari 1 petang, dan suhu turun bersamanya — hari hujan petang yang klasik. Seret merentasi carta untuk membaca setiap jam.",
    defines=["meteogram"], src=["FUN:129", "ERA5-OM"]),
  {"type": "chart", "src": ["ERA5-OM"], "chart": {"kind": "line", "series_file": "kl-2025-06-16",
    "title": T("吉隆坡 2025 年 6 月 16 日：逐时气温和雨量", "Kuala Lumpur, 16 June 2025: hourly temperature and rain", "Kuala Lumpur, 16 Jun 2025: suhu dan hujan setiap jam"),
    "x": {"col": "hour", "label": T("时间", "Time", "Masa"), "format": "hour"},
    "y": {"label": T("气温", "Temperature", "Suhu"), "unit": "°C"},
    "y2": {"label": T("雨量", "Rain", "Hujan"), "unit": "mm"},
    "series": [{"col": "temperature_2m", "name": T("气温", "Temperature", "Suhu"), "color": "mercury"},
               {"col": "precipitation", "name": T("每小时雨量", "Rain per hour", "Hujan sejam"), "color": "rain", "axis": "y2"}]}},
  N("tip", "想比较不同模型对你家的预报，就用 CompareCast：同一个地点、几个模型并排，正好练习第 33 章的多模型集合。",
    "To compare several models' forecasts for your own place, use CompareCast: one location, several models side by side — practice for the multi-model ensembles of Chapter 33.",
    "Untuk membandingkan ramalan beberapa model bagi tempat anda, gunakan CompareCast: satu lokasi, beberapa model bersebelahan — latihan untuk ensemble pelbagai model Bab 33.",
    src=["COMPARECAST"]),
 ]},
 ]}

terms = [
 ("pop", T("降雨概率", "Probability of precipitation", "Kebarangkalian hujan"), T("预报区里任一点下到可量雨量的机会；阵雨时指面积。", "The chance of measurable rain at any spot in the area; for showers, the area covered.", "Peluang hujan boleh diukur di mana-mana tempat; bagi hujan lebat setempat, kawasan diliputi.")),
 ("utc", T("UTC（协调世界时）", "UTC", "UTC"), T("全世界气象通用的时间。", "The world time used across meteorology.", "Waktu dunia yang digunakan dalam meteorologi.")),
 ("myt", T("马来西亚时间（MYT）", "Malaysian time (MYT)", "Waktu Malaysia (MYT)"), T("比 UTC 快 8 小时。", "UTC plus 8 hours.", "UTC tambah 8 jam.")),
 ("meteogram", T("Meteogram（气象时间图）", "Meteogram", "Meteogram"), T("把一个地点的气象要素随时间画在一起的图。", "A chart of one place's weather elements against time.", "Carta unsur cuaca satu tempat melawan masa.")),
]

sources = [
 {"id": "COMPARECAST", "short": "CompareCast", "title": "CompareCast — compare weather models side by side", "publisher": "Bryan Woo", "url": "https://bryanwoo988.github.io/CompareCast/", "accessed": "2026-10-03"},
]

quiz = [
 {"stage": 8, "chapter": "ch35", "q": T("“降雨概率 60 %”（持续性的雨）是什么意思？", "‘60 % chance of rain’ (steady rain) means…", "‘60 % peluang hujan’ (hujan berterusan) bermaksud…"),
  "options": [T("你家下到可量雨量的机会是 60 %", "A 60 % chance your spot gets measurable rain", "Peluang 60 % tempat anda menerima hujan boleh diukur"), T("六成地方会下雨", "Rain over 60 % of the area", "Hujan di 60 % kawasan"), T("会下 60 % 的时间", "Rain 60 % of the time", "Hujan 60 % masa"), T("雨量 60 毫米", "60 mm of rain", "60 mm hujan")],
  "answer": 0, "why": T("阵雨时百分比才指面积。", "Only for showers does it refer to area.", "Hanya bagi hujan lebat setempat ia merujuk kawasan.")},
 {"stage": 8, "chapter": "ch35", "q": T("06 UTC 是马来西亚几点？", "06 UTC is what time in Malaysia?", "06 UTC pukul berapa di Malaysia?"),
  "options": [T("下午 2 点", "2 pm", "2 petang"), T("早上 6 点", "6 am", "6 pagi"), T("晚上 10 点", "10 pm", "10 malam"), T("中午", "Noon", "Tengah hari")],
  "answer": 0, "why": T("加 8 小时。", "Add 8 hours.", "Tambah 8 jam.")},
]

write_chapter(chapter, terms, sources, quiz)
