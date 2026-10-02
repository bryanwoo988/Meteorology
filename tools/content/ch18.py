"""Chapter 18 — Weather warnings."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch18", "num": 18, "stage": 6,
 "title": T("天气预警", "Weather warnings", "Amaran cuaca"),
 "sources": ["MET-WARN-RAIN", "MET-WARN-WIND", "MET-WARN-TS", "MET-WARN-TC", "MET-PHEN", "WMO-CAP"],
 "sections": [
 {"id": "s1", "heading": T("连续降雨预警：三个等级", "Continuous-rain warnings: three levels", "Amaran hujan berterusan: tiga peringkat"), "level": "basic", "blocks": [
  P("预计会下很久的雨时，大马气象局发出连续降雨预警，分三级：{{t:waspada}}、{{t:buruk}}、{{t:bahaya}}。门槛看的是 24 小时的雨量，24 小时从开始下雨的时候算起。",
    "When long-lasting rain is expected, MetMalaysia issues a continuous-rain warning at one of three levels: {{t:waspada}}, {{t:buruk}} and {{t:bahaya}}. The thresholds are rainfall over 24 hours, counted from when the rain begins.",
    "Apabila hujan yang berpanjangan dijangka, MetMalaysia mengeluarkan amaran hujan berterusan pada salah satu daripada tiga peringkat: {{t:waspada}}, {{t:buruk}} dan {{t:bahaya}}. Ambangnya ialah jumlah hujan dalam 24 jam, dikira dari masa hujan bermula.",
    defines=["waspada", "buruk", "bahaya"], src=["MET-WARN-RAIN"]),
  {"type": "table", "src": ["MET-WARN-RAIN"],
   "caption": T("连续降雨预警的标准", "Continuous-rain warning criteria", "Kriteria amaran hujan berterusan"),
   "headers": [T("等级", "Level", "Peringkat"), T("标准（24 小时）", "Criterion (24 hours)", "Kriteria (24 jam)"), T("可能的影响", "Possible effects", "Kesan yang boleh berlaku")],
   "rows": [[T("Waspada（警惕）", "Waspada (alert)", "Waspada"), T("预计连续下雨，雨量少于 150 毫米", "Continuous rain expected, under 150 mm", "Hujan berterusan dijangka, kurang daripada 150 mm"), T("低洼地区可能淹水", "Possible flooding in low-lying areas", "Berkemungkinan banjir di kawasan rendah")],
            [T("Buruk（恶劣）", "Buruk (bad)", "Buruk"), T("预计连续大雨，雨量超过 150 毫米", "Heavy continuous rain expected, over 150 mm", "Hujan lebat berterusan dijangka, melebihi 150 mm"), T("低洼地区和河岸附近可能淹水；季节性作物可能受损", "Possible flooding in low-lying areas and near riverbanks; seasonal crops may be damaged", "Berkemungkinan banjir di kawasan rendah dan berdekatan tebing sungai; tanaman bermusim mungkin rosak")],
            [T("Bahaya（危险）", "Bahaya (danger)", "Bahaya"), T("预计连续非常大的雨，雨量超过 250 毫米", "Very heavy continuous rain expected, over 250 mm", "Hujan sangat lebat berterusan dijangka, melebihi 250 mm"), T("更大范围的水灾、山坡土崩；不牢固的建筑、道路和桥梁可能受损；季节性作物可能大面积被毁", "Wider flooding and landslides on hill slopes; weak structures, roads and bridges may be damaged; seasonal crops may be badly destroyed", "Banjir lebih besar dan tanah runtuh di cerun bukit; struktur tidak kukuh, jalan raya dan jambatan mungkin rosak; tanaman bermusim mungkin musnah teruk")]]},
  N("key", "连续降雨预警看的是预计的 24 小时总雨量。等级越高，可能的影响越大、范围越广，连作物、道路和桥梁都可能受损。",
    "A continuous-rain warning is set by the expected total over 24 hours. The higher the level, the bigger and wider the possible effects — up to damage to crops, roads and bridges.",
    "Amaran hujan berterusan ditentukan oleh jumlah hujan yang dijangka dalam 24 jam. Lebih tinggi peringkat, lebih besar dan luas kesan yang mungkin — sehingga kerosakan tanaman, jalan raya dan jambatan.",
    src=["MET-WARN-RAIN"]),
 ]},
 {"id": "s2", "heading": T("雷暴预警", "Thunderstorm warnings", "Amaran ribut petir"), "level": "basic", "blocks": [
  P("当气象站、雷达、卫星、数值预报和高空图都显示有雷暴，而且雨势会超过每小时 20 毫米时，就发出雷暴预警。这是短时预警，每一次有效时间不超过 6 小时；如果坏天气预计会持续超过 6 小时，可以升级为连续降雨预警。",
    "A thunderstorm warning is issued when station observations, radar, satellite images, computer forecasts and upper-air charts clearly show a thunderstorm with rain heavier than 20 mm an hour happening or on its way. It is a short-term warning, valid for no more than 6 hours each time; if bad weather is expected to last longer than 6 hours, it can be upgraded to a continuous-rain warning.",
    "Amaran ribut petir dikeluarkan apabila pencerapan stesen, gema radar, imej satelit, produk NWP dan carta udara atas jelas menunjukkan ribut petir dengan intensiti hujan melebihi 20 mm sejam sedang atau dijangka berlaku. Ia amaran jangka pendek, sah tidak lebih daripada 6 jam setiap keluaran; jika cuaca buruk dijangka melebihi 6 jam, ia boleh dinaik taraf kepada amaran hujan berterusan.",
    src=["MET-WARN-TS"]),
 ]},
 {"id": "s3", "heading": T("强风和大浪预警", "Strong-wind and rough-sea warnings", "Amaran angin kencang dan laut bergelora"), "level": "basic", "blocks": [
  {"type": "table", "src": ["MET-WARN-WIND"],
   "caption": T("强风和大浪预警的三个类别", "The three categories of strong-wind and rough-sea warning", "Tiga kategori amaran angin kencang dan laut bergelora"),
   "headers": [T("类别", "Category", "Kategori"), T("风和浪", "Wind and waves", "Angin dan ombak"), T("危险对象", "Dangerous to", "Berbahaya kepada")],
   "rows": [[T("第一类", "First", "Pertama"), T("风速 40–50 km/h，和/或浪高可达 3.5 米", "Wind 40–50 km/h and/or waves up to 3.5 m", "Angin 40–50 km/j dan/atau ombak sehingga 3.5 m"), T("小船；所有海上休闲和运动", "Small boats; all sea recreation and sports", "Bot kecil; semua aktiviti rekreasi dan sukan laut")],
            [T("第二类", "Second", "Kedua"), T("风速 50–60 km/h，和/或浪高可达 4.5 米", "Wind 50–60 km/h and/or waves up to 4.5 m", "Angin 50–60 km/j dan/atau ombak sehingga 4.5 m"), T("所有船运，包括渔船和渡轮；所有海边活动", "All shipping, including fishing and ferries; all beach activities", "Semua perkapalan termasuk perikanan dan feri; semua aktiviti pantai")],
            [T("第三类", "Third", "Ketiga"), T("风速超过 60 km/h，和/或浪高超过 4.5 米", "Wind over 60 km/h and/or waves over 4.5 m", "Angin melebihi 60 km/j dan/atau ombak melebihi 4.5 m"), T("所有船运；石油平台工人；所有海边活动", "All shipping; oil-rig workers; all beach activities", "Semua perkapalan; pekerja pelantar minyak; semua aktiviti pantai")]]},
  P("东北季风期间，南中国海的强风大浪预警特别常见；第 16 章讲的季风潮，就是常见的原因。",
    "These warnings are especially common over the South China Sea in the north-east monsoon; the monsoon surges of Chapter 16 are a usual cause.",
    "Amaran ini sangat biasa di Laut China Selatan semasa monsun timur laut; luruan monsun Bab 16 ialah punca yang biasa.",
    src=["MET-PHEN", "MET-WARN-WIND"]),
 ]},
 {"id": "s4", "heading": T("热带气旋和热浪", "Tropical cyclones and heat waves", "Siklon tropika dan gelombang haba"), "level": "basic", "blocks": [
  P("大马气象局负责监测北纬 0–20°、东经 95–130° 范围内的热带气旋，并发出忠告和预警。",
    "MetMalaysia monitors tropical cyclones, and issues advisories and warnings, for the area 0–20°N, 95–130°E.",
    "MetMalaysia memantau dan mengeluarkan nasihat serta amaran siklon tropika bagi kawasan 0–20°U, 95–130°T.",
    src=["MET-WARN-TC"]),
  P("在马来西亚，连续三天最高气温超过 37 °C 就是{{t:heat-wave}}。气象局用四个阶段监测：",
    "In Malaysia a {{t:heat-wave}} means a daily maximum above 37 °C for three days in a row. MetMalaysia monitors it in four stages:",
    "Di Malaysia {{t:heat-wave}} bermaksud suhu maksimum harian melebihi 37 °C selama tiga hari berturut-turut. MetMalaysia memantaunya dalam empat peringkat:",
    defines=["heat-wave"], src=["MET-PHEN"]),
  {"type": "table", "src": ["MET-PHEN"],
   "caption": T("热浪监测的四个阶段", "The four heat-wave monitoring stages", "Empat peringkat pemantauan gelombang haba"),
   "headers": [T("阶段", "Stage", "Peringkat"), T("状态", "Status", "Status"), T("标准", "Criterion", "Kriteria")],
   "rows": [[T("0", "0", "0"), T("正常", "Normal", "Normal"), T("每日最高气温低于 35.0 °C", "Daily maximum below 35.0 °C", "Suhu maksimum harian di bawah 35.0 °C")],
            [T("1", "1", "1"), T("注意", "Caution", "Berjaga-jaga"), T("连续至少三天 35.0–37.0 °C", "35.0–37.0 °C for at least three days in a row", "35.0–37.0 °C sekurang-kurangnya tiga hari berturut-turut")],
            [T("2", "2", "2"), T("热浪", "Heat wave", "Gelombang haba"), T("连续至少三天高于 37.0 °C 到 40.0 °C", "Above 37.0 °C up to 40.0 °C for at least three days in a row", "Melebihi 37.0 °C hingga 40.0 °C sekurang-kurangnya tiga hari berturut-turut")],
            [T("3", "3", "3"), T("极端热浪", "Extreme heat wave", "Gelombang haba ekstrem"), T("连续至少三天高于 40.0 °C", "Above 40.0 °C for at least three days in a row", "Melebihi 40.0 °C sekurang-kurangnya tiga hari berturut-turut")]]},
 ]},
 {"id": "s5", "heading": T("预警怎样传出去", "How warnings reach you", "Bagaimana amaran sampai kepada anda"), "level": "basic", "blocks": [
  P("预警会发给相关机构、媒体和公众，管道包括 myCuaca 手机应用、eMET、短信、气象局网站、大众媒体、社交媒体、传真和电邮。",
    "Warnings go to the relevant agencies, the media and the public through the myCuaca app, eMET, SMS, the MetMalaysia website, the mass media, social media, fax and e-mail.",
    "Amaran disebarkan kepada agensi berkaitan, media dan orang awam melalui aplikasi myCuaca, eMET, SMS, laman web MET Malaysia, media massa, media sosial, faks dan e-mel.",
    src=["MET-WARN-RAIN"]),
  P("在国际上，预警越来越多用{{t:cap}}发送。它是一种统一、电脑读得懂的格式（XML），一条预警就可以同时送到电视、手机、网站等所有管道。2023 年，世界气象大会把 CAP 写进 WMO 的《技术规则》，成为发送预警的推荐标准。",
    "Internationally, more and more warnings are sent in the {{t:cap}}: a single machine-readable format (XML) that lets one warning feed television, phones, websites and every other channel at once. In 2023 the World Meteorological Congress wrote CAP into WMO's Technical Regulations as the recommended standard for sending warnings.",
    "Di peringkat antarabangsa, semakin banyak amaran dihantar dalam {{t:cap}}: satu format yang boleh dibaca mesin (XML) yang membolehkan satu amaran sampai ke televisyen, telefon, laman web dan semua saluran lain serentak. Pada 2023 Kongres Meteorologi Sedunia memasukkan CAP ke dalam Peraturan Teknikal WMO sebagai piawaian yang disyorkan untuk menghantar amaran.",
    defines=["cap"], src=["WMO-CAP"]),
 ]},
 {"id": "s6", "heading": T("收到预警时要做什么", "What to do when a warning comes", "Apa yang perlu dilakukan apabila amaran dikeluarkan"), "level": "basic", "blocks": [
  L(("季风季节前：清理沟渠和排水道，准备足够的水和不易坏的食物", "Before the monsoon season: clear drains and gutters; keep enough water and non-perishable food", "Sebelum musim monsun: bersihkan longkang dan saluran; simpan air dan makanan tahan lama yang mencukupi"),
    ("季风期间：远离水流急的沟渠、河流和淹水地区；不要开车进入淹水地区；把车停在高处；不要乘小船出海", "During the monsoon: keep away from fast-flowing drains, rivers and flooded areas; do not drive into floodwater; park on high ground; do not go to sea in small boats", "Semasa monsun: jauhi longkang dan sungai yang deras serta kawasan banjir; jangan memandu ke dalam air banjir; letak kenderaan di tempat tinggi; jangan ke laut dengan bot kecil"),
    ("雷雨时：躲进坚固的建筑物或车里，不要躲在小棚或孤立的树下；离开船和水边", "In a thunderstorm: get into a solid building or a car; do not shelter in a small hut or under an isolated tree; get out of boats and away from water", "Semasa ribut petir: masuk ke bangunan kukuh atau kereta; jangan berlindung di pondok kecil atau di bawah pokok yang terpencil; keluar dari bot dan jauhi air"),
    ("在野外无处可躲：到低处、远离树木、围栏和电线杆；如果皮肤刺痛或头发竖起，马上蹲下，身体尽量缩小", "Caught outdoors with no shelter: go to low ground away from trees, fences and poles; if your skin tingles or your hair stands up, squat down at once and make yourself as small as possible", "Terperangkap di luar tanpa tempat berlindung: pergi ke tempat rendah jauh dari pokok, pagar dan tiang; jika kulit terasa menggeletar atau rambut tegak, segera mencangkung dan jadikan badan sekecil mungkin"),
    src=["MET-PHEN"]),
 ]},
 ]}

terms = [
 ("waspada", T("Waspada（警惕）", "Waspada (alert)", "Waspada"), T("连续降雨预警的第一级：24 小时雨量预计少于 150 毫米。", "First level of continuous-rain warning: under 150 mm expected in 24 hours.", "Peringkat pertama amaran hujan berterusan: kurang daripada 150 mm dijangka dalam 24 jam.")),
 ("buruk", T("Buruk（恶劣）", "Buruk (bad)", "Buruk"), T("连续降雨预警的第二级：24 小时雨量预计超过 150 毫米。", "Second level: over 150 mm expected in 24 hours.", "Peringkat kedua: melebihi 150 mm dijangka dalam 24 jam.")),
 ("bahaya", T("Bahaya（危险）", "Bahaya (danger)", "Bahaya"), T("连续降雨预警的最高级：24 小时雨量预计超过 250 毫米。", "Highest level: over 250 mm expected in 24 hours.", "Peringkat tertinggi: melebihi 250 mm dijangka dalam 24 jam.")),
 ("heat-wave", T("热浪", "Heat wave", "Gelombang haba"), T("在马来西亚：连续三天最高气温超过 37 °C。", "In Malaysia: a daily maximum above 37 °C for three days in a row.", "Di Malaysia: suhu maksimum harian melebihi 37 °C selama tiga hari berturut-turut.")),
 ("cap", T("CAP（通用预警协议）", "CAP (Common Alerting Protocol)", "CAP (Protokol Amaran Bersama)"), T("国际统一的预警格式（XML），一条预警可以同时送到所有管道。", "The international standard format (XML) for warnings, so one alert can feed every channel.", "Format piawai antarabangsa (XML) untuk amaran, supaya satu amaran sampai ke semua saluran.")),
]

sources = [
 {"id": "MET-WARN-RAIN", "short": "MetMalaysia", "title": "Kriteria amaran hujan berterusan", "publisher": "Jabatan Meteorologi Malaysia", "url": "https://www.met.gov.my/ramalan/hujan-lebat/", "accessed": "2026-10-02"},
 {"id": "MET-WARN-WIND", "short": "MetMalaysia", "title": "Kriteria amaran angin kencang dan laut bergelora", "publisher": "Jabatan Meteorologi Malaysia", "url": "https://www.met.gov.my/ramalan/angin-kencang-and-laut-bergelora", "accessed": "2026-10-02"},
 {"id": "MET-WARN-TS", "short": "MetMalaysia", "title": "Kriteria amaran ribut petir", "publisher": "Jabatan Meteorologi Malaysia", "url": "https://www.met.gov.my/ramalan/ribut-petir", "accessed": "2026-10-02"},
 {"id": "MET-WARN-TC", "short": "MetMalaysia", "title": "Kriteria amaran ribut taufan", "publisher": "Jabatan Meteorologi Malaysia", "url": "https://www.met.gov.my/ramalan/ribut-taufan", "accessed": "2026-10-02"},
 {"id": "WMO-CAP", "short": "WMO", "title": "Leveraging the Common Alerting Protocol and Cell Broadcast technology for advancing Early Warnings for All", "publisher": "World Meteorological Organization", "url": "https://wmo.int/media/magazine-article/leveraging-common-alerting-protocol-and-cell-broadcast-technology-advancing-early-warnings-all", "accessed": "2026-10-02"},
]

quiz = [
 {"stage": 6, "chapter": "ch18", "q": T("预计 24 小时会下 200 毫米雨，是哪一级预警？", "200 mm expected in 24 hours: which warning level?", "200 mm dijangka dalam 24 jam: peringkat amaran mana?"),
  "options": [T("Buruk", "Buruk", "Buruk"), T("Waspada", "Waspada", "Waspada"), T("Bahaya", "Bahaya", "Bahaya"), T("不用预警", "No warning", "Tiada amaran")],
  "answer": 0, "why": T("超过 150 毫米但不超过 250 毫米。", "Over 150 mm but not over 250 mm.", "Melebihi 150 mm tetapi tidak melebihi 250 mm.")},
 {"stage": 6, "chapter": "ch18", "q": T("雷暴预警每次最长有效多久？", "How long is one thunderstorm warning valid at most?", "Berapa lama satu amaran ribut petir sah paling lama?"),
  "options": [T("6 小时", "6 hours", "6 jam"), T("24 小时", "24 hours", "24 jam"), T("3 天", "3 days", "3 hari"), T("1 星期", "1 week", "1 minggu")],
  "answer": 0, "why": T("更久的话就升级为连续降雨预警。", "Longer than that, it becomes a continuous-rain warning.", "Lebih lama daripada itu, ia menjadi amaran hujan berterusan.")},
 {"stage": 6, "chapter": "ch18", "q": T("雷雨时在野外，哪里最不应该躲？", "Caught outdoors in a thunderstorm, where should you not shelter?", "Terperangkap di luar semasa ribut petir, di mana anda tidak patut berlindung?"),
  "options": [T("孤立的大树下", "Under an isolated tree", "Di bawah pokok yang terpencil"), T("坚固的建筑物里", "In a solid building", "Di dalam bangunan kukuh"), T("车里", "In a car", "Di dalam kereta"), T("远离电线杆的低处", "Low ground away from poles", "Tempat rendah jauh dari tiang")],
  "answer": 0, "why": T("孤立的树容易被雷打中。", "An isolated tree is easily struck by lightning.", "Pokok terpencil mudah dipanah petir.")},
]

write_chapter(chapter, terms, sources, quiz)
