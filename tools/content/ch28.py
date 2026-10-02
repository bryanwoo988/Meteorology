"""Chapter 28 — Ensemble forecasting: the idea."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch28", "num": 28, "stage": 8,
 "title": T("集合预报：原理", "Ensemble forecasting: the idea", "Ramalan ensemble: ideanya"),
 "sources": ["ESS", "FUN", "ECMWF-MEDIUM"],
 "sections": [
 {"id": "s1", "heading": T("差一点点，后来差很远", "A tiny difference grows", "Perbezaan kecil membesar"), "level": "basic", "blocks": [
  P("1963 年 Edward Lorenz 发现，描述大气的方程有{{t:chaos}}的性质：起点只要差一点点，误差就会不断放大，几天后可以完全不一样。即使模型和观测都很好，还有许多比格子还小、量不到的小扰动，也会这样慢慢变大。人们常把这叫{{t:butterfly-effect}}。",
    "In 1963 Edward Lorenz found that the equations of the atmosphere are {{t:chaos|chaotic}}: a tiny difference at the start keeps growing until, days later, the outcome can be completely different. Even with good models and observations there are countless eddies smaller than the grid that go unmeasured, and they grow in the same way. This is often called the {{t:butterfly-effect}}.",
    "Pada 1963 Edward Lorenz mendapati persamaan atmosfera bersifat {{t:chaos}}: perbezaan kecil di permulaan terus membesar sehingga, beberapa hari kemudian, hasilnya boleh berbeza sama sekali. Walaupun dengan model dan cerapan yang baik, terdapat banyak pusaran lebih kecil daripada grid yang tidak diukur, dan ia membesar dengan cara yang sama. Ini sering dipanggil {{t:butterfly-effect}}.",
    defines=["chaos", "butterfly-effect"], src=["FUN:128", "ESS:256"]),
  {"type": "widget", "id": "W21"},
 ]},
 {"id": "s2", "heading": T("51 个成员，不是 51 个模型", "51 members, not 51 models", "51 ahli, bukan 51 model"), "level": "basic", "blocks": [
  P("既然起点总有误差，就不要只跑一次。{{t:ensemble-forecast}}用同一个模型跑很多次，每次的起点稍微改一下，代表观测的不确定。ECMWF 的 ENS 有 51 个{{t:ensemble-member}}：1 个{{t:control-member}}用最好的起点、不加扰动；另外 50 个{{t:perturbed-member}}的起点和模型物理都稍微改动过。",
    "Since the start is never perfect, do not run just once. An {{t:ensemble-forecast}} runs the same model many times, each time with the starting point nudged slightly to represent the uncertainty in the observations. ECMWF's ENS has 51 {{t:ensemble-member}}s: one {{t:control-member}} from the best starting point with no nudges, and 50 {{t:perturbed-member}}s whose starting conditions and model physics are slightly altered.",
    "Oleh sebab titik mula tidak pernah sempurna, jangan jalankan sekali sahaja. {{t:ensemble-forecast}} menjalankan model yang sama berkali-kali, setiap kali dengan titik mula diubah sedikit untuk mewakili ketidakpastian cerapan. ENS ECMWF mempunyai 51 {{t:ensemble-member}}: satu {{t:control-member}} dari titik mula terbaik tanpa gangguan, dan 50 {{t:perturbed-member}} yang keadaan awal dan fizik modelnya diubah sedikit.",
    defines=["ensemble-forecast", "ensemble-member", "control-member", "perturbed-member"], src=["ESS:256-257", "ECMWF-MEDIUM"]),
  N("myth", "误解：“51 个成员 = 51 个不同的模型。”其实是同一个模型（ECMWF 的 IFS）跑 51 次。把几个不同机构的模型放在一起比较，叫多模型集合（第 33 章）。",
    "Myth: ‘51 members means 51 different models.’ It is one model — ECMWF's IFS — run 51 times. Putting several centres' models side by side is a multi-model ensemble (Chapter 33).",
    "Mitos: ‘51 ahli bermaksud 51 model berbeza.’ Ia satu model — IFS ECMWF — dijalankan 51 kali. Meletakkan model beberapa pusat bersebelahan ialah ensemble pelbagai model (Bab 33).",
    src=["ECMWF-MEDIUM", "FUN:129"]),
 ]},
 {"id": "s3", "heading": T("平均、离散度和信心", "Mean, spread and confidence", "Purata, serakan dan keyakinan"), "level": "basic", "blocks": [
  P("把所有成员平均起来叫{{t:ensemble-mean}}，通常比单独一个成员稳定。可是平均也会把极端值抹平：如果 5 个成员预报 100 毫米的大雨、其余小雨，平均只剩二三十毫米，看起来不吓人。所以要同时看有几成成员预报大雨。",
    "Averaging all the members gives the {{t:ensemble-mean}}, usually steadier than any single member. But averaging also smooths away extremes: if 5 members forecast 100 mm and the rest light rain, the mean may be only twenty or thirty millimetres and look harmless. So look too at how many members forecast heavy rain.",
    "Purata semua ahli memberi {{t:ensemble-mean}}, biasanya lebih stabil daripada mana-mana satu ahli. Tetapi purata juga melicinkan nilai ekstrem: jika 5 ahli meramal 100 mm dan selebihnya hujan renyai, purata mungkin hanya dua puluh atau tiga puluh milimeter dan kelihatan tidak berbahaya. Jadi lihat juga berapa ahli meramal hujan lebat.",
    defines=["ensemble-mean"], src=["ECMWF-MEDIUM"]),
  P("成员之间差得越远，{{t:spread}}越大，表示越不确定。成员都很接近时，预报员比较有信心；很分散时，就不要太相信任何一个单独的预报。不过离散度和实际误差的关系并不总是很强，有时成员都很集中、真实天气却跑到范围外面，特别是十天左右的预报。",
    "The further apart the members, the bigger the {{t:spread}} and the greater the uncertainty. When members agree, forecasters are more confident; when they scatter, trust no single run too much. Still, spread is not always a strong guide to the actual error: sometimes the members cluster and the real weather falls outside them, especially around ten days ahead.",
    "Semakin jauh ahli berbeza, semakin besar {{t:spread}} dan semakin tinggi ketidakpastian. Apabila ahli bersetuju, peramal lebih yakin; apabila berselerak, jangan terlalu percaya mana-mana satu larian. Namun serakan tidak selalu panduan kuat kepada ralat sebenar: kadangkala ahli berkelompok dan cuaca sebenar jatuh di luar mereka, terutamanya kira-kira sepuluh hari ke depan.",
    defines=["spread"], src=["ECMWF-MEDIUM", "FUN:129", "ESS:257"]),
 ]},
 ]}

terms = [
 ("chaos", T("混沌", "Chaos", "Kekacauan"), T("起点的微小差异会不断放大、使长期结果无法预料的性质。", "The property that tiny differences at the start grow until the outcome cannot be predicted.", "Sifat di mana perbezaan kecil di permulaan membesar sehingga hasilnya tidak dapat diramal.")),
 ("butterfly-effect", T("蝴蝶效应", "Butterfly effect", "Kesan rama-rama"), T("混沌的通俗说法：一点点差别，后来可能造成巨大不同。", "The popular name for chaos: a tiny change can later make a huge difference.", "Nama popular bagi kekacauan: perubahan kecil boleh kemudian membuat perbezaan besar.")),
 ("ensemble-forecast", T("集合预报", "Ensemble forecast", "Ramalan ensemble"), T("用稍微不同的起点把同一个模型跑很多次。", "The same model run many times from slightly different starts.", "Model yang sama dijalankan berkali-kali dari titik mula yang sedikit berbeza.")),
 ("ensemble-member", T("集合成员", "Ensemble member", "Ahli ensemble"), T("集合预报里的其中一次预报。", "One run within an ensemble.", "Satu larian dalam ensemble.")),
 ("control-member", T("control 成员", "Control member", "Ahli kawalan"), T("用最好的起点、没有扰动的那一个成员。", "The member started from the best analysis, unperturbed.", "Ahli yang bermula dari analisis terbaik, tanpa gangguan.")),
 ("perturbed-member", T("扰动成员", "Perturbed member", "Ahli terganggu"), T("起点或模型物理稍微改动过的成员。", "A member with slightly altered start or physics.", "Ahli dengan titik mula atau fizik yang diubah sedikit.")),
 ("ensemble-mean", T("集合平均", "Ensemble mean", "Purata ensemble"), T("所有成员的平均；比较稳定，但会抹平极端值。", "The average of all members; steadier but smooths extremes.", "Purata semua ahli; lebih stabil tetapi melicinkan ekstrem.")),
 ("spread", T("离散度", "Spread", "Serakan"), T("成员之间差得多远；越大越不确定。", "How far the members differ; larger means more uncertain.", "Sejauh mana ahli berbeza; lebih besar bermaksud lebih tidak pasti.")),
]

quiz = [
 {"stage": 8, "chapter": "ch28", "q": T("ECMWF ENS 的 51 个成员是什么？", "What are the 51 members of ECMWF's ENS?", "Apakah 51 ahli ENS ECMWF?"),
  "options": [T("同一个模型，起点和物理稍微不同的 51 次预报", "One model run 51 times with slightly different starts and physics", "Satu model dijalankan 51 kali dengan titik mula dan fizik sedikit berbeza"), T("51 个国家的模型", "Models from 51 countries", "Model dari 51 negara"), T("51 个气象站", "51 stations", "51 stesen"), T("51 天的预报", "51 days of forecast", "Ramalan 51 hari")],
  "answer": 0, "why": T("1 个 control 加 50 个扰动成员。", "One control plus 50 perturbed members.", "Satu kawalan ditambah 50 ahli terganggu.")},
 {"stage": 8, "chapter": "ch28", "q": T("为什么只看集合平均可能低估大雨？", "Why can the ensemble mean underplay heavy rain?", "Mengapa purata ensemble boleh meremehkan hujan lebat?"),
  "options": [T("平均会把少数成员的极端值抹平", "Averaging smooths the extremes of a few members", "Purata melicinkan ekstrem beberapa ahli"), T("平均总是比较大", "The mean is always larger", "Purata sentiasa lebih besar"), T("平均不包括 control", "The mean leaves out the control", "Purata tidak termasuk kawalan"), T("平均只看气温", "The mean is only for temperature", "Purata hanya untuk suhu")],
  "answer": 0, "why": T("要同时看有几成成员预报大雨。", "Also check how many members show heavy rain.", "Semak juga berapa ahli menunjukkan hujan lebat.")},
]

write_chapter(chapter, terms, [], quiz)
