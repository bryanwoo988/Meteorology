"""Chapter 27 — How numerical weather prediction works."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch27", "num": 27, "stage": 8,
 "title": T("数值天气预报怎样运作", "How numerical weather prediction works", "Bagaimana ramalan cuaca berangka berfungsi"),
 "sources": ["ESS", "FUN", "CDS-ERA5", "ECMWF-MEDIUM", "ECMWF-50R1", "METMY-TN0122"],
 "sections": [
 {"id": "s1", "heading": T("用方程算出明天", "Calculating tomorrow from equations", "Mengira esok daripada persamaan"), "level": "basic", "blocks": [
  P("{{t:nwp}}用一组数学方程描述气温、气压、风和水汽怎样随时间改变。电脑把大气切成一格一格，在每个{{t:grid-point}}上解方程，先往前算一小步（例如 5 分钟），再拿结果当新的起点算下一步，一直算到几天以后。每一小步叫{{t:time-step}}。",
    "{{t:nwp}} uses a set of mathematical equations for how temperature, pressure, wind and moisture change with time. The computer divides the atmosphere into boxes and solves the equations at each {{t:grid-point}}, stepping a short time ahead — say five minutes — then using the result as the new start for the next step, again and again until it is days ahead. Each short step is a {{t:time-step}}.",
    "{{t:nwp}} menggunakan set persamaan matematik tentang bagaimana suhu, tekanan, angin dan lembapan berubah mengikut masa. Komputer membahagikan atmosfera kepada kotak dan menyelesaikan persamaan pada setiap {{t:grid-point}}, melangkah sedikit masa ke depan — katakan lima minit — kemudian menggunakan hasilnya sebagai titik mula langkah seterusnya, berulang-ulang hingga beberapa hari ke depan. Setiap langkah pendek ialah {{t:time-step}}.",
    defines=["nwp", "grid-point", "time-step"], src=["ESS:254", "FUN:124-125"]),
  P("格点之间的距离叫{{t:resolution}}。格子越细，看得到的东西越小，但计算量增加得很快：把格距减半，计算量变成约 8 倍，跑的时间约 16 倍。",
    "The distance between grid points is the {{t:resolution}}. The finer the grid, the smaller the features it can see — but the cost climbs fast: halve the spacing and there are about 8 times as many calculations, taking about 16 times as long.",
    "Jarak antara titik grid ialah {{t:resolution}}. Semakin halus grid, semakin kecil ciri yang dapat dilihat — tetapi kosnya naik dengan pantas: kurangkan jarak separuh dan pengiraan menjadi kira-kira 8 kali, mengambil masa kira-kira 16 kali.",
    defines=["resolution"], src=["ESS:255-256"]),
  {"type": "widget", "id": "W20"},
 ]},
 {"id": "s2", "heading": T("起点：数据同化", "The starting point: data assimilation", "Titik mula: asimilasi data"), "level": "basic", "blocks": [
  P("预报要有一个准确的起点，叫{{t:initial-conditions}}。可是观测站分布不均，海上和高空很少。{{t:data-assimilation}}的做法是：每隔一段时间（ECMWF 是 12 小时），把上一次的预报和新收到的卫星、探空、飞机、浮标等观测，用最合适的方式结合起来，得到当时大气状态的最佳估计（分析场），再从这里出发做新的预报。",
    "A forecast needs an accurate starting point: its {{t:initial-conditions}}. But stations are unevenly spread, and few observe the oceans or the upper air. {{t:data-assimilation}} does this: every so many hours (12 at ECMWF) the previous forecast is combined in the best way with newly arrived satellite, radiosonde, aircraft and buoy observations to give a best estimate of the atmosphere — the analysis — from which the new forecast starts.",
    "Ramalan memerlukan titik mula yang tepat: {{t:initial-conditions}}. Tetapi stesen tidak tersebar sekata, dan sedikit yang mencerap lautan atau udara atas. {{t:data-assimilation}} berbuat begini: setiap beberapa jam (12 di ECMWF) ramalan sebelumnya digabungkan dengan cara terbaik bersama cerapan satelit, radiosonde, pesawat dan boya yang baru tiba untuk memberi anggaran terbaik atmosfera — analisis — dari mana ramalan baharu bermula.",
    defines=["initial-conditions", "data-assimilation"], src=["CDS-ERA5", "ESS:256"]),
 ]},
 {"id": "s3", "heading": T("雷雨太小：参数化", "Storms too small to see: parameterisation", "Ribut terlalu kecil: parameterisasi"), "level": "basic", "blocks": [
  P("格距几十公里的模型，看不到一个只有几公里宽的雷雨云；所以大范围的模型比较会预报大片的雨，不太会预报局部的阵雨。格子里放不下的过程，就用简化的公式估计它对整格的影响，这叫{{t:parameterisation}}。热带的雨大多来自对流，所以对流参数化对马来西亚特别重要。",
    "A model with grid spacing of tens of kilometres cannot see a thunderstorm a few kilometres across, which is why such models predict widespread rain better than local showers. Processes too small for the grid are estimated with simplified formulas for their effect on the whole box: {{t:parameterisation}}. Most tropical rain is convective, so the convection scheme matters especially for Malaysia.",
    "Model dengan jarak grid puluhan kilometer tidak dapat melihat ribut petir selebar beberapa kilometer, sebab itulah model sebegini meramal hujan meluas lebih baik daripada hujan setempat. Proses yang terlalu kecil untuk grid dianggar dengan formula ringkas bagi kesannya ke atas seluruh kotak: {{t:parameterisation}}. Kebanyakan hujan tropika ialah perolakan, jadi skema perolakan sangat penting bagi Malaysia.",
    defines=["parameterisation"], src=["ESS:256"]),
  N("key", "ECMWF 在 2026 年 5 月 12 日上线的 IFS 50r1 版本，修改了对流和云的计算方法，减少雨“停在原地下太多”的毛病，让雨更真实地从海上移到陆地上。",
    "ECMWF's IFS Cycle 50r1, live from 12 May 2026, revised its convection and cloud scheme to cut excessive stationary rain and show more realistically how rain moves from the ocean onto land.",
    "Kitaran IFS 50r1 ECMWF, berkuat kuasa 12 Mei 2026, menyemak skema perolakan dan awannya untuk mengurangkan hujan pegun yang berlebihan dan menunjukkan dengan lebih realistik bagaimana hujan bergerak dari laut ke darat.",
    src=["ECMWF-50R1"]),
 ]},
 {"id": "s4", "heading": T("全球模型和区域模型", "Global and regional models", "Model global dan serantau"), "level": "basic", "blocks": [
  P("{{t:global-model}}算整个地球，例如 ECMWF 的 IFS（约 9 公里）和美国的 GFS。{{t:regional-model}}只算一个地区，格子可以细得多，但边界要靠全球模型提供，边界上的误差会慢慢渗进来。",
    "A {{t:global-model}} covers the whole Earth — ECMWF's IFS (about 9 km) and the US GFS, for example. A {{t:regional-model}} covers one region with a much finer grid, but it takes its boundaries from a global model, and errors at the edges can creep in.",
    "{{t:global-model}} meliputi seluruh bumi — IFS ECMWF (kira-kira 9 km) dan GFS AS, contohnya. {{t:regional-model}} meliputi satu rantau dengan grid lebih halus, tetapi sempadannya diambil daripada model global, dan ralat di tepi boleh meresap masuk.",
    defines=["global-model", "regional-model"], src=["ESS:256", "ECMWF-MEDIUM"]),
  P("大马气象局从 2008 年起用 WRF 区域模型做预报，边界和起点资料来自美国 NOAA 的 GFS，每天 00 和 12 UTC（早上 8 点和晚上 8 点）跑两次。升级后，它覆盖全马来西亚，格距 3 公里，预报 4 天。",
    "MetMalaysia has run the WRF regional model since 2008, driven by NOAA's GFS for its boundaries and starting data, twice a day at 00 and 12 UTC (8 am and 8 pm). Since its upgrade it covers all of Malaysia at 3 km and forecasts 4 days ahead.",
    "MetMalaysia telah menjalankan model serantau WRF sejak 2008, dipacu oleh GFS NOAA untuk sempadan dan data permulaannya, dua kali sehari pada 00 dan 12 UTC (8 pagi dan 8 malam). Sejak dinaik taraf, ia meliputi seluruh Malaysia pada 3 km dan meramal 4 hari ke depan.",
    src=["METMY-TN0122"]),
 ]},
 ]}

terms = [
 ("nwp", T("数值天气预报（NWP）", "Numerical weather prediction (NWP)", "Ramalan cuaca berangka (NWP)"), T("用电脑解大气方程来预报天气。", "Forecasting by solving the atmosphere's equations on a computer.", "Meramal dengan menyelesaikan persamaan atmosfera pada komputer.")),
 ("grid-point", T("格点", "Grid point", "Titik grid"), T("模型计算的每一个点。", "Each point at which a model calculates.", "Setiap titik di mana model mengira.")),
 ("time-step", T("时间步长", "Time step", "Langkah masa"), T("模型每次往前算的一小段时间。", "The short interval a model steps ahead each time.", "Selang pendek yang dilangkah model setiap kali.")),
 ("resolution", T("分辨率", "Resolution", "Resolusi"), T("格点之间的距离；越小越细。", "The spacing between grid points; smaller is finer.", "Jarak antara titik grid; lebih kecil lebih halus.")),
 ("initial-conditions", T("初始场", "Initial conditions", "Keadaan awal"), T("预报出发时的大气状态。", "The state of the atmosphere a forecast starts from.", "Keadaan atmosfera tempat ramalan bermula.")),
 ("data-assimilation", T("数据同化", "Data assimilation", "Asimilasi data"), T("把上一次预报和新观测结合，得到最佳起点。", "Combining the last forecast with new observations to get the best starting point.", "Menggabungkan ramalan terakhir dengan cerapan baharu untuk titik mula terbaik.")),
 ("parameterisation", T("参数化", "Parameterisation", "Parameterisasi"), T("用简化公式估计格子里放不下的过程（例如雷雨）。", "Estimating processes too small for the grid, such as storms, with simplified formulas.", "Menganggar proses terlalu kecil untuk grid, seperti ribut, dengan formula ringkas.")),
 ("global-model", T("全球模型", "Global model", "Model global"), T("计算整个地球的模型。", "A model covering the whole Earth.", "Model yang meliputi seluruh bumi.")),
 ("regional-model", T("区域模型", "Regional model", "Model serantau"), T("只计算一个地区、格子较细，边界由全球模型提供。", "A finer-grid model of one region, with boundaries from a global model.", "Model grid halus bagi satu rantau, dengan sempadan daripada model global.")),
]

sources = [
 {"id": "CDS-ERA5", "short": "Copernicus CDS", "title": "ERA5 hourly data on single levels from 1940 to present", "publisher": "Copernicus Climate Change Service / ECMWF", "url": "https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels", "accessed": "2026-10-03"},
 {"id": "ECMWF-MEDIUM", "short": "ECMWF", "title": "Medium-range forecasts", "publisher": "European Centre for Medium-Range Weather Forecasts", "url": "https://www.ecmwf.int/en/forecasts/documentation-and-support/medium-range-forecasts", "accessed": "2026-10-03"},
 {"id": "ECMWF-50R1", "short": "ECMWF", "title": "Significant update to ECMWF’s key forecasting systems IFS and AIFS goes live (12 May 2026)", "publisher": "European Centre for Medium-Range Weather Forecasts", "url": "https://www.ecmwf.int/en/about/media-centre/news/2026/ifs-cycle-50r1-aifsv2-live", "accessed": "2026-10-03"},
 {"id": "METMY-TN0122", "short": "MetMalaysia 2022", "title": "Peningkatan Model Ramalan Cuaca Numerikal dari 3-Hari dengan Resolusi 4km kepada 4-Hari dengan Resolusi 3km bagi Seluruh Malaysia (Technical Note No. 1/2022)", "publisher": "M. S. Muhamad Yusof, Jabatan Meteorologi Malaysia", "url": "https://www.met.gov.my/data/research/researchpapers/2022/RP04_2022.pdf", "accessed": "2026-10-03"},
]

quiz = [
 {"stage": 8, "chapter": "ch27", "q": T("把模型格距减半，计算量大约变成几倍？", "Halve a model's grid spacing: how many times the calculations?", "Kurangkan jarak grid separuh: berapa kali pengiraan?"),
  "options": [T("约 8 倍", "About 8 times", "Kira-kira 8 kali"), T("2 倍", "2 times", "2 kali"), T("一样", "The same", "Sama"), T("一半", "Half", "Separuh")],
  "answer": 0, "why": T("两个水平方向加上时间步长都要加倍；跑的时间约 16 倍。", "Both horizontal directions and the time step double; run time rises about 16-fold.", "Kedua-dua arah mendatar dan langkah masa berganda; masa larian naik kira-kira 16 kali.")},
 {"stage": 8, "chapter": "ch27", "q": T("为什么格距 25 公里的模型常漏掉午后阵雨？", "Why does a 25 km model often miss afternoon showers?", "Mengapa model 25 km sering terlepas hujan petang?"),
  "options": [T("雷雨比格子小，只能用参数化估计", "Storms are smaller than a box and can only be parameterised", "Ribut lebih kecil daripada kotak dan hanya boleh diparameterkan"), T("模型不算下午", "Models skip afternoons", "Model melangkau petang"), T("没有卫星资料", "No satellite data", "Tiada data satelit"), T("马来西亚太小", "Malaysia is too small", "Malaysia terlalu kecil")],
  "answer": 0, "why": T("所以区域模型要用 3 公里这种细格子。", "Hence regional models use grids as fine as 3 km.", "Sebab itu model serantau menggunakan grid sehalus 3 km.")},
 {"stage": 8, "chapter": "ch27", "q": T("大马气象局的 WRF 模型，边界资料来自哪里？", "Where does MetMalaysia's WRF take its boundary data from?", "Dari manakah WRF MetMalaysia mengambil data sempadannya?"),
  "options": [T("美国 NOAA 的 GFS", "NOAA's GFS", "GFS NOAA"), T("ECMWF 的 ERA5", "ECMWF's ERA5", "ERA5 ECMWF"), T("雷达", "Radar", "Radar"), T("不需要", "None needed", "Tidak perlu")],
  "answer": 0, "why": T("区域模型需要全球模型提供边界。", "A regional model needs a global model at its edges.", "Model serantau memerlukan model global di tepinya.")},
]

write_chapter(chapter, terms, sources, quiz)
