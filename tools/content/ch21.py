"""Chapter 21 — Weather stations and instruments."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch21", "num": 21, "stage": 7,
 "title": T("地面观测站与仪器", "Weather stations and instruments", "Stesen cuaca dan peralatan"),
 "sources": ["PAM", "ESS", "NEWS-MM-2025"],
 "sections": [
 {"id": "s1", "heading": T("观测站的种类和选址", "Kinds of station and where to put them", "Jenis stesen dan lokasinya"), "level": "basic", "blocks": [
  P("按测量的项目、次数和观测员，气象站分四种：天气（综观）站有专职观测员，每小时观测，资料用来画天气图；农业气象站每天至少观测两次，还要量蒸发、草温、土温和太阳辐射；气候站每天一两次，量气温、湿度、雨量和风；雨量站每天只量雨量。",
    "By what they measure, how often and who observes, there are four kinds of station: synoptic stations, with full-time observers making hourly readings for weather maps; agricultural stations, read at least twice a day and also measuring evaporation, grass and soil temperature and solar radiation; climatological stations, read once or twice a day for temperature, humidity, rain and wind; and rainfall stations, which read only the rain each day.",
    "Mengikut apa yang diukur, kekerapan dan pencerap, terdapat empat jenis stesen: stesen sinoptik, dengan pencerap sepenuh masa membuat bacaan setiap jam untuk peta cuaca; stesen pertanian, dibaca sekurang-kurangnya dua kali sehari dan turut mengukur penyejatan, suhu rumput dan tanah serta sinaran suria; stesen klimatologi, dibaca sekali atau dua kali sehari untuk suhu, kelembapan, hujan dan angin; dan stesen hujan, yang hanya membaca hujan setiap hari.",
    src=["PAM:131-132"]),
  P("农业气象站要设在农场中间，地方要开阔，远离高楼、树木和沟渠，不会积水，土壤能代表当地；场地约 60 × 40 米，长边南北向，四周围起来。",
    "An agricultural station belongs in the middle of the farm, on open ground away from tall buildings, trees and drains, where water does not pool and the soil is typical of the area; the plot is about 60 × 40 m with its long side north–south, and fenced.",
    "Stesen pertanian patut terletak di tengah ladang, di kawasan terbuka jauh dari bangunan tinggi, pokok dan longkang, di mana air tidak bertakung dan tanahnya mewakili kawasan itu; plotnya kira-kira 60 × 40 m dengan sisi panjang utara–selatan, dan berpagar.",
    src=["PAM:132-133"]),
  N("key", "大马气象局目前管理 32 个主要气象站、382 个自动和传统气象站、8 个高空站和 18 个天气雷达站（2025 年 10 月公布）。",
    "MetMalaysia runs 32 principal meteorological stations, 382 automatic and conventional weather stations, 8 upper-air stations and 18 weather-radar stations (announced October 2025).",
    "MetMalaysia mengendalikan 32 stesen meteorologi utama, 382 stesen cuaca automatik dan konvensional, 8 stesen udara atas dan 18 stesen radar cuaca (diumumkan Oktober 2025).",
    src=["NEWS-MM-2025"]),
 ]},
 {"id": "s2", "heading": T("量气温和湿度", "Measuring temperature and humidity", "Mengukur suhu dan kelembapan"), "level": "basic", "blocks": [
  P("温度计放在{{t:stevenson-screen}}里：一个双层百叶的木箱，空气可以自由流通，又挡住阳光和雨；箱底离地 120 厘米。箱里有干球、湿球、最高和最低四支温度计。",
    "Thermometers live in a {{t:stevenson-screen}}: a louvred, double-walled wooden box that lets air flow freely while keeping off sun and rain, with its floor 120 cm above the ground. Inside are four thermometers: dry bulb, wet bulb, maximum and minimum.",
    "Termometer diletakkan dalam {{t:stevenson-screen}}: kotak kayu berdinding dua dan berlouver yang membiarkan udara mengalir bebas sambil melindungi daripada matahari dan hujan, dengan lantainya 120 cm dari tanah. Di dalamnya ada empat termometer: bebuli kering, bebuli basah, maksimum dan minimum.",
    defines=["stevenson-screen"], src=["PAM:137-139"]),
  L(("最高温度计：水银柱有收缩口，温度下降时水银退不回去，所以记得住最高温；要甩一下才复位", "Maximum thermometer: a narrowing in the mercury column stops it falling back, so it keeps the highest reading until shaken to reset", "Termometer maksimum: penyempitan pada turus merkuri menghalangnya jatuh semula, jadi ia menyimpan bacaan tertinggi sehingga digoncang"),
    ("最低温度计：酒精温度计，里面有一根小指标，停在最低温的位置", "Minimum thermometer: an alcohol thermometer with a small index that stays at the lowest point", "Termometer minimum: termometer alkohol dengan penunjuk kecil yang kekal pada titik terendah"),
    ("湿球温度计：球部包着湿纱布，蒸发会让它变冷；空气越干，干湿球相差越大", "Wet-bulb thermometer: its bulb is wrapped in wet muslin and cooled by evaporation; the drier the air, the bigger the gap from the dry bulb", "Termometer bebuli basah: bebulinya dibalut kain muslin basah dan disejukkan oleh penyejatan; semakin kering udara, semakin besar beza dengan bebuli kering"),
    src=["PAM:138-139", "PAM:164"]),
  P("干球和湿球一起叫{{t:psychrometer}}。用两者的读数查表或计算，就得到相对湿度、露点和水汽压——第 5 章的“湿球”就是这样量出来的。",
    "A dry and a wet bulb together make a {{t:psychrometer}}. From their two readings, by table or by calculation, you get the relative humidity, dew point and vapour pressure — the wet bulb of Chapter 5 is measured this way.",
    "Bebuli kering dan basah bersama dipanggil {{t:psychrometer}}. Daripada dua bacaannya, melalui jadual atau pengiraan, anda mendapat kelembapan relatif, takat embun dan tekanan wap — bebuli basah Bab 5 diukur begini.",
    defines=["psychrometer"], src=["PAM:162-165"]),
  N("tip", "读温度计要快，不要让身体的热影响读数；眼睛和刻度平齐，避免视差；湿球用蒸馏水或雨水，纱布每星期换。",
    "Read thermometers quickly so your body heat does not affect them; keep your eye level with the scale to avoid parallax; use distilled water or rainwater for the wet bulb and change the muslin every week.",
    "Baca termometer dengan cepat supaya haba badan tidak menjejaskannya; mata separas skala untuk mengelakkan paralaks; gunakan air suling atau air hujan untuk bebuli basah dan tukar kain muslin setiap minggu.",
    src=["PAM:141"]),
 ]},
 {"id": "s3", "heading": T("量雨量", "Measuring rain", "Mengukur hujan"), "level": "basic", "blocks": [
  P("{{t:rain-gauge}}有一个口径刚好 127 毫米（5 英寸）的漏斗，把雨水收进里面的瓶子，再用专用量筒读出毫米数。10 毫米雨，意思是雨水如果留在平地上不流走，会积到 10 毫米深。没有专用量筒时，用普通量杯量到的 126.7 毫升，就等于 10 毫米雨。",
    "A {{t:rain-gauge}} has a funnel exactly 127 mm (5 inches) across that leads the rain into a bottle inside; a special measuring cylinder then reads it in millimetres. Ten millimetres of rain means the water would stand 10 mm deep on flat ground if none ran off. Without the special cylinder, 126.7 ml in an ordinary measuring jug equals 10 mm of rain.",
    "{{t:rain-gauge}} mempunyai corong tepat 127 mm (5 inci) lebar yang menyalurkan hujan ke dalam botol; silinder penyukat khas kemudian membacanya dalam milimeter. Sepuluh milimeter hujan bermaksud air akan bertakung 10 mm dalam di tanah rata jika tiada yang mengalir. Tanpa silinder khas, 126.7 ml dalam bikar penyukat biasa bersamaan 10 mm hujan.",
    defines=["rain-gauge"], src=["PAM:143-144"]),
  P("雨量筒要装在平地上，不能放在斜坡、阶梯、墙上或屋顶；旁边任何东西的距离，至少要是它高出筒口的高度的两倍，免得挡住雨。自记雨量计用浮子带动笔，在转动的纸上画出雨量随时间的变化，所以还能算出雨势：雨量 ÷ 下雨时间，单位是毫米/小时。",
    "The gauge goes on level ground, never on a slope, a terrace, a wall or a roof; anything nearby must be at least twice as far away as it stands above the rim, so it does not block the rain. A self-recording gauge uses a float to move a pen across a turning chart, tracing rain against time, so it also gives the intensity: rain ÷ time, in millimetres an hour.",
    "Tolok mesti dipasang di tanah rata, bukan di cerun, teres, dinding atau bumbung; apa-apa objek berhampiran mesti sekurang-kurangnya dua kali lebih jauh daripada ketinggiannya di atas bibir tolok, supaya tidak menghalang hujan. Tolok perakam sendiri menggunakan pelampung untuk menggerakkan pena di atas carta yang berputar, menurih hujan melawan masa, jadi ia juga memberi keamatan: hujan ÷ masa, dalam milimeter sejam.",
    src=["PAM:144-145"]),
  N("key", "自动气象站常用翻斗式雨量计：每积满一小斗就翻一次，送出一个电讯号；数翻了几次，就知道下了多少雨。",
    "Automatic stations often use a tipping-bucket gauge: each time a small bucket fills it tips and sends an electrical signal, and counting the tips gives the rainfall.",
    "Stesen automatik sering menggunakan tolok baldi jongkit: setiap kali baldi kecil penuh ia terjongkit dan menghantar isyarat elektrik, dan mengira jongkitan memberi jumlah hujan.",
    src=["ESS:144", "PAM:169"]),
 ]},
 {"id": "s4", "heading": T("蒸发、风、日照和气压", "Evaporation, wind, sunshine and pressure", "Penyejatan, angin, cahaya matahari dan tekanan"), "level": "basic", "blocks": [
  L(("{{t:pan-evaporimeter}}：直径 120 厘米、深 25 厘米的圆盘装水，每天早上加水回到基准点，加了多少就是蒸发了多少（有下雨要扣掉）", "{{t:pan-evaporimeter}}: a pan 120 cm across and 25 cm deep; each morning water is added back to a reference point, and the amount added is the evaporation (allowing for any rain)", "{{t:pan-evaporimeter}}: dulang 120 cm lebar dan 25 cm dalam; setiap pagi air ditambah semula ke titik rujukan, dan jumlah yang ditambah ialah penyejatan (mengambil kira hujan)"),
    ("{{t:anemometer}}：三或四个半球形的杯子被风吹着转，计数器把转数换成风速；装在离地约 3 米（10 英尺）", "{{t:anemometer}}: three or four hemispherical cups spun by the wind, with a counter turning revolutions into speed; mounted about 3 m (10 ft) up", "{{t:anemometer}}: tiga atau empat cawan hemisfera diputar angin, dengan pembilang menukar putaran kepada kelajuan; dipasang kira-kira 3 m (10 kaki) tinggi"),
    ("{{t:wind-vane}}：箭头指向风吹来的方向，用 16 个方位或度数（北 360°、东 90°）记录", "{{t:wind-vane}}: its arrow points to where the wind comes from, recorded as one of 16 compass points or in degrees (north 360°, east 90°)", "{{t:wind-vane}}: anak panahnya menunjuk ke arah angin datang, direkod sebagai satu daripada 16 mata kompas atau dalam darjah (utara 360°, timur 90°)"),
    ("{{t:sunshine-recorder}}：直径 10 厘米的玻璃球把阳光聚焦，在卡片上烧出痕迹；痕迹多长，就是日照几小时", "{{t:sunshine-recorder}}: a 10 cm glass sphere focuses sunlight and burns a trace on a card; the length of the trace gives the hours of sunshine", "{{t:sunshine-recorder}}: sfera kaca 10 cm memfokuskan cahaya matahari dan membakar kesan pada kad; panjang kesan memberi jam cahaya matahari"),
    ("{{t:barometer}}：水银气压计或无液（空盒）气压计；空盒会随气压压扁或胀开，用之前要先和水银气压计校准", "{{t:barometer}}: mercury or aneroid; the aneroid's sealed box squeezes and swells with pressure and must first be set against a mercury barometer", "{{t:barometer}}: merkuri atau aneroid; kotak tertutup aneroid mengecut dan mengembang mengikut tekanan dan mesti ditentukur dahulu dengan barometer merkuri"),
    defines=["pan-evaporimeter", "anemometer", "wind-vane", "sunshine-recorder", "barometer"], src=["PAM:146-161"]),
 ]},
 {"id": "s5", "heading": T("自动气象站", "Automatic weather stations", "Stesen cuaca automatik"), "level": "basic", "blocks": [
  P("{{t:aws}}按设定的时间间隔（15 分钟到 24 小时）自动、连续地记录天气，不需要人一直在旁边。它的核心是数据记录器，连着温度、湿度、风向、风速、雨量、辐射和气压等感应器，把读数换成实际单位储存起来，再传到电脑。",
    "An {{t:aws}} records the weather automatically and continuously at set intervals, from 15 minutes to 24 hours, without an observer standing by. At its heart is a data logger wired to sensors for temperature, humidity, wind direction and speed, rain, radiation and pressure; it turns their signals into real units, stores them and passes them to a computer.",
    "{{t:aws}} merekod cuaca secara automatik dan berterusan pada selang yang ditetapkan, dari 15 minit hingga 24 jam, tanpa pencerap di sisi. Terasnya ialah perekod data yang disambung kepada penderia suhu, kelembapan, arah dan kelajuan angin, hujan, sinaran dan tekanan; ia menukar isyarat kepada unit sebenar, menyimpannya dan menghantarnya ke komputer.",
    defines=["aws"], src=["PAM:167-169"]),
  N("warn", "自动站也要人照顾：定期检查电池和记忆体，清洁太阳能板，检查风杯有没有裂、风向标能不能自由转动。",
    "Automatic stations still need care: check the battery and memory regularly, clean the solar panel, and inspect the cups for cracks and the vane for free movement.",
    "Stesen automatik masih memerlukan penjagaan: periksa bateri dan memori secara berkala, bersihkan panel solar, dan periksa cawan untuk retak serta bilah angin untuk pergerakan bebas.",
    src=["PAM:169-170"]),
 ]},
 ]}

terms = [
 ("stevenson-screen", T("百叶箱", "Stevenson screen", "Skrin Stevenson"), T("放温度计的双层百叶木箱，通风又挡太阳和雨。", "A louvred wooden box that shelters thermometers from sun and rain while letting air through.", "Kotak kayu berlouver yang melindungi termometer daripada matahari dan hujan sambil membiarkan udara masuk.")),
 ("psychrometer", T("干湿球温度计", "Psychrometer", "Psikrometer"), T("一对干球和湿球温度计，用来求相对湿度和露点。", "A dry-bulb and wet-bulb pair used to find humidity and dew point.", "Pasangan bebuli kering dan basah untuk mencari kelembapan dan takat embun.")),
 ("rain-gauge", T("雨量筒", "Rain gauge", "Tolok hujan"), T("收集雨水来量雨量的仪器；口径 127 毫米。", "An instrument that collects rain to measure it; the funnel is 127 mm across.", "Alat yang mengumpul hujan untuk mengukurnya; corongnya 127 mm lebar.")),
 ("pan-evaporimeter", T("蒸发皿", "Pan evaporimeter", "Panci penyejatan"), T("装水的大圆盘，量每天蒸发掉多少毫米水。", "A large water pan that measures how many millimetres evaporate each day.", "Dulang air besar yang mengukur berapa milimeter tersejat setiap hari.")),
 ("anemometer", T("风杯风速计", "Cup anemometer", "Anemometer cawan"), T("风吹杯子转动，用转数量风速。", "Measures wind speed from how fast the wind spins a set of cups.", "Mengukur kelajuan angin daripada kelajuan angin memutar set cawan.")),
 ("wind-vane", T("风向标", "Wind vane", "Bilah angin"), T("指向风吹来方向的仪器。", "Points to the direction the wind comes from.", "Menunjuk ke arah angin datang.")),
 ("sunshine-recorder", T("日照计", "Sunshine recorder", "Perakam cahaya matahari"), T("玻璃球聚光在卡片上烧出痕迹，量日照时数。", "A glass sphere that burns a trace on a card to measure hours of sunshine.", "Sfera kaca yang membakar kesan pada kad untuk mengukur jam cahaya matahari.")),
 ("barometer", T("气压计", "Barometer", "Barometer"), T("量气压的仪器，有水银式和空盒式。", "An instrument for air pressure, mercury or aneroid.", "Alat untuk tekanan udara, merkuri atau aneroid.")),
 ("aws", T("自动气象站", "Automatic weather station", "Stesen cuaca automatik"), T("按设定时间自动记录天气的气象站。", "A station that records the weather by itself at set intervals.", "Stesen yang merekod cuaca sendiri pada selang yang ditetapkan.")),
]

sources = [
 {"id": "NEWS-MM-2025", "short": "Malay Mail / Bernama", "title": "Wet spell warning: heavy rain to lash Kelantan, Terengganu, Pahang first… (MetMalaysia station counts), 8 October 2025", "publisher": "Malay Mail (Bernama)", "url": "https://www.malaymail.com/news/malaysia/2025/10/08/wet-spell-warning-heavy-rain-to-lash-kelantan-terengganu-pahang-first-then-johor-sabah-sarawak-in-novmarch-monsoon/193953", "accessed": "2026-10-02"},
]

quiz = [
 {"stage": 7, "chapter": "ch21", "q": T("干湿球温度计相差越大，表示什么？", "The bigger the gap between dry and wet bulb, the…", "Semakin besar beza bebuli kering dan basah, semakin…"),
  "options": [T("空气越干", "drier the air", "kering udara"), T("空气越湿", "more humid the air", "lembap udara"), T("风越弱", "lighter the wind", "lemah angin"), T("气压越高", "higher the pressure", "tinggi tekanan")],
  "answer": 0, "why": T("空气干，湿球蒸发快、冷得多。", "Dry air evaporates more from the wet bulb, cooling it more.", "Udara kering menyejat lebih banyak dari bebuli basah, menyejukkannya lebih.")},
 {"stage": 7, "chapter": "ch21", "q": T("用普通量杯量雨，多少毫升等于 10 毫米雨？", "With an ordinary jug, how many ml equal 10 mm of rain?", "Dengan bikar biasa, berapa ml bersamaan 10 mm hujan?"),
  "options": [T("126.7 毫升", "126.7 ml", "126.7 ml"), T("10 毫升", "10 ml", "10 ml"), T("1,000 毫升", "1,000 ml", "1,000 ml"), T("50 毫升", "50 ml", "50 ml")],
  "answer": 0, "why": T("127 毫米的漏斗面积约 126.7 平方厘米，乘 1 厘米就是 126.7 毫升。", "A 127 mm funnel has about 126.7 cm² of area; times 1 cm is 126.7 ml.", "Corong 127 mm mempunyai luas kira-kira 126.7 cm²; darab 1 cm ialah 126.7 ml.")},
 {"stage": 7, "chapter": "ch21", "q": T("风向标的箭头指向哪里？", "Where does a wind vane's arrow point?", "Ke manakah anak panah bilah angin menunjuk?"),
  "options": [T("风吹来的方向", "Where the wind comes from", "Arah angin datang"), T("风吹去的方向", "Where the wind goes", "Arah angin pergi"), T("永远指北", "Always north", "Sentiasa utara"), T("太阳的方向", "At the sun", "Ke arah matahari")],
  "answer": 0, "why": T("所以“西南风”是从西南吹来的风。", "So a ‘south-west wind’ comes from the south-west.", "Jadi ‘angin barat daya’ datang dari barat daya.")},
]

write_chapter(chapter, terms, sources, quiz)
