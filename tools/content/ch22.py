"""Chapter 22 — Observing the upper air and the ocean."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch22", "num": 22, "stage": 7,
 "title": T("高空与海洋观测", "Observing the upper air and the ocean", "Mencerap udara atas dan lautan"),
 "sources": ["ESS", "FUN", "TERM", "WMO-ABO", "ARGO", "PMEL-TAO", "NDBC-STATIONS", "UWYO-SND", "NEWS-MM-2025"],
 "sections": [
 {"id": "s1", "heading": T("探空气球", "Weather balloons", "Belon cuaca"), "level": "basic", "blocks": [
  P("{{t:radiosonde}}是挂在气球下的一小盒仪器，一边上升一边用无线电传回气温、湿度和气压，最高常到 30 公里左右。地面追踪气球的位置，还能算出各高度的风。这样得到的一条垂直资料叫{{t:sounding}}。气球最后会破，仪器挂着降落伞落回地面。",
    "A {{t:radiosonde}} is a small instrument package hung below a balloon; as it rises it radios back temperature, humidity and pressure, often to about 30 km. Tracking the balloon from the ground also gives the wind at each height. The vertical record it makes is a {{t:sounding}}. Eventually the balloon bursts and the instrument drifts back down on a parachute.",
    "{{t:radiosonde}} ialah pakej alat kecil yang digantung di bawah belon; semasa naik ia menghantar balik suhu, kelembapan dan tekanan melalui radio, sering hingga kira-kira 30 km. Menjejak belon dari darat turut memberi angin pada setiap ketinggian. Rekod menegak yang dihasilkan ialah {{t:sounding}}. Akhirnya belon pecah dan alat turun semula dengan payung terjun.",
    defines=["radiosonde", "sounding"], src=["ESS:12", "ESS:171", "TERM:273"]),
  P("大部分探空站一天放两次，时间是格林尼治的午夜和中午，也就是协调世界时 00 和 12 时。马来西亚比它快 8 小时，所以是早上 8 点和晚上 8 点。早上 8 点那一次，正好用来判断当天下午会不会有雷雨（第 25 章）。大马气象局有 8 个高空站。",
    "Most stations launch twice a day, at the times of midnight and noon in Greenwich — 00 and 12 UTC. Malaysia is 8 hours ahead, so that is 8 am and 8 pm here. The 8 am launch is just right for judging whether storms will build that afternoon (Chapter 25). MetMalaysia has 8 upper-air stations.",
    "Kebanyakan stesen melepaskan belon dua kali sehari, pada masa tengah malam dan tengah hari di Greenwich — 00 dan 12 UTC. Malaysia 8 jam lebih awal, jadi itu jam 8 pagi dan 8 malam di sini. Pelepasan jam 8 pagi sangat sesuai untuk menilai sama ada ribut akan terbina petang itu (Bab 25). MetMalaysia mempunyai 8 stesen udara atas.",
    src=["ESS:12", "NEWS-MM-2025"]),
  {"type": "dataset", "id": "uwyo-soundings"},
 ]},
 {"id": "s2", "heading": T("民航飞机顺便量的资料", "Weather from airliners", "Cuaca daripada pesawat"), "level": "basic", "blocks": [
  P("飞机在起降和巡航时，机上仪器会自动量气温和风，连同位置一起传回地面。这种资料以前是机师用无线电报告，后来变成自动的；其中一种重要的来源叫{{t:amdar}}。WMO 把飞机资料收集起来，供全球的数值预报模型使用。",
    "As aircraft climb, cruise and descend, their instruments automatically measure air temperature and wind and send them down with the position. These reports began as pilots' radio messages and became automatic; one important source is {{t:amdar}}. WMO gathers aircraft data for the world's computer forecast models.",
    "Semasa pesawat naik, terbang dan turun, peralatannya secara automatik mengukur suhu udara dan angin serta menghantarnya ke bumi bersama kedudukan. Laporan ini bermula sebagai mesej radio juruterbang dan menjadi automatik; satu sumber penting ialah {{t:amdar}}. WMO mengumpul data pesawat untuk model ramalan komputer dunia.",
    defines=["amdar"], src=["WMO-ABO", "FUN:133"]),
 ]},
 {"id": "s3", "heading": T("海上的浮标", "Buoys at sea", "Boya di laut"), "level": "basic", "blocks": [
  P("全世界有一万多个陆地站，加上几百艘船和{{t:buoy}}，每天四次报告地面天气。海洋占地球七成以上，海上的资料特别珍贵。赤道太平洋的 TAO 浮标阵列在 1985 到 1994 年间建成，目的就是了解和预报 ENSO（第 14 章）；印度洋和大西洋也有类似的阵列 RAMA 和 PIRATA。",
    "Over 10,000 land stations, with hundreds of ships and {{t:buoy}}s, report the surface weather four times a day. With oceans covering over 70 % of the Earth, data from the sea are precious. The TAO array of buoys along the equatorial Pacific was built from 1985 to 1994 to understand and predict ENSO (Chapter 14); the Indian and Atlantic Oceans have similar arrays, RAMA and PIRATA.",
    "Lebih 10,000 stesen darat, bersama ratusan kapal dan {{t:buoy}}, melaporkan cuaca permukaan empat kali sehari. Dengan lautan meliputi lebih 70 % bumi, data dari laut amat berharga. Tatasusunan boya TAO di sepanjang Pasifik khatulistiwa dibina dari 1985 hingga 1994 untuk memahami dan meramal ENSO (Bab 14); Lautan Hindi dan Atlantik mempunyai tatasusunan serupa, RAMA dan PIRATA.",
    defines=["buoy"], src=["ESS:246", "ESS:250", "PMEL-TAO"]),
  {"type": "map", "id": "M13"},
  P("{{t:argo}}浮标则在水里上下移动：平常停在约 1 公里深，每 10 天先沉到 2 公里，再一路量温度和盐度浮上水面，把资料传给卫星，然后再沉下去。这个计划从 2000 年开始。",
    "{{t:argo}} floats move up and down in the water: they normally drift at about 1 km deep, and every 10 days sink to 2 km and then rise to the surface measuring temperature and salinity, send the data to a satellite, and sink again. The programme began in 2000.",
    "Pelampung {{t:argo}} bergerak naik turun dalam air: biasanya hanyut pada kira-kira 1 km dalam, dan setiap 10 hari tenggelam ke 2 km kemudian naik ke permukaan sambil mengukur suhu dan kemasinan, menghantar data ke satelit, lalu tenggelam semula. Program ini bermula pada 2000.",
    defines=["argo"], src=["ARGO"]),
 ]},
 ]}

terms = [
 ("radiosonde", T("探空仪（探空气球）", "Radiosonde", "Radiosonde"), T("挂在气球下、边升边传回气温、湿度和气压的仪器。", "A balloon-borne instrument that radios back temperature, humidity and pressure as it rises.", "Alat dibawa belon yang menghantar suhu, kelembapan dan tekanan semasa naik.")),
 ("sounding", T("探空曲线", "Sounding", "Profil sonde"), T("从地面到高空的一条垂直资料，例如一次探空的结果。", "A vertical profile of the air, such as one radiosonde flight.", "Profil menegak udara, seperti satu penerbangan radiosonde.")),
 ("amdar", T("AMDAR（飞机气象资料）", "AMDAR", "AMDAR"), T("民航飞机自动量、自动传回的气温和风资料。", "Temperature and wind measured and sent automatically by airliners.", "Suhu dan angin yang diukur dan dihantar secara automatik oleh pesawat.")),
 ("buoy", T("浮标", "Buoy", "Boya"), T("漂在海上或锚定的观测站，量海面天气和海温。", "A floating or moored station measuring weather and sea temperature at sea.", "Stesen terapung atau tertambat yang mengukur cuaca dan suhu laut.")),
 ("argo", T("Argo 浮标", "Argo float", "Pelampung Argo"), T("每 10 天沉到 2 公里再浮上来、量温度和盐度的海洋浮标。", "An ocean float that sinks to 2 km and rises every 10 days, measuring temperature and salinity.", "Pelampung lautan yang tenggelam ke 2 km dan naik setiap 10 hari, mengukur suhu dan kemasinan.")),
]

sources = [
 {"id": "WMO-ABO", "short": "WMO", "title": "Aircraft-Based Observations Programme", "publisher": "World Meteorological Organization", "url": "https://community.wmo.int/en/activity-areas/aircraft-based-observations", "accessed": "2026-10-02"},
 {"id": "ARGO", "short": "Argo", "title": "About Argo", "publisher": "Argo Program (UC San Diego)", "url": "https://argo.ucsd.edu/about/", "accessed": "2026-10-02"},
 {"id": "PMEL-TAO", "short": "NOAA PMEL", "title": "Pacific Ocean — TAO (Global Tropical Moored Buoy Array)", "publisher": "NOAA Pacific Marine Environmental Laboratory", "url": "https://www.pmel.noaa.gov/gtmba/pmel-theme/pacific-ocean-tao", "accessed": "2026-10-02"},
 {"id": "NDBC-STATIONS", "short": "NOAA NDBC", "title": "Active stations and station table (TAO, RAMA, PIRATA positions)", "publisher": "NOAA National Data Buoy Center", "url": "https://www.ndbc.noaa.gov/", "accessed": "2026-10-02"},
 {"id": "UWYO-SND", "short": "Univ. of Wyoming", "title": "Upper air soundings archive — KLIA Sepang (48650), 00 UTC 30 Sep 2026", "publisher": "University of Wyoming, Department of Atmospheric Science", "url": "https://weather.uwyo.edu/upperair/sounding.shtml", "accessed": "2026-10-02"},
]

datasets = [
 {"id": "uwyo-soundings", "name": "Upper-air soundings (University of Wyoming archive)", "provider": "University of Wyoming",
  "what": T("全世界探空站每天两次的探空资料，可以选文字表、CSV 或 Skew-T 图。第 25 章的 Skew-T 用的就是这里的吉隆坡国际机场资料。", "Twice-daily radiosonde data from stations worldwide, as a text list, CSV or Skew-T plot. Chapter 25's Skew-T uses the KLIA data from here.", "Data radiosonde dua kali sehari dari stesen seluruh dunia, sebagai senarai teks, CSV atau plot Skew-T. Skew-T Bab 25 menggunakan data KLIA dari sini."),
  "resolution": T("每个探空站", "Per station", "Setiap stesen"), "update": T("每天两次（00、12 UTC）", "Twice a day (00 and 12 UTC)", "Dua kali sehari (00 dan 12 UTC)"), "format": "Text / CSV",
  "licence": {"text": "No licence stated by the archive; the soundings are radiosonde reports exchanged through WMO", "url": "https://weather.uwyo.edu/upperair/sounding.shtml"},
  "params": [{"raw": "PRES", "meaning": T("气压", "Pressure", "Tekanan"), "unit": "hPa", "chapter": 22},
             {"raw": "HGHT", "meaning": T("位势高度", "Geopotential height", "Ketinggian geoupaya"), "unit": "m", "chapter": 10},
             {"raw": "TEMP / DWPT", "meaning": T("气温 / 露点", "Temperature / dew point", "Suhu / takat embun"), "unit": "°C", "chapter": 5},
             {"raw": "DRCT / SPED", "meaning": T("风向 / 风速", "Wind direction / speed", "Arah / kelajuan angin"), "unit": "° / m/s", "chapter": 9}],
  "sample": {"columns": ["PRES", "HGHT", "TEMP", "DWPT"], "rows": [["1000.2", "102", "25.5", "20.6"], ["850.1", "1522", "18.4", "11.6"], ["500.0", "5886", "-5.2", "-12.6"]], "source": "KLIA Sepang (48650), 00 UTC 30 Sep 2026", "fetched": "2026-10-02"},
  "links": [
   {"level": "view", "label": T("探空资料首页", "Sounding archive home", "Laman arkib sonde"), "url": "https://weather.uwyo.edu/upperair/sounding.shtml"},
   {"level": "try", "label": T("打开这次 KLIA 探空（文字表）", "Open this KLIA sounding (text list)", "Buka sonde KLIA ini (senarai teks)"), "url": "https://weather.uwyo.edu/wsgi/sounding?datetime=2026-09-30%2000:00:00&id=48650&type=TEXT:LIST&src=BUFR"}]},
]

quiz = [
 {"stage": 7, "chapter": "ch22", "q": T("马来西亚的探空气球通常什么时候放？", "When are Malaysia's weather balloons usually launched?", "Bilakah belon cuaca Malaysia biasanya dilepaskan?"),
  "options": [T("早上 8 点和晚上 8 点", "8 am and 8 pm", "8 pagi dan 8 malam"), T("中午 12 点和半夜", "Noon and midnight", "Tengah hari dan tengah malam"), T("每小时", "Every hour", "Setiap jam"), T("只在下雨时", "Only when it rains", "Hanya ketika hujan")],
  "answer": 0, "why": T("00 和 12 UTC，加 8 小时。", "00 and 12 UTC, plus 8 hours.", "00 dan 12 UTC, tambah 8 jam.")},
 {"stage": 7, "chapter": "ch22", "q": T("TAO 浮标阵列主要是为了什么而建？", "What was the TAO buoy array built for?", "Untuk apakah tatasusunan boya TAO dibina?"),
  "options": [T("了解和预报 ENSO", "To understand and predict ENSO", "Memahami dan meramal ENSO"), T("量地震", "Earthquakes", "Gempa bumi"), T("导航", "Navigation", "Navigasi"), T("捕鱼", "Fishing", "Menangkap ikan")],
  "answer": 0, "why": T("它沿着赤道太平洋，正好是厄尔尼诺发生的地方。", "It lines the equatorial Pacific, where El Niño happens.", "Ia di sepanjang Pasifik khatulistiwa, tempat El Niño berlaku.")},
]

write_chapter(chapter, terms, sources, quiz, datasets)
