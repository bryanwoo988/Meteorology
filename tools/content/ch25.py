"""Chapter 25 — Reading a Skew-T."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch25", "num": 25, "stage": 7,
 "title": T("Skew-T 探空图", "Reading a Skew-T", "Membaca Skew-T"),
 "sources": ["NOAA-SKEWT", "ESS", "TERM", "UWYO-SND"],
 "sections": [
 {"id": "s1", "heading": T("一张图上的五组线", "Five sets of lines on one chart", "Lima set garisan pada satu carta"), "level": "basic", "blocks": [
  P("{{t:skew-t}}是画探空资料的标准图。早期的图把等温线画成直的；1947 年改成斜 45°，比较好分析，所以叫“Skew-T”（斜温）。图上有几组固定的线：",
    "The {{t:skew-t}} is the standard chart for plotting a sounding. Early versions drew the temperature lines straight up; in 1947 they were tilted 45° to make analysis easier — hence ‘Skew-T’. It carries several sets of fixed lines:",
    "{{t:skew-t}} ialah carta piawai untuk memplot data sonde. Versi awal melukis garisan suhu tegak; pada 1947 ia dicondongkan 45° untuk memudahkan analisis — maka ‘Skew-T’. Ia mengandungi beberapa set garisan tetap:",
    defines=["skew-t"], src=["NOAA-SKEWT"]),
  L(("气压线：横线，从下面约 1,050 hPa 到上面 100 hPa；因为气压随高度按对数减少，越往上间距越大", "Pressure lines: horizontal, from about 1,050 hPa at the bottom to 100 hPa at the top; spaced further apart higher up because pressure falls logarithmically with height", "Garisan tekanan: mendatar, dari kira-kira 1,050 hPa di bawah hingga 100 hPa di atas; semakin jarak ke atas kerana tekanan menurun secara logaritma dengan ketinggian"),
    ("等温线：斜 45°，从左上往右下数值增加", "Temperature lines: tilted 45°, increasing from upper left to lower right", "Garisan suhu: condong 45°, meningkat dari kiri atas ke kanan bawah"),
    ("干绝热线：未饱和空气上升时每 1,000 米冷 9.8 °C 的路线", "Dry adiabats: the path of rising unsaturated air, cooling 9.8 °C per 1,000 m", "Adiabat kering: laluan udara tak tepu yang naik, menyejuk 9.8 °C setiap 1,000 m"),
    ("湿绝热线：饱和空气上升时的路线，因为凝结放出潜热，冷得比较慢", "Moist adiabats: the path of rising saturated air, cooling more slowly because condensation releases heat", "Adiabat lembap: laluan udara tepu yang naik, menyejuk lebih perlahan kerana pemeluwapan membebaskan haba"),
    ("混合比线：每公斤干空气里有几克水汽", "Mixing-ratio lines: grams of water vapour per kilogram of dry air", "Garisan nisbah campuran: gram wap air bagi setiap kilogram udara kering"),
    src=["NOAA-SKEWT"]),
  P("一次探空画上去是两条曲线：右边的是气温，左边的是露点。两条线越靠近，那一层空气越接近饱和、越湿。",
    "A plotted sounding is two curves: temperature on the right and dew point on the left. The closer the two lines, the nearer that layer is to saturation — the moister it is.",
    "Sonde yang diplot ialah dua lengkung: suhu di kanan dan takat embun di kiri. Semakin dekat dua garisan, semakin hampir lapisan itu kepada tepu — semakin lembap.",
    src=["NOAA-SKEWT", "ESS:250"]),
 ]},
 {"id": "s2", "heading": T("逆温层：一个盖子", "The inversion: a lid", "Songsangan: penutup"), "level": "basic", "blocks": [
  P("通常气温越往上越低，但有时某一层反而越往上越暖，这叫{{t:inversion}}。逆温层非常稳定，像盖子一样压住上升的空气；逆温层贴近地面时，层云、雾、霾和污染物都被困在下面。",
    "Normally the air cools with height, but sometimes a layer grows warmer upwards: an {{t:inversion}}. An inversion is very stable and acts as a lid on rising air; when one sits near the ground, stratus, fog, haze and pollution are all trapped beneath it.",
    "Biasanya udara menyejuk dengan ketinggian, tetapi kadangkala satu lapisan menjadi lebih panas ke atas: {{t:inversion}}. Songsangan sangat stabil dan bertindak sebagai penutup pada udara yang naik; apabila ia berada dekat tanah, stratus, kabus, jerebu dan pencemaran semuanya terperangkap di bawahnya.",
    defines=["inversion"], src=["ESS:12", "ESS:120", "TERM:184"]),
  P("2026 年 9 月 30 日早上 8 点吉隆坡国际机场的探空里，就有一个浅浅的逆温：1,000 hPa 是 25.5 °C，往上到 975 hPa（约 330 米）反而升到 26.2 °C。这是清晨地面冷却留下的盖子；太阳把地面晒热后，它就会被冲破。",
    "The 8 am sounding at KLIA on 30 September 2026 has a shallow inversion: 25.5 °C at 1,000 hPa rising to 26.2 °C at 975 hPa, about 330 m up. It is a lid left by the ground cooling overnight; once the sun heats the ground it is broken.",
    "Sonde jam 8 pagi di KLIA pada 30 September 2026 mempunyai songsangan cetek: 25.5 °C pada 1,000 hPa naik ke 26.2 °C pada 975 hPa, kira-kira 330 m tinggi. Ia penutup yang ditinggalkan oleh tanah yang menyejuk semalaman; sebaik matahari memanaskan tanah ia dipecahkan.",
    src=["UWYO-SND", "ESS:120"]),
 ]},
 {"id": "s3", "heading": T("早上看探空，判断下午", "Reading the morning sounding for the afternoon", "Membaca sonde pagi untuk petang"), "level": "basic", "blocks": [
  {"type": "widget", "id": "W18"},
  P("在图上找第 7 章学过的东西：从地面的气温和露点出发，沿着干绝热线往上，碰到露点那条混合比线的地方就是 LCL（云底）；之后沿着湿绝热线往上。气块线在气温线右边（比周围暖）的那一块面积就是 CAPE，左边那一块就是 CIN。",
    "Find Chapter 7's quantities on the chart: from the surface temperature and dew point, follow a dry adiabat up until it meets the mixing-ratio line through the dew point — that is the LCL, the cloud base; from there follow a moist adiabat. Where the parcel line lies right of the temperature curve (warmer than its surroundings) the area is CAPE; where it lies left, CIN.",
    "Cari kuantiti Bab 7 pada carta: dari suhu dan takat embun permukaan, ikut adiabat kering ke atas sehingga bertemu garisan nisbah campuran melalui takat embun — itulah LCL, dasar awan; dari situ ikut adiabat lembap. Di mana garisan bungkusan berada di kanan lengkung suhu (lebih panas daripada sekeliling) kawasan itu ialah CAPE; di mana di kiri, CIN.",
    src=["NOAA-SKEWT"]),
  P("用这次真实的早上 8 点探空算：如果地面空气保持早上的 24.8 °C、露点 20.8 °C，气块完全没有 CAPE；下午晒到 31 °C、露点不变，CAPE 约 380 J/kg；如果海风再带来湿空气，把露点提高到 23 °C，CAPE 就升到约 1,200 J/kg，而 CIN 几乎没有——这就是午后雷雨的燃料。",
    "Worked from this real 8 am sounding: if the surface air stayed at the morning's 24.8 °C with a 20.8 °C dew point, the parcel would have no CAPE at all; heated to 31 °C with the same dew point, CAPE is about 380 J/kg; and if the sea breeze then brings moister air, lifting the dew point to 23 °C, CAPE climbs to about 1,200 J/kg with almost no CIN — the fuel for an afternoon thunderstorm.",
    "Dikira daripada sonde sebenar jam 8 pagi ini: jika udara permukaan kekal pada 24.8 °C pagi dengan takat embun 20.8 °C, bungkusan langsung tiada CAPE; dipanaskan ke 31 °C dengan takat embun yang sama, CAPE kira-kira 380 J/kg; dan jika bayu laut kemudian membawa udara lebih lembap, menaikkan takat embun ke 23 °C, CAPE meningkat ke kira-kira 1,200 J/kg dengan hampir tiada CIN — bahan api ribut petir petang.",
    src=["UWYO-SND"]),
  N("key", "这就是第 4、7、9、17 章午后阵雨的整条线索：早上的探空告诉你“燃料”有多少，太阳加热和海风决定下午能不能点着它。",
    "This ties together the afternoon-shower thread of Chapters 4, 7, 9 and 17: the morning sounding says how much fuel is there; the sun's heating and the sea breeze decide whether the afternoon lights it.",
    "Ini menyatukan benang hujan petang Bab 4, 7, 9 dan 17: sonde pagi memberitahu berapa banyak bahan api; pemanasan matahari dan bayu laut menentukan sama ada petang menyalakannya.",
    src=["UWYO-SND", "ESS:352"]),
 ]},
 ]}

terms = [
 ("skew-t", T("Skew-T 图", "Skew-T diagram", "Gambar rajah Skew-T"), T("等温线斜 45° 的探空图，用来看大气稳定度、云底和 CAPE。", "A sounding chart with temperature lines tilted 45°, used to read stability, cloud base and CAPE.", "Carta sonde dengan garisan suhu condong 45°, untuk membaca kestabilan, dasar awan dan CAPE.")),
 ("inversion", T("逆温层", "Inversion", "Songsangan suhu"), T("气温随高度上升的一层，像盖子一样压住对流。", "A layer where temperature rises with height, acting as a lid on convection.", "Lapisan di mana suhu meningkat dengan ketinggian, bertindak sebagai penutup perolakan.")),
]

sources = [
 {"id": "NOAA-SKEWT", "short": "NOAA JetStream", "title": "Skew-T Log-P diagrams", "publisher": "NOAA National Weather Service, JetStream", "url": "https://www.noaa.gov/jetstream/upperair/skew-t-log-p-diagrams", "accessed": "2026-10-02"},
]

quiz = [
 {"stage": 7, "chapter": "ch25", "q": T("Skew-T 上，气温线和露点线很靠近表示什么？", "On a Skew-T, temperature and dew-point lines close together mean…", "Pada Skew-T, garisan suhu dan takat embun yang rapat bermaksud…"),
  "options": [T("那一层很湿，接近饱和", "That layer is moist, near saturation", "Lapisan itu lembap, hampir tepu"), T("那一层很干", "That layer is dry", "Lapisan itu kering"), T("风很大", "Strong wind", "Angin kuat"), T("有逆温", "An inversion", "Songsangan")],
  "answer": 0, "why": T("气温接近露点，就接近饱和。", "Temperature near dew point means near saturation.", "Suhu hampir takat embun bermaksud hampir tepu.")},
 {"stage": 7, "chapter": "ch25", "q": T("逆温层对午后雷雨有什么影响？", "What does an inversion do to afternoon storms?", "Apakah kesan songsangan terhadap ribut petang?"),
  "options": [T("像盖子一样压住上升空气，要先被冲破", "It caps rising air and must be broken first", "Ia menutup udara yang naik dan mesti dipecahkan dahulu"), T("让雷雨更容易形成", "Makes storms easier", "Memudahkan ribut"), T("没有影响", "No effect", "Tiada kesan"), T("让气温下降", "Cools the ground", "Menyejukkan tanah")],
  "answer": 0, "why": T("逆温非常稳定。", "An inversion is very stable.", "Songsangan sangat stabil.")},
 {"stage": 7, "chapter": "ch25", "q": T("同一张早上的探空，下午哪种情况 CAPE 最大？", "Same morning sounding: which afternoon gives the most CAPE?", "Sonde pagi yang sama: petang mana memberi CAPE paling banyak?"),
  "options": [T("地面 31 °C、露点 23 °C", "Surface 31 °C, dew point 23 °C", "Permukaan 31 °C, takat embun 23 °C"), T("地面 31 °C、露点 20.8 °C", "Surface 31 °C, dew point 20.8 °C", "Permukaan 31 °C, takat embun 20.8 °C"), T("地面 24.8 °C、露点 20.8 °C", "Surface 24.8 °C, dew point 20.8 °C", "Permukaan 24.8 °C, takat embun 20.8 °C"), T("都一样", "All the same", "Semua sama")],
  "answer": 0, "why": T("又热又湿的地面空气，上升后比周围暖得最多。", "Hot, moist surface air ends up warmest relative to its surroundings.", "Udara permukaan panas dan lembap menjadi paling panas berbanding sekeliling.")},
]

write_chapter(chapter, terms, sources, quiz)
