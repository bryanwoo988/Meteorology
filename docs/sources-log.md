# Sources log

Every fact in the app that does not come from the reference books is checked
against its source before it is written. One row per claim.

| 章 | 说法 | 网址 | 查阅日期 |
|---|---|---|---|
| 5 | 吉隆坡 2025 年逐时平均气温、露点、相对湿度（露点约 22–24 °C，相对湿度清晨约 93 %、下午约 59 %） | https://archive-api.open-meteo.com/v1/archive?latitude=3.139&longitude=101.6869&start_date=2025-01-01&end_date=2025-12-31&hourly=temperature_2m,dew_point_2m,relative_humidity_2m&timezone=Asia%2FKuala_Lumpur | 2026-10-02 |
| 2 | 全球月平均 CO₂：2026 年 6 月 427.62 ppm | https://gml.noaa.gov/ccgg/trends/global.html | 2026-10-02 |
| 2 | WHO 紫外线指数建议：0–2 / 3–7 / 8+ | https://www.who.int/news-room/questions-and-answers/item/radiation-the-ultraviolet-(uv)-index | 2026-10-02 |
| 1 | ECMWF：1975 年成立、独立政府间组织、35 个国家支持；Reading、Bologna、Bonn | https://www.ecmwf.int/en/about/who-we-are ；https://www.ecmwf.int/en/about | 2026-10-02 |
| 1 | WMO：193 个会员国和地区；1950 年公约生效，一年后成为联合国专门机构 | https://wmo.int/resources/wmo-bulletin/wmo-bulletin-vol-73-2-2024/2025-celebrating-75-years-of-wmo-science-action | 2026-10-02 |
| 1 | MetMalaysia 服务：天气、海洋预报、地震海啸、气候监测 | https://www.met.gov.my/en/ | 2026-10-02 |
| 1 | ASMC：1993 年 1 月成立，设于新加坡气象局，监测火灾与跨境烟霾 | https://asmc.asean.org/asmc-about/ | 2026-10-02 |
| 1 | GEFS 由 NOAA EMC 运行（GFS 集合，31 成员） | https://emc.ncep.noaa.gov/emc/pages/numerical_forecast_systems/gefs.php | 2026-10-02 |
| 1 | JMA 运行 Himawari-8/9 | https://www.data.jma.go.jp/mscweb/en/himawari89/himawari_cast/himawari_cast.php | 2026-10-02 |
| 4 | 吉隆坡 2025-03-18（晴，日较差约 11 °C，最高温在午后）与 2025-01-28（阴雨，日较差约 2 °C）逐时气温、短波辐射 | https://archive-api.open-meteo.com/v1/archive?latitude=3.139&longitude=101.6869&start_date=2025-01-01&end_date=2025-12-31&hourly=temperature_2m,cloud_cover,shortwave_radiation,precipitation&timezone=Asia%2FKuala_Lumpur | 2026-10-02 |
| 4 | 吉隆坡 2025 年各月平均气温 26.1–29.7 °C（相差约 3.6 °C） | （同 ch05 的 ERA5 逐时资料） | 2026-10-02 |
| 4 | ERA5 网格 0.25°（约 25 km），1940 年至今，逐时 | https://open-meteo.com/en/docs/historical-weather-api | 2026-10-02 |
| 7 | 吉隆坡上空 0 °C 层（冻结高度）：2026 年 8–10 月逐时预报平均约 5,030 m（4,760–5,350 m） | https://api.open-meteo.com/v1/forecast?latitude=3.139&longitude=101.6869&hourly=freezing_level_height,temperature_500hPa,geopotential_height_500hPa&past_days=60&forecast_days=1&timezone=Asia%2FKuala_Lumpur | 2026-10-02 |
| 7 | CAPE：上升气块正浮力的垂直积分；CIN：比气块暖的气层的累积抑制 | https://www.noaa.gov/jetstream/appendix/weather-glossary-c | 2026-10-02 |
| 16/17 | MetMalaysia《Review of the Southwest Monsoon 2024 in Malaysia》（Research Publication No. 2/2025）：西南季风约 5 月中至 10 月中；西海岸 5–8 月雨量略高，与夜间及清晨苏门答腊飑线和局地对流有关；西南季风比东北季风和季风转换期干 | https://www.met.gov.my/data/research/researchpapers/2025/RP04_2025.pdf | 2026-10-02 |
| 10 | 吉隆坡上空气压层平均高度与气温（2026-08-03 至 10-02 逐时预报平均）：见 data/series/kl-levels-2026.json | https://api.open-meteo.com/v1/forecast（参数见 series 文件） | 2026-10-02 |
| 12 | 台风 Vamei：2001-12-27 在新加坡附近 1.5°N 形成，有记录以来最接近赤道 | https://doi.org/10.1029/2002GL016365 （Crossref 元数据核对作者） | 2026-10-02 |
| 14 | MetMalaysia：中等或强厄尔尼诺时，沙巴、砂拉越在西南季风（6–8 月）和东北季风（11–2 月）雨量远低于平均；半岛只在西南季风（6–8 月）偏低；弱厄尔尼诺影响很小；拉尼娜时西太平洋赤道气压降低、云多雨大 | https://www.met.gov.my/en/pendidikan/fenomena-cuaca/ | 2026-10-02 |
| 16/17 | MetMalaysia：东北季风 11–3 月，西南季风 5 月底–9 月，其间为季风转换期；雷暴多在 4–5 月和 10–11 月季风转换期；飑线（Sumatras）4–11 月在半岛西海岸 | https://www.met.gov.my/en/pendidikan/fenomena-cuaca/ | 2026-10-02 |
| 13/14 | NOAA OI SST V2 月平均（1° 网格）与 1991–2020 气候平均；2015-12、2013-12、2010-12 距平；Niño 3.4 区平均 +2.76 / −1.69 °C（与 ONI 相符） | https://psl.noaa.gov/data/gridded/data.noaa.oisst.v2.html | 2026-10-02 |
| 14 | MJO：热带季节内（30–90 天）变化最大的成分，以约 4–8 m/s 向东移动，周期约 30–60 天 | Fundamentals of Meteorology p.175 | — |
| 14 | MetMalaysia：MJO 第 4、5 相位活跃时增强海洋性大陆（含马来西亚）的对流 | https://www.met.gov.my/data/research/researchpapers/2025/RP04_2025.pdf | 2026-10-02 |
| 14 | NOAA CPC 自 2026-02-01 起改用 RONI 作为官方 ENSO 指数：Niño 3.4 区 3 个月滑动平均海温距平减去热带（20°N–20°S）平均，再调整方差；±0.5 °C 门槛，至少连续 5 个重叠季 | https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/ ；https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/announcement.php | 2026-10-02 |
| 14 | RONI 数据（至 2026 JJA = +1.36 °C） | https://www.cpc.ncep.noaa.gov/data/indices/RONI.ascii.txt | 2026-10-02 |
| 15 | Köppen–Geiger 1991–2020 气候分区（Beck et al. 2023，CC0）；吉隆坡格点为 Af | https://doi.org/10.6084/m9.figshare.21789074 （figshare 文件 42602809） | 2026-10-02 |
| 13 | NOAA：大潮在新月与满月（每月两次），小潮在上、下弦月，日月成直角 | https://oceanservice.noaa.gov/facts/springtide.html | 2026-10-02 |
| 13 | NOAA：风暴潮=单由风暴造成的海水上升，主要因风把水推向岸；风暴潮位=风暴潮+天文潮 | https://oceanservice.noaa.gov/facts/stormsurge-stormtide.html | 2026-10-02 |
| 14 | IOD 正相位：爪哇、苏门答腊附近（东印度洋）偏冷、西印度洋偏暖，印尼和澳洲偏干、东非偏湿；负相位相反；DMI 西区 10°S–10°N 50°–70°E，东区 10°S–0° 90°–108°E；多在 9–11 月达到高峰 | https://www.climate.gov/news-features/blogs/enso/meet-enso%E2%80%99s-neighbor-indian-ocean-dipole | 2026-10-02 |
| 14 | MJO：向东移动的云、雨、风、气压扰动，约 30–60 天绕回原处 | https://www.climate.gov/news-features/blogs/enso/what-mjo-and-why-do-we-care | 2026-10-02 |
| 14 | RMM 相位：8、1 西半球与非洲；2、3 印度洋；4、5 海洋性大陆；6、7 西太平洋 | https://repository.library.noaa.gov/view/noaa/52430/noaa_52430_DS1.pdf | 2026-10-02 |
| 14 | ONI（旧指数）2026 JJA = +1.80 °C，对比 RONI +1.36 °C | https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt | 2026-10-02 |
| 14 | MetMalaysia 2024 西南季风检讨：ENSO 中性、IOD 中性，远方影响小；MJO 5 月第 5 相位、9 月上中旬第 4–5 相位活跃，可能加强海洋性大陆对流；6–8 月 MJO 弱 | https://www.met.gov.my/data/research/researchpapers/2025/RP04_2025.pdf（pp. 5–7） | 2026-10-02 |
| 14 | FUN p.175：拉尼娜使东南亚海温下降，马来西亚、菲律宾、印尼大雨（书中原文） | Fundamentals of Meteorology p.175 | — |
| 14 | BoM RMM 文件栏位 year, month, day, RMM1, RMM2, phase, amplitude；最后一行 2024-02-24 | http://www.bom.gov.au/climate/mjo/graphics/rmm.74toRealtime.txt | 2026-10-02 |
| 15 | WMO 气候标准平均值：最近一个以 0 结尾的 30 年（如 1991–2020） | https://community.wmo.int/site/knowledge-hub/programmes-and-initiatives/climate-services/wmo-climatological-normals | 2026-10-02 |
| 15 | WMO 主要气候参数：Number of days with precipitation ≥ 1 mm | https://www.ncei.noaa.gov/data/oceans/archive/arc0216/0253808/6.6/data/0-data/documents/WMO_Normals_9120_Format_and_Parameters.pdf | 2026-10-02 |
| 15 | ETCCDI：wet day = RR ≥ 1 mm | https://etccdi.pacificclimate.org/list_27_indices.shtml | 2026-10-02 |
| 15 | IMD：Rainy Day = 一天雨量 2.5 mm 或以上 | https://www.imdpune.gov.in/Reports/glossary.pdf | 2026-10-02 |
| 15 | TERM p.285：Rain day 国际惯例 ≥ 0.2 mm（书中原文） | Terminology p.285 | — |
| 15 | 吉隆坡 2025 年 ERA5 日雨量：≥0.2 mm 315 天、≥1 mm 267 天、≥2.5 mm 215 天；全年 2,800.9 mm | https://archive-api.open-meteo.com/v1/archive?latitude=3.139&longitude=101.6869&start_date=2025-01-01&end_date=2025-12-31&daily=precipitation_sum&timezone=Asia%2FKuala_Lumpur | 2026-10-02 |
| 15 | Open-Meteo ERA5：0.25°、1940 至今、每天更新、延迟 5 天 | https://open-meteo.com/en/docs/historical-weather-api | 2026-10-02 |
| 15 | WMO：2025 年全球平均地面气温比 1850–1900 高 1.44 ± 0.13 °C（八套数据）；2015–2025 为最热 11 年；2025 年首尾有拉尼娜 | https://wmo.int/news/media-centre/wmo-confirms-2025-was-one-of-warmest-years-record | 2026-10-02 |
| 15 | Beck et al. 2023, Scientific Data 10, 724（Crossref 核对） | https://doi.org/10.1038/s41597-023-02549-6 | 2026-10-02 |
