"""Chapter 32 — AI weather models."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, write_chapter

chapter = {"id": "ch32", "num": 32, "stage": 8,
 "title": T("AI 天气模型", "AI weather models", "Model cuaca AI"),
 "sources": ["GRAPHCAST", "ECMWF-AIFS", "ECMWF-50R1", "CDS-ERA5", "OM-ENS"],
 "sections": [
 {"id": "s1", "heading": T("从历史资料里“学”天气", "Learning weather from the record", "Belajar cuaca daripada rekod"), "level": "basic", "blocks": [
  P("物理模型（第 27 章）一步一步解方程。{{t:ml-weather-model}}则不直接解方程，而是用几十年的{{t:training-data}}——通常是 ERA5 再分析——学会“现在是这样，6 小时后通常会变成怎样”，然后一步一步往前推。",
    "A physics model (Chapter 27) solves the equations step by step. A {{t:ml-weather-model}} does not solve them directly; it learns from decades of {{t:training-data}} — usually the ERA5 reanalysis — how the weather tends to change over the next few hours, and steps forward with that.",
    "Model fizik (Bab 27) menyelesaikan persamaan langkah demi langkah. {{t:ml-weather-model}} tidak menyelesaikannya secara langsung; ia belajar daripada {{t:training-data}} berdekad-dekad — biasanya analisis semula ERA5 — bagaimana cuaca cenderung berubah dalam beberapa jam akan datang, dan melangkah ke depan dengannya.",
    defines=["ml-weather-model", "training-data"], src=["GRAPHCAST", "CDS-ERA5"]),
  P("Google DeepMind 的 {{t:graphcast}}（2023 年发表在《Science》）直接从再分析资料训练，不到 1 分钟就能做出全球 0.25°、10 天的预报，在 1,380 个检验指标里有 90 % 胜过当时最准的确定性物理模型，对热带气旋路径也有帮助。",
    "Google DeepMind's {{t:graphcast}}, published in Science in 2023, is trained directly on reanalysis data; it produces a global 10-day forecast at 0.25° in under a minute and beat the most accurate operational deterministic systems on 90 % of 1,380 verification targets, including better tropical-cyclone tracks.",
    "{{t:graphcast}} Google DeepMind, diterbitkan dalam Science pada 2023, dilatih terus pada data analisis semula; ia menghasilkan ramalan global 10 hari pada 0.25° dalam kurang seminit dan mengatasi sistem deterministik operasi paling tepat pada 90 % daripada 1,380 sasaran pengesahan, termasuk jejak siklon tropika yang lebih baik.",
    defines=["graphcast"], src=["GRAPHCAST"]),
 ]},
 {"id": "s2", "heading": T("ECMWF 的 AIFS", "ECMWF's AIFS", "AIFS ECMWF"), "level": "basic", "blocks": [
  P("ECMWF 的 {{t:aifs}} 有两种：单一预报 AIFS Single 从 2025 年 2 月 25 日起正式运作，集合预报 AIFS ENS 从 2025 年 7 月 1 日起；两者在 2026 年 5 月 12 日升级到第 2 版，还第一次加入了用资料驱动的海浪预报。AIFS 的输出和 IFS 一样以 CC BY 4.0 开放。",
    "ECMWF's {{t:aifs}} comes in two forms: AIFS Single has run operationally since 25 February 2025 and AIFS ENS, an ensemble, since 1 July 2025; both were upgraded to version 2 on 12 May 2026, adding ECMWF's first data-driven wave forecasts. AIFS output is open under CC BY 4.0, like the IFS.",
    "{{t:aifs}} ECMWF hadir dalam dua bentuk: AIFS Single beroperasi sejak 25 Februari 2025 dan AIFS ENS, satu ensemble, sejak 1 Julai 2025; kedua-duanya dinaik taraf ke versi 2 pada 12 Mei 2026, menambah ramalan ombak berasaskan data pertama ECMWF. Output AIFS terbuka di bawah CC BY 4.0, seperti IFS.",
    defines=["aifs"], src=["ECMWF-AIFS", "ECMWF-50R1"]),
  N("key", "ECMWF 现在同时跑物理模型 IFS 和 AI 模型 AIFS，两者在同一天一起升级。AI 模型从历史学来，最依赖的正是物理模型和数据同化做出来的再分析；所以两者是互相配合，不是谁取代谁。",
    "ECMWF now runs both the physics-based IFS and the AI-based AIFS, upgraded on the same day. An AI model learns from the past, and the past it learns from is a reanalysis made by a physics model and data assimilation; the two work together rather than one replacing the other.",
    "ECMWF kini menjalankan IFS berasaskan fizik dan AIFS berasaskan AI, dinaik taraf pada hari yang sama. Model AI belajar daripada masa lalu, dan masa lalu yang dipelajarinya ialah analisis semula yang dibuat oleh model fizik dan asimilasi data; kedua-duanya bekerjasama dan bukan saling menggantikan.",
    src=["ECMWF-50R1", "GRAPHCAST", "CDS-ERA5"]),
  N("tip", "Open-Meteo 的集合预报 API 也提供 ECMWF AIFS 0.25° 的 51 个成员，可以和 IFS 的 51 个成员放在一起比较。",
    "Open-Meteo's ensemble API also offers the 51 members of ECMWF AIFS at 0.25°, so you can set them beside the IFS's 51 members.",
    "API ensemble Open-Meteo juga menawarkan 51 ahli ECMWF AIFS pada 0.25°, jadi anda boleh membandingkannya dengan 51 ahli IFS.",
    src=["OM-ENS"]),
 ]},
 ]}

terms = [
 ("ml-weather-model", T("机器学习天气模型", "Machine-learning weather model", "Model cuaca pembelajaran mesin"), T("从历史资料学会天气怎样变化、再往前推的模型。", "A model that learns from past data how weather evolves, then steps forward.", "Model yang belajar daripada data lalu bagaimana cuaca berkembang, kemudian melangkah ke depan.")),
 ("training-data", T("训练数据", "Training data", "Data latihan"), T("AI 模型用来学习的历史资料，例如 ERA5。", "The historical data an AI model learns from, such as ERA5.", "Data sejarah tempat model AI belajar, seperti ERA5.")),
 ("graphcast", T("GraphCast", "GraphCast", "GraphCast"), T("Google DeepMind 的 AI 天气模型，2023 年发表。", "Google DeepMind's AI weather model, published 2023.", "Model cuaca AI Google DeepMind, diterbitkan 2023.")),
 ("aifs", T("AIFS（ECMWF 人工智能预报系统）", "AIFS", "AIFS"), T("ECMWF 的 AI 模型，有单一和集合两种，2025 年起运作。", "ECMWF's AI model, single and ensemble, operational since 2025.", "Model AI ECMWF, tunggal dan ensemble, beroperasi sejak 2025.")),
]

sources = [
 {"id": "GRAPHCAST", "short": "Lam et al. 2023", "title": "Learning skillful medium-range global weather forecasting (Science 382, 6677)", "publisher": "R. Lam, A. Sanchez-Gonzalez, M. Willson et al. (Google DeepMind), 2023", "url": "https://doi.org/10.1126/science.adi2336", "accessed": "2026-10-03"},
]

quiz = [
 {"stage": 8, "chapter": "ch32", "q": T("AI 天气模型主要从哪里学？", "What do AI weather models mostly learn from?", "Daripada apa model cuaca AI kebanyakannya belajar?"),
  "options": [T("几十年的再分析资料，例如 ERA5", "Decades of reanalysis such as ERA5", "Analisis semula berdekad-dekad seperti ERA5"), T("新闻报道", "News reports", "Laporan berita"), T("只有今天的雷达", "Only today's radar", "Hanya radar hari ini"), T("气象员的直觉", "Forecasters' hunches", "Firasat peramal")],
  "answer": 0, "why": T("所以物理模型做的再分析仍然很重要。", "So the physics-made reanalysis still matters.", "Jadi analisis semula buatan fizik masih penting.")},
 {"stage": 8, "chapter": "ch32", "q": T("ECMWF 的 AIFS ENS 从什么时候正式运作？", "Since when has ECMWF's AIFS ENS run operationally?", "Sejak bila AIFS ENS ECMWF beroperasi?"),
  "options": [T("2025 年 7 月 1 日", "1 July 2025", "1 Julai 2025"), T("1975 年", "1975", "1975"), T("2010 年", "2010", "2010"), T("还没有", "Not yet", "Belum lagi")],
  "answer": 0, "why": T("AIFS Single 更早，2025 年 2 月 25 日。", "AIFS Single came earlier, 25 Feb 2025.", "AIFS Single lebih awal, 25 Feb 2025.")},
]

write_chapter(chapter, terms, sources, quiz)
