"""Chapter 38 — Weather and crops."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch38", "num": 38, "stage": 9,
 "title": T("天气与作物", "Weather and crops", "Cuaca dan tanaman"),
 "sources": ["PAM", "TERM"],
 "sections": [
 {"id": "s1", "heading": T("光、温度、水和风", "Light, temperature, water and wind", "Cahaya, suhu, air dan angin"), "level": "basic", "blocks": [
  P("作物的生长、发育和产量，主要看它所在环境的物理条件。对作物有好有坏的天气要素包括雨量和水、气温、太阳辐射、湿度、风和土温；而过多或不合时的雨、雨太少、热浪、雷暴和冰雹、强风、水灾等，则通常是坏的。",
    "A crop's growth, development and yield depend mainly on the physical conditions it lives in. Elements that can help or harm include rain and water, air temperature, solar radiation, humidity, wind and soil temperature; excessive or untimely rain, too little rain, heat waves, thunderstorms and hail, high winds and floods are usually harmful.",
    "Pertumbuhan, perkembangan dan hasil tanaman bergantung terutamanya pada keadaan fizikal persekitarannya. Unsur yang boleh membantu atau merosakkan termasuk hujan dan air, suhu udara, sinaran suria, kelembapan, angin dan suhu tanah; hujan berlebihan atau tidak kena masa, hujan terlalu sedikit, gelombang haba, ribut petir dan hujan batu, angin kencang dan banjir biasanya merosakkan.",
    src=["PAM:32", "PAM:34-35"]),
  L(("水：光合作用的原料，也把养分溶解带进植物；雨太多或太少都会减产，雨还会妨碍田间工作、助长病虫害", "Water: a raw material of photosynthesis that dissolves nutrients and carries them in; too much or too little cuts yields, and rain also hampers field work and favours pests and diseases", "Air: bahan mentah fotosintesis yang melarutkan nutrien dan membawanya masuk; terlalu banyak atau sedikit mengurangkan hasil, dan hujan juga mengganggu kerja ladang serta menggalakkan perosak dan penyakit"),
    ("温度：每种作物有最低、最适和最高三个{{t:cardinal-temperature}}；热季作物的最适范围约 31–37 °C，最高约 44–50 °C", "Temperature: each crop has minimum, optimum and maximum {{t:cardinal-temperature}}s; for hot-season crops the optimum is about 31–37 °C and the maximum about 44–50 °C", "Suhu: setiap tanaman mempunyai {{t:cardinal-temperature}} minimum, optimum dan maksimum; bagi tanaman musim panas optimum kira-kira 31–37 °C dan maksimum kira-kira 44–50 °C"),
    ("光：光合作用离不开光；光的强度、长短和颜色都会影响开花、长高和产量", "Light: photosynthesis needs it; its intensity, duration and colour all affect flowering, growth and yield", "Cahaya: fotosintesis memerlukannya; keamatan, tempoh dan warnanya semua mempengaruhi pembungaan, pertumbuhan dan hasil"),
    ("湿度：湿度高可减少水分亏缺，但也助长病虫害；湿度低会加快蒸腾", "Humidity: high humidity eases water stress but favours pests and diseases; low humidity speeds transpiration", "Kelembapan: kelembapan tinggi mengurangkan tekanan air tetapi menggalakkan perosak dan penyakit; kelembapan rendah mempercepat transpirasi"),
    ("风：增加光合作用和蒸腾；强风会折断枝干、吹落果实，造成倒伏", "Wind: raises photosynthesis and transpiration; strong winds snap branches, shed fruit and flatten crops", "Angin: meningkatkan fotosintesis dan transpirasi; angin kencang mematahkan dahan, menggugurkan buah dan merebahkan tanaman"),
    defines=["cardinal-temperature"], src=["PAM:35-40", "TERM:49"]),
  P("作物从发芽、开花到成熟，每个阶段出现的时间叫{{t:phenology}}。很多天气的影响要看发生在哪个阶段：同样的干旱，碰到开花期和碰到生长后期，结果可以差很多。",
    "The timing of a crop's stages, from germination through flowering to maturity, is its {{t:phenology}}. Much of the weather's effect depends on the stage it hits: the same dry spell can do very different harm at flowering and late in the season.",
    "Masa peringkat tanaman, dari percambahan hingga pembungaan dan kematangan, ialah {{t:phenology}}nya. Kebanyakan kesan cuaca bergantung pada peringkat yang terkena: kemarau yang sama boleh membawa kerosakan yang sangat berbeza semasa pembungaan dan lewat musim.",
    defines=["phenology"], src=["PAM:97-98", "TERM:258"]),
 ]},
 {"id": "s2", "heading": T("农业气象服务", "Agrometeorological services", "Perkhidmatan agrometeorologi"), "level": "basic", "blocks": [
  P("农业气象学帮助农民决定播种期、什么时候除草和收割、怎样减少农药和肥料的流失，也帮助了解天气和病虫害的关系。中期预报（未来几天到一星期）对农业特别有用：可以安排人工、机械和灌溉用水。",
    "Agrometeorology helps farmers choose sowing dates, time weeding and harvest, cut losses of chemicals and fertiliser, and understand how weather drives pests and diseases. Medium-range forecasts, a few days to a week ahead, are especially useful in farming, for planning labour, machines and irrigation water.",
    "Agrometeorologi membantu petani memilih tarikh menyemai, menentukan masa merumpai dan menuai, mengurangkan kehilangan bahan kimia dan baja, serta memahami bagaimana cuaca memacu perosak dan penyakit. Ramalan jarak sederhana, beberapa hari hingga seminggu, sangat berguna dalam pertanian, untuk merancang tenaga kerja, jentera dan air pengairan.",
    src=["PAM:33", "PAM:100-102"]),
  P("{{t:agromet-advisory}}把天气预报翻译成农场上要做的事。书里的例子是一份公报分三部分：过去一星期的天气、未来四天的预报，以及给农民的建议。",
    "An {{t:agromet-advisory}} turns the forecast into farm actions. The book's example bulletin has three parts: the past week's weather, the forecast for the next four days, and advice to farmers.",
    "{{t:agromet-advisory}} menterjemah ramalan kepada tindakan di ladang. Contoh buletin dalam buku mempunyai tiga bahagian: cuaca minggu lalu, ramalan empat hari akan datang, dan nasihat kepada petani.",
    defines=["agromet-advisory"], src=["PAM:102"]),
  N("tip", "照这个格式替自己的园做一份：看大马气象局的预警（第 18 章）、ECMWF 的集合（第 30 章）和 CompareCast，决定这星期什么时候施肥、喷药、收割。",
    "Make one for your own farm in the same format: check MetMalaysia's warnings (Chapter 18), the ECMWF ensemble (Chapter 30) and CompareCast, then decide when to fertilise, spray and harvest this week.",
    "Buat satu untuk ladang anda dalam format yang sama: semak amaran MetMalaysia (Bab 18), ensemble ECMWF (Bab 30) dan CompareCast, kemudian tentukan bila membaja, menyembur dan menuai minggu ini.",
    src=["PAM:102"]),
 ]},
 ]}

terms = [
 ("cardinal-temperature", T("基点温度", "Cardinal temperature", "Suhu kardinal"), T("作物生长的最低、最适和最高温度。", "The minimum, optimum and maximum temperatures for a crop's growth.", "Suhu minimum, optimum dan maksimum bagi pertumbuhan tanaman.")),
 ("phenology", T("作物物候", "Crop phenology", "Fenologi tanaman"), T("作物各生长阶段（发芽、开花、成熟）出现的时间。", "The timing of a crop's stages: germination, flowering, maturity.", "Masa peringkat tanaman: percambahan, pembungaan, kematangan.")),
 ("agromet-advisory", T("农业气象服务（农业气象建议）", "Agrometeorological advisory", "Nasihat agrometeorologi"), T("把天气预报转成对农民的具体建议。", "Turning forecasts into specific advice for farmers.", "Menukar ramalan kepada nasihat khusus untuk petani.")),
]

quiz = [
 {"stage": 9, "chapter": "ch38", "q": T("为什么中期预报对农业特别有用？", "Why are medium-range forecasts especially useful in farming?", "Mengapa ramalan jarak sederhana sangat berguna dalam pertanian?"),
  "options": [T("可以提前安排人工、机械和灌溉", "Labour, machines and irrigation can be planned ahead", "Tenaga kerja, jentera dan pengairan boleh dirancang awal"), T("它预报下个月", "It forecasts next month", "Ia meramal bulan depan"), T("它只报气温", "It gives only temperature", "Ia hanya memberi suhu"), T("它不会错", "It is never wrong", "Ia tidak pernah salah")],
  "answer": 0, "why": T("几天到一星期正好是农场安排工作的时间。", "A few days to a week is the span farms plan work in.", "Beberapa hari hingga seminggu ialah tempoh ladang merancang kerja.")},
 {"stage": 9, "chapter": "ch38", "q": T("同样的干旱，为什么对作物的伤害可以不同？", "Why can the same dry spell do different harm?", "Mengapa kemarau yang sama boleh membawa kerosakan berbeza?"),
  "options": [T("要看碰到哪个生长阶段（物候）", "It depends on the crop stage it hits", "Bergantung pada peringkat tanaman yang terkena"), T("干旱都一样", "Droughts are all the same", "Semua kemarau sama"), T("只看风向", "Only the wind direction matters", "Hanya arah angin penting"), T("看月亮", "The Moon decides", "Bulan menentukan")],
  "answer": 0, "why": T("开花期等敏感阶段最怕缺水。", "Sensitive stages such as flowering suffer most.", "Peringkat sensitif seperti pembungaan paling terjejas.")},
]

write_chapter(chapter, terms, [], quiz)
