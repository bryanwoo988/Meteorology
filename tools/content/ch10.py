"""Chapter 10 — The upper air."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch10", "num": 10, "stage": 4,
 "title": T("高空大气", "The upper air", "Atmosfera atas"),
 "sources": ["ESS", "PAM", "OM-LEVELS-KL"],
 "sections": [
 {"id": "s1", "heading": T("为什么用气压代表高度", "Why height is given as pressure", "Mengapa ketinggian diberi sebagai tekanan"), "level": "basic", "blocks": [
  P("高空天气图不是画“10 公里高”的地方，而是画某个气压的地方。例如 500 hPa 图，就是把各地气压正好是 500 hPa 的那个面画出来，看它离海平面有多高。这样的一层叫{{t:pressure-level}}。",
    "Upper-air charts are not drawn for ‘10 km up’ but for a given pressure. A 500 hPa chart shows the surface where the pressure is exactly 500 hPa everywhere, and how high above sea level that surface lies. Such a surface is a {{t:pressure-level}}.",
    "Carta udara atas tidak dilukis untuk ‘10 km ke atas’ tetapi untuk tekanan tertentu. Carta 500 hPa menunjukkan permukaan yang tekanannya tepat 500 hPa di semua tempat, dan berapa tinggi permukaan itu dari paras laut. Permukaan sebegini ialah {{t:pressure-level}}.",
    defines=["pressure-level"], src=["ESS:156"]),
  P("这个面离海平面的高度叫{{t:geopotential-height}}。暖空气比较“胖”，所以热带上空同一个气压层比较高：标准大气的 500 hPa 约在 5,600 米，而吉隆坡上空平均约 5,890 米。图上高度高的地方相当于高压，低的地方相当于低压。",
    "The height of that surface above sea level is its {{t:geopotential-height}}. Warm air takes up more room, so over the tropics a given pressure level sits higher: in the standard atmosphere 500 hPa is about 5,600 m up, while over Kuala Lumpur it averages about 5,890 m. On such a chart, high heights act like high pressure and low heights like low pressure.",
    "Ketinggian permukaan itu dari paras laut ialah {{t:geopotential-height}}nya. Udara panas mengambil lebih banyak ruang, jadi di atas kawasan tropika sesuatu aras tekanan berada lebih tinggi: dalam atmosfera piawai 500 hPa kira-kira 5,600 m, manakala di atas Kuala Lumpur puratanya kira-kira 5,890 m. Pada carta sebegini, ketinggian tinggi bertindak seperti tekanan tinggi dan yang rendah seperti tekanan rendah.",
    defines=["geopotential-height"], src=["ESS:156", "OM-LEVELS-KL"]),
 ]},
 {"id": "s2", "heading": T("几个常用的气压层", "The levels forecasters use", "Aras yang digunakan peramal"), "level": "basic", "blocks": [
  {"type": "widget", "id": "W9"},
  L(("850 hPa（吉隆坡上空约 1.5 公里）：低空的风和水汽，看季风强弱、湿空气从哪里来", "850 hPa (about 1.5 km over Kuala Lumpur): low-level wind and moisture — how strong the monsoon is and where moist air comes from", "850 hPa (kira-kira 1.5 km di atas Kuala Lumpur): angin dan lembapan aras rendah — kekuatan monsun dan dari mana udara lembap datang"),
    ("700 hPa（约 3.2 公里）：中低层的水汽；这一层干燥时，雷雨云比较难长高", "700 hPa (about 3.2 km): moisture in the lower-middle air; when it is dry, storm clouds struggle to grow", "700 hPa (kira-kira 3.2 km): lembapan udara tengah bawah; apabila kering, awan ribut sukar tumbuh"),
    ("500 hPa（约 5.9 公里）：大约一半的空气在下面；天气系统主要跟着这一层的风移动", "500 hPa (about 5.9 km): about half the air is below; weather systems mostly move with the wind at this level", "500 hPa (kira-kira 5.9 km): kira-kira separuh udara di bawah; sistem cuaca kebanyakannya bergerak dengan angin pada aras ini"),
    ("250 hPa（约 11 公里）：急流和飞机巡航的高度，也是雷雨云顶摊开的地方", "250 hPa (about 11 km): where the jet streams and cruising airliners are, and where storm tops spread", "250 hPa (kira-kira 11 km): tempat aliran jet dan pesawat terbang, dan tempat puncak ribut merebak"),
    src=["OM-LEVELS-KL", "ESS:156", "ESS:200"]),
  N("tip", "Windy 可以选高度：“地面”“850 hPa”“500 hPa”“250 hPa”等。选 850 hPa 看风的流向，往往比看地面风更清楚季风的样子。",
    "Windy lets you pick the height — ‘surface’, ‘850 hPa’, ‘500 hPa’, ‘250 hPa’ and so on. Picking 850 hPa often shows the monsoon flow more clearly than the surface wind.",
    "Windy membolehkan anda memilih ketinggian — ‘permukaan’, ‘850 hPa’, ‘500 hPa’, ‘250 hPa’ dan sebagainya. Memilih 850 hPa sering menunjukkan aliran monsun lebih jelas daripada angin permukaan.",
    src=["OM-LEVELS-KL"]),
 ]},
 {"id": "s3", "heading": T("急流", "Jet streams", "Aliran jet"), "level": "basic", "blocks": [
  P("{{t:jet-stream}}是高空一条又窄又快的风带，像空中的河流，大致由西向东吹，常常弯弯曲曲。主要有两条：副热带急流在约北纬或南纬 30°、约 13 公里高；极地锋急流在冷暖空气交界的极锋附近、约 10 公里高。冬天的急流比较强，位置也比较靠近赤道。",
    "A {{t:jet-stream}} is a narrow, fast river of wind high in the atmosphere, blowing broadly from west to east and often meandering. There are two main ones: the subtropical jet near 30° latitude at about 13 km, and the polar-front jet near the boundary between cold and warm air, at about 10 km. In winter the jets are stronger and lie closer to the equator.",
    "{{t:jet-stream}} ialah sungai angin yang sempit dan laju tinggi di atmosfera, bertiup secara umum dari barat ke timur dan sering berliku. Terdapat dua utama: jet subtropika berhampiran latitud 30° pada kira-kira 13 km, dan jet front kutub berhampiran sempadan udara sejuk dan panas, kira-kira 10 km. Pada musim sejuk jet lebih kuat dan lebih dekat ke khatulistiwa.",
    defines=["jet-stream"], src=["ESS:199-200"]),
  {"type": "map", "id": "M1"},
  P("急流附近风速变化很大，就算天空晴朗、没有云，飞机也会突然颠簸，这叫{{t:clear-air-turbulence}}。",
    "Around a jet stream the wind changes sharply with height and distance, and aircraft can be jolted suddenly even in a clear, cloudless sky: {{t:clear-air-turbulence}}.",
    "Di sekitar aliran jet, angin berubah dengan ketara mengikut ketinggian dan jarak, dan pesawat boleh tersentak tiba-tiba walaupun langit cerah tanpa awan: {{t:clear-air-turbulence}}.",
    defines=["clear-air-turbulence"], src=["ESS:178", "ESS:200"]),
 ]},
 ]}

terms = [
 ("pressure-level", T("气压层", "Pressure level", "Aras tekanan"), T("气压处处相同的一个面，例如 500 hPa；高空天气图就画在这样的面上。", "A surface of equal pressure, such as 500 hPa; upper-air charts are drawn on these.", "Permukaan bertekanan sama, seperti 500 hPa; carta udara atas dilukis padanya.")),
 ("geopotential-height", T("位势高度", "Geopotential height", "Ketinggian geoupaya"), T("某个气压层离海平面的高度；热带比较高。", "The height of a pressure level above sea level; higher over the tropics.", "Ketinggian sesuatu aras tekanan dari paras laut; lebih tinggi di atas tropika.")),
 ("jet-stream", T("急流", "Jet stream", "Aliran jet"), T("高空又窄又快、大致由西向东吹的风带。", "A narrow, fast band of wind high up, blowing broadly west to east.", "Jalur angin sempit dan laju di udara tinggi, bertiup secara umum dari barat ke timur.")),
 ("clear-air-turbulence", T("晴空湍流", "Clear-air turbulence", "Gelora udara jernih"), T("没有云的高空中突然的颠簸，常在急流附近。", "Sudden bumpiness in cloudless air aloft, often near a jet stream.", "Gegaran tiba-tiba dalam udara tanpa awan di tempat tinggi, sering berhampiran aliran jet.")),
]

sources = [
 {"id": "OM-LEVELS-KL", "short": "Open-Meteo forecasts", "title": "Pressure-level heights and temperatures over Kuala Lumpur, 3 Aug – 2 Oct 2026 (hourly forecasts, averaged)", "publisher": "Open-Meteo Forecast API (CC BY 4.0)", "url": "https://open-meteo.com/en/docs", "accessed": "2026-10-02"},
]

quiz = [
 {"stage": 4, "chapter": "ch10", "q": T("为什么吉隆坡上空的 500 hPa 比标准大气高？", "Why is 500 hPa higher over Kuala Lumpur than in the standard atmosphere?", "Mengapa 500 hPa lebih tinggi di atas Kuala Lumpur berbanding atmosfera piawai?"),
  "options": [T("热带的空气比较暖，占的空间比较大", "Tropical air is warmer and takes up more room", "Udara tropika lebih panas dan mengambil lebih banyak ruang"), T("吉隆坡海拔很高", "Kuala Lumpur is very high above sea level", "Kuala Lumpur sangat tinggi dari paras laut"), T("那里的风比较大", "The wind is stronger there", "Angin lebih kuat di sana"), T("测量错误", "A measuring error", "Kesilapan pengukuran")],
  "answer": 0, "why": T("暖空气密度小，同样的空气量要更厚的一层，气压层就被抬高。", "Warm air is less dense, so the same mass of air needs a thicker layer and the pressure levels sit higher.", "Udara panas kurang tumpat, jadi jisim udara yang sama memerlukan lapisan lebih tebal dan aras tekanan berada lebih tinggi.")},
 {"stage": 4, "chapter": "ch10", "q": T("想看季风低空的风往哪里吹，Windy 上选哪一层最适合？", "Which Windy level best shows where the low-level monsoon wind is going?", "Aras Windy manakah paling baik menunjukkan arah angin monsun aras rendah?"),
  "options": [T("850 hPa", "850 hPa", "850 hPa"), T("250 hPa", "250 hPa", "250 hPa"), T("150 hPa", "150 hPa", "150 hPa"), T("哪一层都一样", "Any level is the same", "Semua aras sama")],
  "answer": 0, "why": T("850 hPa 约 1.5 公里高，避开了地面摩擦，又在季风气流里面。", "850 hPa is about 1.5 km up: above most surface friction but inside the monsoon flow.", "850 hPa kira-kira 1.5 km: di atas kebanyakan geseran permukaan tetapi dalam aliran monsun.")},
]

write_chapter(chapter, terms, sources, quiz)
