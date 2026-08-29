# 貢獻指南

語言 / Languages: [English](CONTRIBUTING.en.md) · [简体中文](CONTRIBUTING.md) · [繁體中文](CONTRIBUTING.zh-TW.md) · [日本語](CONTRIBUTING.ja.md)

歡迎世界各地的貢獻者，感謝您協助擴充與改善本資料庫！

## 1. 可貢獻的項目

| 類型 | 說明 |
|------|------|
| **新增車型** | 新增現行或停產車型 |
| **修正譯名** | 修正過時或錯誤的簡體中文、繁體中文或日語名稱 |
| **新增品牌** | 補充資料庫未收錄的品牌（必須提供四語名稱） |
| **擴充術語** | 新增遺漏的汽車專業術語 |
| **跨市場異名** | 記錄同一車型在不同市場的名稱差異 |
| **改善文件或工具** | 改進 README、翻譯、範例或建置、驗證腳本 |

## 2. 快速開始

1. Fork 本倉庫並複製到本機。
2. 建立分支：`git checkout -b add-xxx-models`。
3. 編輯 `data/` 下的資料檔。
4. 執行 `python3 scripts/validate.py`，且必須通過。
5. 執行 `python3 scripts/build.py`，並提交重新產生的 `dist/` 檔案。
6. 提交、推送，並建立 Pull Request。

無須另行註冊或簽署 CLA；提交即表示您同意依 [CC BY-SA 4.0](../LICENSE) 授權您的貢獻。

## 3. 資料編輯規則

### 3.1 新增車型

在 `data/models/` 對應品牌的檔案中新增項目：

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
  "note": "全球暢銷車系；Levin 為中國一汽的姊妹名稱",
  "verified": "verified"
}
```

- `id`：`model:{brand_lowercase}:{model_lowercase}`，全域唯一。
- `brand`：必須與 `data/brands.json` 的英文品牌名稱一致。
- `names`：必須包含 `en`、`zh-CN`、`zh-TW`、`ja` 四個鍵。
- `segment`、`body_style`、`powertrain`：必須引用 `data/vehicle_classes.json` 中既有的 id。
- `status`：使用 `current`、`discontinued` 或 `concept`；`years` 為生產年份，例如 `1995–2012` 或 `1995–present`。
- 若某語言名稱不明，請以「—」或英文作為暫代值，設為 `verified: "pending"`，並登錄於 `pending_verification.json`。

### 3.2 新增品牌與術語

- 品牌請追加至 `data/brands.json`，欄位為 `id`、`country`、`names{en,zh-CN,zh-TW,ja}` 與 `note`。
- 術語請追加至 `data/glossary.json` 的既有 10 個類別之一，欄位為 `id`、`category`、`names`、`abbr` 與 `note`。

### 3.3 通用規則

- **單一資料來源**：只編輯 `data/`，再執行 `scripts/build.py` 更新 `dist/`。
- **標記來源**：在 `note` 中記錄官方網站、維基百科或標準編號等依據。
- **不可無聲猜測**：未確認的內容一律標為 `verified: "pending"`。
- **維持排序**：車型以 `id` 排序，便於檢視差異。
- 除非剛執行完建置，否則不要手動修改 `dist/`。

## 4. 驗證、PR 與求助

```bash
python3 scripts/validate.py  # 必做
python3 scripts/build.py     # 修改資料後必做
```

驗證失敗會列出重複 id、無效引用與遺漏語言鍵等具體錯誤；請逐項修正。PR 請使用清楚的標題、說明修改與資料來源，並盡量聚焦單一主題。大量資料請分批提交，方便審閱。

參與本專案即表示同意遵守 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。譯名爭議請以可查證的來源討論。若發現錯誤資料，可提交修正 PR，或在 Issue 中附上條目 id 與官方連結、截圖等證據。
