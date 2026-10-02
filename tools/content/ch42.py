"""Chapter 42 — Remote sensing and crop models."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch42", "num": 42, "stage": 9,
 "title": T("遥感与作物模型", "Remote sensing and crop models", "Penderiaan jauh dan model tanaman"),
 "sources": ["PAM", "TERM", "NASA-NDVI", "NDVI-APP"],
 "sections": [
 {"id": "s1", "heading": T("不碰到也能量", "Measuring without touching", "Mengukur tanpa menyentuh"), "level": "basic", "blocks": [
  P("{{t:remote-sensing}}是用不接触对象的仪器收集资料、再分析得到资讯，现在主要指分析物体发出或反射的电磁辐射。被动式感应器接收自然的辐射（例如卫星相机）；主动式自己发出能量再收回来（例如雷达，第 24 章）。",
    "{{t:remote-sensing}} gathers information with instruments that never touch the object, today mainly by analysing the electromagnetic radiation it emits or reflects. Passive sensors receive natural radiation, like a satellite camera; active sensors send out their own energy and catch the return, like radar (Chapter 24).",
    "{{t:remote-sensing}} mengumpul maklumat dengan alat yang tidak menyentuh objek, kini terutamanya dengan menganalisis sinaran elektromagnet yang dipancarkan atau dipantulkannya. Penderia pasif menerima sinaran semula jadi, seperti kamera satelit; penderia aktif menghantar tenaganya sendiri dan menangkap pantulannya, seperti radar (Bab 24).",
    defines=["remote-sensing"], src=["PAM:110-111", "TERM:293"]),
  P("遥感可以一次看大片地区、资料可以长期保存、可以定期重拍以追踪变化；还能“看到”眼睛看不到的紫外线、红外线和微波，所以作物受病虫害时，往往在肉眼看出来之前就能发现。",
    "Remote sensing gives a synoptic view of large areas, a permanent record and regular repeat passes to follow change; and it ‘sees’ ultraviolet, infrared and microwaves invisible to the eye, so crops hit by disease or pests can often be spotted before the damage shows to us.",
    "Penderiaan jauh memberi pandangan sinoptik kawasan luas, rekod kekal dan laluan berulang yang tetap untuk mengikuti perubahan; dan ia ‘melihat’ ultraungu, inframerah dan gelombang mikro yang tidak kelihatan oleh mata, jadi tanaman yang diserang penyakit atau perosak sering dapat dikesan sebelum kerosakan kelihatan.",
    src=["PAM:113"]),
 ]},
 {"id": "s2", "heading": T("植被指数和 NDVI", "Vegetation indices and NDVI", "Indeks tumbuhan dan NDVI"), "level": "basic", "blocks": [
  P("叶子里的叶绿素强烈吸收可见光（0.4–0.7 微米）来做光合作用，叶片的细胞结构却强烈反射近红外线（0.7–1.1 微米）。比较这两种光，就得到{{t:vegetation-index}}，最常用的是 {{t:ndvi}}：NDVI =（近红外 − 可见光）÷（近红外 + 可见光）。",
    "Chlorophyll in leaves strongly absorbs visible light (0.4–0.7 µm) for photosynthesis, while the leaf's cell structure strongly reflects near-infrared (0.7–1.1 µm). Comparing the two gives a {{t:vegetation-index}}, the commonest being the {{t:ndvi}}: NDVI = (NIR − VIS) ÷ (NIR + VIS).",
    "Klorofil dalam daun menyerap kuat cahaya nampak (0.4–0.7 µm) untuk fotosintesis, manakala struktur sel daun memantulkan kuat inframerah dekat (0.7–1.1 µm). Membandingkan kedua-duanya memberi {{t:vegetation-index}}, yang paling biasa ialah {{t:ndvi}}: NDVI = (NIR − VIS) ÷ (NIR + VIS).",
    defines=["vegetation-index", "ndvi"], src=["NASA-NDVI"]),
  L(("NDVI 在 −1 和 +1 之间；没有绿叶的地方接近 0", "NDVI runs from −1 to +1; places with no green leaves come out near 0", "NDVI dari −1 hingga +1; tempat tanpa daun hijau hampir 0"),
    ("0.1 以下：岩石、沙或雪", "Below 0.1: rock, sand or snow", "Di bawah 0.1: batu, pasir atau salji"),
    ("0.2–0.3：灌木和草地", "0.2–0.3: shrub and grassland", "0.2–0.3: semak dan padang rumput"),
    ("0.6–0.8：温带和热带雨林", "0.6–0.8: temperate and tropical rain forest", "0.6–0.8: hutan hujan sederhana dan tropika"),
    src=["NASA-NDVI"]),
  N("tip", "想看自己园地的 NDVI 变化，可以用 NDVI App。干旱时（第 19 章），NDVI 下降常常是作物受胁迫的早期信号。",
    "To follow the NDVI of your own field, use the NDVI app. In a drought (Chapter 19) a falling NDVI is often an early sign of stress.",
    "Untuk mengikuti NDVI ladang anda, gunakan aplikasi NDVI. Semasa kemarau (Bab 19) NDVI yang menurun sering menjadi tanda awal tekanan.",
    src=["NDVI-APP", "NASA-NDVI"]),
 ]},
 {"id": "s3", "heading": T("作物模型", "Crop models", "Model tanaman"), "level": "basic", "blocks": [
  P("{{t:crop-model}}是一组描述“土壤–植物–大气”系统的数学方程，模拟作物的叶、根、茎和谷粒怎样生长，不只预测最后的产量，也说明中间的生长过程。它可以帮助决定最佳播种期和品种、评估灌溉投资、预测整个地区的产量，以及评估气候变化对产量的影响。",
    "A {{t:crop-model}} is a set of mathematical equations for the soil–plant–atmosphere system that simulates how a crop's leaves, roots, stems and grain grow — predicting not just the final yield but the processes along the way. It helps choose sowing dates and varieties, weigh irrigation investments, forecast yields over whole regions and assess how climate change will affect them.",
    "{{t:crop-model}} ialah set persamaan matematik bagi sistem tanah–tumbuhan–atmosfera yang menyimulasikan bagaimana daun, akar, batang dan bijirin tanaman tumbuh — meramal bukan sahaja hasil akhir tetapi proses di sepanjang jalan. Ia membantu memilih tarikh menyemai dan varieti, menilai pelaburan pengairan, meramal hasil seluruh rantau dan menilai kesan perubahan iklim.",
    defines=["crop-model"], src=["PAM:117-121"]),
  P("模型有很多种：统计模型只找出产量和天气的关系，不解释原因（第 39 章油棕的研究也用了这种方法）；动态模型则跟着时间计算蒸散、光合作用和呼吸作用这些速率，比较复杂。",
    "Models come in several kinds: a statistical model finds the link between yield and weather without explaining the mechanism (the oil palm study of Chapter 39 built one); a dynamic model works through time with rates such as evapotranspiration, photosynthesis and respiration, and is more complex.",
    "Model terdiri daripada beberapa jenis: model statistik mencari hubungan antara hasil dan cuaca tanpa menerangkan mekanismenya (kajian kelapa sawit Bab 39 membina satu); model dinamik bekerja mengikut masa dengan kadar seperti sejatpeluhan, fotosintesis dan respirasi, dan lebih kompleks.",
    src=["PAM:122-123", "OETTLI2018"]),
  N("key", "这本书到这里结束：从太阳和空气（第 1–3 章），一路到季风、预报、集合和模型，最后回到农田。下一次看天气 App 或 Windy，试着把每个数字背后的道理说出来。",
    "This is where the book ends: from the Sun and the air (Chapters 1–3), through the monsoons, forecasts, ensembles and models, and back to the field. Next time you open a weather app or Windy, try to explain the reason behind each number.",
    "Di sinilah buku ini berakhir: dari matahari dan udara (Bab 1–3), melalui monsun, ramalan, ensemble dan model, dan kembali ke ladang. Lain kali anda membuka aplikasi cuaca atau Windy, cuba terangkan sebab di sebalik setiap nombor.",
    src=["PAM:32-33"]),
 ]},
 ]}

terms = [
 ("remote-sensing", T("遥感", "Remote sensing", "Penderiaan jauh"), T("不接触对象、用电磁辐射收集资料的技术。", "Gathering information without touching the object, using electromagnetic radiation.", "Mengumpul maklumat tanpa menyentuh objek, menggunakan sinaran elektromagnet.")),
 ("vegetation-index", T("植被指数", "Vegetation index", "Indeks tumbuhan"), T("用可见光和近红外线的反射比较植物多寡的数值。", "A number comparing visible and near-infrared reflection to measure vegetation.", "Nombor yang membandingkan pantulan cahaya nampak dan inframerah dekat untuk mengukur tumbuhan.")),
 ("ndvi", T("NDVI（归一化植被指数）", "NDVI (Normalised Difference Vegetation Index)", "NDVI (Indeks Tumbuhan Perbezaan Ternormal)"), T("（近红外 − 可见光）÷（近红外 + 可见光）；绿叶越多越接近 1。", "(NIR − VIS) ÷ (NIR + VIS); the more green leaves, the nearer 1.", "(NIR − VIS) ÷ (NIR + VIS); semakin banyak daun hijau, semakin hampir 1.")),
 ("crop-model", T("作物模型", "Crop model", "Model tanaman"), T("模拟作物生长和产量的数学方程。", "Mathematical equations that simulate a crop's growth and yield.", "Persamaan matematik yang menyimulasikan pertumbuhan dan hasil tanaman.")),
]

sources = [
 {"id": "NASA-NDVI", "short": "NASA Earth Observatory", "title": "Measuring Vegetation (NDVI & EVI)", "publisher": "NASA Earth Observatory", "url": "https://earthobservatory.nasa.gov/features/MeasuringVegetation/measuring_vegetation_2.php", "accessed": "2026-10-03"},
 {"id": "NDVI-APP", "short": "NDVI", "title": "NDVI app", "publisher": "Bryan Woo", "url": "https://bryanwoo988.github.io/NDVI/", "accessed": "2026-10-03"},
]

quiz = [
 {"stage": 9, "chapter": "ch42", "q": T("为什么健康的叶子 NDVI 高？", "Why does a healthy leaf have a high NDVI?", "Mengapa daun sihat mempunyai NDVI tinggi?"),
  "options": [T("吸收很多可见光、反射很多近红外线", "It absorbs much visible light and reflects much near-infrared", "Ia menyerap banyak cahaya nampak dan memantulkan banyak inframerah dekat"), T("叶子会发光", "Leaves glow", "Daun bercahaya"), T("叶子反射所有颜色", "Leaves reflect every colour", "Daun memantulkan semua warna"), T("叶子很冷", "Leaves are cold", "Daun sejuk")],
  "answer": 0, "why": T("近红外减可见光越大，NDVI 越高。", "The bigger NIR minus VIS, the higher the NDVI.", "Semakin besar NIR tolak VIS, semakin tinggi NDVI.")},
 {"stage": 9, "chapter": "ch42", "q": T("雷达属于哪一种遥感？", "Radar is which kind of remote sensing?", "Radar ialah jenis penderiaan jauh yang mana?"),
  "options": [T("主动式", "Active", "Aktif"), T("被动式", "Passive", "Pasif"), T("都不是", "Neither", "Bukan kedua-duanya"), T("化学式", "Chemical", "Kimia")],
  "answer": 0, "why": T("它自己发出能量再接收回波。", "It sends its own energy and receives the echo.", "Ia menghantar tenaganya sendiri dan menerima gema.")},
]

write_chapter(chapter, terms, sources, quiz)
