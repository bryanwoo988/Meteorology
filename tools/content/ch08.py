"""Chapter 8 — The colours of the sky."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch08", "num": 8, "stage": 3,
 "title": T("天空的颜色", "The colours of the sky", "Warna langit"),
 "sources": ["ESS"],
 "sections": [
 {"id": "s1", "heading": T("为什么天空是蓝色", "Why the sky is blue", "Mengapa langit biru"), "level": "basic", "blocks": [
  P("阳光看起来是白色，其实混合了所有颜色。光碰到空气分子时会被弹向四面八方，这叫{{t:scattering}}。空气分子非常小，对波长短的蓝光、紫光散射得特别厉害，所以不管你往天空哪个方向看，都有蓝光射进眼睛，天空就是蓝色的。",
    "Sunlight looks white but is a mixture of every colour. When light meets air molecules it is bounced off in all directions: {{t:scattering}}. Air molecules are so small that they scatter short-wavelength blue and violet light far more strongly than red, so blue light reaches your eye from every part of the sky — and the sky looks blue.",
    "Cahaya matahari kelihatan putih tetapi campuran semua warna. Apabila cahaya bertemu molekul udara, ia dipantulkan ke semua arah: {{t:scattering}}. Molekul udara begitu kecil sehingga ia menyerakkan cahaya biru dan ungu yang berpanjang gelombang pendek jauh lebih kuat daripada merah, jadi cahaya biru sampai ke mata anda dari setiap bahagian langit — dan langit kelihatan biru.",
    defines=["scattering"], src=["ESS:436"]),
  P("云滴比空气分子大得多，把所有颜色的光都差不多一样地散射，所以云是白的。空气里尘埃、烟和盐粒多的时候，它们也把各种颜色都散射出来，天空就从蓝色变成乳白色，看得也比较不远——这就是霾天。",
    "Cloud droplets are much bigger than air molecules and scatter all colours about equally, so clouds are white. When the air is full of dust, smoke and salt, these too scatter every colour, the sky turns from blue to milky white and you cannot see as far — a hazy day.",
    "Titisan awan jauh lebih besar daripada molekul udara dan menyerakkan semua warna hampir sama rata, jadi awan putih. Apabila udara penuh dengan debu, asap dan garam, zarah ini juga menyerakkan setiap warna, langit bertukar daripada biru kepada putih susu dan anda tidak dapat melihat sejauh biasa — hari berjerebu.",
    src=["ESS:435", "ESS:437"]),
 ]},
 {"id": "s2", "heading": T("红色的日出和日落", "Red sunrises and sunsets", "Matahari terbit dan terbenam yang merah"), "level": "basic", "blocks": [
  P("太阳快落山时，阳光要斜斜地穿过很厚的一层大气才到你眼里。一路上蓝光几乎都被散射掉了，剩下的是橙色和红色，所以太阳和附近的云看起来红红的。空气里颗粒越多，越只剩下最长的红光。海边的日落常常特别红，海盐颗粒也有份。",
    "Near sunset, sunlight must cross a very long path through the atmosphere to reach you. Along the way almost all the blue is scattered out, leaving orange and red — so the Sun and nearby clouds glow red. The more particles in the air, the more only the longest red wavelengths get through. Sunsets at the coast are often especially red, partly thanks to sea-salt particles.",
    "Menjelang matahari terbenam, cahaya matahari mesti melalui laluan yang sangat panjang dalam atmosfera untuk sampai kepada anda. Sepanjang jalan hampir semua biru diserakkan keluar, meninggalkan jingga dan merah — jadi Matahari dan awan berhampiran bercahaya merah. Semakin banyak zarah dalam udara, semakin hanya panjang gelombang merah terpanjang yang lepas. Matahari terbenam di pantai sering sangat merah, sebahagiannya kerana zarah garam laut.",
    src=["ESS:438"]),
 ]},
 {"id": "s3", "heading": T("彩虹", "Rainbows", "Pelangi"), "level": "basic", "blocks": [
  P("{{t:rainbow}}出现在一边下雨、另一边有阳光的时候。你必须背对太阳、面对雨。阳光进入雨滴时被折射，在雨滴背面反射，再折射出来；不同颜色弯折的角度不一样，红光大约在离太阳光线 42° 的方向，紫光约 40°，所以彩虹外圈红、内圈紫。",
    "A {{t:rainbow}} appears when rain is falling in one part of the sky and the Sun is shining in another. You must stand with the Sun at your back, facing the rain. Sunlight is bent as it enters each drop, reflected off the back, and bent again on the way out; each colour bends by a different amount — red leaves at about 42° from the sunbeam, violet at about 40° — so the bow is red outside and violet inside.",
    "{{t:rainbow}} muncul apabila hujan turun di satu bahagian langit dan Matahari bersinar di bahagian lain. Anda mesti membelakangi Matahari, menghadap hujan. Cahaya matahari dibengkokkan apabila memasuki setiap titisan, dipantulkan dari bahagian belakang, dan dibengkokkan semula ketika keluar; setiap warna terbengkok berbeza — merah keluar kira-kira 42° dari alur cahaya, ungu kira-kira 40° — jadi pelangi merah di luar dan ungu di dalam.",
    defines=["rainbow"], src=["ESS:447-448"]),
  N("key", "🌦️ 因为彩虹在背对太阳约 42° 的地方，太阳要低于 42° 才看得到彩虹露出地平线。所以在马来西亚，彩虹多半出现在早上或傍晚：例如午后阵雨快停、太阳已经低低地挂在西边时，背对太阳往东边还在下雨的地方看。",
    "🌦️ Because the rainbow sits about 42° from the point directly opposite the Sun, the Sun must be lower than 42° for the bow to show above the horizon. So in Malaysia rainbows belong to the morning and late afternoon: for example, as an afternoon shower is ending and the Sun hangs low in the west, turn your back to it and look east, where rain is still falling.",
    "🌦️ Oleh sebab pelangi terletak kira-kira 42° dari titik bertentangan dengan Matahari, Matahari mesti lebih rendah daripada 42° supaya pelangi kelihatan di atas ufuk. Jadi di Malaysia pelangi lazimnya muncul pada waktu pagi dan lewat petang: contohnya, apabila hujan petang hampir berhenti dan Matahari rendah di barat, belakangi Matahari dan lihat ke timur, tempat hujan masih turun.",
    src=["ESS:447-448"]),
 ]},
 {"id": "s4", "heading": T("日晕和月晕", "Halos round the Sun and Moon", "Halo di sekeliling Matahari dan Bulan"), "level": "basic", "blocks": [
  P("有时太阳或月亮外面有一个大光圈，最常见的离太阳约 22°，叫{{t:halo}}。它是光穿过冰晶时被折射出来的，所以看到日晕，就表示高空有卷层云这类冰晶云。",
    "Sometimes a large ring of light surrounds the Sun or Moon, most often at about 22° from it: a {{t:halo}}. It is made by light refracting through ice crystals, so a halo tells you there is icy high cloud such as cirrostratus overhead.",
    "Kadangkala cincin cahaya besar mengelilingi Matahari atau Bulan, paling kerap kira-kira 22° daripadanya: {{t:halo}}. Ia terhasil apabila cahaya dibiaskan melalui hablur ais, jadi halo menunjukkan ada awan tinggi berais seperti sirostratus di atas.",
    defines=["halo"], src=["ESS:443"]),
  P("如果月亮外面是一圈贴得很近、带彩色的小光环，那是华（corona），由很小的球形水滴造成，和冰晶造成的晕不一样。",
    "A small, tight, coloured ring right around the Moon is a corona, made by tiny spherical water droplets — different from the ice-crystal halo.",
    "Cincin kecil berwarna yang rapat di sekeliling Bulan ialah korona, terhasil daripada titisan air sfera yang halus — berbeza daripada halo hablur ais.",
    src=["ESS:449"]),
 ]},
 ]}

terms = [
 ("scattering", T("散射", "Scattering", "Penyerakan"), T("光被空气分子或颗粒弹向四面八方；蓝光被空气分子散射得最多。", "Light bounced in all directions by molecules or particles; air molecules scatter blue most.", "Cahaya dipantulkan ke semua arah oleh molekul atau zarah; molekul udara paling banyak menyerakkan biru.")),
 ("rainbow", T("彩虹", "Rainbow", "Pelangi"), T("背对太阳看雨时，阳光在雨滴里折射、反射形成的彩色弧，约离对日点 42°。", "A coloured arc from sunlight refracted and reflected in raindrops, seen with the Sun behind you, about 42° from the antisolar point.", "Lengkung berwarna daripada cahaya matahari yang dibiaskan dan dipantulkan dalam titisan hujan, dilihat dengan Matahari di belakang, kira-kira 42° dari titik antisuria.")),
 ("halo", T("晕", "Halo", "Halo"), T("光穿过冰晶折射形成、绕着太阳或月亮的光圈，常见 22°。", "A ring round the Sun or Moon from light refracted by ice crystals, usually at 22°.", "Cincin di sekeliling Matahari atau Bulan daripada cahaya yang dibiaskan hablur ais, biasanya pada 22°.")),
]

quiz = [
 {"stage": 3, "chapter": "ch08", "q": T("想看到彩虹，太阳应该在哪里？", "Where must the Sun be for you to see a rainbow?", "Di manakah Matahari mesti berada untuk anda melihat pelangi?"),
  "options": [T("在你前面、和雨同一边", "In front of you, beside the rain", "Di hadapan anda, sebelah hujan"), T("在你背后，而且不要太高", "Behind you, and not too high", "Di belakang anda, dan tidak terlalu tinggi"), T("正在头顶", "Directly overhead", "Tegak di atas kepala"), T("已经下山", "Already set", "Sudah terbenam")],
  "answer": 1, "why": T("彩虹在对日点周围约 42°，太阳要在背后而且低于 42°。", "The bow lies about 42° around the point opposite the Sun, so the Sun must be behind you and below 42°.", "Pelangi terletak kira-kira 42° di sekeliling titik bertentangan Matahari, jadi Matahari mesti di belakang dan di bawah 42°.")},
 {"stage": 3, "chapter": "ch08", "q": T("霾天的天空为什么偏白？", "Why does a hazy sky look whitish?", "Mengapa langit berjerebu kelihatan keputihan?"),
  "options": [T("颗粒把各种颜色都散射出来", "Particles scatter all colours", "Zarah menyerakkan semua warna"), T("太阳变弱了", "The Sun is weaker", "Matahari lebih lemah"), T("空气变冷了", "The air is colder", "Udara lebih sejuk"), T("臭氧变多了", "There is more ozone", "Ozon lebih banyak")],
  "answer": 0, "why": T("尘、烟、盐粒比空气分子大，各种颜色都散射，混在一起就是白色。", "Dust, smoke and salt are larger than molecules and scatter every colour, which mixes to white.", "Debu, asap dan garam lebih besar daripada molekul dan menyerakkan setiap warna, yang bercampur menjadi putih.")},
]

write_chapter(chapter, terms, [], quiz)
