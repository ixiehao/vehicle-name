# 变更记录 / Changelog

本仓库遵循「语义化版本 2.0.0」(MAJOR.MINOR.PATCH)近似约定:
This project loosely follows Semantic Versioning 2.0.0 (MAJOR.MINOR.PATCH):

- MAJOR:结构/许可等不兼容变更 — breaking structural/license changes
- MINOR:新增数据/功能,向后兼容 — backward-compatible additions
- PATCH:修正与微调 — fixes and tweaks

---

## [1.3.0] — 2026-08-09

### 新增 Added

- **大规模扩充品牌**:新增 37 个品牌,覆盖 16 个国家/地区,品牌总数达 103。
  - 欧洲:路特斯、MG、摩根、卡特汉姆、蓝旗亚、阿巴斯、帕加尼、布加迪、阿尔派、萨博、达契亚、西雅特、Cupra、拉达、塔塔、马恒达、宝腾、Perodua、迈巴赫、阿尔宾娜。
  - 美洲:悍马、庞蒂亚克、奥兹莫比尔、水星、普利茅斯、德罗宁、Rivian、Lucid。
  - 亚洲:双龙(KGM)及中国新能源品牌埃安、零跑、哪吒、岚图、智己、极狐、问界、广汽传祺。
- **新增车型 161 款**(1195 → 1356):含路特斯Elise/Eletre、布加迪Chiron/Tourbillon、蓝旗亚Delta/Stratos、问界M9、埃安昊铂、仰望U9、方程豹豹5/豹8、腾势N7/N8/Z9 等。
- **补充 BYD 子品牌车型 6 款**(仰望U9、腾势N7/N8/Z9、方程豹豹5/豹8),并入 `cn_byd.json`。

### 统计 Statistics

- 车型总数:1356(现售 768 / 停产 588)
- 覆盖品牌:103 个(16 国分组)
- 待核实条目:`data/pending_verification.json` 剩 16 项

---

## [1.2.0] — 2026-08-09

### 新增 Added

- **新增品牌 3 个**:斯柯达 Škoda(捷克,cz_skoda.json)、GMC(美国,us_gmc.json)、小米 Xiaomi(中国,cn_xiaomi.json),并补齐对应车型条目。
- **补充现有品牌缺失车型 21 款**:NIO Firefly(萤火虫)、XPeng P7+、理想 i8/i6、smart精灵#5、Genesis GV80 Coupe、RAM Rampage、林肯 Z、劳斯莱斯 Silver Cloud(银云)、Tesla Semi、Koenigsegg CC850、红旗 EH7/EHS7、Jeep Recon/Wagoneer S、宾利 Brooklands、极氪 7X/MIX/007 GT、欧拉闪电猫、魏牌高山。
- **联网核实并关闭待核实条目 35 项**(51 → 16):依据维基百科与媒体/官方报道确认多款车型的停产年份与市场状态(如 Acura TLX/ZDX、Nissan Tiida 2026 停产、Genesis G70 中国停售/韩国 2027 停产、Cadillac Escalade 台湾「凱雷德」、Mazda CX-4/CX-9 等),并同步修正对应条目。

### 修正 Fixed

- `scripts/validate.py`:`_DIACRITICS` 增加 `š`/`ß` 归一化(支持 Škoda 品牌 id 前缀匹配)。
- 修正 Genesis GV80 轿跑版年份(2023 → 2024)。

### 统计 Statistics

- 车型总数:1195(现售 655 / 停产 540)
- 覆盖品牌:66 个
- 待核实条目:`data/pending_verification.json` 剩 16 项

---

## [1.1.0] — 2026-08-09

### 新增 Added

- **项目更名**:`carsname` → `vehiclename`(汽车的全球通用名 vehicle),仓库 URL 与文档同步更新。
- **开源化改造**:新增 `LICENSE`(CC BY-SA 4.0)、`CODE_OF_CONDUCT.md`、`SECURITY.md`、`PRIVACY.md`、`DISCLAIMER.md`、`CONTRIBUTING.md`(中/英)、`README.en.md`。
- **文件系统重构**:数据拆分为 `data/`(meta/vehicle_classes/glossary/brands/models/pending),构建产物输出至 `dist/`,新增 `scripts/build.py` 与 `scripts/validate.py`。
- **车型数据大幅扩充**:现售 + 停产车型名录(见下方统计);基于各品牌官网历史资料库(铃木、丰田、日产、本田、马自达、三菱、大发等)补充了大量 1955-2000 年代历史车型。
- **模型字段新增**:`status`(current/discontinued/concept)与 `years`(生产年份)。

### 统计 Statistics

- 车型总数:1158(现售 620 / 停产 538)
- 覆盖品牌:63 个(全覆盖)
- 待核实条目:`data/pending_verification.json` 共 51 项(其中车型 38 项)

---

## [1.0.0] — 2026-08-09

### 新增 Added

- 初始版本。
- 内容:级别体系 6 类、术语 72 条(10 大类)、品牌 63 个、车型 84 款、跨市场异名 24 组、待核实清单 13 项。
- 文件:`README.md`、`car-names-database.json`、`car-names-database.md`。
