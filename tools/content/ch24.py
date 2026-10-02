"""Chapter 24 — Radar and lightning detection."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch24", "num": 24, "stage": 7,
 "title": T("雷达与闪电定位", "Radar and lightning detection", "Radar dan pengesanan kilat"),
 "sources": ["ESS", "AMS-MP", "NWS-ZR", "NASA-GPM-DPR", "ESA-S1", "BLITZORTUNG", "NEWS-MM-2025", "MET-RADAR"],
 "sections": [
 {"id": "s1", "heading": T("雷达怎样“看见”雨", "How radar sees rain", "Bagaimana radar melihat hujan"), "level": "basic", "blocks": [
  P("{{t:radar}}的发射器送出很短、很强的微波脉冲，碰到雨滴时有一小部分能量被散射回来，由接收器收到。从发出到收回的时间，告诉我们雨在多远；回波越强，雨下得越大。所以雷达图不但显示哪里在下雨，还显示雨有多大。",
    "A {{t:radar}} transmitter sends out short, powerful microwave pulses; when they hit raindrops a small part of the energy is scattered back to a receiver. The time between sending and receiving tells how far away the rain is, and the stronger the echo, the heavier the rain. So a radar picture shows not only where it is raining but how hard.",
    "Pemancar {{t:radar}} menghantar denyut gelombang mikro yang pendek dan kuat; apabila ia mengenai titisan hujan, sebahagian kecil tenaga diserak kembali ke penerima. Masa antara menghantar dan menerima memberitahu jarak hujan, dan semakin kuat gema, semakin lebat hujan. Jadi gambar radar menunjukkan bukan sahaja di mana hujan turun tetapi betapa lebatnya.",
    defines=["radar"], src=["ESS:144"]),
  P("回波的强弱用{{t:dbz}}表示，是一种对数刻度：每多 10 dBZ，回波强 10 倍。把 dBZ 换成雨量要用经验公式，最有名的是 Marshall–Palmer 关系 Z = 200 R^1.6。",
    "Echo strength is given in {{t:dbz}}, a logarithmic scale: every 10 dBZ more means an echo ten times stronger. Turning dBZ into rainfall needs an empirical formula, the best known being the Marshall–Palmer relation, Z = 200 R^1.6.",
    "Kekuatan gema diberi dalam {{t:dbz}}, skala logaritma: setiap 10 dBZ lebih bermakna gema sepuluh kali lebih kuat. Menukar dBZ kepada hujan memerlukan formula empirik, yang paling terkenal ialah hubungan Marshall–Palmer, Z = 200 R^1.6.",
    defines=["dbz"], src=["AMS-MP", "ESS:145"]),
  {"type": "widget", "id": "W17"},
  N("warn", "雷达显示在下雨，外面却没有雨，可能是雨滴在半空就蒸发了：雷达波走直线，离雷达越远看到的位置越高，看到的是云里的雨。",
    "If radar shows rain but none is falling where you are, the drops may be evaporating on the way down: the beam travels in a straight line while the Earth curves away, so far from the radar it sees rain high in the cloud.",
    "Jika radar menunjukkan hujan tetapi tiada hujan di tempat anda, titisan mungkin tersejat dalam perjalanan turun: alur radar bergerak lurus sementara bumi melengkung, jadi jauh dari radar ia melihat hujan tinggi di dalam awan.",
    src=["ESS:144-145"]),
 ]},
 {"id": "s2", "heading": T("多普勒雷达和双偏振雷达", "Doppler and dual-polarisation radar", "Radar Doppler dan dwi-pengutuban"), "level": "basic", "blocks": [
  P("{{t:doppler-radar}}利用多普勒效应（就像火车靠近和离开时汽笛声调不同），量出雨滴朝着或离开雷达移动的速度。雨滴跟着风走，所以它能看到雷雨云里的风。",
    "A {{t:doppler-radar}} uses the Doppler shift — like the change in a train whistle's pitch as it passes — to measure how fast raindrops move towards or away from the antenna. Rain moves with the wind, so it can see the winds inside a storm.",
    "{{t:doppler-radar}} menggunakan anjakan Doppler — seperti perubahan nada wisel kereta api apabila ia lalu — untuk mengukur kelajuan titisan hujan bergerak ke arah atau menjauhi antena. Hujan bergerak bersama angin, jadi ia dapat melihat angin di dalam ribut.",
    defines=["doppler-radar"], src=["ESS:144"]),
  P("{{t:dual-pol-radar}}同时发出水平和垂直的脉冲，比较两者的回波，更容易分辨落下来的是雨还是雪。",
    "A {{t:dual-pol-radar}} sends both horizontal and vertical pulses; comparing their echoes makes it easier to tell whether what is falling is rain or snow.",
    "{{t:dual-pol-radar}} menghantar denyut mendatar dan menegak; membandingkan gemanya memudahkan untuk membezakan sama ada yang jatuh ialah hujan atau salji.",
    defines=["dual-pol-radar"], src=["ESS:145"]),
 ]},
 {"id": "s3", "heading": T("太空中的雷达", "Radar in space", "Radar di angkasa"), "level": "basic", "blocks": [
  P("GPM 核心卫星带着双频降雨雷达（Ku 和 Ka 两个波段），从上往下看雨，得到雨的立体结构和雨量；它的前身是 TRMM 上的降雨雷达。欧洲的 Sentinel-1 则用{{t:sar}}给地面拍照，不管白天黑夜、有没有云都能拍。",
    "The GPM Core Observatory carries a Dual-frequency Precipitation Radar (Ku and Ka bands) that looks down into rain, giving its three-dimensional structure and rate; its forerunner flew on TRMM. Europe's Sentinel-1 images the ground with {{t:sar}}, day or night, cloud or no cloud.",
    "Balai Cerap Teras GPM membawa Radar Kerpasan Dwi-frekuensi (jalur Ku dan Ka) yang melihat ke bawah ke dalam hujan, memberi struktur tiga dimensi dan kadarnya; pendahulunya terbang pada TRMM. Sentinel-1 Eropah mengimej permukaan bumi dengan {{t:sar}}, siang atau malam, berawan atau tidak.",
    defines=["sar"], src=["NASA-GPM-DPR", "ESA-S1"]),
 ]},
 {"id": "s4", "heading": T("闪电定位", "Finding lightning", "Mengesan kilat"), "level": "basic", "blocks": [
  P("每一次闪电都会发出无线电波。几个相距很远的接收站记下电波到达的时间差，就能算出闪电的位置，这样的网络叫{{t:lightning-network}}。Blitzortung.org 是一个义工社区网络，用 500 多个甚低频（VLF）接收器，按到达时间差定位闪电，网上可以看即时地图。",
    "Every lightning flash sends out radio waves. Several distant receivers note the differences in arrival time, and from those the flash can be located; such a system is a {{t:lightning-network}}. Blitzortung.org is a volunteer community network of more than 500 very-low-frequency (VLF) receivers that locates flashes by time of arrival and shows them on a live map.",
    "Setiap kilat memancarkan gelombang radio. Beberapa penerima yang berjauhan mencatat beza masa ketibaan, dan daripadanya kedudukan kilat dapat dikira; sistem sebegini ialah {{t:lightning-network}}. Blitzortung.org ialah rangkaian komuniti sukarelawan dengan lebih 500 penerima frekuensi sangat rendah (VLF) yang mengesan kilat mengikut masa ketibaan dan memaparkannya pada peta langsung.",
    defines=["lightning-network"], src=["BLITZORTUNG"]),
 ]},
 {"id": "s5", "heading": T("马来西亚的雷达", "Malaysia's radars", "Radar Malaysia"), "level": "basic", "blocks": [
  P("大马气象局有 18 个天气雷达站，雷达回波图放在气象局网站和 myCuaca 手机应用上，可以看全国和半岛、沙巴砂拉越的即时雨区。",
    "MetMalaysia operates 18 weather-radar stations; the radar echo images are on its website and in the myCuaca app, for the whole country and separately for the Peninsula and for Sabah and Sarawak.",
    "MetMalaysia mengendalikan 18 stesen radar cuaca; imej gema radar terdapat di laman webnya dan dalam aplikasi myCuaca, untuk seluruh negara serta berasingan untuk Semenanjung dan untuk Sabah dan Sarawak.",
    src=["NEWS-MM-2025", "MET-RADAR"]),
  N("tip", "午后阵雨在雷达上：中午以后，雷达图上常会突然冒出一块块黄色、红色的回波（40 dBZ 以上），一两个小时后又消失。用动画看几张，就知道雨区往哪里移动。",
    "Afternoon showers on radar: after noon, blobs of yellow and red echo (40 dBZ and up) often pop up on the radar picture and fade an hour or two later. Run a few frames as an animation to see which way the rain is moving.",
    "Hujan petang pada radar: selepas tengah hari, tompok gema kuning dan merah (40 dBZ ke atas) sering muncul pada gambar radar dan hilang sejam dua kemudian. Mainkan beberapa bingkai sebagai animasi untuk melihat ke mana hujan bergerak.",
    src=["ESS:145", "ESS:352"]),
  {"type": "dataset", "id": "metmy-radar"},
 ]},
 ]}

terms = [
 ("radar", T("雷达", "Radar", "Radar"), T("发出微波、接收雨滴散射回来的回波，看雨在哪里、有多大。", "Sends out microwaves and receives the echo from raindrops, showing where and how hard it rains.", "Menghantar gelombang mikro dan menerima gema dari titisan hujan, menunjukkan di mana dan betapa lebat hujan.")),
 ("dbz", T("dBZ", "dBZ", "dBZ"), T("雷达回波强度的对数单位；每多 10 dBZ 强 10 倍。", "The logarithmic unit of radar echo strength; +10 dBZ is ten times stronger.", "Unit logaritma kekuatan gema radar; +10 dBZ sepuluh kali lebih kuat.")),
 ("doppler-radar", T("多普勒雷达", "Doppler radar", "Radar Doppler"), T("能量出雨滴朝向或离开雷达速度的雷达，可看到风。", "A radar that measures how fast drops move towards or away from it, revealing the wind.", "Radar yang mengukur kelajuan titisan ke arah atau menjauhinya, mendedahkan angin.")),
 ("dual-pol-radar", T("双偏振雷达", "Dual-polarisation radar", "Radar dwi-pengutuban"), T("同时发水平和垂直脉冲，更容易分辨雨和雪。", "Sends horizontal and vertical pulses, making rain and snow easier to tell apart.", "Menghantar denyut mendatar dan menegak, memudahkan membezakan hujan dan salji.")),
 ("sar", T("合成孔径雷达（SAR）", "Synthetic-aperture radar (SAR)", "Radar apertur sintetik (SAR)"), T("卫星上给地面拍雷达照片的仪器，不怕云也不怕黑夜。", "A satellite radar that images the ground through cloud and darkness.", "Radar satelit yang mengimej permukaan menembusi awan dan kegelapan.")),
 ("lightning-network", T("闪电定位网", "Lightning detection network", "Rangkaian pengesanan kilat"), T("多个接收站按电波到达时间差算出闪电位置的网络。", "Receivers that locate flashes from differences in radio-wave arrival times.", "Penerima yang mengesan kilat daripada beza masa ketibaan gelombang radio.")),
]

sources = [
 {"id": "AMS-MP", "short": "AMS Glossary", "title": "Marshall–Palmer relation", "publisher": "American Meteorological Society, Glossary of Meteorology", "url": "https://glossary.ametsoc.org/wiki/marshall-palmer-relation/", "accessed": "2026-10-02"},
 {"id": "NWS-ZR", "short": "NWS Tallahassee", "title": "Reflectivity–rainfall rate relationships in operational meteorology (J. D. Fournier, 1999)", "publisher": "US National Weather Service, Tallahassee", "url": "https://www.weather.gov/tae/research-zrpaper", "accessed": "2026-10-02"},
 {"id": "BLITZORTUNG", "short": "Blitzortung.org", "title": "Cover your area — project description", "publisher": "Blitzortung.org", "url": "https://www.blitzortung.org/en/cover_your_area.php", "accessed": "2026-10-02"},
 {"id": "MET-RADAR", "short": "MetMalaysia", "title": "Radar Malaysia (radar echo images)", "publisher": "Malaysian Meteorological Department", "url": "https://www.met.gov.my/en/pencerapan/radar-malaysia/", "accessed": "2026-10-02"},
]

datasets = [
 {"id": "metmy-radar", "name": "MetMalaysia radar composite", "provider": "Malaysian Meteorological Department",
  "what": T("全国雷达回波合成图（GIF 图片），也有半岛和沙巴砂拉越的版本。", "A national radar-echo composite (GIF image), with separate Peninsula and Sabah–Sarawak versions.", "Komposit gema radar nasional (imej GIF), dengan versi berasingan Semenanjung dan Sabah–Sarawak."),
  "resolution": T("全国合成", "National composite", "Komposit nasional"), "update": T("经常更新（看档案的 Last-Modified 时间）", "Frequently (see the file's Last-Modified time)", "Kerap (lihat masa Last-Modified fail)"), "format": "GIF",
  "licence": {"text": "© Jabatan Meteorologi Malaysia", "url": "https://www.met.gov.my/"},
  "params": [{"raw": "colour", "meaning": T("回波强度（dBZ），颜色越暖雨越大", "Echo strength (dBZ): warmer colours, heavier rain", "Kekuatan gema (dBZ): warna lebih panas, hujan lebih lebat"), "unit": "dBZ", "chapter": 24}],
  "sample": {"columns": ["File", "Type", "Size", "Last-Modified"], "rows": [["radar_malaysia.gif", "image/gif", "196,611 bytes", "Fri, 02 Oct 2026 21:49:05 GMT"]], "source": "HTTP headers of https://www.met.gov.my/data/radar_malaysia.gif", "fetched": "2026-10-02"},
  "links": [
   {"level": "view", "label": T("大马气象局雷达页", "MetMalaysia radar page", "Halaman radar MetMalaysia"), "url": "https://www.met.gov.my/en/pencerapan/radar-malaysia/"},
   {"level": "try", "label": T("直接打开最新合成图", "Open the latest composite", "Buka komposit terkini"), "url": "https://www.met.gov.my/data/radar_malaysia.gif"},
   {"level": "pro", "label": T("Blitzortung 即时闪电地图", "Blitzortung live lightning map", "Peta kilat langsung Blitzortung"), "url": "https://www.blitzortung.org/en/live_lightning_maps.php"}]},
]

quiz = [
 {"stage": 7, "chapter": "ch24", "q": T("从 30 dBZ 到 40 dBZ，雷达回波强了多少？", "From 30 to 40 dBZ, how much stronger is the echo?", "Dari 30 ke 40 dBZ, berapa kali lebih kuat gema?"),
  "options": [T("10 倍", "10 times", "10 kali"), T("10 %", "10 %", "10 %"), T("2 倍", "2 times", "2 kali"), T("一样", "The same", "Sama")],
  "answer": 0, "why": T("dBZ 是对数刻度。", "dBZ is logarithmic.", "dBZ ialah logaritma.")},
 {"stage": 7, "chapter": "ch24", "q": T("多普勒雷达比普通雷达多了什么本领？", "What extra can a Doppler radar do?", "Apakah kebolehan tambahan radar Doppler?"),
  "options": [T("量雨滴朝向或离开雷达的速度，看到风", "Measure drops' speed towards or away from it, seeing the wind", "Mengukur kelajuan titisan ke arah atau menjauhinya, melihat angin"), T("看穿地面", "See underground", "Melihat bawah tanah"), T("量气温", "Measure temperature", "Mengukur suhu"), T("拍彩色照片", "Take colour photos", "Mengambil gambar berwarna")],
  "answer": 0, "why": T("靠多普勒效应。", "By the Doppler shift.", "Melalui anjakan Doppler.")}
]

write_chapter(chapter, terms, sources, quiz, datasets)
