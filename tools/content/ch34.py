"""Chapter 34 — How good are forecasts?"""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch34", "num": 34, "stage": 8,
 "title": T("预报准不准", "How good are forecasts?", "Sejauh mana ramalan tepat?"),
 "sources": ["ESS", "FUN", "ECMWF-QUALITY", "SH2002", "ECMWF-PERF2017", "VITART2013"],
 "sections": [
 {"id": "s1", "heading": T("怎样给预报打分", "Scoring a forecast", "Memberi markah kepada ramalan"), "level": "basic", "blocks": [
  P("把预报和后来真正发生的天气比较，叫{{t:verification}}。如果预报总是偏高或偏低，这个固定的差叫{{t:bias}}。光说“准”还不够，还要和一个简单的参考比，例如“明天和今天一样”或“照气候平均”；比参考好多少，叫{{t:forecast-skill}}。",
    "Comparing forecasts with what actually happened is {{t:verification}}. If a forecast is always too high or too low, that steady error is its {{t:bias}}. ‘Accurate’ is not enough on its own: a forecast is compared with a simple reference, such as ‘tomorrow will be like today’ or ‘the climate average’, and how much better it does is its {{t:forecast-skill}}.",
    "Membandingkan ramalan dengan apa yang sebenarnya berlaku ialah {{t:verification}}. Jika ramalan sentiasa terlalu tinggi atau rendah, ralat tetap itu ialah {{t:bias}}. ‘Tepat’ sahaja tidak cukup: ramalan dibandingkan dengan rujukan mudah, seperti ‘esok sama seperti hari ini’ atau ‘purata iklim’, dan sejauh mana ia lebih baik ialah {{t:forecast-skill}}.",
    defines=["verification", "bias", "forecast-skill"], src=["ESS:258", "FUN:128"]),
  P("ECMWF 最主要的成绩指标之一：北半球中纬度 500 hPa 高度的距平相关，降到 80 % 时是预报第几天。天数越大，表示好的预报能看得越远。",
    "One of ECMWF's two headline scores is the forecast day at which the anomaly correlation of 500 hPa height over the northern extratropics falls to 80 %. The more days, the further ahead a good forecast reaches.",
    "Salah satu daripada dua skor utama ECMWF ialah hari ramalan di mana korelasi anomali ketinggian 500 hPa di ekstratropika utara jatuh ke 80 %. Semakin banyak hari, semakin jauh ramalan yang baik mencapai.",
    src=["ECMWF-QUALITY"]),
  {"type": "widget", "id": "W27"},
 ]},
 {"id": "s2", "heading": T("越远越不准，但每十年进步一天", "Worse with range, but a day better each decade", "Lebih teruk dengan jarak, tetapi sehari lebih baik setiap dekad"), "level": "basic", "blocks": [
  P("混沌（第 28 章）让起点的小误差不断放大，大约每五天翻一倍；所以超过两星期，就很难预报某一天的天气了。教科书说，模型通常能把四到六天内的天气预报得相当好，而且气温和急流比雨更好预报。",
    "Chaos (Chapter 28) makes small starting errors keep growing — roughly doubling every five days — so beyond about two weeks the weather on a given day can hardly be forecast. The textbooks put good model forecasts at about four to six days, with temperature and jet streams forecast better than rain.",
    "Kekacauan (Bab 28) membuat ralat permulaan yang kecil terus membesar — kira-kira berganda setiap lima hari — jadi melebihi kira-kira dua minggu cuaca pada hari tertentu hampir tidak dapat diramal. Buku teks meletakkan ramalan model yang baik pada kira-kira empat hingga enam hari, dengan suhu dan aliran jet diramal lebih baik daripada hujan.",
    src=["FUN:128", "ESS:255"]),
  P("但预报一直在进步。研究发现，过去几十年，北半球的预报每十年大约多看一天：今天的第 6 天预报，大约和十年前的第 5 天一样好。2017 年 ECMWF 也说，集合预报的主要成绩在过去十年进步了一天多。",
    "Forecasts keep improving, though. Studies found a gain of about one day of predictability per decade in the northern hemisphere: today's day-6 forecast is about as good as a day-5 forecast ten years earlier. In 2017 ECMWF reported its ensemble headline score up more than a day over the previous decade.",
    "Namun ramalan terus bertambah baik. Kajian mendapati peningkatan kira-kira satu hari kebolehramalan setiap dekad di hemisfera utara: ramalan hari ke-6 hari ini lebih kurang sebaik ramalan hari ke-5 sepuluh tahun lalu. Pada 2017 ECMWF melaporkan skor utama ensemblenya naik lebih sehari berbanding dekad sebelumnya.",
    src=["SH2002", "ECMWF-PERF2017"]),
 ]},
 {"id": "s3", "heading": T("热带和 MJO", "The tropics and the MJO", "Tropika dan MJO"), "level": "basic", "blocks": [
  P("马来西亚的雨大多来自几公里大的对流，比模型格子小，只能靠参数化（第 27 章）；所以这里的雨量特别难预报，某一个钟头、某一个镇会不会下雨，往往只能说概率。",
    "Most of Malaysia's rain comes from convection a few kilometres across — smaller than the model grid and handled only by parameterisation (Chapter 27). That makes rain here especially hard to forecast; whether it rains in one town in one hour can often only be given as a probability.",
    "Kebanyakan hujan Malaysia datang daripada perolakan selebar beberapa kilometer — lebih kecil daripada grid model dan hanya dikendalikan melalui parameterisasi (Bab 27). Ini menjadikan hujan di sini sangat sukar diramal; sama ada hujan di satu bandar dalam satu jam sering hanya boleh diberi sebagai kebarangkalian.",
    src=["ESS:255-256"]),
  P("不过热带也有慢慢变化的“节拍器”：MJO（第 14 章）。ECMWF 的研究显示，从 2002 年起，它预报 MJO 的能力平均每年进步约一天；MJO 让几个星期后的预报仍有一些把握。",
    "The tropics have a slow metronome, though: the MJO (Chapter 14). ECMWF research shows that its skill at forecasting the MJO improved by about one day a year on average from 2002, and the MJO gives forecasts some skill weeks ahead.",
    "Namun tropika mempunyai metronom perlahan: MJO (Bab 14). Penyelidikan ECMWF menunjukkan kemahirannya meramal MJO meningkat kira-kira satu hari setahun secara purata dari 2002, dan MJO memberi ramalan sedikit kemahiran beberapa minggu ke depan.",
    src=["VITART2013"]),
 ]},
 ]}

terms = [
 ("verification", T("预报校验", "Verification", "Pengesahan ramalan"), T("把预报和实际天气比较。", "Comparing forecasts with what happened.", "Membandingkan ramalan dengan apa yang berlaku.")),
 ("bias", T("偏差", "Bias", "Bias"), T("预报总是偏高或偏低的固定误差。", "A steady tendency to forecast too high or too low.", "Kecenderungan tetap meramal terlalu tinggi atau rendah.")),
 ("forecast-skill", T("预报技巧", "Forecast skill", "Kemahiran ramalan"), T("预报比简单参考（如气候平均）好多少。", "How much better a forecast does than a simple reference such as climatology.", "Sejauh mana ramalan lebih baik daripada rujukan mudah seperti klimatologi.")),
]

sources = [
 {"id": "ECMWF-QUALITY", "short": "ECMWF", "title": "Quality of our forecasts (headline scores)", "publisher": "European Centre for Medium-Range Weather Forecasts", "url": "https://www.ecmwf.int/en/forecasts/quality-our-forecasts", "accessed": "2026-10-03"},
 {"id": "SH2002", "short": "Simmons & Hollingsworth 2002", "title": "Some aspects of the improvement in skill of numerical weather prediction (QJRMS 128, 647–677)", "publisher": "A. J. Simmons and A. Hollingsworth, 2002", "url": "https://doi.org/10.1256/003590002321042135", "accessed": "2026-10-03"},
 {"id": "ECMWF-PERF2017", "short": "ECMWF Newsletter 154", "title": "Forecast performance 2017", "publisher": "European Centre for Medium-Range Weather Forecasts", "url": "https://www.ecmwf.int/en/newsletter/154/news/forecast-performance-2017", "accessed": "2026-10-03"},
 {"id": "VITART2013", "short": "ECMWF TM 694", "title": "Evolution of ECMWF sub-seasonal forecast skill scores over the past 10 years (Technical Memorandum 694)", "publisher": "F. Vitart, ECMWF, 2013", "url": "https://www.ecmwf.int/sites/default/files/elibrary/2013/12932-evolution-ecmwf-sub-seasonal-forecast-skill-scores-over-past-10-years.pdf", "accessed": "2026-10-03"},
]

quiz = [
 {"stage": 8, "chapter": "ch34", "q": T("预报能力大约以什么速度进步？", "Roughly how fast has forecast skill improved?", "Kira-kira seberapa pantas kemahiran ramalan bertambah baik?"),
  "options": [T("每十年多看约一天", "About a day further each decade", "Kira-kira sehari lebih jauh setiap dekad"), T("每年多看十天", "Ten days a year", "Sepuluh hari setahun"), T("没有进步", "Not at all", "Tiada langsung"), T("每百年一天", "A day a century", "Sehari setiap abad")],
  "answer": 0, "why": T("今天的第 6 天预报约等于十年前的第 5 天。", "Today's day 6 is about as good as day 5 a decade ago.", "Hari ke-6 hari ini lebih kurang sebaik hari ke-5 sedekad lalu.")},
 {"stage": 8, "chapter": "ch34", "q": T("为什么马来西亚的雨特别难预报？", "Why is Malaysian rain especially hard to forecast?", "Mengapa hujan Malaysia sangat sukar diramal?"),
  "options": [T("大多是比模型格子还小的对流", "Most is convection smaller than the grid", "Kebanyakannya perolakan lebih kecil daripada grid"), T("这里没有气象站", "There are no stations", "Tiada stesen"), T("模型不算热带", "Models skip the tropics", "Model melangkau tropika"), T("雨都在晚上", "It only rains at night", "Hujan hanya pada waktu malam")],
  "answer": 0, "why": T("所以常常只能给概率。", "So it is often given as a probability.", "Jadi ia sering diberi sebagai kebarangkalian.")},
]

write_chapter(chapter, terms, sources, quiz)
