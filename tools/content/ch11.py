"""Chapter 11 — The global circulation."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch11", "num": 11, "stage": 4,
 "title": T("全球环流", "The global circulation", "Peredaran global"),
 "sources": ["PAM", "ESS"],
 "sections": [
 {"id": "s1", "heading": T("热带太热，两极太冷", "Too much heat at the equator, too little at the poles", "Terlalu banyak haba di khatulistiwa, terlalu sedikit di kutub"), "level": "basic", "blocks": [
  P("热带一年到头收到的阳光比送出去的热多，两极则相反。大气和海洋就像一部巨大的热机，不停把多余的热从赤道搬往两极。如果地球不转，这会是一个简单的大环流；但地球在转，科里奥利力把它拆成了南北半球各三个环流圈。",
    "The tropics receive more sunshine than they lose as heat all year round; the poles do the opposite. The atmosphere and oceans act like a vast heat engine, carrying the surplus from the equator towards the poles. On a non-spinning Earth this would be one simple loop; the spin, through the Coriolis effect, breaks it into three cells in each hemisphere.",
    "Kawasan tropika menerima lebih banyak cahaya matahari daripada haba yang hilang sepanjang tahun; kutub sebaliknya. Atmosfera dan lautan bertindak seperti enjin haba yang besar, membawa lebihan dari khatulistiwa ke kutub. Pada Bumi yang tidak berputar ini akan menjadi satu gelung mudah; putaran, melalui kesan Coriolis, memecahkannya kepada tiga sel di setiap hemisfera.",
    src=["ESS:194", "PAM:67"]),
 ]},
 {"id": "s2", "heading": T("三圈环流和气压带", "Three cells and the pressure belts", "Tiga sel dan jalur tekanan"), "level": "basic", "blocks": [
  P("赤道附近空气受热上升，在高空流向两极，到了约 30° 下沉，再从地面流回赤道。这个最靠近赤道的环流圈叫{{t:hadley-cell}}。下沉的地方形成{{t:subtropical-high}}，那里晴朗干燥，世界上许多大沙漠都在这一带。",
    "Near the equator air is heated and rises, flows poleward aloft, sinks near 30° and returns to the equator along the surface. This loop nearest the equator is the {{t:hadley-cell}}. Where it sinks, the {{t:subtropical-high}} forms: clear and dry, home to many of the world's great deserts.",
    "Berhampiran khatulistiwa udara dipanaskan dan naik, mengalir ke kutub di udara atas, turun berhampiran 30° dan kembali ke khatulistiwa sepanjang permukaan. Gelung paling dekat khatulistiwa ini ialah {{t:hadley-cell}}. Di tempat ia turun, {{t:subtropical-high}} terbentuk: cerah dan kering, tempat banyak gurun besar dunia.",
    defines=["hadley-cell", "subtropical-high"], src=["ESS:194-196", "PAM:68"]),
  P("从副热带高压吹回赤道的地面风，被科里奥利力偏转，北半球成了东北风，南半球成了东南风，这就是{{t:trade-winds}}。东北信风和东南信风在赤道附近相遇的地带叫{{t:itcz}}：空气在这里辐合上升，长出巨大的雷雨云，雨量非常多。ITCZ 里风很弱，旧时的帆船常被困住，所以也叫赤道无风带。",
    "The surface air flowing back from the subtropical highs to the equator is turned by the Coriolis effect into north-easterlies in the Northern Hemisphere and south-easterlies in the Southern: the {{t:trade-winds}}. Where the north-east and south-east trades meet near the equator is the {{t:itcz}}: air converges and rises, building huge thunderclouds and very heavy rain. Winds there are light — sailing ships used to be stranded — hence its old name, the doldrums.",
    "Udara permukaan yang mengalir kembali dari tekanan tinggi subtropika ke khatulistiwa dipesongkan oleh kesan Coriolis menjadi angin timur laut di Hemisfera Utara dan tenggara di Selatan: {{t:trade-winds}}. Tempat angin pasat timur laut dan tenggara bertemu berhampiran khatulistiwa ialah {{t:itcz}}: udara menumpu dan naik, membina awan ribut yang besar dan hujan sangat lebat. Angin di sana lemah — kapal layar dahulu sering terkandas — sebab itu nama lamanya kawasan tenang khatulistiwa (doldrum).",
    defines=["trade-winds", "itcz"], src=["ESS:194-195", "PAM:68-70"]),
  P("在 30° 到 60° 之间，地面风由西向东吹，叫{{t:westerlies}}；这一带的环流圈叫{{t:ferrel-cell}}。约 60° 是副极地低压，冷暖空气在这里交锋，形成极锋。60° 以外的{{t:polar-cell}}里，冷空气从极地高压吹出，成为极地东风。",
    "Between 30° and 60° the surface winds blow from west to east — the {{t:westerlies}} — in the {{t:ferrel-cell}}. Near 60° lie the subpolar lows, where cold and warm air meet along the polar front. Beyond 60°, in the {{t:polar-cell}}, cold air flows out of the polar highs as the polar easterlies.",
    "Antara 30° dan 60° angin permukaan bertiup dari barat ke timur — {{t:westerlies}} — dalam {{t:ferrel-cell}}. Berhampiran 60° terletak tekanan rendah subkutub, tempat udara sejuk dan panas bertemu di sepanjang front kutub. Melepasi 60°, dalam {{t:polar-cell}}, udara sejuk mengalir keluar dari tekanan tinggi kutub sebagai angin timur kutub.",
    defines=["westerlies", "ferrel-cell", "polar-cell"], src=["ESS:196", "PAM:68-71"]),
  {"type": "map", "id": "M2"},
 ]},
 {"id": "s3", "heading": T("随季节移动", "Shifting with the seasons", "Beralih mengikut musim"), "level": "basic", "blocks": [
  P("太阳 7 月直射北半球，1 月直射南半球，最热的带子跟着移动，气压带、风带和 ITCZ 也一起移动：7 月偏北，1 月偏南，一年来回大约 10 到 15 度。经过的地方雨量就多，离开后就变干，热带许多地方的雨季和旱季就是这样来的。",
    "The Sun is overhead in the Northern Hemisphere in July and in the Southern in January, so the zone of strongest heating moves, and the pressure belts, wind belts and ITCZ move with it: north in July, south in January, by roughly 10 to 15 degrees through the year. Places it passes over get their rainy season; when it leaves, they dry out. That is the origin of the wet and dry seasons across much of the tropics.",
    "Matahari tegak di atas Hemisfera Utara pada Julai dan Selatan pada Januari, jadi zon pemanasan terkuat bergerak, dan jalur tekanan, jalur angin serta ITCZ bergerak bersamanya: ke utara pada Julai, ke selatan pada Januari, kira-kira 10 hingga 15 darjah sepanjang tahun. Tempat yang dilaluinya mendapat musim hujan; apabila ia beredar, tempat itu menjadi kering. Itulah asal-usul musim hujan dan kemarau di banyak kawasan tropika.",
    src=["ESS:199"]),
 ]},
 {"id": "s4", "heading": T("沿赤道的东西向环流：Walker 环流", "The east–west loop along the equator: the Walker circulation", "Gelung timur–barat di sepanjang khatulistiwa: peredaran Walker"), "level": "basic", "blocks": [
  P("除了南北方向的三圈，沿着赤道还有一个东西方向的环流。信风把太平洋表面的暖水吹向西边，西太平洋（包括印尼、马来西亚一带）海水暖、空气上升、多雨；东太平洋海水较冷、空气下沉、干燥。空气在高空由西往东流回，形成一个圈，叫{{t:walker-circulation}}。",
    "As well as the three north–south cells, there is an east–west loop along the equator. The trade winds push warm surface water westward across the Pacific, so the western Pacific — Indonesia and Malaysia's side — has warm water, rising air and plenty of rain, while the eastern Pacific has cooler water, sinking air and dry weather. Aloft the air returns eastward, closing the loop: the {{t:walker-circulation}}.",
    "Selain tiga sel utara–selatan, terdapat gelung timur–barat di sepanjang khatulistiwa. Angin pasat menolak air permukaan yang panas ke barat merentasi Pasifik, jadi Pasifik barat — sebelah Indonesia dan Malaysia — mempunyai air panas, udara naik dan banyak hujan, manakala Pasifik timur mempunyai air lebih sejuk, udara turun dan cuaca kering. Di udara atas udara kembali ke timur, melengkapkan gelung: {{t:walker-circulation}}.",
    defines=["walker-circulation"], src=["ESS:205"]),
  N("key", "Walker 环流一变弱或变强，东南亚的雨就跟着变少或变多。这就是厄尔尼诺和拉尼娜的核心，第 14 章会详细讲。",
    "When the Walker circulation weakens or strengthens, South-East Asia's rainfall falls or rises with it. That is the heart of El Niño and La Niña, the subject of Chapter 14.",
    "Apabila peredaran Walker melemah atau menguat, hujan di Asia Tenggara berkurang atau bertambah bersamanya. Itulah teras El Niño dan La Niña, topik Bab 14.",
    src=["ESS:205"]),
 ]},
 ]}

terms = [
 ("hadley-cell", T("哈德来环流圈", "Hadley cell", "Sel Hadley"), T("赤道空气上升、在约 30° 下沉、再沿地面流回赤道的环流。", "The loop in which equatorial air rises, sinks near 30° and flows back along the surface.", "Gelung udara khatulistiwa yang naik, turun berhampiran 30° dan mengalir kembali sepanjang permukaan.")),
 ("subtropical-high", T("副热带高压", "Subtropical high", "Tekanan tinggi subtropika"), T("约南北纬 30° 空气下沉形成的高压带，晴朗干燥。", "The belt of high pressure near 30° where air sinks; clear and dry.", "Jalur tekanan tinggi berhampiran 30° tempat udara turun; cerah dan kering.")),
 ("trade-winds", T("信风", "Trade winds", "Angin pasat"), T("从副热带高压吹向赤道的地面风：北半球东北风，南半球东南风。", "Surface winds from the subtropical highs to the equator: north-easterly in the north, south-easterly in the south.", "Angin permukaan dari tekanan tinggi subtropika ke khatulistiwa: timur laut di utara, tenggara di selatan.")),
 ("itcz", T("热带辐合带", "Intertropical convergence zone", "Zon penumpuan antara tropika"), T("两边信风在赤道附近相遇、空气上升、多雷雨的地带；随季节南北移动。", "Where the trade winds meet near the equator; rising air and thunderstorms; moves north and south with the seasons.", "Tempat angin pasat bertemu berhampiran khatulistiwa; udara naik dan ribut petir; bergerak ke utara dan selatan mengikut musim."), "ITCZ"),
 ("westerlies", T("西风带", "Westerlies", "Angin barat"), T("约 30°–60° 之间由西向东吹的地面风。", "Surface winds blowing west to east between about 30° and 60°.", "Angin permukaan bertiup dari barat ke timur antara kira-kira 30° dan 60°.")),
 ("ferrel-cell", T("费雷尔环流圈", "Ferrel cell", "Sel Ferrel"), T("中纬度（约 30°–60°）的环流圈。", "The middle-latitude cell, between about 30° and 60°.", "Sel latitud sederhana, antara kira-kira 30° dan 60°.")),
 ("polar-cell", T("极地环流圈", "Polar cell", "Sel kutub"), T("60° 以外的环流圈；冷空气从极地吹出成为极地东风。", "The cell beyond 60°; cold air flowing out of the poles as the polar easterlies.", "Sel melepasi 60°; udara sejuk mengalir keluar dari kutub sebagai angin timur kutub.")),
 ("walker-circulation", T("沃克环流", "Walker circulation", "Peredaran Walker"), T("沿赤道太平洋的东西向环流：西边上升多雨，东边下沉干燥。", "The east–west loop along the equatorial Pacific: rising and wet in the west, sinking and dry in the east.", "Gelung timur–barat di sepanjang Pasifik khatulistiwa: naik dan basah di barat, turun dan kering di timur.")),
]

quiz = [
 {"stage": 4, "chapter": "ch11", "q": T("ITCZ 是什么地方？", "What is the ITCZ?", "Apakah ITCZ?"),
  "options": [T("两边信风相遇、空气上升、多雷雨的地带", "Where the trade winds meet, air rises and thunderstorms are frequent", "Tempat angin pasat bertemu, udara naik dan ribut petir kerap"), T("副热带的沙漠", "The subtropical deserts", "Gurun subtropika"), T("急流的另一个名字", "Another name for the jet stream", "Nama lain bagi aliran jet"), T("北极的高压", "The polar high", "Tekanan tinggi kutub")],
  "answer": 0, "why": T("东北信风和东南信风在赤道附近辐合，空气被迫上升。", "The north-east and south-east trades converge near the equator and the air is forced up.", "Angin pasat timur laut dan tenggara menumpu berhampiran khatulistiwa dan udara dipaksa naik.")},
 {"stage": 4, "chapter": "ch11", "q": T("北半球的信风大致从哪个方向吹来？", "From which direction do the Northern Hemisphere trade winds blow?", "Dari arah manakah angin pasat Hemisfera Utara bertiup?"),
  "options": [T("东北", "North-east", "Timur laut"), T("西南", "South-west", "Barat daya"), T("正北", "Due north", "Utara"), T("西", "West", "Barat")],
  "answer": 0, "why": T("流向赤道的空气在北半球被偏向右方，成为东北风。", "Air flowing towards the equator is deflected to the right in the north, becoming a north-easterly.", "Udara yang mengalir ke khatulistiwa dipesongkan ke kanan di utara, menjadi angin timur laut.")},
 {"stage": 4, "chapter": "ch11", "q": T("Walker 环流里，西太平洋（东南亚这边）通常是怎样？", "In the Walker circulation, what is the western Pacific (South-East Asia's side) usually like?", "Dalam peredaran Walker, bagaimanakah biasanya Pasifik barat (sebelah Asia Tenggara)?"),
  "options": [T("海水暖、空气上升、多雨", "Warm water, rising air, plenty of rain", "Air panas, udara naik, banyak hujan"), T("海水冷、空气下沉、干燥", "Cool water, sinking air, dry", "Air sejuk, udara turun, kering"), T("一直刮台风", "Constant typhoons", "Taufan berterusan"), T("没有风", "No wind at all", "Tiada angin langsung")],
  "answer": 0, "why": T("信风把暖水吹到西边，暖水上方空气上升、成云下雨。", "The trades pile warm water in the west; above it the air rises and rains out.", "Angin pasat mengumpul air panas di barat; di atasnya udara naik dan menurunkan hujan.")},
]

write_chapter(chapter, terms, [], quiz)
