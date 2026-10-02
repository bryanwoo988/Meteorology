"""Chapter 13 — The ocean and weather."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch13", "num": 13, "stage": 5,
 "title": T("海洋与天气", "The ocean and weather", "Lautan dan cuaca"),
 "sources": ["ESS", "PAM", "NOAA-OISST", "NOAA-TIDES", "NOAA-SURGE", "WINDY-OVERLAYS", "MET-PHEN"],
 "sections": [
 {"id": "s1", "heading": T("海面温度", "Sea-surface temperature", "Suhu permukaan laut"), "level": "basic", "blocks": [
  P("海洋表层水的温度叫{{t:sst}}。海水升温降温都很慢，又会把热量和水汽交给上面的空气，所以海温影响着天气：暖海上的空气比较暖湿、容易上升成雷雨云；冷海上的空气比较稳定，常有低云和雾。",
    "The temperature of the ocean's surface water is the {{t:sst}}. The sea warms and cools slowly and hands heat and moisture to the air above, so sea temperature shapes the weather: air over warm water is warm, moist and quick to rise into thunderclouds, while air over cold water is stable, with low cloud and fog.",
    "Suhu air permukaan lautan ialah {{t:sst}}. Laut memanas dan menyejuk perlahan serta memberikan haba dan lembapan kepada udara di atasnya, jadi suhu laut membentuk cuaca: udara di atas air panas adalah panas, lembap dan cepat naik menjadi awan ribut, manakala udara di atas air sejuk stabil, dengan awan rendah dan kabus.",
    defines=["sst"], src=["ESS:204"]),
  {"type": "map", "id": "M5"},
  P("拖动上面的月份可以看到：马来西亚周围的海，全年都是全世界最暖的海域之一。这片暖水就是这里湿热天气的“暖炉”。",
    "Drag the month above and you will see that the seas around Malaysia stay among the warmest anywhere all year. That warm water is the stove behind the hot, humid weather here.",
    "Seret bulan di atas dan anda akan melihat laut di sekeliling Malaysia kekal antara yang paling panas di dunia sepanjang tahun. Air panas itulah dapur di sebalik cuaca panas dan lembap di sini.",
    src=["NOAA-OISST"]),
  {"type": "dataset", "id": "noaa-oisst"},
 ]},
 {"id": "s2", "heading": T("洋流", "Ocean currents", "Arus lautan"), "level": "basic", "blocks": [
  P("风长期吹在海面上，带动表层海水一起流动，形成大范围的{{t:ocean-current}}。洋流比风慢，每天几公里到每小时几公里。大陆东岸通常有从赤道流向两极的暖流（如墨西哥湾流、黑潮），西岸通常有从两极流向赤道的寒流（如加利福尼亚寒流、秘鲁寒流）。北半球大约 40 % 由热带往两极搬运的热，是洋流完成的。",
    "Wind blowing steadily over the sea drags the surface water along, setting up great {{t:ocean-current}}s. They move more slowly than the wind — a few kilometres a day to a few kilometres an hour. East coasts of continents usually have warm currents flowing poleward (the Gulf Stream, the Kuroshio); west coasts have cold currents flowing towards the equator (the California and Peru currents). About 40 % of the heat carried poleward in the Northern Hemisphere travels in ocean currents.",
    "Angin yang bertiup berterusan di atas laut menyeret air permukaan bersamanya, membentuk {{t:ocean-current}} yang besar. Ia bergerak lebih perlahan daripada angin — beberapa kilometer sehari hingga beberapa kilometer sejam. Pantai timur benua biasanya mempunyai arus panas yang mengalir ke kutub (Arus Teluk, Kuroshio); pantai barat mempunyai arus sejuk yang mengalir ke khatulistiwa (arus California dan Peru). Kira-kira 40 % haba yang dibawa ke kutub di Hemisfera Utara bergerak dalam arus lautan.",
    defines=["ocean-current"], src=["ESS:202-203"]),
  {"type": "map", "id": "M4"},
  P("风沿着海岸吹时，科里奥利力把表层海水推离海岸，底下冰冷而富含养分的海水就会涌上来补充，这叫{{t:upwelling}}。上升流让海边变凉、多雾，但渔获丰富，秘鲁外海就是例子。",
    "When the wind blows along a coast, the Coriolis effect pushes the surface water out to sea and cold, nutrient-rich water rises from below to replace it: {{t:upwelling}}. It makes the coast cool and foggy but the fishing rich — as off Peru.",
    "Apabila angin bertiup sepanjang pantai, kesan Coriolis menolak air permukaan ke laut dan air sejuk yang kaya nutrien naik dari bawah untuk menggantikannya: {{t:upwelling}}. Ia menjadikan pantai sejuk dan berkabus tetapi perikanan kaya — seperti di luar Peru.",
    defines=["upwelling"], src=["ESS:203-204"]),
 ]},
 {"id": "s3", "heading": T("风浪和涌浪", "Wind waves and swell", "Ombak angin dan alun"), "level": "basic", "blocks": [
  P("海浪分两种。由当地正在吹的风直接吹起来的叫{{t:wind-waves}}，比较乱、比较陡。在远方风暴里形成、传了很远才到达的叫{{t:swell}}，比较整齐、周期比较长，就算当地没风也可以很大。天气预报说的“浪高”通常是{{t:significant-wave-height}}：大约是最高三分之一的浪的平均高度，接近有经验的人肉眼估计的浪高。",
    "Waves come in two kinds. Those raised directly by the wind blowing here and now are {{t:wind-waves}}: choppy and steep. Those formed by a distant storm and travelled far are {{t:swell}}: regular, with a long period, and big even when there is no wind locally. The ‘wave height’ in a forecast is usually the {{t:significant-wave-height}} — roughly the average of the highest third of the waves, close to what an experienced observer would judge by eye.",
    "Ombak ada dua jenis. Yang dinaikkan terus oleh angin yang bertiup di sini dan sekarang ialah {{t:wind-waves}}: berkocak dan curam. Yang terbentuk oleh ribut jauh dan bergerak jauh ialah {{t:swell}}: teratur, berkala panjang, dan besar walaupun tiada angin setempat. ‘Ketinggian ombak’ dalam ramalan biasanya {{t:significant-wave-height}} — lebih kurang purata sepertiga ombak tertinggi, hampir dengan anggaran pemerhati berpengalaman.",
    defines=["wind-waves", "swell", "significant-wave-height"], src=["WINDY-OVERLAYS"]),
  N("warn", "东北季风期间（11 月到 3 月），强劲的东北风长时间吹过南中国海，半岛东海岸常有大风大浪。出海和沿海作业前，要看马来西亚气象局的强风和大浪警告（第 18 章）。",
    "During the north-east monsoon (November to March), strong north-easterlies blow for days across the South China Sea and the east coast of the Peninsula often has strong winds and rough seas. Check MetMalaysia's strong-wind and rough-sea warnings before going to sea (Chapter 18).",
    "Semasa monsun timur laut (November hingga Mac), angin timur laut yang kuat bertiup berhari-hari merentasi Laut China Selatan dan pantai timur Semenanjung sering mengalami angin kuat dan laut bergelora. Semak amaran angin kencang dan laut bergelora MetMalaysia sebelum ke laut (Bab 18).",
    src=["MET-PHEN"]),
 ]},
 {"id": "s4", "heading": T("潮汐与风暴潮", "Tides and storm surge", "Pasang surut dan ribut air pasang"), "level": "basic", "blocks": [
  P("月亮和太阳的引力让海面每天有规律地涨落，这就是{{t:tide}}。新月和满月时，太阳、地球、月亮排成一直线，两边的引力叠加，涨得最高、退得最低，叫{{t:spring-tide}}；上弦和下弦月时，太阳和月亮成直角，涨落比较温和，叫{{t:neap-tide}}。两者每个月各出现两次，和季节无关。",
    "The pull of the Moon and Sun makes the sea rise and fall in a regular daily rhythm: the {{t:tide}}. At new and full moon the Sun, Earth and Moon line up, their pulls add, and the highs are highest and the lows lowest — {{t:spring-tide}}s; at the first and last quarter they pull at right angles and the range is moderate — {{t:neap-tide}}s. Each happens twice a month, whatever the season.",
    "Tarikan Bulan dan Matahari menjadikan laut naik dan turun dengan irama harian yang teratur: {{t:tide}}. Pada bulan baharu dan purnama, Matahari, Bumi dan Bulan sebaris, tarikan bergabung, dan pasang paling tinggi serta surut paling rendah — {{t:spring-tide}}; pada suku pertama dan akhir ia menarik pada sudut tegak dan julat sederhana — {{t:neap-tide}}. Setiap satu berlaku dua kali sebulan, tanpa mengira musim.",
    defines=["tide", "spring-tide", "neap-tide"], src=["NOAA-TIDES"]),
  {"type": "widget", "id": "W11"},
  P("风暴的强风把海水推向岸边，使海面额外升高，这叫{{t:storm-surge}}。如果风暴潮刚好遇上天文大潮，两者加起来的总水位最高，沿海淹水最严重。",
    "A storm's winds pushing water onshore raise the sea level further: a {{t:storm-surge}}. When a surge arrives on top of a spring tide, the combined water level is highest and coastal flooding worst.",
    "Angin ribut yang menolak air ke pantai menaikkan paras laut lagi: {{t:storm-surge}}. Apabila ribut air pasang tiba bersama pasang besar, paras air gabungan paling tinggi dan banjir pantai paling teruk.",
    defines=["storm-surge"], src=["NOAA-SURGE"]),
 ]},
 ]}

terms = [
 ("sst", T("海表温度", "Sea-surface temperature", "Suhu permukaan laut"), T("海洋表层水的温度；影响上方空气的冷暖和湿度。", "The temperature of the ocean's surface water; it shapes the warmth and moisture of the air above.", "Suhu air permukaan lautan; ia membentuk kehangatan dan kelembapan udara di atasnya."), "SST"),
 ("ocean-current", T("洋流", "Ocean current", "Arus lautan"), T("被长期的风带动、大范围流动的表层海水。", "Large-scale flow of surface water set going by the prevailing winds.", "Aliran air permukaan berskala besar yang digerakkan oleh angin lazim.")),
 ("upwelling", T("上升流", "Upwelling", "Julangan air"), T("表层海水被风推走后，底下冰冷富养分的海水涌上来补充。", "Cold, nutrient-rich water rising to replace surface water pushed away by the wind.", "Air sejuk kaya nutrien yang naik menggantikan air permukaan yang ditolak angin.")),
 ("wind-waves", T("风浪", "Wind waves", "Ombak angin"), T("由当地正在吹的风直接吹起的浪，较乱较陡。", "Waves raised by the local wind; choppy and steep.", "Ombak yang dinaikkan angin setempat; berkocak dan curam.")),
 ("swell", T("涌浪", "Swell", "Alun"), T("远方风暴形成、长距离传来的浪，整齐、周期长。", "Waves from a distant storm that have travelled far; regular, long-period.", "Ombak dari ribut jauh yang bergerak jauh; teratur, berkala panjang.")),
 ("significant-wave-height", T("有效波高", "Significant wave height", "Ketinggian ombak bererti"), T("约等于最高三分之一海浪的平均高度；预报里的“浪高”。", "Roughly the mean height of the highest third of the waves; the ‘wave height’ in forecasts.", "Lebih kurang purata ketinggian sepertiga ombak tertinggi; ‘ketinggian ombak’ dalam ramalan.")),
 ("tide", T("潮汐", "Tide", "Pasang surut"), T("月亮和太阳引力造成的海面规律涨落。", "The regular rise and fall of the sea caused by the pull of the Moon and Sun.", "Naik turun laut yang teratur akibat tarikan Bulan dan Matahari.")),
 ("spring-tide", T("大潮", "Spring tide", "Pasang besar"), T("新月和满月时的潮汐，涨落幅度最大。", "The tides around new and full moon, with the greatest range.", "Pasang surut sekitar bulan baharu dan purnama, dengan julat terbesar.")),
 ("neap-tide", T("小潮", "Neap tide", "Pasang perbani"), T("上弦和下弦月时的潮汐，涨落幅度较小。", "The tides around first and last quarter, with a smaller range.", "Pasang surut sekitar suku pertama dan akhir, dengan julat lebih kecil.")),
 ("storm-surge", T("风暴潮", "Storm surge", "Ribut air pasang"), T("风暴的风把海水推向岸边造成的额外水位上升。", "The extra rise in sea level caused by a storm's winds pushing water onshore.", "Kenaikan tambahan paras laut akibat angin ribut menolak air ke pantai.")),
]

sources = [
 {"id": "NOAA-OISST", "short": "NOAA OISST", "title": "NOAA OI SST V2 (monthly, 1°) and 1991–2020 climatology", "publisher": "NOAA Physical Sciences Laboratory", "url": "https://psl.noaa.gov/data/gridded/data.noaa.oisst.v2.html", "accessed": "2026-10-02"},
 {"id": "NOAA-TIDES", "short": "NOAA", "title": "What is a spring tide? / neap tide", "publisher": "NOAA Ocean Service", "url": "https://oceanservice.noaa.gov/facts/springtide.html", "accessed": "2026-10-02"},
 {"id": "NOAA-SURGE", "short": "NOAA", "title": "What is the difference between storm surge and storm tide?", "publisher": "NOAA Ocean Service", "url": "https://oceanservice.noaa.gov/facts/stormsurge-stormtide.html", "accessed": "2026-10-02"},
 {"id": "WINDY-OVERLAYS", "short": "Windy", "title": "Description of weather overlays", "publisher": "Windy.com community", "url": "https://community.windy.com/topic/3361/description-of-weather-overlays", "accessed": "2026-10-02"},
 {"id": "MET-PHEN", "short": "MetMalaysia", "title": "Weather phenomena (monsoons, El Niño, thunderstorms, squall lines)", "publisher": "Malaysian Meteorological Department", "url": "https://www.met.gov.my/en/pendidikan/fenomena-cuaca/", "accessed": "2026-10-02"},
]

datasets = [
 {"id": "noaa-oisst", "name": "NOAA OI SST V2", "provider": "NOAA Physical Sciences Laboratory",
  "what": T("全球每月海表温度，1981 年 12 月起，1° 网格；另有 1991–2020 各月平均。本章的两张海温地图就是用它画的。", "Monthly global sea-surface temperature from December 1981 on a 1° grid, plus 1991–2020 monthly averages. This chapter's sea-temperature maps are drawn from it.", "Suhu permukaan laut global bulanan sejak Disember 1981 pada grid 1°, serta purata bulanan 1991–2020. Peta suhu laut bab ini dilukis daripadanya."),
  "resolution": "1° (≈ 110 km)", "update": T("每月", "Monthly", "Bulanan"), "format": "NetCDF (OPeNDAP)",
  "licence": {"text": "US Government work", "url": "https://psl.noaa.gov/data/gridded/data.noaa.oisst.v2.html"},
  "params": [{"raw": "sst", "meaning": T("月平均海表温度（存成整数，×0.01 得 °C）", "Monthly mean SST (stored as integers; × 0.01 gives °C)", "Purata SST bulanan (disimpan sebagai integer; × 0.01 memberi °C)"), "unit": "°C × 100", "chapter": 13}],
  "sample": {"columns": ["time", "lat", "lon 100.5", "101.5", "102.5", "103.5", "104.5"], "rows": [["2015-12", "0.5°N", "2956", "2958", "2956", "2955", "2949"]], "source": "sst.mnmean.nc via OPeNDAP — 29.56 °C means 2956 × 0.01", "fetched": "2026-10-02"},
  "links": [
   {"level": "view", "label": T("数据集说明页", "Dataset page", "Halaman set data"), "url": "https://psl.noaa.gov/data/gridded/data.noaa.oisst.v2.html"},
   {"level": "try", "label": T("在浏览器里取一小块数据（OPeNDAP 文本）", "Fetch a small piece in the browser (OPeNDAP text)", "Ambil sebahagian kecil dalam pelayar (teks OPeNDAP)"), "url": "https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/sst.mnmean.nc.ascii?sst%5B408:1:408%5D%5B89:1:89%5D%5B100:1:104%5D"},
   {"level": "pro", "label": T("每日 0.25° 高分辨率版本", "Daily 0.25° high-resolution version", "Versi resolusi tinggi harian 0.25°"), "url": "https://www.ncei.noaa.gov/products/optimum-interpolation-sst",
    "note": T("NetCDF 文件，要用 Python（xarray）、Panoply 等软件打开。", "NetCDF files: open them with Python (xarray), Panoply or similar.", "Fail NetCDF: buka dengan Python (xarray), Panoply atau seumpamanya.")}]},
]

quiz = [
 {"stage": 5, "chapter": "ch13", "q": T("大陆东岸通常是哪一种洋流？", "What kind of current usually runs along the east coast of a continent?", "Jenis arus apakah biasanya mengalir di pantai timur benua?"),
  "options": [T("从赤道流向两极的暖流", "A warm current flowing poleward", "Arus panas mengalir ke kutub"), T("从两极流向赤道的寒流", "A cold current flowing towards the equator", "Arus sejuk mengalir ke khatulistiwa"), T("没有洋流", "No current", "Tiada arus"), T("潮流", "A tidal current", "Arus pasang surut")],
  "answer": 0, "why": T("例如墨西哥湾流和黑潮；西岸通常是寒流。", "For example the Gulf Stream and Kuroshio; west coasts usually have cold currents.", "Contohnya Arus Teluk dan Kuroshio; pantai barat biasanya mempunyai arus sejuk.")},
 {"stage": 5, "chapter": "ch13", "q": T("大潮出现在什么时候？", "When do spring tides happen?", "Bilakah pasang besar berlaku?"),
  "options": [T("新月和满月", "At new and full moon", "Pada bulan baharu dan purnama"), T("上弦和下弦月", "At first and last quarter", "Pada suku pertama dan akhir"), T("只在雨季", "Only in the rainy season", "Hanya pada musim hujan"), T("只在春天", "Only in spring", "Hanya pada musim bunga")],
  "answer": 0, "why": T("太阳、地球、月亮排成一线，引力叠加；名字里的“春”和季节无关。", "Sun, Earth and Moon line up and their pulls add; ‘spring’ has nothing to do with the season.", "Matahari, Bumi dan Bulan sebaris dan tarikan bergabung; ‘spring’ tiada kaitan dengan musim.")},
 {"stage": 5, "chapter": "ch13", "q": T("当地没有风，海上却有很大的浪，最可能是哪一种？", "No wind here, yet big waves at sea: which kind are they most likely to be?", "Tiada angin di sini, tetapi ombak besar di laut: jenis manakah paling mungkin?"),
  "options": [T("涌浪", "Swell", "Alun"), T("风浪", "Wind waves", "Ombak angin"), T("潮汐", "Tide", "Pasang surut"), T("上升流", "Upwelling", "Julangan air")],
  "answer": 0, "why": T("涌浪在远方风暴里形成，可以传得很远。", "Swell is made by a distant storm and can travel far.", "Alun dihasilkan ribut jauh dan boleh bergerak jauh.")},
]

write_chapter(chapter, terms, sources, quiz, datasets)
