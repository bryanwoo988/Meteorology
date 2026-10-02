"""Chapter 30 — Reading ECMWF ensemble charts."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch30", "num": 30, "stage": 8,
 "title": T("读懂 ECMWF 的集合预报图", "Reading ECMWF ensemble charts", "Membaca carta ensemble ECMWF"),
 "sources": ["ECMWF-MEDIUM", "ECMWF-OPEN", "OM-ENS", "ECMWF-EFI", "FUN", "ESS"],
 "sections": [
 {"id": "s1", "heading": T("EPSgram：一个地点的集合预报", "The EPSgram: an ensemble for one place", "EPSgram: ensemble untuk satu tempat"), "level": "basic", "blocks": [
  P("{{t:epsgram}}把一个地点所有成员的预报，按日子画成一排盒子。成员按大小排好，{{t:percentile}}说的是“有多少成员比这个值小”：中位数（第 50 百分位）一半成员比它小；第 10 和第 90 百分位之间，包含了中间八成的成员。这本书的图：盒子是 25%–75%，线是 10%–90%，盒子里的横线是中位数。ECMWF 自己的图也是类似的盒子，看图时先看图例。",
    "An {{t:epsgram}} draws all the members' forecasts for one place as a row of boxes, one per day. Sort the members by size: a {{t:percentile}} tells how many fall below a value — half the members lie below the median (50th percentile), and the middle eight in ten lie between the 10th and 90th. In this book's chart the box spans 25–75 %, the whiskers 10–90 %, and the line in the box is the median. ECMWF's own charts use similar boxes; always check the legend.",
    "{{t:epsgram}} melukis ramalan semua ahli bagi satu tempat sebagai barisan kotak, satu setiap hari. Susun ahli mengikut saiz: {{t:percentile}} memberitahu berapa yang jatuh di bawah sesuatu nilai — separuh ahli di bawah median (persentil ke-50), dan lapan daripada sepuluh di tengah antara persentil ke-10 dan ke-90. Dalam carta buku ini kotak meliputi 25–75 %, misai 10–90 %, dan garisan dalam kotak ialah median. Carta ECMWF sendiri menggunakan kotak serupa; sentiasa semak petunjuk.",
    defines=["epsgram", "percentile"], src=["FUN:129", "ECMWF-MEDIUM"]),
  {"type": "widget", "id": "W26"},
  P("这是 2026 年 10 月 3 日拿到的一次真实预报。头几天，51 个成员的最高气温都在约 27–33 °C 之间，每天都有几毫米雨；到第二个星期，盒子变高、离散度变大：10 月 13 日有 27 个成员（过半）预报超过 10 毫米，正符合 10 月进入季风转换期、午后雷雨增多的季节（第 16 章）。",
    "This is a real forecast fetched on 3 October 2026. For the first few days all 51 members keep the maximum between about 27 and 33 °C with a few millimetres of rain each day; in the second week the boxes grow taller and the spread widens: on 13 October 27 members — more than half — forecast over 10 mm, just as October brings the inter-monsoon and more afternoon storms (Chapter 16).",
    "Ini ramalan sebenar yang diambil pada 3 Oktober 2026. Untuk beberapa hari pertama semua 51 ahli mengekalkan suhu maksimum antara kira-kira 27 dan 33 °C dengan beberapa milimeter hujan setiap hari; pada minggu kedua kotak menjadi lebih tinggi dan serakan melebar: pada 13 Oktober 27 ahli — lebih separuh — meramal lebih 10 mm, tepat ketika Oktober membawa peralihan monsun dan lebih banyak ribut petang (Bab 16).",
    src=["OM-ENS", "MET-PHEN"]),
 ]},
 {"id": "s2", "heading": T("什么时候看 control，什么时候看全部", "When to look at the control, when at them all", "Bila melihat kawalan, bila melihat semua"), "level": "basic", "blocks": [
  P("切换到“只看 control”：10 月 15 日 control 只下 1.5 毫米，好像是干的一天；可是 51 个成员里有 12 个预报超过 10 毫米。只看一条预报，就看不到这种风险。头一两天成员还很集中时，control 和集合差不多；越往后，越要看全部成员和概率。",
    "Switch to ‘control only’: on 15 October the control gives just 1.5 mm and looks like a dry day — yet 12 of the 51 members forecast over 10 mm. A single run cannot show that risk. In the first day or two, while the members still cluster, the control and the ensemble agree; the further ahead, the more you should look at all the members and their probabilities.",
    "Tukar kepada ‘kawalan sahaja’: pada 15 Oktober kawalan memberi hanya 1.5 mm dan kelihatan seperti hari kering — namun 12 daripada 51 ahli meramal lebih 10 mm. Satu larian tidak dapat menunjukkan risiko itu. Dalam satu dua hari pertama, semasa ahli masih berkelompok, kawalan dan ensemble bersetuju; semakin jauh, semakin anda patut melihat semua ahli dan kebarangkaliannya.",
    src=["OM-ENS", "ESS:257"]),
  P("把所有成员都画成线的图叫{{t:plume-chart}}；把“有几成成员超过某个门槛”画成地图，就是{{t:probability-map}}，例如“24 小时雨量超过 50 毫米的概率”。12 个成员超过 10 毫米，就是约 24 % 的概率。",
    "A chart drawing every member as its own line is a {{t:plume-chart}}; mapping the share of members above a threshold gives a {{t:probability-map}}, such as ‘chance of more than 50 mm in 24 hours’. Twelve members above 10 mm is a probability of about 24 %.",
    "Carta yang melukis setiap ahli sebagai garisan sendiri ialah {{t:plume-chart}}; memetakan bahagian ahli melebihi ambang memberi {{t:probability-map}}, seperti ‘peluang melebihi 50 mm dalam 24 jam’. Dua belas ahli melebihi 10 mm ialah kebarangkalian kira-kira 24 %.",
    defines=["plume-chart", "probability-map"], src=["FUN:129", "ECMWF-MEDIUM"]),
 ]},
 {"id": "s3", "heading": T("EFI：跟当地的平常比", "The EFI: compared with local normal", "EFI: berbanding normal tempatan"), "level": "basic", "blocks": [
  P("同样 50 毫米的雨，在吉隆坡和在沙漠意义完全不同。{{t:efi}}把这一次的集合预报，和模型用过去多年重新预报得到的“模型气候”比较，看这次有多不寻常。EFI 在 −1 到 1 之间：越接近 1，表示越多成员预报出当地少见的高值；越接近 −1，表示少见的低值。它像一个“警钟”，不必为每个地方另定门槛。",
    "Fifty millimetres means one thing in Kuala Lumpur and another in a desert. The {{t:efi}} compares this ensemble with the ‘model climate’ — re-forecasts of many past years by the same model — to show how unusual it is. It runs from −1 to 1: the nearer 1, the more members forecast values that are rare there on the high side; the nearer −1, rare on the low side. It works as an alarm bell without setting separate thresholds for every place.",
    "Lima puluh milimeter bermakna satu perkara di Kuala Lumpur dan lain pula di gurun. {{t:efi}} membandingkan ensemble ini dengan ‘iklim model’ — ramalan semula banyak tahun lalu oleh model yang sama — untuk menunjukkan betapa luar biasanya. Ia dari −1 hingga 1: semakin hampir 1, semakin banyak ahli meramal nilai yang jarang di sebelah tinggi; semakin hampir −1, jarang di sebelah rendah. Ia berfungsi sebagai loceng amaran tanpa menetapkan ambang berasingan untuk setiap tempat.",
    defines=["efi"], src=["ECMWF-EFI"]),
 ]},
 ]}

terms = [
 ("epsgram", T("EPSgram（集合预报图）", "EPSgram", "EPSgram"), T("一个地点的集合预报，每天画成一个盒子。", "An ensemble forecast for one place drawn as one box per day.", "Ramalan ensemble untuk satu tempat dilukis sebagai satu kotak setiap hari.")),
 ("percentile", T("百分位数", "Percentile", "Persentil"), T("把数值排好后，有多少比例比它小；中位数是第 50 百分位。", "The share of sorted values below it; the median is the 50th.", "Bahagian nilai tersusun di bawahnya; median ialah ke-50.")),
 ("plume-chart", T("羽状图", "Plume chart", "Carta bulu"), T("把每个成员画成一条线的图。", "A chart with every member drawn as its own line.", "Carta dengan setiap ahli dilukis sebagai garisan sendiri.")),
 ("probability-map", T("概率图", "Probability map", "Peta kebarangkalian"), T("显示有几成成员超过某个门槛的地图。", "A map of the share of members above a threshold.", "Peta bahagian ahli melebihi ambang.")),
 ("efi", T("EFI（极端预报指数）", "EFI (Extreme Forecast Index)", "EFI (Indeks Ramalan Ekstrem)"), T("把集合预报和模型气候比较的指数，−1 到 1。", "Compares an ensemble with the model climate, from −1 to 1.", "Membandingkan ensemble dengan iklim model, dari −1 hingga 1.")),
]

sources = [
 {"id": "OM-ENS", "short": "Open-Meteo", "title": "Ensemble API — ECMWF IFS 0.25° (51 members), fetched for Kuala Lumpur on 3 Oct 2026", "publisher": "Open-Meteo (CC BY 4.0); data ECMWF open data", "url": "https://open-meteo.com/en/docs/ensemble-api", "accessed": "2026-10-03"},
 {"id": "ECMWF-EFI", "short": "ECMWF", "title": "Extreme Forecast Index (EFI) and Shift of Tails — training presentation (I. Tsonevsky)", "publisher": "European Centre for Medium-Range Weather Forecasts", "url": "https://confluence.ecmwf.int/download/attachments/95063314/Forecasting_Extremes_Jan2018.pdf?api=v2", "accessed": "2026-10-03"},
]

quiz = [
 {"stage": 8, "chapter": "ch30", "q": T("51 个成员里有 12 个预报超过 10 毫米，概率大约多少？", "12 of 51 members forecast over 10 mm: roughly what probability?", "12 daripada 51 ahli meramal lebih 10 mm: kira-kira berapa kebarangkalian?"),
  "options": [T("约 24 %", "About 24 %", "Kira-kira 24 %"), T("12 %", "12 %", "12 %"), T("51 %", "51 %", "51 %"), T("100 %", "100 %", "100 %")],
  "answer": 0, "why": T("12 ÷ 51 ≈ 0.24。", "12 ÷ 51 ≈ 0.24.", "12 ÷ 51 ≈ 0.24.")},
 {"stage": 8, "chapter": "ch30", "q": T("EFI 接近 1 表示什么？", "An EFI near 1 means…", "EFI hampir 1 bermaksud…"),
  "options": [T("很多成员预报出当地少见的高值", "Many members forecast values rare there on the high side", "Banyak ahli meramal nilai yang jarang di sebelah tinggi"), T("一定会下 100 毫米", "Exactly 100 mm will fall", "Tepat 100 mm akan turun"), T("预报很准", "The forecast is accurate", "Ramalan tepat"), T("天气很平常", "Ordinary weather", "Cuaca biasa")],
  "answer": 0, "why": T("EFI 比的是模型气候，不是绝对值。", "EFI compares with the model climate, not a fixed amount.", "EFI membandingkan dengan iklim model, bukan jumlah tetap.")},
]

write_chapter(chapter, terms, sources, quiz)
