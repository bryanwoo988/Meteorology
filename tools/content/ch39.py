"""Chapter 39 — Weather and oil palm."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch39", "num": 39, "stage": 9,
 "title": T("天气与油棕", "Weather and oil palm", "Cuaca dan kelapa sawit"),
 "sources": ["OETTLI2018", "IDRIS2024", "NAITO2026", "PAM", "OILPALMWIKI"],
 "sections": [
 {"id": "s1", "heading": T("水分胁迫：最主要的天气风险", "Water stress: the main weather risk", "Tekanan air: risiko cuaca utama"), "level": "basic", "blocks": [
  P("马来西亚油棕研究期刊（MPOB 出版）2024 年的一篇回顾指出：气候变化让雨量不足、雨不规律、干旱期变长、气温升高，使油棕承受{{t:water-stress}}，产量逐渐下降。缺水会影响气孔导度、叶片水势、脯氨酸合成、性别分化和水分利用效率，最后减少生物量和产量。",
    "A 2024 review in the Journal of Oil Palm Research (published by MPOB) notes that climate variability has progressively reduced oil palm productivity by subjecting it to {{t:water-stress}} through inadequate and irregular rainfall, prolonged dry spells and higher temperatures. Water stress impairs stomatal conductance, leaf water potential, proline synthesis, sex differentiation and water-use efficiency, together cutting biomass and yield.",
    "Satu ulasan 2024 dalam Journal of Oil Palm Research (diterbitkan MPOB) mencatat bahawa kebolehubahan iklim telah mengurangkan produktiviti kelapa sawit secara beransur-ansur dengan mendedahkannya kepada {{t:water-stress}} melalui hujan yang tidak mencukupi dan tidak teratur, tempoh kering berpanjangan dan suhu lebih tinggi. Tekanan air menjejaskan konduktans stomata, keupayaan air daun, sintesis prolin, pembezaan jantina dan kecekapan penggunaan air, bersama-sama mengurangkan biojisim dan hasil.",
    defines=["water-stress"], src=["IDRIS2024"]),
 ]},
 {"id": "s2", "heading": T("厄尔尼诺和滞后效应", "El Niño and the delayed effect", "El Niño dan kesan tertunda"), "level": "basic", "blocks": [
  P("2018 年《Scientific Reports》的研究分析了马来西亚的{{t:ffb}}产量：前一个冬天太平洋的海温会影响马来西亚的气候。厄尔尼诺时雨量减少、气温升高，油棕承受很大的水分胁迫，那一年的产量就比平常低；拉尼娜则降低缺水的风险，有利于增产。",
    "A 2018 study in Scientific Reports analysed Malaysia's {{t:ffb}} yields: Pacific sea temperatures in the previous northern winter influence Malaysia's climate. In El Niño, rainfall falls and temperatures rise, putting palms under heavy water stress, and that year's production is lower than normal; La Niña lowers the risk of water stress and favours higher yields.",
    "Satu kajian 2018 dalam Scientific Reports menganalisis hasil {{t:ffb}} Malaysia: suhu laut Pasifik pada musim sejuk utara sebelumnya mempengaruhi iklim Malaysia. Semasa El Niño, hujan berkurang dan suhu meningkat, meletakkan pokok di bawah tekanan air yang tinggi, dan pengeluaran tahun itu lebih rendah daripada biasa; La Niña mengurangkan risiko tekanan air dan menggalakkan hasil lebih tinggi.",
    defines=["ffb"], src=["OETTLI2018"]),
  P("油棕从花芽形成到果串成熟要很久，所以天气的影响有{{t:lag-effect}}。这项研究把收成之前几年分成几个对胁迫敏感的时期：",
    "Oil palm takes a long time from flower initiation to a ripe bunch, so weather acts with a {{t:lag-effect}}. The study picks out stress-sensitive periods well before the harvest year:",
    "Kelapa sawit mengambil masa yang lama dari permulaan bunga hingga tandan masak, jadi cuaca bertindak dengan {{t:lag-effect}}. Kajian itu mengenal pasti tempoh sensitif tekanan jauh sebelum tahun tuaian:",
    defines=["lag-effect"], src=["OETTLI2018"]),
  L(("性别决定：收成年之前约 31 到 20 个月", "Sex determination: about 31 to 20 months before the harvest year", "Penentuan jantina: kira-kira 31 hingga 20 bulan sebelum tahun tuaian"),
    ("花序败育：约 12 到 8 个月之前", "Inflorescence abortion: about 12 to 8 months before", "Keguguran jambak bunga: kira-kira 12 hingga 8 bulan sebelum"),
    ("果串失败：约 4 到 2 个月之前", "Bunch failure: about 4 to 2 months before", "Kegagalan tandan: kira-kira 4 hingga 2 bulan sebelum"),
    src=["OETTLI2018"]),
  P("2026 年 7 月发表的另一项研究，用 22 年的产量和七种气候资料比较马来西亚和印尼各地区：厄尔尼诺时，半岛特别受到空气{{t:vpd}}升高的影响；卫星重力资料（GRACE）显示，厄尔尼诺时缺水是主要压力。",
    "Another study, published in July 2026, compared regions of Malaysia and Indonesia using 22 years of yields and seven climate variables: during El Niño the Peninsula was hit especially by a higher atmospheric {{t:vpd}}, and satellite gravity data (GRACE) showed water deficit as the dominant stressor in El Niño.",
    "Satu lagi kajian, diterbitkan Julai 2026, membandingkan rantau Malaysia dan Indonesia menggunakan hasil 22 tahun dan tujuh pemboleh ubah iklim: semasa El Niño Semenanjung terjejas terutamanya oleh {{t:vpd}} atmosfera yang lebih tinggi, dan data graviti satelit (GRACE) menunjukkan defisit air sebagai tekanan utama semasa El Niño.",
    defines=["vpd"], src=["NAITO2026", "PAM:163"]),
  N("key", "把它和现在连起来：大马气象局预计这次厄尔尼诺持续到 2027 年 5 月，2027 年初可能有极端干热（第 19 章）。按照上面的研究，影响可能要过几个月甚至一两年才完全反映在产量上。",
    "Link it to now: MetMalaysia expects this El Niño to last until May 2027, with extreme hot, dry weather possible in early 2027 (Chapter 19). By the studies above, the effect may take months, even a year or two, to show fully in yields.",
    "Kaitkan dengan sekarang: MetMalaysia menjangkakan El Niño ini berterusan hingga Mei 2027, dengan cuaca kering dan panas ekstrem mungkin pada awal 2027 (Bab 19). Mengikut kajian di atas, kesannya mungkin mengambil masa beberapa bulan, malah setahun dua, untuk kelihatan sepenuhnya dalam hasil.",
    src=["MET-ENSO-STATUS", "OETTLI2018"]),
  N("tip", "想知道更多油棕的种植和管理，看 OilPalmWiki。",
    "For more on growing and managing oil palm, see OilPalmWiki.",
    "Untuk maklumat lanjut tentang penanaman dan pengurusan kelapa sawit, lihat OilPalmWiki.",
    src=["OILPALMWIKI"]),
 ]},
 ]}

terms = [
 ("water-stress", T("水分胁迫", "Water stress", "Tekanan air"), T("植物得到的水不够需要，生理功能受损。", "When a plant gets less water than it needs and its functions suffer.", "Apabila tumbuhan mendapat kurang air daripada keperluan dan fungsinya terjejas.")),
 ("ffb", T("鲜果串（FFB）", "Fresh fruit bunches (FFB)", "Buah tandan segar (BTS)"), T("油棕收成的果串，用来算产量。", "The harvested bunches of oil palm, used to measure yield.", "Tandan kelapa sawit yang dituai, digunakan untuk mengukur hasil.")),
 ("lag-effect", T("滞后效应", "Lag effect", "Kesan tertunda"), T("天气的影响要过一段时间才在产量上显现。", "A weather effect that shows in yield only after a delay.", "Kesan cuaca yang hanya kelihatan pada hasil selepas tempoh tertentu.")),
 ("vpd", T("饱和水汽压差（VPD）", "Vapour pressure deficit (VPD)", "Defisit tekanan wap (VPD)"), T("空气还能再吸多少水汽；越大，植物越容易失水。", "How much more vapour the air could hold; the larger, the faster plants lose water.", "Berapa banyak lagi wap boleh ditampung udara; semakin besar, semakin cepat tumbuhan kehilangan air.")),
]

sources = [
 {"id": "OETTLI2018", "short": "Oettli et al. 2018", "title": "Climate based predictability of oil palm tree yield in Malaysia (Scientific Reports 8, CC BY 4.0)", "publisher": "P. Oettli, S. K. Behera and T. Yamagata, 2018", "url": "https://doi.org/10.1038/s41598-018-20298-0", "accessed": "2026-10-03"},
 {"id": "IDRIS2024", "short": "JOPR 2024", "title": "Climate variability and water stress effects on oil palm (Elaeis guineensis Jacq.) productivity in Malaysia (Journal of Oil Palm Research, MPOB)", "publisher": "Malaysian Palm Oil Board, Journal of Oil Palm Research, 2024", "url": "https://doi.org/10.21894/jopr.2024.0054", "accessed": "2026-10-03"},
 {"id": "NAITO2026", "short": "Naito & Takeuchi 2026", "title": "Regional water stress dynamics in oil palm under ENSO in Malaysia and Indonesia using 22-year multiple climate data (Scientific Reports)", "publisher": "C. Naito and W. Takeuchi, 2026", "url": "https://doi.org/10.1038/s41598-026-63806-3", "accessed": "2026-10-03"},
 {"id": "OILPALMWIKI", "short": "OilPalmWiki", "title": "OilPalmWiki", "publisher": "Bryan Woo", "url": "https://bryanwoo988.github.io/OilPalmWiki/", "accessed": "2026-10-03"},
]

quiz = [
 {"stage": 9, "chapter": "ch39", "q": T("研究发现，厄尔尼诺年马来西亚的油棕产量通常怎样？", "In El Niño years, what happens to Malaysian oil palm yields, according to the study?", "Pada tahun El Niño, apakah berlaku kepada hasil kelapa sawit Malaysia, menurut kajian?"),
  "options": [T("因为缺水而比平常低", "Lower than normal, from water stress", "Lebih rendah daripada biasa, akibat tekanan air"), T("比平常高很多", "Much higher", "Jauh lebih tinggi"), T("完全没有影响", "No effect at all", "Tiada kesan langsung"), T("只有果实变大", "Only the fruit grows bigger", "Hanya buah menjadi besar")],
  "answer": 0, "why": T("雨少、气温高，水分胁迫大。", "Less rain and higher temperatures mean more water stress.", "Kurang hujan dan suhu lebih tinggi bermaksud lebih tekanan air.")},
 {"stage": 9, "chapter": "ch39", "q": T("为什么今年的干旱可能到明年才影响产量？", "Why might this year's drought show in next year's yield?", "Mengapa kemarau tahun ini mungkin kelihatan pada hasil tahun depan?"),
  "options": [T("油棕的花芽和果串要很多个月才发育成熟", "Palm flowers and bunches take many months to develop", "Bunga dan tandan sawit mengambil masa berbulan-bulan untuk berkembang"), T("雨要一年才落到地上", "Rain takes a year to fall", "Hujan mengambil masa setahun untuk turun"), T("卫星资料延迟", "Satellite data is late", "Data satelit lewat"), T("不会这样", "It cannot", "Tidak mungkin")],
  "answer": 0, "why": T("例如性别决定在收成年之前约 31 到 20 个月。", "Sex determination, for example, is about 31–20 months before the harvest year.", "Penentuan jantina, contohnya, kira-kira 31–20 bulan sebelum tahun tuaian.")},
]

write_chapter(chapter, terms, sources, quiz)
