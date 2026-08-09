# 变更记录 / Changelog

本仓库遵循「语义化版本 2.0.0」(MAJOR.MINOR.PATCH)近似约定:
This project loosely follows Semantic Versioning 2.0.0 (MAJOR.MINOR.PATCH):

- MAJOR:结构/许可等不兼容变更 — breaking structural/license changes
- MINOR:新增数据/功能,向后兼容 — backward-compatible additions
- PATCH:修正与微调 — fixes and tweaks

---

## [1.1.0] — 2026-08-09

### 项目 Project

- **国际化命名**:项目名 `vehiclename`,数据目录 `vehicle-names-database/`,构建产物 `dist/vehicle-names-database.json` / `dist/vehicle-names-database.md`,英文标题统一为 *Multilingual Vehicle Name Database*;CI 工作流同步适配。
- **开源化改造**:新增 `LICENSE`(CC BY-SA 4.0)、行为准则/安全/隐私/免责声明文档、中英贡献指南、README.en.md,以及 GitHub Issue/PR 模板与 CI 校验工作流。
- **文件系统重构**:数据拆分为 `data/`,构建产物输出至 `dist/`,新增 `scripts/build.py` 与 `scripts/validate.py`。

### 新增 Added

- **品牌大规模扩充**:品牌总数 63 → 164,覆盖 16 个国家/地区(新增欧洲、美洲及中国品牌 100+ 个)。
- **车型数据大幅扩充**:车型总数 84 → 2041(含 1955-2000 年代历史车型与中国在售/历史车型)。
- **补充子品牌车型**:BYD(仰望/腾势/方程豹)、吉利(极氪/领克/银河/几何)、长城(哈弗/魏牌/坦克/欧拉)、奇瑞(捷途/星途)、铃木(长安铃木系列)等。
- **模型字段新增**:`status`(current/discontinued/concept)与 `years`(生产年份)。
- **联网核实待核实条目**:依据权威资料关闭大量待核实条目,部分年份不确定的条目以 `verified: "pending"` 标注。

### 修正 Fixed

- `scripts/validate.py`:`_DIACRITICS` 增加 `š`/`ß` 归一化(支持 Škoda 品牌 id 前缀匹配)。
- 修正部分车型年份与市场状态数据。

### 统计 Statistics

- 车型总数:2041(现售 / 停产)
- 覆盖品牌:164 个
- 术语:72 条(10 大类) | 级别体系:6 类 | 跨市场异名:24 组
- 待核实条目:`data/pending_verification.json` 及条目内 pending 标记若干

---

## [1.0.0] — 2026-08-09

### 新增 Added

- 初始版本。
- 内容:级别体系 6 类、术语 72 条(10 大类)、品牌 63 个、车型 84 款、跨市场异名 24 组、待核实清单 13 项。
- 文件:`README.md`、`vehicle-names-database.json`、`vehicle-names-database.md`。
