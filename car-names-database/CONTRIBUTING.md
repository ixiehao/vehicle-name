# 贡献指南(Contributing Guide)

English: [CONTRIBUTING.en.md](CONTRIBUTING.en.md)

欢迎全球网友参与本资料库的补充与修改!感谢您的贡献。

---

## 1. 贡献类型

| 类型 | 说明 |
|------|------|
| **补充车型** | 新增现售或停产车型(最常见,欢迎多多提交) |
| **修正译名** | 修正错误或过时的中文(简/繁)、日文名称 |
| **补充品牌** | 新增资料库未收录的品牌(需同时提供 4 语言名称) |
| **术语扩充** | 补充 glossary 缺失的汽车专业术语 |
| **跨市场异名** | 补充同一车型在不同市场的名称差异 |
| **文档改进** | 改进 README、翻译、示例等 |
| **工具改进** | 改进 build.py / validate.py 等构建工具 |

---

## 2. 快速开始

1. **Fork** 本仓库并克隆到本地。
2. 创建新分支:`git checkout -b add-xxx-models`。
3. 修改 `data/` 下的数据文件(见 §3 编辑规则)。
4. 运行校验:`python3 scripts/validate.py`(**必须通过**)。
5. 重新构建:`python3 scripts/build.py`,将生成的 `dist/` 产物一并提交。
6. 提交并推送,发起 **Pull Request**。

> 不需要注册任何账号或签署 CLA。提交即表示您同意在 [CC BY-SA 4.0](../LICENSE) 下授权您的贡献。

---

## 3. 数据编辑规则

### 3.1 新增车型

在 `data/models/` 对应品牌的 JSON 文件中追加:

```json
{
  "id": "model:toyota:corolla",
  "brand": "Toyota",
  "names": {"en": "Corolla", "zh-CN": "卡罗拉/雷凌(广汽)", "zh-TW": "Corolla Altis", "ja": "カローラ"},
  "segment": "class:cn:a",
  "body_style": "body:sedan",
  "powertrain": "pt:ice",
  "status": "current",
  "years": "1966–present",
  "note": "全球累计销量最高车型;雷凌为大陆姊妹名",
  "verified": "verified"
}
```

字段要求:

- `id`:`model:{品牌小写英文}:{车型小写英文}`,全球唯一。
- `brand`:与 `data/brands.json` 中的英文名一致。
- `names`:必须包含 `en` / `zh-CN` / `zh-TW` / `ja` 四个键。
- `segment` / `body_style` / `powertrain`:必须是 `data/vehicle_classes.json` 中已存在的 id。
- `status`:`current` / `discontinued` / `concept`。
- `years`:生产年份,如 `1995–2012` 或 `1995–present`。
- 若某语言名称不确定:**写"无"或留英文名**,`verified` 置 `pending`,并登记到 `pending_verification.json`。

### 3.2 新增品牌

在 `data/brands.json` 中按国别分组追加,字段:`id`、`country`、`names{en,zh-CN,zh-TW,ja}`、`note`。同时同步更新 README 中的品牌计数(可选,构建脚本会重新统计)。

### 3.3 新增术语

在 `data/glossary.json` 的 `terms` 中追加,归入现有 10 大类别;字段:`id`、`category`、`names`、`abbr`、`note`。

### 3.4 通用规则

- **同步原则**:只改 `data/`,然后运行 `build.py` 生成 `dist/`,两者永远一致。
- **来源标注**:在 `note` 中记录来源(官网 / 维基 / 标准号),便于追溯。
- **不确定即标注**:无法确认的条目一律 `verified: "pending"`,严禁静默猜测。
- **保持排序**:车型条目按 `id` 排序,便于 diff 审阅。
- **不要改动** `dist/` 中的文件,除非您已运行 `build.py`。

---

## 4. 校验与构建

```bash
# 校验(必做)
python3 scripts/validate.py

# 构建(修改数据后必做)
python3 scripts/build.py
```

校验失败会列出具体错误(重复 ID、无效引用、缺少语言键等),请逐一修复。

---

## 5. Pull Request 规范

- PR 标题清晰,如 `add: Toyota bZ4X / fix: Mazda 日文表记`。
- 说明改动内容与数据来源。
- 一个 PR 尽量聚焦一个主题(如"新增某品牌车型"或"修正某译名"),避免混合无关修改。
- 若 PR 涉及大量新增数据,可拆分为多个 PR 便于审阅。

---

## 6. 行为准则

参与本项目即表示同意遵守 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。请保持友善、尊重,翻译争议请基于来源证据讨论,而非情绪化争论。

---

## 7. 常见问题

**Q: 我不知道某车型的台湾/日本名称怎么办?**
A: 可以只填你知道的语言,其余语言写英文名占位,`verified: "pending"`,并在 PR 描述中说明。其他贡献者会帮助补齐。

**Q: 车型太多,我可以一次提交很多吗?**
A: 可以,但建议按品牌分组,并确保每个条目的 `id` 唯一、引用有效。运行 validate.py 是底线要求。

**Q: 我发现的错误数据怎么报告?**
A: 直接提交修正 PR,或在 Issues 中附上条目 ID 与证据(官方链接/截图)。
