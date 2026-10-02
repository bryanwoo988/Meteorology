"""Chapter 9 — Pressure and wind."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch09", "num": 9, "stage": 4,
 "title": T("气压与风", "Pressure and wind", "Tekanan dan angin"),
 "sources": ["PAM", "ESS", "TERM"],
 "sections": [
 {"id": "s1", "heading": T("高压和低压", "High and low pressure", "Tekanan tinggi dan rendah"), "level": "basic", "blocks": [
  P("同一高度上，各地的气压并不一样。把海平面气压相同的地点连成线，就是{{t:isobar}}。被等压线围起来、中心气压最高的地方是{{t:high-pressure}}，最低的是{{t:low-pressure}}。气象站会把读数换算到海平面，这样山上和海边才可以比较。",
    "Pressure at the same height is not the same everywhere. Lines joining places with equal sea-level pressure are {{t:isobar}}s. Where the isobars enclose the highest pressure is a {{t:high-pressure}}; where they enclose the lowest is a {{t:low-pressure}}. Stations convert their readings to sea level so that a hilltop and a beach can be compared.",
    "Tekanan pada ketinggian yang sama tidak sama di semua tempat. Garisan yang menghubungkan tempat dengan tekanan paras laut yang sama ialah {{t:isobar}}. Kawasan yang dikelilingi isobar dengan tekanan tertinggi ialah {{t:high-pressure}}; yang terendah ialah {{t:low-pressure}}. Stesen menukar bacaan ke paras laut supaya puncak bukit dan pantai boleh dibandingkan.",
    defines=["isobar", "high-pressure", "low-pressure"], src=["PAM:63-64", "ESS:156"]),
  {"type": "table", "src": ["PAM:71-72"],
   "caption": T("低压（气旋）和高压（反气旋）的天气", "Weather in lows (cyclones) and highs (anticyclones)", "Cuaca dalam tekanan rendah (siklon) dan tinggi (antisiklon)"),
   "headers": [T("项目", "Feature", "Ciri"), T("低压", "Low", "Rendah"), T("高压", "High", "Tinggi")],
   "rows": [[T("中心", "Centre", "Pusat"), T("气压最低，空气辐合上升", "Lowest pressure; air converges and rises", "Tekanan terendah; udara menumpu dan naik"), T("气压最高，空气下沉辐散", "Highest pressure; air sinks and spreads out", "Tekanan tertinggi; udara turun dan menyebar")],
            [T("天气", "Weather", "Cuaca"), T("多云，常下雨", "Cloudy, often rainy", "Berawan, kerap hujan"), T("少云，天气晴好", "Little cloud, fair weather", "Sedikit awan, cuaca baik")],
            [T("风", "Wind", "Angin"), T("越近中心越强", "Stronger towards the centre", "Lebih kuat ke arah pusat"), T("一般比较弱", "Generally light", "Biasanya lemah")]]},
 ]},
 {"id": "s2", "heading": T("推动风的力", "The forces that drive the wind", "Daya yang menggerakkan angin"), "level": "basic", "blocks": [
  P("气压本身不是力，气压的差才会产生力。从高压指向低压、推动空气的这个力叫{{t:pressure-gradient-force}}。等压线越密，气压变化越快，这个力越大，风越强。",
    "Pressure itself is not a force; a difference in pressure is. The push from high towards low pressure is the {{t:pressure-gradient-force}}. The closer the isobars, the faster pressure changes, the stronger the push and the stronger the wind.",
    "Tekanan itu sendiri bukan daya; perbezaan tekanan ialah daya. Tolakan dari tekanan tinggi ke rendah ialah {{t:pressure-gradient-force}}. Semakin rapat isobar, semakin cepat tekanan berubah, semakin kuat tolakan dan semakin kuat angin.",
    defines=["pressure-gradient-force"], src=["PAM:64", "ESS:158"]),
  P("地球在自转，从地面上看，移动中的空气会被偏转：北半球向右，南半球向左。这叫{{t:coriolis-effect}}。它不是真正推动空气的力，而是因为我们站在一个会转的地球上看。它在两极最强，在赤道是零，而且只影响风向、不影响风速；距离超过约 100 公里的运动才明显。",
    "The Earth spins, so from the ground moving air appears to be deflected: to the right in the Northern Hemisphere, to the left in the Southern. This is the {{t:coriolis-effect}}. It is not a real push but a result of watching from a rotating planet. It is strongest at the poles and zero at the equator, changes only the wind's direction, not its speed, and matters only for motions larger than about 100 km.",
    "Bumi berputar, jadi dari permukaan, udara yang bergerak kelihatan terpesong: ke kanan di Hemisfera Utara, ke kiri di Selatan. Inilah {{t:coriolis-effect}}. Ia bukan tolakan sebenar tetapi akibat melihat dari planet yang berputar. Ia paling kuat di kutub dan sifar di khatulistiwa, hanya mengubah arah angin, bukan kelajuannya, dan hanya penting bagi gerakan lebih besar daripada kira-kira 100 km.",
    defines=["coriolis-effect"], src=["PAM:65-66"]),
  P("在高空，气压梯度力和科里奥利力会互相平衡，风就沿着等压线吹，北半球低压在左手边，这种风叫地转风。贴近地面时，摩擦力把风减慢，风就会斜斜地穿过等压线吹向低压。摩擦力在森林和城市上空大，在水面上小，离地 1 公里以上就不太重要了。",
    "Aloft, the pressure-gradient force and the Coriolis effect balance and the wind blows along the isobars, with low pressure on its left in the Northern Hemisphere: the geostrophic wind. Near the ground, friction slows the wind and it crosses the isobars at an angle towards low pressure. Friction is strong over forest and cities, weak over water, and unimportant above about 1 km.",
    "Di udara atas, daya kecerunan tekanan dan kesan Coriolis seimbang dan angin bertiup sepanjang isobar, dengan tekanan rendah di sebelah kiri di Hemisfera Utara: angin geostrofik. Berhampiran permukaan, geseran memperlahankan angin dan ia merentasi isobar secara serong ke arah tekanan rendah. Geseran kuat di atas hutan dan bandar, lemah di atas air, dan tidak penting melebihi kira-kira 1 km.",
    src=["ESS:161-165", "PAM:66"]),
  {"type": "widget", "id": "W8"},
  N("key", "马来西亚离赤道很近，科里奥利力很弱，所以这里很少有中纬度那种大范围、有组织地旋转的风暴，风也常常直接从高压吹向低压。",
    "Malaysia is close to the equator, where the Coriolis effect is weak. That is why large, organised spinning storms of the middle-latitude kind are rare here, and why winds often blow more directly from high to low pressure.",
    "Malaysia berhampiran khatulistiwa, tempat kesan Coriolis lemah. Itulah sebabnya ribut berputar besar dan teratur jenis latitud sederhana jarang berlaku di sini, dan angin sering bertiup lebih terus dari tekanan tinggi ke rendah.",
    src=["PAM:66", "ESS:164"]),
  P("在北半球，空气绕着低压中心逆时针旋转并向中心汇聚，绕着高压中心顺时针旋转并向外散开；南半球方向相反。",
    "In the Northern Hemisphere air spirals anticlockwise into a low and clockwise out of a high; in the Southern Hemisphere the directions are reversed.",
    "Di Hemisfera Utara udara berpusar lawan arah jam masuk ke tekanan rendah dan ikut arah jam keluar dari tekanan tinggi; di Hemisfera Selatan arahnya terbalik.",
    src=["ESS:156"]),
 ]},
 {"id": "s3", "heading": T("平均风和阵风", "Average wind and gusts", "Angin purata dan tiupan kencang"), "level": "basic", "blocks": [
  P("天气预报和观测说的风速，通常是 10 分钟的平均值。比平均值突然高一下、又很快降回来的那一阵风，叫{{t:gust}}。雷雨云底下的阵风可以比平均风强很多，所以 Windy 等 App 会分开显示“风”和“阵风”。",
    "The wind speed in forecasts and reports is usually a 10-minute average. A sudden, brief burst above that average, followed by a lull, is a {{t:gust}}. Under a thunderstorm, gusts can be far stronger than the average wind, which is why apps such as Windy show ‘wind’ and ‘gusts’ separately.",
    "Kelajuan angin dalam ramalan dan laporan biasanya purata 10 minit. Lonjakan singkat dan tiba-tiba melebihi purata itu, diikuti reda, ialah {{t:gust}}. Di bawah ribut petir, tiupan kencang boleh jauh lebih kuat daripada angin purata, sebab itu aplikasi seperti Windy memaparkan ‘angin’ dan ‘tiupan kencang’ berasingan.",
    defines=["gust"], src=["TERM:155"]),
  P("没有仪器时，可以看风对周围东西的影响来估计风速，这就是{{t:beaufort-scale}}：0 级无风、烟直上；4 级吹起灰尘纸张；8 级折断小树枝、走路困难；12 级是飓风级。工具页有完整的对照表。",
    "Without instruments you can estimate wind speed from its effects on things around you: the {{t:beaufort-scale}}. Force 0 is calm, smoke rising straight up; force 4 lifts dust and paper; force 8 breaks twigs and makes walking hard; force 12 is hurricane force. The full table is among the tools.",
    "Tanpa alat, anda boleh menganggar kelajuan angin daripada kesannya pada benda di sekeliling: {{t:beaufort-scale}}. Skala 0 tenang, asap naik tegak; skala 4 menerbangkan debu dan kertas; skala 8 mematahkan ranting dan menyukarkan berjalan; skala 12 kekuatan taufan. Jadual penuh ada dalam alatan.",
    defines=["beaufort-scale"], src=["ESS:468"]),
 ]},
 {"id": "s4", "heading": T("海风、陆风、山风、谷风", "Sea, land, mountain and valley breezes", "Bayu laut, bayu darat, angin gunung dan lembah"), "level": "basic", "blocks": [
  P("白天陆地比海热得快，陆地上的空气受热上升、气压变低，海上比较凉的空气就吹向陆地，这是{{t:sea-breeze}}。晚上陆地冷得比海快，方向反过来，空气从陆地吹向海，这是{{t:land-breeze}}，一般比海风弱。",
    "By day the land heats faster than the sea; air over the land warms, rises and leaves lower pressure, so cooler air from the sea blows inland: the {{t:sea-breeze}}. At night the land cools faster, the pattern reverses and air flows from land to sea: the {{t:land-breeze}}, usually weaker.",
    "Pada siang hari daratan memanas lebih cepat daripada laut; udara di atas darat memanas, naik dan meninggalkan tekanan lebih rendah, jadi udara lebih sejuk dari laut bertiup ke darat: {{t:sea-breeze}}. Pada waktu malam daratan menyejuk lebih cepat, corak terbalik dan udara mengalir dari darat ke laut: {{t:land-breeze}}, biasanya lebih lemah.",
    defines=["sea-breeze", "land-breeze"], src=["PAM:73-74", "ESS:182-183"]),
  P("山区也一样：白天山坡被晒热，空气沿着山坡往上吹，叫谷风；晚上山坡冷却，冷空气沿坡往下流进山谷，叫山风。",
    "Hills do the same: by day the sunlit slopes warm and air blows up them — the valley breeze; at night the slopes cool and cold air drains down into the valleys — the mountain breeze.",
    "Kawasan berbukit juga begitu: pada siang hari cerun yang disinari memanas dan udara bertiup ke atasnya — angin lembah; pada waktu malam cerun menyejuk dan udara sejuk mengalir turun ke lembah — angin gunung.",
    src=["PAM:72-73"]),
  N("key", "🌦️ 午后阵雨的第四块拼图：在美国的佛罗里达半岛，东西两边的海风白天同时吹进内陆，在半岛中间相撞，空气被迫上升，配合白天的对流，下午就长出云和阵雨，而海面上反而晴朗。马来半岛同样是夹在两个海之间的狭长半岛——第 17 章会看这件事在这里怎样发生。",
    "🌦️ Afternoon storms, piece four: on the Florida peninsula, sea breezes push inland from both coasts by day and collide in the middle; the air is forced up and, together with daytime convection, grows afternoon clouds and showers while the sea stays clear. Peninsular Malaysia is likewise a narrow peninsula between two seas — Chapter 17 looks at how this plays out here.",
    "🌦️ Ribut petang, kepingan keempat: di semenanjung Florida, bayu laut menolak ke darat dari kedua-dua pantai pada siang hari dan bertembung di tengah; udara dipaksa naik dan, bersama perolakan siang, menumbuhkan awan dan hujan petang sementara laut kekal cerah. Semenanjung Malaysia juga semenanjung sempit di antara dua laut — Bab 17 melihat bagaimana ini berlaku di sini.",
    src=["ESS:183-184"]),
 ]},
 {"id": "s5", "heading": T("风的尺度", "Scales of wind", "Skala angin"), "level": "advanced", "blocks": [
  {"type": "keyval", "src": ["ESS:178", "PAM:69-72"], "rows": [
   {"k": T("微尺度", "Microscale", "Skala mikro"), "v": T("几米以内、几分钟：吹动树枝、卷起尘土的小涡旋", "Metres and minutes: the small eddies that sway branches and swirl dust", "Beberapa meter dan minit: pusaran kecil yang menggoyang dahan dan memusar debu")},
   {"k": T("中尺度", "Mesoscale", "Skala meso"), "v": T("几公里到约 100 公里、几小时：海陆风、山谷风、雷暴", "A few km to about 100 km, hours: sea and mountain breezes, thunderstorms", "Beberapa km hingga kira-kira 100 km, beberapa jam: bayu laut dan gunung, ribut petir")},
   {"k": T("天气尺度", "Synoptic scale", "Skala sinoptik"), "v": T("几百到几千公里、几天：高压、低压、季风、热带气旋", "Hundreds to thousands of km, days: highs, lows, monsoons, tropical cyclones", "Ratusan hingga ribuan km, beberapa hari: tekanan tinggi, rendah, monsun, siklon tropika")},
   {"k": T("行星尺度", "Planetary scale", "Skala planet"), "v": T("整个地球：信风、西风带（第 11 章）", "The whole Earth: trade winds and westerlies (Chapter 11)", "Seluruh Bumi: angin pasat dan angin barat (Bab 11)")}]},
  P("气压每天还有很规律的小起伏：一天两次高、两次低，大约在上午和晚上 10 点最高、下午和清晨 4 点最低，这是太阳加热造成的“大气潮”，在热带特别明显。",
    "Pressure also rises and falls a little twice a day with clockwork regularity — highest around 10 am and 10 pm, lowest around 4 pm and 4 am. This ‘atmospheric tide’ is driven by solar heating and is especially clear in the tropics.",
    "Tekanan juga naik dan turun sedikit dua kali sehari dengan sangat teratur — paling tinggi sekitar jam 10 pagi dan 10 malam, paling rendah sekitar jam 4 petang dan 4 pagi. ‘Pasang surut atmosfera’ ini didorong pemanasan suria dan amat jelas di kawasan tropika.",
    src=["PAM:63"]),
 ]},
 ]}

terms = [
 ("isobar", T("等压线", "Isobar", "Isobar"), T("地图上连接海平面气压相同地点的线。", "A line on a map joining places of equal sea-level pressure.", "Garisan pada peta yang menghubungkan tempat bertekanan paras laut sama.")),
 ("high-pressure", T("高压", "High pressure", "Tekanan tinggi"), T("气压比周围高的区域；空气下沉，天气多晴好。", "An area of higher pressure than its surroundings; air sinks and the weather is usually fair.", "Kawasan bertekanan lebih tinggi daripada sekeliling; udara turun dan cuaca biasanya baik.")),
 ("low-pressure", T("低压", "Low pressure", "Tekanan rendah"), T("气压比周围低的区域；空气辐合上升，多云多雨。", "An area of lower pressure than its surroundings; air converges and rises, bringing cloud and rain.", "Kawasan bertekanan lebih rendah daripada sekeliling; udara menumpu dan naik, membawa awan dan hujan.")),
 ("pressure-gradient-force", T("气压梯度力", "Pressure-gradient force", "Daya kecerunan tekanan"), T("由气压差产生、从高压推向低压的力；等压线越密越强。", "The push from high to low pressure caused by a pressure difference; stronger where isobars are close.", "Tolakan dari tekanan tinggi ke rendah akibat perbezaan tekanan; lebih kuat apabila isobar rapat.")),
 ("coriolis-effect", T("科里奥利力", "Coriolis effect", "Kesan Coriolis"), T("地球自转使移动的空气看起来被偏转：北半球向右；赤道上为零。", "The apparent deflection of moving air by the Earth's spin: to the right in the north; zero at the equator.", "Pesongan ketara udara bergerak akibat putaran Bumi: ke kanan di utara; sifar di khatulistiwa.")),
 ("gust", T("阵风", "Gust", "Tiupan kencang"), T("比 10 分钟平均风速突然高出、又很快减弱的一阵风。", "A sudden, short burst above the 10-minute average wind speed.", "Lonjakan singkat dan tiba-tiba melebihi kelajuan angin purata 10 minit.")),
 ("beaufort-scale", T("蒲福风级", "Beaufort scale", "Skala Beaufort"), T("按风对周围事物的影响把风速分成 0–12 级。", "Wind speed graded 0–12 by its effects on things around you.", "Kelajuan angin dikelaskan 0–12 mengikut kesannya pada benda di sekeliling.")),
 ("sea-breeze", T("海风", "Sea breeze", "Bayu laut"), T("白天陆地比海热，空气从海面吹向陆地。", "By day the land is warmer than the sea, and air blows from sea to land.", "Pada siang hari darat lebih panas daripada laut, dan udara bertiup dari laut ke darat.")),
 ("land-breeze", T("陆风", "Land breeze", "Bayu darat"), T("晚上陆地比海冷，空气从陆地吹向海面。", "At night the land is cooler than the sea, and air blows from land to sea.", "Pada waktu malam darat lebih sejuk daripada laut, dan udara bertiup dari darat ke laut.")),
]

quiz = [
 {"stage": 4, "chapter": "ch09", "q": T("地图上等压线很密，表示什么？", "What do closely spaced isobars mean?", "Apakah maksud isobar yang rapat?"),
  "options": [T("风很弱", "Light winds", "Angin lemah"), T("风很强", "Strong winds", "Angin kuat"), T("一定下雨", "It must rain", "Pasti hujan"), T("气温很高", "High temperature", "Suhu tinggi")],
  "answer": 1, "why": T("气压变化快，气压梯度力大，风就强。", "Pressure changes quickly, the pressure-gradient force is large, so the wind is strong.", "Tekanan berubah cepat, daya kecerunan tekanan besar, jadi angin kuat.")},
 {"stage": 4, "chapter": "ch09", "q": T("为什么赤道附近很少有大型旋转风暴？", "Why are large spinning storms rare right at the equator?", "Mengapa ribut berputar besar jarang berlaku tepat di khatulistiwa?"),
  "options": [T("那里太热", "It is too hot", "Terlalu panas"), T("科里奥利力在赤道接近零", "The Coriolis effect is close to zero there", "Kesan Coriolis hampir sifar di situ"), T("那里没有海", "There is no sea there", "Tiada laut di situ"), T("那里气压太高", "Pressure is too high", "Tekanan terlalu tinggi")],
  "answer": 1, "why": T("没有科里奥利力，辐合的空气不会开始旋转。", "Without the Coriolis effect, converging air does not start to spin.", "Tanpa kesan Coriolis, udara yang menumpu tidak mula berputar.")},
 {"stage": 4, "chapter": "ch09", "q": T("海风在什么时候吹？", "When does the sea breeze blow?", "Bilakah bayu laut bertiup?"),
  "options": [T("白天，从海吹向陆地", "By day, from sea to land", "Pada siang, dari laut ke darat"), T("晚上，从海吹向陆地", "At night, from sea to land", "Pada malam, dari laut ke darat"), T("白天，从陆地吹向海", "By day, from land to sea", "Pada siang, dari darat ke laut"), T("只在下雨时", "Only when it rains", "Hanya ketika hujan")],
  "answer": 0, "why": T("白天陆地比海热，陆地气压较低，凉的海风吹进来。", "By day the land is hotter and its pressure lower, so cool sea air flows in.", "Pada siang hari darat lebih panas dan tekanannya lebih rendah, jadi udara laut yang sejuk mengalir masuk.")},
]

write_chapter(chapter, terms, [], quiz)
