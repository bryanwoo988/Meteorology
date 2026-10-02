"""Chapter 16 — Malaysia's monsoons."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch16", "num": 16, "stage": 6,
 "title": T("马来西亚的季风", "Malaysia's monsoons", "Monsun di Malaysia"),
 "sources": ["ESS", "MET-PHEN", "MET-PHEN-MS", "TERM", "ERA5-OM", "METMY-SWM2024", "ASMC-HOME"],
 "sections": [
 {"id": "s1", "heading": T("什么是季风", "What a monsoon is", "Apakah monsun"), "level": "basic", "blocks": [
  P("“季风”（monsoon）这个词来自阿拉伯文，意思是“季节”。古时候在印度洋做买卖的商人用它来称呼一种会换方向的风：北半球冬天从东北吹来，夏天反过来从西南吹来。{{t:monsoon}}就是随季节换方向、而且持续吹很久的大范围风。",
    "The word ‘monsoon’ comes from Arabic for ‘season’. Traders crossing the Indian Ocean used it for a wind that changes direction: from the north-east in the northern winter and the opposite way, from the south-west, in the northern summer. A {{t:monsoon}} is a large-scale wind that keeps blowing from one direction for a season and then reverses.",
    "Perkataan ‘monsun’ berasal daripada bahasa Arab yang bermaksud ‘musim’. Pedagang yang merentasi Lautan Hindi menggunakannya untuk angin yang bertukar arah: dari timur laut pada musim sejuk utara dan sebaliknya, dari barat daya, pada musim panas utara. {{t:monsoon}} ialah angin berskala besar yang bertiup dari satu arah sepanjang satu musim dan kemudian berbalik.",
    defines=["monsoon"], src=["MET-PHEN", "TERM:230"]),
  P("原因是陆地和海洋受热的速度不同。冬天亚洲大陆冷得快，西伯利亚形成很强的高压，冷空气往外流，到中国沿海变成东北风，再吹向东南亚。夏天亚洲大陆变得很热，空气上升，形成低压；从南印度洋和印尼–澳洲一带吹来的潮湿东南风，越过赤道后转成西南风。",
    "The cause is that land and sea heat at different rates. In winter the Asian continent cools quickly and a very strong high builds over Siberia; cold air flows out of it, turns into a north-east wind along the coast of China and heads for South-East Asia. In summer the continent becomes very hot, the air rises and a low forms; moist south-east winds from the southern Indian Ocean and the Indonesia–Australia region turn into south-west winds as they cross the equator.",
    "Puncanya ialah darat dan laut menjadi panas pada kadar berbeza. Pada musim sejuk benua Asia cepat menyejuk dan tekanan tinggi yang sangat kuat terbentuk di Siberia; udara sejuk mengalir keluar, bertukar menjadi angin timur laut di pantai China dan menuju ke Asia Tenggara. Pada musim panas benua menjadi sangat panas, udara naik dan tekanan rendah terbentuk; angin tenggara yang lembap dari selatan Lautan Hindi dan rantau Indonesia–Australia bertukar menjadi angin barat daya apabila merentasi khatulistiwa.",
    src=["MET-PHEN"]),
  N("key", "第 9 章讲过科氏效应：它在赤道是零，离开赤道才开始让风偏转。东南风越过赤道变成西南风，就是这个道理。",
    "Recall the Coriolis effect from Chapter 9: it is zero at the equator and starts turning the wind once the air moves away from it. That is why a south-east wind becomes a south-west wind after crossing the equator.",
    "Ingat kesan Coriolis dari Bab 9: ia sifar di khatulistiwa dan mula membelokkan angin apabila udara bergerak menjauhinya. Itulah sebabnya angin tenggara menjadi angin barat daya selepas merentasi khatulistiwa.",
    src=["ESS:161", "MET-PHEN"]),
 ]},
 {"id": "s2", "heading": T("一年里的季风", "The monsoon year", "Tahun monsun"), "level": "basic", "blocks": [
  P("马来西亚的天气由两个季风主导：{{t:sw-monsoon}}从 5 月底到 9 月，{{t:ne-monsoon}}从 11 月到 3 月。两个季风之间的过渡期叫{{t:inter-monsoon}}，大约在 4–5 月和 10 月。",
    "Malaysia's weather is ruled by two monsoons: the {{t:sw-monsoon}} from late May to September, and the {{t:ne-monsoon}} from November to March. The changeover between them is the {{t:inter-monsoon}}, roughly April–May and October.",
    "Cuaca Malaysia dikuasai oleh dua monsun: {{t:sw-monsoon}} dari akhir Mei hingga September, dan {{t:ne-monsoon}} dari November hingga Mac. Tempoh peralihan antara keduanya ialah {{t:inter-monsoon}}, kira-kira April–Mei dan Oktober.",
    defines=["sw-monsoon", "ne-monsoon", "inter-monsoon"], src=["MET-PHEN"]),
  {"type": "widget", "id": "W13", "src": ["ERA5-OM", "MET-PHEN"]},
  P("拖动月份就能看到风向转换：12、1 月南中国海吹 25–30 km/h 的东北风，6–8 月转成西南风。哥打巴鲁 12 月平均雨量约 412 毫米，2 月只有约 81 毫米；吉隆坡则在 4 月（约 293 毫米）和 11 月（约 374 毫米）各有一个高峰，正好落在两个季风转换期。",
    "Drag the month and the wind swings round: in December and January a 25–30 km/h north-east wind blows over the South China Sea, turning south-west in June–August. Kota Bharu averages about 412 mm of rain in December but only about 81 mm in February; Kuala Lumpur has two peaks, in April (about 293 mm) and November (about 374 mm), right in the two inter-monsoon periods.",
    "Seret bulan dan arah angin berpusing: pada Disember dan Januari angin timur laut 25–30 km/j bertiup di Laut China Selatan, bertukar ke barat daya pada Jun–Ogos. Kota Bharu berpurata kira-kira 412 mm hujan pada Disember tetapi hanya kira-kira 81 mm pada Februari; Kuala Lumpur mempunyai dua puncak, pada April (kira-kira 293 mm) dan November (kira-kira 374 mm), tepat dalam dua tempoh peralihan monsun.",
    src=["ERA5-OM"]),
  N("warn", "这些数字是 ERA5 约 25 公里格子的 1991–2020 年平均，不是气象站的官方平均值，和 MetMalaysia 公布的数字会有出入；这里用来看一年的形状。",
    "These figures are ERA5 averages for 1991–2020 over grid boxes about 25 km across, not official station normals, so they will differ from MetMalaysia's numbers; use them to see the shape of the year.",
    "Angka-angka ini ialah purata ERA5 bagi 1991–2020 untuk kotak grid kira-kira 25 km, bukan normal rasmi stesen, jadi ia akan berbeza daripada angka MetMalaysia; gunakannya untuk melihat bentuk setahun.",
    src=["ERA5-OM"]),
 ]},
 {"id": "s3", "heading": T("东北季风：主要的雨季", "The north-east monsoon: the main rainy season", "Monsun timur laut: musim hujan utama"), "level": "basic", "blocks": [
  P("东北季风是马来西亚主要的雨季，半岛东海岸、砂拉越西部和沙巴东部雨最多。一阵阵从西伯利亚冲出来的强冷空气，叫{{t:monsoon-surge}}。它和赤道附近的低压、气旋性涡旋互相作用，就会在南中国海造成强风和大浪，在东海岸、砂拉越西部和沙巴东部下大雨。",
    "The north-east monsoon is Malaysia's main rainy season, wettest on the Peninsula's east coast, in western Sarawak and in eastern Sabah. From time to time a strong blast of cold air bursts out from Siberia: a {{t:monsoon-surge}}. When it meets low-pressure systems and swirling eddies near the equator it brings strong winds and rough seas to the South China Sea and heavy rain to the east coast, western Sarawak and eastern Sabah.",
    "Monsun timur laut ialah musim hujan utama Malaysia, paling basah di pantai timur Semenanjung, barat Sarawak dan timur Sabah. Dari semasa ke semasa ledakan udara sejuk yang kuat keluar dari Siberia: {{t:monsoon-surge}}. Apabila ia bertindak dengan sistem tekanan rendah dan pusaran berhampiran khatulistiwa, ia membawa angin kencang dan laut bergelora di Laut China Selatan serta hujan lebat di pantai timur, barat Sarawak dan timur Sabah.",
    defines=["monsoon-surge"], src=["MET-PHEN", "MET-PHEN-MS"]),
  P("这些大雨常在吉兰丹、登嘉楼、彭亨、柔佛东部，以及砂拉越和沙巴造成大水灾。第 19 章会再讲水灾。",
    "This heavy rain often causes large floods in Kelantan, Terengganu, Pahang and East Johor, and in Sarawak and Sabah. Chapter 19 returns to floods.",
    "Hujan lebat ini sering menyebabkan banjir besar di Kelantan, Terengganu, Pahang dan Johor Timur, serta di Sarawak dan Sabah. Bab 19 akan kembali kepada banjir.",
    src=["MET-PHEN"]),
 ]},
 {"id": "s4", "heading": T("西南季风：比较干", "The south-west monsoon: the drier season", "Monsun barat daya: musim lebih kering"), "level": "basic", "blocks": [
  P("西南季风期间全国都比较干，沙巴除外。大部分州每月雨量只有 100–150 毫米左右。半岛比较干，主要是因为苏门答腊的山脉挡住了雨（雨影效应）；沙巴则因为常有经过菲律宾、横越南中国海的台风尾巴，比较湿，每月超过 200 毫米。",
    "During the south-west monsoon the whole country is relatively dry, except Sabah. Most states get only about 100–150 mm a month. The Peninsula is dry mainly because Sumatra's mountains shelter it from rain — a rain shadow; Sabah is wetter, over 200 mm a month, from the tails of typhoons that cross the Philippines and the South China Sea.",
    "Semasa monsun barat daya seluruh negara agak kering, kecuali Sabah. Kebanyakan negeri hanya menerima kira-kira 100–150 mm sebulan. Semenanjung kering terutamanya kerana banjaran Sumatera melindunginya daripada hujan — bayang hujan; Sabah lebih basah, melebihi 200 mm sebulan, akibat ekor taufan yang merentasi Filipina dan Laut China Selatan.",
    src=["MET-PHEN"]),
  N("key", "“比较干”不等于每年都干。2024 年的西南季风，半岛和婆罗洲 5 到 9 月整体反而比平常湿，只有 7 月明显偏少。",
    "‘Drier’ does not mean dry every year. In the 2024 south-west monsoon, May to September was wetter than normal overall on both the Peninsula and Borneo, with July the main exception.",
    "‘Lebih kering’ tidak bermakna kering setiap tahun. Dalam monsun barat daya 2024, Mei hingga September secara keseluruhan lebih basah daripada normal di Semenanjung dan Borneo, dengan Julai sebagai pengecualian utama.",
    src=["METMY-SWM2024"]),
 ]},
 {"id": "s5", "heading": T("季风转换期", "The inter-monsoon", "Peralihan monsun"), "level": "basic", "blocks": [
  P("季风转换期风很弱，风向不定。早上天空通常晴朗，这有助于下午形成雷雨。半岛西海岸各州的月平均雨量最高值，就出现在这两个转换期，主要来自雷雨。",
    "In the inter-monsoon the wind is light and its direction changes. Mornings are usually clear, which helps thunderstorms form in the afternoon. In the west-coast states of the Peninsula, the highest average monthly rainfall comes in these two transition periods, mostly from thunderstorms.",
    "Semasa peralihan monsun angin lemah dan arahnya berubah-ubah. Pagi biasanya cerah, yang membantu ribut petir terbentuk pada sebelah petang. Di negeri-negeri pantai barat Semenanjung, purata hujan bulanan tertinggi berlaku dalam dua tempoh peralihan ini, kebanyakannya daripada ribut petir.",
    src=["MET-PHEN", "MET-PHEN-MS"]),
  N("tip", "ASMC 2026 年 9–11 月的展望说：西南季风预计持续到 10 月初，之后转入季风转换期，风变弱、风向不定，赤道一带的阵雨也通常会增加。",
    "ASMC's outlook for September–November 2026 says the south-west monsoon is expected to last into early October and then give way to the inter-monsoon, with light, variable winds and, typically, more showers over the equatorial region.",
    "Tinjauan ASMC bagi September–November 2026 menyatakan monsun barat daya dijangka berterusan hingga awal Oktober dan kemudian beralih kepada peralihan monsun, dengan angin lemah dan berubah-ubah serta, lazimnya, lebih banyak hujan di rantau khatulistiwa.",
    src=["ASMC-HOME"]),
 ]},
 ]}

terms = [
 ("monsoon", T("季风", "Monsoon", "Monsun"), T("随季节换方向、而且持续吹一整季的大范围风。", "A large-scale wind that blows from one direction for a season and then reverses.", "Angin berskala besar yang bertiup dari satu arah sepanjang musim dan kemudian berbalik.")),
 ("sw-monsoon", T("西南季风", "South-west monsoon", "Monsun barat daya"), T("5 月底到 9 月；马来西亚大部分地方比较干，沙巴例外。", "Late May to September; relatively dry over most of Malaysia except Sabah.", "Akhir Mei hingga September; agak kering di kebanyakan Malaysia kecuali Sabah.")),
 ("ne-monsoon", T("东北季风", "North-east monsoon", "Monsun timur laut"), T("11 月到 3 月；主要雨季，东海岸、砂拉越西部和沙巴东部雨最多。", "November to March; the main rainy season, wettest on the east coast, western Sarawak and eastern Sabah.", "November hingga Mac; musim hujan utama, paling basah di pantai timur, barat Sarawak dan timur Sabah.")),
 ("inter-monsoon", T("季风转换期", "Inter-monsoon", "Peralihan monsun"), T("两个季风之间，约 4–5 月和 10 月；风弱，下午多雷雨。", "Between the two monsoons, about April–May and October; light winds and afternoon thunderstorms.", "Antara dua monsun, kira-kira April–Mei dan Oktober; angin lemah dan ribut petir petang.")),
 ("monsoon-surge", T("季风潮（寒潮）", "Monsoon surge", "Luruan monsun"), T("东北季风期间从西伯利亚冲出的一阵强冷空气，带来强风、大浪和大雨。", "A strong blast of cold air from Siberia during the north-east monsoon, bringing strong winds, rough seas and heavy rain.", "Ledakan udara sejuk yang kuat dari Siberia semasa monsun timur laut, membawa angin kencang, laut bergelora dan hujan lebat.")),
]

sources = [
 {"id": "MET-PHEN-MS", "short": "MetMalaysia", "title": "Fenomena cuaca (monsun, ribut petir, garis badai, gelombang haba)", "publisher": "Jabatan Meteorologi Malaysia", "url": "https://www.met.gov.my/pendidikan/fenomena-cuaca/", "accessed": "2026-10-02"},
 {"id": "ASMC-HOME", "short": "ASMC", "title": "Regional haze situation; seasonal forecast for September–November 2026", "publisher": "ASEAN Specialised Meteorological Centre", "url": "https://asmc.asean.org/home/", "accessed": "2026-10-02"},
]

quiz = [
 {"stage": 6, "chapter": "ch16", "q": T("马来西亚主要的雨季是哪一个？", "Which is Malaysia's main rainy season?", "Yang manakah musim hujan utama Malaysia?"),
  "options": [T("东北季风（11 月到 3 月）", "The north-east monsoon (November to March)", "Monsun timur laut (November hingga Mac)"), T("西南季风（5 月底到 9 月）", "The south-west monsoon (late May to September)", "Monsun barat daya (akhir Mei hingga September)"), T("没有雨季", "There is none", "Tiada"), T("只有 7 月", "July only", "Julai sahaja")],
  "answer": 0, "why": T("东北季风为东海岸、砂拉越西部和沙巴东部带来最多的雨。", "It brings the most rain to the east coast, western Sarawak and eastern Sabah.", "Ia membawa paling banyak hujan ke pantai timur, barat Sarawak dan timur Sabah.")},
 {"stage": 6, "chapter": "ch16", "q": T("西南季风期间半岛比较干，主要原因是什么？", "Why is the Peninsula relatively dry in the south-west monsoon?", "Mengapa Semenanjung agak kering semasa monsun barat daya?"),
  "options": [T("苏门答腊的山脉挡住了雨", "Sumatra's mountains shelter it from the rain", "Banjaran Sumatera melindunginya daripada hujan"), T("海水太冷", "The sea is too cold", "Laut terlalu sejuk"), T("太阳太弱", "The sun is too weak", "Matahari terlalu lemah"), T("西伯利亚高压", "The Siberian high", "Tekanan tinggi Siberia")],
  "answer": 0, "why": T("这叫雨影效应。", "This is a rain shadow.", "Ini ialah bayang hujan.")},
 {"stage": 6, "chapter": "ch16", "q": T("吉隆坡一年的雨量高峰在什么时候？", "When are Kuala Lumpur's rainfall peaks?", "Bilakah puncak hujan Kuala Lumpur?"),
  "options": [T("4 月和 11 月左右的季风转换期", "Around April and November, the inter-monsoons", "Sekitar April dan November, peralihan monsun"), T("只有 1 月", "January only", "Januari sahaja"), T("7 月", "July", "Julai"), T("全年都一样", "Same all year", "Sama sepanjang tahun")],
  "answer": 0, "why": T("转换期风弱、早上晴，下午雷雨多。", "Light winds and clear mornings give many afternoon thunderstorms.", "Angin lemah dan pagi cerah memberi banyak ribut petir petang.")},
]

write_chapter(chapter, terms, sources, quiz)
