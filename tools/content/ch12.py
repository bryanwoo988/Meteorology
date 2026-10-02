"""Chapter 12 — Air masses, fronts and storms."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch12", "num": 12, "stage": 4,
 "title": T("气团、锋面与风暴", "Air masses, fronts and storms", "Jisim udara, front dan ribut"),
 "sources": ["ESS", "PAM", "TERM", "CHANG2003", "METMY-SWM2024"],
 "sections": [
 {"id": "s1", "heading": T("气团和锋面", "Air masses and fronts", "Jisim udara dan front"), "level": "basic", "blocks": [
  P("一大块温度和湿度都差不多的空气，范围可以有上千公里、厚几公里，叫{{t:air-mass}}。它的性质来自它形成的地方：在热带海洋上形成的又暖又湿，在大陆内部形成的比较干。",
    "A huge body of air with nearly the same temperature and humidity throughout — a thousand kilometres or more across and several kilometres deep — is an {{t:air-mass}}. It takes its character from where it formed: over tropical seas it is warm and moist; deep inside a continent it is drier.",
    "Kumpulan udara yang sangat besar dengan suhu dan kelembapan hampir sama di seluruhnya — seribu kilometer atau lebih lebar dan beberapa kilometer dalam — ialah {{t:air-mass}}. Ia mendapat cirinya daripada tempat ia terbentuk: di atas laut tropika ia panas dan lembap; jauh di dalam benua ia lebih kering.",
    defines=["air-mass"], src=["TERM:13"]),
  P("两个性质不同的气团交界的地方叫{{t:front}}。冷锋是冷空气推进、把暖空气抬起，常带来短时间的雷阵雨；暖锋是暖空气慢慢爬到冷空气上面，带来范围大、时间长的毛毛雨。锋面是中纬度天气的主角；在马来西亚这样的赤道地区，冷暖气团的差别小，典型的锋面很少见。",
    "The boundary between two different air masses is a {{t:front}}. At a cold front the cold air pushes forward and lifts the warm air, often bringing short, thundery showers; at a warm front the warm air slides slowly up over the cold, bringing widespread, long-lasting drizzle. Fronts dominate middle-latitude weather; near the equator, as in Malaysia, air masses differ too little for classic fronts to be common.",
    "Sempadan antara dua jisim udara yang berbeza ialah {{t:front}}. Di front sejuk, udara sejuk menolak ke hadapan dan mengangkat udara panas, sering membawa hujan ribut yang singkat; di front panas, udara panas menggelongsor perlahan ke atas udara sejuk, membawa gerimis yang meluas dan berpanjangan. Front menguasai cuaca latitud sederhana; berhampiran khatulistiwa, seperti di Malaysia, jisim udara terlalu sedikit bezanya untuk front klasik menjadi biasa.",
    defines=["front"], src=["PAM:87", "ESS:229"]),
 ]},
 {"id": "s2", "heading": T("雷暴的一生", "The life of a thunderstorm", "Kitaran hidup ribut petir"), "level": "basic", "blocks": [
  P("{{t:thunderstorm}}就是有雷有电的积雨云。一个普通的雷暴从出生到消散通常不到一小时，分三个阶段：",
    "A {{t:thunderstorm}} is a cumulonimbus cloud with thunder and lightning. An ordinary one goes from birth to decay in less than an hour, in three stages:",
    "{{t:thunderstorm}} ialah awan kumulonimbus dengan guruh dan kilat. Ribut biasa melalui kelahiran hingga reput dalam kurang sejam, dalam tiga peringkat:",
    defines=["thunderstorm"], src=["ESS:275"]),
  {"type": "keyval", "src": ["ESS:275-277"], "rows": [
   {"k": T("积云阶段", "Cumulus stage", "Peringkat kumulus"), "v": T("上升气流把暖湿空气送上去，积云几分钟内就长成浓积云；还没下雨。", "Updraughts carry warm, moist air up and the cumulus grows into a towering cumulus within minutes; no rain yet.", "Arus naik membawa udara panas lembap ke atas dan kumulus tumbuh menjadi kumulus menjulang dalam beberapa minit; belum hujan.")},
   {"k": T("成熟阶段", "Mature stage", "Peringkat matang"), "v": T("雨开始落下，把空气拖下来成为下沉气流；雷电、暴雨、强阵风都在这时；云顶在稳定层摊开成铁砧状。", "Rain begins to fall and drags air down as a downdraught; lightning, downpours and strong gusts all come now; the top spreads into an anvil at a stable layer.", "Hujan mula turun dan menyeret udara ke bawah sebagai arus turun; kilat, hujan lebat dan tiupan kencang berlaku sekarang; puncak merebak menjadi andas di lapisan stabil.")},
   {"k": T("消散阶段", "Dissipating stage", "Peringkat lerai"), "v": T("进入成熟阶段约 15 到 30 分钟后，下沉气流占满了云，切断暖湿空气的来源，雨渐渐停。", "About 15 to 30 minutes after maturity, downdraughts fill the cloud, cut off its supply of warm, moist air, and the rain dies away.", "Kira-kira 15 hingga 30 minit selepas matang, arus turun memenuhi awan, memutuskan bekalan udara panas lembap, dan hujan beransur berhenti.")}]},
  N("key", "🌦️ 午后阵雨的第五块拼图：这就是为什么马来西亚的午后雷雨常常“来得猛、去得快”——一个雷暴单体通常一小时左右就结束了。",
    "🌦️ Afternoon storms, piece five: this is why Malaysia's afternoon storms so often arrive hard and leave fast — a single thunderstorm cell is usually over within about an hour.",
    "🌦️ Ribut petang, kepingan kelima: inilah sebabnya ribut petang di Malaysia sering datang dengan kuat dan pergi dengan cepat — satu sel ribut petir biasanya berakhir dalam kira-kira sejam.",
    src=["ESS:275", "ESS:286"]),
  P("如果高空风比较强，新的雷暴单体会在旧单体旁边不断长出来，形成可以维持好几个小时的多单体雷暴，有时排成一长条，叫飑线。第 17 章的苏门答腊飑线就是这一类。",
    "When the winds aloft are stronger, new cells keep forming beside the old ones and a multicell storm can last for hours; sometimes the cells line up in a long squall line. The Sumatra squalls of Chapter 17 are of this kind.",
    "Apabila angin di udara atas lebih kuat, sel baharu terus terbentuk di sebelah sel lama dan ribut berbilang sel boleh bertahan berjam-jam; kadangkala sel-sel tersusun dalam garisan badai yang panjang. Badai Sumatera dalam Bab 17 adalah jenis ini.",
    src=["ESS:278", "ESS:281"]),
 ]},
 {"id": "s3", "heading": T("闪电和安全", "Lightning and staying safe", "Kilat dan keselamatan"), "level": "basic", "blocks": [
  P("积雨云里冰粒和水滴互相碰撞，使云的上部带正电、下部带负电，地面上则感应出正电，而且集中在树、杆子、建筑物和人这些突出的东西上。电位差大到空气挡不住时，就放电成为{{t:lightning}}。一次闪电的电流可以高达 10 万安培。",
    "Inside a cumulonimbus, colliding ice and water particles leave the top of the cloud positively charged and the lower part negative, while positive charge gathers on the ground below — concentrated on tall objects such as trees, poles, buildings and people. When the difference grows too large for the air to hold back, it discharges as {{t:lightning}}. A single stroke can carry a current of 100,000 amperes.",
    "Di dalam kumulonimbus, zarah ais dan air yang berlanggar menjadikan bahagian atas awan bercas positif dan bahagian bawah negatif, manakala cas positif berkumpul di tanah di bawah — tertumpu pada objek tinggi seperti pokok, tiang, bangunan dan manusia. Apabila perbezaan terlalu besar untuk ditahan udara, ia dilepaskan sebagai {{t:lightning}}. Satu sambaran boleh membawa arus 100,000 ampere.",
    defines=["lightning"], src=["ESS:291-292", "ESS:296"]),
  N("warn", "在园里或户外遇到雷暴：最好马上进入建筑物，或坐进有金属车身的汽车、卡车（高尔夫球车不算）；不要躲在孤立的树下，也要远离高处。找不到遮蔽时，尽量蹲低、只用脚尖或脚跟着地，但不要趴下。头发竖起、皮肤发麻、听到嗒嗒声，就是闪电快要打下来的警告。在室内也不要用接电线的电器、有线电话，不要洗澡。",
    "Caught by a thunderstorm in the field or outdoors: get into a building, or into a car or truck with a metal body (a golf cart does not count). Do not shelter under an isolated tree and keep off high ground. With no shelter, crouch as low as you can touching the ground only with your toes or heels — but do not lie down. Hair standing on end, tingling skin and clicking sounds warn that a strike is imminent. Indoors, avoid electrical appliances, corded phones and showers.",
    "Ditimpa ribut petir di ladang atau di luar: masuk ke bangunan, atau ke dalam kereta atau lori berbadan logam (kereta golf tidak dikira). Jangan berteduh di bawah pokok yang terpencil dan jauhi tempat tinggi. Jika tiada tempat berlindung, bertinggung serendah mungkin dengan hanya hujung jari kaki atau tumit menyentuh tanah — tetapi jangan berbaring. Rambut tegak, kulit kesemutan dan bunyi berdetik memberi amaran sambaran akan berlaku. Di dalam rumah, elakkan perkakas elektrik, telefon berwayar dan mandi.",
    src=["ESS:296"]),
  N("myth", "“闪电不会打同一个地方两次”——错。闪电偏爱又高又突出的东西，同一个高处会被打很多次，这正是避雷针的原理。",
    "‘Lightning never strikes the same place twice’ — wrong. Lightning favours tall, prominent objects, and the same high point can be struck again and again; that is exactly how a lightning rod works.",
    "‘Kilat tidak menyambar tempat yang sama dua kali’ — salah. Kilat memilih objek yang tinggi dan menonjol, dan titik tinggi yang sama boleh disambar berulang kali; begitulah cara penangkal kilat berfungsi.",
    src=["ESS:291-294"]),
 ]},
 {"id": "s4", "heading": T("热带气旋", "Tropical cyclones", "Siklon tropika"), "level": "basic", "blocks": [
  P("{{t:tropical-cyclone}}是在暖洋面上形成、绕着低压中心旋转的巨大风暴群。在西北太平洋叫台风，在大西洋叫飓风，在印度洋叫气旋。它按风力分级：一群有组织的雷雨刚开始绕圈、风速约 20 到 34 节时，叫{{t:tropical-depression}}；35 到 64 节叫热带风暴（这时会取名字）；超过 64 节才叫台风或飓风。",
    "A {{t:tropical-cyclone}} is a vast, spinning system of storms formed over warm ocean around a centre of low pressure. In the western North Pacific it is called a typhoon, in the Atlantic a hurricane, in the Indian Ocean a cyclone. It is graded by wind: when an organised cluster of thunderstorms begins to circulate with winds of about 20–34 knots it is a {{t:tropical-depression}}; at 35–64 knots a tropical storm, which gets a name; above 64 knots a typhoon or hurricane.",
    "{{t:tropical-cyclone}} ialah sistem ribut berputar yang sangat besar, terbentuk di atas lautan panas di sekeliling pusat tekanan rendah. Di Pasifik Barat Laut ia dipanggil taufan, di Atlantik hurikan, di Lautan Hindi siklon. Ia dikelaskan mengikut angin: apabila kelompok ribut petir yang teratur mula berpusar dengan angin kira-kira 20–34 knot ia ialah {{t:tropical-depression}}; pada 35–64 knot ribut tropika, yang diberi nama; melebihi 64 knot taufan atau hurikan.",
    defines=["tropical-cyclone", "tropical-depression"], src=["ESS:314", "ESS:320"]),
  P("它需要几个条件：大范围的暖海水（通常 26.5 °C 以上）、很深的潮湿空气、微弱的高空风，以及足够的科里奥利力让辐合的空气开始旋转。所以热带气旋多半在纬度 5° 到 20° 之间形成，赤道上几乎不会有。",
    "It needs several ingredients: a large area of warm sea, usually 26.5 °C or more; moist air through a deep layer; light winds aloft; and enough Coriolis effect to set converging air spinning. That is why tropical cyclones mostly form between about 5° and 20° latitude and almost never on the equator.",
    "Ia memerlukan beberapa bahan: kawasan laut panas yang luas, biasanya 26.5 °C atau lebih; udara lembap dalam lapisan yang dalam; angin lemah di udara atas; dan kesan Coriolis yang cukup untuk memusarkan udara yang menumpu. Itulah sebabnya siklon tropika kebanyakannya terbentuk antara kira-kira latitud 5° dan 20° dan hampir tidak pernah di khatulistiwa.",
    src=["ESS:317"]),
  {"type": "map", "id": "M3"},
  N("tip", "马来西亚大部分地方在赤道附近这条“几乎没有台风”的带子里，台风很少直接登陆，但附近海域的台风可以间接影响这里的天气，例如牵动季风的气流。罕见的例外是 2001 年 12 月 27 日在新加坡附近北纬 1.5° 形成的台风画眉（Vamei），它是有记录以来离赤道最近形成的热带气旋。",
    "Most of Malaysia lies in the near-equatorial belt where typhoons almost never form, so direct landfalls are rare — though typhoons in nearby seas can affect the weather here indirectly, for example by steering the monsoon flow. A rare exception was Typhoon Vamei, which formed at 1.5°N near Singapore on 27 December 2001: the closest to the equator a tropical cyclone has been recorded forming.",
    "Kebanyakan Malaysia terletak dalam jalur hampir khatulistiwa tempat taufan hampir tidak pernah terbentuk, jadi pendaratan terus jarang berlaku — walaupun taufan di laut berhampiran boleh menjejaskan cuaca di sini secara tidak langsung, contohnya dengan memandu aliran monsun. Pengecualian yang jarang ialah Taufan Vamei, yang terbentuk pada 1.5°U berhampiran Singapura pada 27 Disember 2001: siklon tropika paling dekat dengan khatulistiwa yang pernah direkodkan terbentuk.",
    src=["CHANG2003", "ESS:317", "METMY-SWM2024"]),
 ]},
 ]}

terms = [
 ("air-mass", T("气团", "Air mass", "Jisim udara"), T("温度、湿度都很均匀的一大块空气，可达上千公里。", "A huge body of air with nearly uniform temperature and humidity, a thousand kilometres or more across.", "Kumpulan udara yang sangat besar dengan suhu dan kelembapan hampir seragam, seribu kilometer atau lebih.")),
 ("front", T("锋面", "Front", "Front"), T("两个性质不同的气团之间的交界。", "The boundary between two different air masses.", "Sempadan antara dua jisim udara yang berbeza.")),
 ("thunderstorm", T("雷暴", "Thunderstorm", "Ribut petir"), T("有雷有电的积雨云；普通雷暴一小时内走完一生。", "A cumulonimbus with thunder and lightning; an ordinary one lives less than an hour.", "Kumulonimbus dengan guruh dan kilat; yang biasa hidup kurang sejam.")),
 ("lightning", T("闪电", "Lightning", "Kilat"), T("雷雨云里或云和地面之间的巨大放电。", "A giant electrical discharge within a storm cloud or between cloud and ground.", "Nyahcas elektrik yang besar dalam awan ribut atau antara awan dan tanah.")),
 ("tropical-cyclone", T("热带气旋", "Tropical cyclone", "Siklon tropika"), T("在暖海上形成、绕低压中心旋转的大风暴；台风、飓风、气旋都是它。", "A great spinning storm over warm sea around a low-pressure centre; typhoons, hurricanes and cyclones are all tropical cyclones.", "Ribut besar berputar di atas laut panas di sekeliling pusat tekanan rendah; taufan, hurikan dan siklon semuanya siklon tropika.")),
 ("tropical-depression", T("热带低压", "Tropical depression", "Lekukan tropika"), T("刚开始旋转、风速约 20–34 节的热带气旋初期阶段。", "The early stage of a tropical cyclone, circulating with winds of about 20–34 knots.", "Peringkat awal siklon tropika, berpusar dengan angin kira-kira 20–34 knot.")),
]

sources = [
 {"id": "METMY-SWM2024", "short": "MetMalaysia 2025", "title": "Review of the Southwest Monsoon 2024 in Malaysia (Research Publication No. 2/2025)", "publisher": "N. Mohd Rashid, W. F. Mustafah, Z. A. Mokhtar & M. F. A. Abdullah, Malaysian Meteorological Department, December 2025", "url": "https://www.met.gov.my/data/research/researchpapers/2025/RP04_2025.pdf", "accessed": "2026-10-02"},
 {"id": "CHANG2003", "short": "Chang et al. 2003", "title": "Typhoon Vamei: An equatorial tropical cyclone formation", "publisher": "C.-P. Chang, C.-H. Liu & H.-C. Kuo, Geophysical Research Letters 30(3), 2003", "url": "https://doi.org/10.1029/2002GL016365", "accessed": "2026-10-02"},
]

quiz = [
 {"stage": 4, "chapter": "ch12", "q": T("普通雷暴从出生到消散大约多久？", "How long does an ordinary thunderstorm usually last from birth to decay?", "Berapa lama biasanya ribut petir biasa dari lahir hingga lerai?"),
  "options": [T("不到一小时", "Less than an hour", "Kurang sejam"), T("一整天", "A whole day", "Sehari suntuk"), T("一个星期", "A week", "Seminggu"), T("几分钟", "A few minutes", "Beberapa minit")],
  "answer": 0, "why": T("下沉气流很快占满整朵云，切断了暖湿空气的来源。", "Downdraughts soon fill the cloud and cut off its supply of warm, moist air.", "Arus turun segera memenuhi awan dan memutuskan bekalan udara panas lembap.")},
 {"stage": 4, "chapter": "ch12", "q": T("在空旷的园里遇到雷暴，哪个做法最危险？", "Caught in an open field in a thunderstorm, which is most dangerous?", "Ditimpa ribut petir di ladang terbuka, yang manakah paling berbahaya?"),
  "options": [T("躲到一棵孤立的大树下", "Sheltering under a lone tall tree", "Berteduh di bawah pokok tinggi yang terpencil"), T("坐进金属车身的卡车", "Getting into a metal-bodied truck", "Masuk ke dalam lori berbadan logam"), T("进入建筑物", "Going into a building", "Masuk ke dalam bangunan"), T("离开高处", "Leaving high ground", "Meninggalkan tempat tinggi")],
  "answer": 0, "why": T("突出的物体最容易被闪电打中，许多闪电伤亡都发生在孤立的树附近。", "Tall, prominent objects are struck most; many lightning casualties happen near isolated trees.", "Objek tinggi dan menonjol paling kerap disambar; banyak mangsa kilat berlaku berhampiran pokok terpencil.")},
 {"stage": 4, "chapter": "ch12", "q": T("热带气旋为什么几乎不在赤道上形成？", "Why do tropical cyclones almost never form on the equator?", "Mengapa siklon tropika hampir tidak pernah terbentuk di khatulistiwa?"),
  "options": [T("那里海水不够暖", "The sea is not warm enough", "Laut tidak cukup panas"), T("科里奥利力几乎为零，辐合的空气转不起来", "The Coriolis effect is almost zero, so converging air does not spin", "Kesan Coriolis hampir sifar, jadi udara yang menumpu tidak berputar"), T("那里没有雷雨", "There are no thunderstorms there", "Tiada ribut petir di sana"), T("那里风太强", "The wind is too strong", "Angin terlalu kuat")],
  "answer": 1, "why": T("热带气旋要靠科里奥利力开始旋转，所以多在 5° 到 20° 之间形成。", "They need the Coriolis effect to start spinning, so most form between 5° and 20°.", "Ia memerlukan kesan Coriolis untuk mula berputar, jadi kebanyakannya terbentuk antara 5° dan 20°.")},
]

write_chapter(chapter, terms, sources, quiz)
