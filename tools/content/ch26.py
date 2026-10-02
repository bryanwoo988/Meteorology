"""Chapter 26 — Weather maps."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch26", "num": 26, "stage": 8,
 "title": T("天气图", "Weather maps", "Peta cuaca"),
 "sources": ["PAM", "ESS", "FUN"],
 "sections": [
 {"id": "s1", "heading": T("天气图是什么", "What a weather map is", "Apakah peta cuaca"), "level": "basic", "blocks": [
  P("{{t:synoptic-chart}}是在同一时刻、把一大片地区各个气象站的观测画在一张地图上，让人一眼看到当时的天气全貌。地面天气图通常每 6 小时更新一次。画好站点资料后，预报员把气压相同的点连起来成为等压线，再标出高压、低压、锋面和槽脊。",
    "A {{t:synoptic-chart}} plots the observations from many stations over a large area at one moment, so the whole weather picture can be seen at a glance. Surface charts are usually redrawn at least every 6 hours. Once the station reports are plotted, the forecaster joins equal pressures into isobars and marks the highs, lows, fronts, troughs and ridges.",
    "{{t:synoptic-chart}} memplot cerapan dari banyak stesen di kawasan luas pada satu masa, supaya gambaran cuaca keseluruhan dapat dilihat sekali imbas. Carta permukaan biasanya dilukis semula sekurang-kurangnya setiap 6 jam. Selepas laporan stesen diplot, peramal menyambung tekanan yang sama menjadi isobar dan menandakan tekanan tinggi, rendah, front, palung dan rabung.",
    defines=["synoptic-chart"], src=["PAM:171-172"]),
 ]},
 {"id": "s2", "heading": T("站点模型", "The station model", "Model stesen"), "level": "basic", "blocks": [
  P("每个气象站在图上是一个小圆圈，四周用固定位置的数字和符号写出它的观测，这叫{{t:station-model}}：左上是气温，左下是露点，右上是海平面气压（只写最后三位），右边下面是过去 3 小时的气压变化；圆圈涂黑多少表示云量，左边的符号是现在的天气，风杆指向风吹来的方向，羽毛表示风速。",
    "Each station is a small circle with its observations written in fixed places around it: the {{t:station-model}}. Upper left is the temperature, lower left the dew point, upper right the sea-level pressure (last three digits only), and below it the pressure change over the past 3 hours; how much of the circle is filled shows the cloud cover, the symbol on the left is the present weather, and the wind shaft points to where the wind comes from, with barbs for its speed.",
    "Setiap stesen ialah bulatan kecil dengan cerapannya ditulis di tempat tetap di sekelilingnya: {{t:station-model}}. Kiri atas ialah suhu, kiri bawah takat embun, kanan atas tekanan paras laut (tiga digit terakhir sahaja), dan di bawahnya perubahan tekanan 3 jam lalu; berapa banyak bulatan diisi menunjukkan litupan awan, simbol di kiri ialah cuaca semasa, dan batang angin menunjuk ke arah angin datang, dengan bulu untuk kelajuannya.",
    defines=["station-model"], src=["ESS:461-462", "PAM:172-173"]),
  {"type": "widget", "id": "W19"},
 ]},
 {"id": "s3", "heading": T("等压线、等高线和流线", "Isobars, contours and streamlines", "Isobar, kontur dan garis arus"), "level": "basic", "blocks": [
  P("地面图画等压线（第 9 章）。高空图因为画的是同一个气压层（第 10 章），所以画的是这一层的高度，叫{{t:height-contour}}：例如 500 hPa 图上的 “588” 表示 5,880 米。等高线越密，高空风越大，风大致沿着等高线吹。",
    "Surface charts carry isobars (Chapter 9). Upper-air charts show one pressure level (Chapter 10), so they draw that level's height instead: {{t:height-contour}}s. On a 500 hPa chart, ‘588’ means 5,880 m. The closer the contours, the stronger the wind aloft, which blows roughly along them.",
    "Carta permukaan memaparkan isobar (Bab 9). Carta udara atas menunjukkan satu aras tekanan (Bab 10), jadi ia melukis ketinggian aras itu: {{t:height-contour}}. Pada carta 500 hPa, ‘588’ bermaksud 5,880 m. Semakin rapat kontur, semakin kuat angin di atas, yang bertiup lebih kurang di sepanjangnya.",
    defines=["height-contour"], src=["ESS:461", "ESS:254-255"]),
  P("在赤道附近，气压差别很小，等压线不好用；这时更常用{{t:streamline}}，直接画出风往哪里流，看哪里汇合（容易下雨）、哪里分散。",
    "Near the equator pressure differences are tiny and isobars say little; there {{t:streamline}}s are more useful — lines that simply trace where the wind flows, showing where air converges (rain is likely) and where it spreads out.",
    "Berhampiran khatulistiwa perbezaan tekanan sangat kecil dan isobar kurang berguna; di situ {{t:streamline}} lebih berguna — garisan yang menjejak ke mana angin mengalir, menunjukkan di mana udara menumpu (hujan berkemungkinan) dan di mana ia menyebar.",
    defines=["streamline"], src=["ESS:314", "FUN:97"]),
  N("tip", "Windy 的“风”图层在地图上画的流动线条，就是流线的一种画法；选 850 hPa 看季风的汇合最清楚（第 10 章）。",
    "The moving lines of Windy's wind layer are one way of drawing streamlines; at 850 hPa they show the monsoon's convergence most clearly (Chapter 10).",
    "Garisan bergerak lapisan angin Windy ialah satu cara melukis garis arus; pada 850 hPa ia menunjukkan penumpuan monsun dengan paling jelas (Bab 10).",
    src=["WINDY-OVERLAYS"]),
 ]},
 ]}

terms = [
 ("synoptic-chart", T("天气图", "Synoptic chart", "Carta sinoptik"), T("同一时刻、把大范围各站观测画在一起的地图。", "A map of many stations' observations over a large area at one moment.", "Peta cerapan banyak stesen di kawasan luas pada satu masa.")),
 ("station-model", T("站点模型", "Station model", "Model stesen"), T("用固定位置的数字和符号在一个小圆圈四周写出一个站的观测。", "A station's observations written in fixed places around a small circle.", "Cerapan stesen yang ditulis di tempat tetap di sekeliling bulatan kecil.")),
 ("height-contour", T("等高线", "Height contour", "Kontur ketinggian"), T("高空图上连接某气压层同一高度的线。", "On an upper-air chart, a line joining equal heights of a pressure level.", "Pada carta udara atas, garisan yang menyambung ketinggian sama sesuatu aras tekanan.")),
 ("streamline", T("流线", "Streamline", "Garis arus"), T("顺着风的流向画的线；热带天气图常用。", "A line drawn along the wind's flow; common on tropical charts.", "Garisan mengikut aliran angin; biasa pada carta tropika.")),
]

sources = [
 {"id": "METMY-NEM2122", "short": "MetMalaysia 2024", "title": "Review of the Northeast Monsoon 2021/2022 in Malaysia (Research Publication No. 1/2024)", "publisher": "W. F. Mustafah, J. Y. Diong, F. J. Fakaruddin et al., Malaysian Meteorological Department", "url": "https://www.met.gov.my/data/research/researchpapers/2024/RP01_2024.pdf", "accessed": "2026-10-03"},
]

quiz = [
 {"stage": 8, "chapter": "ch26", "q": T("站点模型右上角写 “086”，气压是多少？", "‘086’ at the upper right of a station model: what is the pressure?", "‘086’ di kanan atas model stesen: berapakah tekanannya?"),
  "options": [T("1008.6 hPa", "1008.6 hPa", "1008.6 hPa"), T("86 hPa", "86 hPa", "86 hPa"), T("908.6 hPa", "908.6 hPa", "908.6 hPa"), T("1086 hPa", "1086 hPa", "1086 hPa")],
  "answer": 0, "why": T("只写最后三位、单位 0.1 hPa；接近 1000 的值前面补 10。", "Last three digits in tenths; values near 1000 take a leading 10.", "Tiga digit terakhir dalam persepuluh; nilai hampir 1000 ditambah 10 di depan.")},
 {"stage": 8, "chapter": "ch26", "q": T("500 hPa 图上的 “588” 是什么意思？", "‘588’ on a 500 hPa chart means…", "‘588’ pada carta 500 hPa bermaksud…"),
  "options": [T("这一层的高度是 5,880 米", "The level is 5,880 m high", "Aras itu setinggi 5,880 m"), T("气压 588 hPa", "Pressure 588 hPa", "Tekanan 588 hPa"), T("温度 58.8 °C", "58.8 °C", "58.8 °C"), T("风速 588 km/h", "Wind 588 km/h", "Angin 588 km/j")],
  "answer": 0, "why": T("高空图画的是气压层的高度。", "Upper-air charts show the height of a pressure level.", "Carta udara atas menunjukkan ketinggian aras tekanan.")},
]

write_chapter(chapter, terms, sources, quiz)
