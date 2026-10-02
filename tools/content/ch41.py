"""Chapter 41 — Micrometeorology and microclimate."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch41", "num": 41, "stage": 9,
 "title": T("微气象与小气候", "Micrometeorology and microclimate", "Mikrometeorologi dan mikroiklim"),
 "sources": ["PAM", "TERM"],
 "sections": [
 {"id": "s1", "heading": T("作物身边的天气", "The weather right around a crop", "Cuaca di sekeliling tanaman"), "level": "basic", "blocks": [
  P("{{t:micrometeorology}}研究几平方公里范围、离地几米以内的天气：辐射、温度、风、水汽和二氧化碳在作物冠层上下的小变化。这一层的天气叫{{t:microclimate}}，就是植物和动物真正生活的气候，和几米以上的大气候可以很不一样。",
    "{{t:micrometeorology}} studies the weather over a few square kilometres and within a few metres of the ground: small changes in radiation, temperature, wind, vapour and carbon dioxide above and inside the crop canopy. The weather of this layer is the {{t:microclimate}} — the climate plants and animals actually live in, which can be quite different from the climate a few metres higher.",
    "{{t:micrometeorology}} mengkaji cuaca di kawasan beberapa kilometer persegi dan dalam beberapa meter dari tanah: perubahan kecil sinaran, suhu, angin, wap dan karbon dioksida di atas dan di dalam kanopi tanaman. Cuaca lapisan ini ialah {{t:microclimate}} — iklim yang sebenarnya didiami tumbuhan dan haiwan, yang boleh sangat berbeza daripada iklim beberapa meter lebih tinggi.",
    defines=["micrometeorology", "microclimate"], src=["PAM:103", "TERM:221"]),
  P("越接近地面，风越小，因为动量被地面吸走；日夜的温差也在贴近地面的这一层最大。所以 1.2 米高百叶箱里的气温（第 21 章），不一定等于叶片或地面的温度。",
    "Close to the ground the wind slows, its momentum taken by the surface, and the day–night swing of temperature is biggest in this layer. So the air temperature in a Stevenson screen 1.2 m up (Chapter 21) is not necessarily the temperature of a leaf or of the soil.",
    "Dekat tanah angin menjadi perlahan, momentumnya diambil oleh permukaan, dan perbezaan suhu siang–malam paling besar dalam lapisan ini. Jadi suhu udara dalam skrin Stevenson setinggi 1.2 m (Bab 21) tidak semestinya suhu daun atau tanah.",
    src=["PAM:103-105", "PAM:138"]),
 ]},
 {"id": "s2", "heading": T("人工改善小气候", "Modifying the microclimate", "Mengubah mikroiklim"), "level": "basic", "blocks": [
  P("改善小气候的方法可以分成三类：控制热量、控制水分平衡、控制风速。在热带，热太多，所以重点是“避热”。",
    "Ways of modifying the microclimate fall into three groups: controlling the heat load, controlling the water balance and controlling the wind. In the tropics the heat load is too high, so the aim is to shed heat.",
    "Cara mengubah mikroiklim terbahagi kepada tiga kumpulan: mengawal beban haba, mengawal imbangan air dan mengawal angin. Di kawasan tropika beban haba terlalu tinggi, jadi tujuannya ialah membuang haba.",
    src=["PAM:107"]),
  L(("遮荫：减少作物的蒸散", "Shade: cuts the crop's evapotranspiration", "Teduhan: mengurangkan sejatpeluhan tanaman"),
    ("覆盖（mulching）：减少土壤的热量交换；覆盖秸秆和作物残体还能增加入渗", "Mulching: reduces heat exchange at the soil; straw and crop residues also raise infiltration", "Sungkupan: mengurangkan pertukaran haba di tanah; jerami dan sisa tanaman juga meningkatkan resapan"),
    ("增加储水：用带状种植、等高耕作、梯田、田埂减少径流", "Store more water: strip cropping, contour ploughing, terracing and bunds reduce run-off", "Simpan lebih banyak air: penanaman jalur, pembajakan kontur, teres dan batas mengurangkan air larian"),
    ("{{t:shelterbelt}}和防风障：改变风速、辐射和能量平衡，减少蒸散", "{{t:shelterbelt}}s and windbreaks: alter wind, radiation and the energy balance, and cut evapotranspiration", "{{t:shelterbelt}} dan penghadang angin: mengubah angin, sinaran dan imbangan tenaga, serta mengurangkan sejatpeluhan"),
    defines=["shelterbelt"], src=["PAM:107-109"]),
 ]},
 ]}

terms = [
 ("micrometeorology", T("微气象学", "Micrometeorology", "Mikrometeorologi"), T("研究离地几米以内、小范围天气的学问。", "The study of small-scale weather within a few metres of the ground.", "Kajian cuaca berskala kecil dalam beberapa meter dari tanah.")),
 ("microclimate", T("小气候", "Microclimate", "Mikroiklim"), T("贴近地面、植物和动物生活的那一层的气候。", "The climate of the layer near the ground where plants and animals live.", "Iklim lapisan dekat tanah tempat tumbuhan dan haiwan hidup.")),
 ("shelterbelt", T("防风林", "Shelterbelt", "Tali pelindung"), T("一长排挡风的植物，保护后面的作物。", "A long line of planting that breaks the wind for the crops behind it.", "Barisan tanaman panjang yang menghalang angin untuk tanaman di belakangnya.")),
]

quiz = [
 {"stage": 9, "chapter": "ch41", "q": T("在热带，改善小气候的重点是什么？", "In the tropics, what is the main aim in modifying the microclimate?", "Di tropika, apakah tujuan utama mengubah mikroiklim?"),
  "options": [T("避热：遮荫、覆盖", "Shedding heat: shade, mulch", "Membuang haba: teduhan, sungkupan"), T("收集更多热量", "Trapping more heat", "Memerangkap lebih haba"), T("让风更大", "More wind", "Lebih angin"), T("减少光照到零", "No light at all", "Tiada cahaya langsung")],
  "answer": 0, "why": T("热带的热量已经超过作物能忍受的程度。", "Tropical heat already exceeds what crops tolerate.", "Haba tropika sudah melebihi apa yang boleh ditahan tanaman.")},
 {"stage": 9, "chapter": "ch41", "q": T("为什么百叶箱的气温不一定等于叶片的温度？", "Why may the screen temperature differ from a leaf's?", "Mengapa suhu skrin mungkin berbeza daripada suhu daun?"),
  "options": [T("贴近地面那一层的条件变化很大", "Conditions change sharply in the layer near the ground", "Keadaan berubah dengan ketara dalam lapisan dekat tanah"), T("温度计坏了", "The thermometer is broken", "Termometer rosak"), T("叶子不会热", "Leaves never warm", "Daun tidak pernah panas"), T("百叶箱在室内", "The screen is indoors", "Skrin di dalam rumah")],
  "answer": 0, "why": T("这就是小气候和大气候的分别。", "That is the difference between micro- and macroclimate.", "Itulah perbezaan mikro dan makroiklim.")},
]

write_chapter(chapter, terms, [], quiz)
