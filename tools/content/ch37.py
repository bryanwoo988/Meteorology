"""Chapter 37 — A guide to Windy's layers."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

def C(ch, zh, en, ms):
    """A chapter link, labelled in each language."""
    return T(f"{{{{ch:{ch}|{zh}}}}}", f"{{{{ch:{ch}|{en}}}}}", f"{{{{ch:{ch}|{ms}}}}}")

def n(k):
    return (f"第 {k} 章", f"Chapter {k}", f"Bab {k}")

ROWS = [
 ("风", "Wind", "Angin", "地面 10 米的平均风（或选的气压层）", "Mean wind 10 m above the surface (or at a chosen pressure level)", "Purata angin 10 m dari permukaan (atau pada aras tekanan dipilih)", 9),
 ("阵风", "Wind gusts", "Tiupan angin", "过去 3 小时 10 米的阵风；ECMWF 的算法给的值比较高", "10 m gusts over the last 3 hours; ECMWF's method gives higher values", "Tiupan 10 m dalam 3 jam lalu; kaedah ECMWF memberi nilai lebih tinggi", 9),
 ("雷达、闪电", "Radar, lightning", "Radar, kilat", "雷达回波加上 Blitzortung 的即时闪电", "Radar echoes plus live lightning from Blitzortung", "Gema radar ditambah kilat langsung dari Blitzortung", 24),
 ("雨、雷", "Rain, thunder", "Hujan, guruh", "过去 3 小时的雨量加闪电密度预报", "Rain over the last 3 hours with forecast lightning density", "Hujan 3 jam lalu dengan ramalan ketumpatan kilat", 12),
 ("累积雨量", "Rain accumulation", "Hujan terkumpul", "未来几小时或几天的总雨量", "Total rain over the coming hours or days", "Jumlah hujan beberapa jam atau hari akan datang", 7),
 ("气温", "Temperature", "Suhu", "离地 2 米的气温（或选的气压层）", "Temperature 2 m above the surface (or at a chosen level)", "Suhu 2 m dari permukaan (atau pada aras dipilih)", 4),
 ("露点", "Dew point", "Takat embun", "空气要冷到几度才会结露", "The temperature at which dew would form", "Suhu di mana embun akan terbentuk", 5),
 ("湿度", "Humidity", "Kelembapan", "2 米的相对湿度", "Relative humidity at 2 m", "Kelembapan relatif pada 2 m", 5),
 ("湿球温度", "Wet-bulb temperature", "Suhu bebuli basah", "靠蒸发能冷到的最低温度；持续超过 35 °C 会危及生命", "The lowest temperature evaporation can reach; above 35 °C for long it is life-threatening", "Suhu terendah yang boleh dicapai penyejatan; melebihi 35 °C lama mengancam nyawa", 5),
 ("冻结高度", "Freezing altitude", "Aras beku", "0 °C 的高度", "The height of the 0 °C level", "Ketinggian aras 0 °C", 7),
 ("CAPE 指数", "CAPE index", "Indeks CAPE", "对流能量；1,000–2,000 可能有中等雷雨，2,000 以上可能很强", "Convective energy; 1,000–2,000 may mean moderate storms, over 2,000 severe ones", "Tenaga perolakan; 1,000–2,000 mungkin ribut sederhana, melebihi 2,000 ribut teruk", 7),
 ("云、低云、中云、高云", "Clouds (low, medium, high)", "Awan (rendah, sederhana, tinggi)", "低云在地面到约 2,000 米，中云约 2,000–6,500 米，高云约 6,500 米以上", "Low cloud up to about 2,000 m, medium about 2,000–6,500 m, high above about 6,500 m", "Awan rendah hingga kira-kira 2,000 m, sederhana kira-kira 2,000–6,500 m, tinggi melebihi kira-kira 6,500 m", 6),
 ("云顶、云底", "Cloud tops, cloud base", "Puncak awan, dasar awan", "云最高和最低的高度", "The heights of the highest and lowest parts of the cloud", "Ketinggian bahagian tertinggi dan terendah awan", 6),
 ("能见度", "Visibility", "Ketampakan", "看得多远；空气有多透明", "How far you can see; how clear the air is", "Sejauh mana boleh dilihat; betapa jernih udara", 6),
 ("太阳能、紫外线", "Solar power, UV index", "Kuasa suria, indeks UV", "到达地面的太阳辐射；晒伤的紫外线强度", "Sunlight reaching the ground; the strength of sunburning UV", "Cahaya matahari sampai ke tanah; kekuatan UV yang membakar kulit", 2),
 ("海浪、涌浪", "Waves, swell", "Ombak, alun", "有效波高和周期；涌浪来自远方的风", "Significant wave height and period; swell comes from distant winds", "Ketinggian ombak bererti dan tempoh; alun datang dari angin jauh", 13),
 ("海温、洋流、潮流", "Sea temperature, currents, tidal currents", "Suhu laut, arus, arus pasang surut", "海面温度和海流", "Sea-surface temperature and currents", "Suhu permukaan laut dan arus", 13),
 ("CO、粉尘、SO₂", "CO, dust, SO₂", "CO, debu, SO₂", "大气成分（霾里有什么）", "Atmospheric composition — what is in haze", "Komposisi atmosfera — apa ada dalam jerebu", 20),
 ("土壤湿度、干旱强度", "Soil moisture, drought intensity", "Lembapan tanah, keamatan kemarau", "作物可用的土壤水和缺水程度", "Soil water available to crops, and how short it is", "Air tanah tersedia untuk tanaman, dan kekurangannya", 19),
 ("气压", "Pressure", "Tekanan", "海平面气压", "Mean sea-level pressure", "Tekanan purata paras laut", 9),
 ("天气预警", "Weather warnings", "Amaran cuaca", "各国气象局用 CAP 格式发的预警", "National warnings sent in the CAP format", "Amaran negara yang dihantar dalam format CAP", 18),
]

rows = []
for zh, en, ms, wz, we, wm, k in ROWS:
    ch = f"ch{k:02d}"
    rows.append([T(zh, en, ms), T(wz, we, wm), C(ch, *n(k))])

chapter = {"id": "ch37", "num": 37, "stage": 8,
 "title": T("Windy 图层导读", "A guide to Windy's layers", "Panduan lapisan Windy"),
 "sources": ["WINDY-OVERLAYS"],
 "sections": [
 {"id": "s1", "heading": T("每个图层在第几章学过", "Where each layer was covered", "Di mana setiap lapisan dipelajari"), "level": "basic", "blocks": [
  P("Windy 有几十个图层。下面这张表把常用的图层和这本书的章节对起来：点章节就回到那一章复习。",
    "Windy has dozens of layers. This table matches the common ones to the chapters of this book: tap a chapter to go back and revise it.",
    "Windy mempunyai berpuluh-puluh lapisan. Jadual ini memadankan lapisan biasa dengan bab buku ini: ketik bab untuk kembali dan mengulang kaji.",
    src=["WINDY-OVERLAYS"]),
  {"type": "table", "src": ["WINDY-OVERLAYS"],
   "caption": T("Windy 图层对照表", "Windy layers at a glance", "Lapisan Windy sepintas lalu"),
   "headers": [T("图层", "Layer", "Lapisan"), T("是什么", "What it shows", "Apa yang ditunjukkan"), T("复习", "Revise", "Ulang kaji")],
   "rows": rows},
 ]},
 {"id": "s2", "heading": T("模型、高度和单点预报", "Models, heights and point forecasts", "Model, ketinggian dan ramalan titik"), "level": "basic", "blocks": [
  L(("模型：可以在 ECMWF、GFS 等模型之间切换；几个模型说法一致时比较可信（第 33 章）", "Model: switch between ECMWF, GFS and others; when they agree, trust rises (Chapter 33)", "Model: tukar antara ECMWF, GFS dan lain-lain; apabila bersetuju, keyakinan meningkat (Bab 33)"),
    ("高度：风、气温、湿度等可以选地面或某个气压层，例如 850 hPa 看季风（第 10 章）", "Height: wind, temperature, humidity and more can be shown at the surface or at a pressure level, such as 850 hPa for the monsoon (Chapter 10)", "Ketinggian: angin, suhu, kelembapan dan lain-lain boleh ditunjukkan di permukaan atau pada aras tekanan, seperti 850 hPa untuk monsun (Bab 10)"),
    ("单点预报：点地图上的一个地方，看那里的逐时预报，就是一张 meteogram（第 35 章）", "Point forecast: tap a place on the map for its hour-by-hour forecast — a meteogram (Chapter 35)", "Ramalan titik: ketik satu tempat pada peta untuk ramalan jam demi jamnya — sebuah meteogram (Bab 35)"),
    src=["WINDY-OVERLAYS"]),
  N("warn", "Windy 自己也提醒：地面的实际风和气温会受山、城市、对流云影响；模型的格子平均不等于某一点的观测（第 27 章）。",
    "Windy itself warns that the actual wind and temperature at the ground are affected by mountains, cities and convective clouds; a model's grid average is not an observation at one spot (Chapter 27).",
    "Windy sendiri mengingatkan bahawa angin dan suhu sebenar di tanah dipengaruhi gunung, bandar dan awan perolakan; purata grid model bukan cerapan di satu tempat (Bab 27).",
    src=["WINDY-OVERLAYS"]),
 ]},
 ]}

quiz = [
 {"stage": 8, "chapter": "ch37", "q": T("Windy 的 CAPE 图层显示 2,500，代表什么？", "Windy's CAPE layer shows 2,500. What might that mean?", "Lapisan CAPE Windy menunjukkan 2,500. Apakah maksudnya?"),
  "options": [T("可能有很强的雷雨", "Severe storms are possible", "Ribut teruk mungkin"), T("天气很稳定", "Very stable weather", "Cuaca sangat stabil"), T("有雾", "Fog", "Kabus"), T("海浪 2.5 米", "2.5 m waves", "Ombak 2.5 m")],
  "answer": 0, "why": T("2,000 以上可能是强雷雨。", "Over 2,000 may mean severe storms.", "Melebihi 2,000 mungkin ribut teruk.")},
 {"stage": 8, "chapter": "ch37", "q": T("在 Windy 点一个地方看逐时预报，看到的是什么图？", "Tapping a place in Windy for its hourly forecast shows a…", "Mengetik satu tempat dalam Windy untuk ramalan setiap jam menunjukkan…"),
  "options": [T("Meteogram", "Meteogram", "Meteogram"), T("Skew-T", "Skew-T", "Skew-T"), T("卫星图", "Satellite image", "Imej satelit"), T("雷达图", "Radar image", "Imej radar")],
  "answer": 0, "why": T("一个地点的要素随时间变化。", "One place's elements against time.", "Unsur satu tempat melawan masa.")},
]

write_chapter(chapter, [], [], quiz)
