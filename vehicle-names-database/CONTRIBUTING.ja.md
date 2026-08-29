# コントリビューションガイド

言語 / Languages: [English](CONTRIBUTING.en.md) · [简体中文](CONTRIBUTING.md) · [繁體中文](CONTRIBUTING.zh-TW.md) · [日本語](CONTRIBUTING.ja.md)

世界中のコントリビューターを歓迎します。データベースの拡充と改善にご協力いただき、ありがとうございます。

## 1. 貢献できる内容

| 種類 | 内容 |
|------|------|
| **車種の追加** | 現行車・生産終了車を追加します |
| **翻訳の修正** | 古い、または誤った簡体字中国語・繁体字中国語・日本語の名称を修正します |
| **ブランドの追加** | 未収録のブランドを追加します（4 言語すべての名称が必要です） |
| **用語集の拡充** | 不足している自動車専門用語を追加します |
| **市場別名称の追加** | 同じ車種の市場ごとの名称差を記録します |
| **文書・ツールの改善** | README、翻訳、例、ビルド・検証スクリプトを改善します |

## 2. クイックスタート

1. このリポジトリを Fork し、ローカルに clone します。
2. ブランチを作成します：`git checkout -b add-xxx-models`。
3. `data/` 配下のデータファイルを編集します。
4. `python3 scripts/validate.py` を実行し、必ず成功させます。
5. `python3 scripts/build.py` を実行し、再生成された `dist/` をコミットします。
6. コミット、push の後、Pull Request を作成します。

アカウント登録や CLA への署名は不要です。提出により、あなたの貢献を [CC BY-SA 4.0](../LICENSE) でライセンスすることに同意したものとみなされます。

## 3. データ編集ルール

### 3.1 車種を追加する

対象ブランドの `data/models/` ファイルに項目を追加します。

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
  "note": "世界的なベストセラー車名。Levin は中国の一汽系における姉妹車名",
  "verified": "verified"
}
```

- `id`：`model:{brand_lowercase}:{model_lowercase}` 形式で、全体で一意にします。
- `brand`：`data/brands.json` の英語ブランド名と一致させます。
- `names`：`en`、`zh-CN`、`zh-TW`、`ja` の 4 キーをすべて含めます。
- `segment`、`body_style`、`powertrain`：`data/vehicle_classes.json` にある id を参照します。
- `status` は `current`、`discontinued`、`concept` のいずれか、`years` は生産年（例：`1995–2012` または `1995–present`）です。
- ある言語の名称が不明な場合は、「—」または英語名を仮値にし、`verified: "pending"` を設定して `pending_verification.json` に登録します。

### 3.2 ブランドと用語を追加する

- ブランドは `data/brands.json` に追加します。必要なフィールドは `id`、`country`、`names{en,zh-CN,zh-TW,ja}`、`note` です。
- 用語は `data/glossary.json` の既存 10 カテゴリのいずれかに追加します。必要なフィールドは `id`、`category`、`names`、`abbr`、`note` です。

### 3.3 共通ルール

- **唯一のデータソース**：編集は `data/` のみで行い、`scripts/build.py` で `dist/` を更新します。
- **出典を記載する**：公式サイト、Wikipedia、規格番号などを `note` に記録します。
- **根拠のない推測をしない**：未確認の項目は必ず `verified: "pending"` にします。
- **並び順を維持する**：車種は `id` 順にして、差分を確認しやすくします。
- ビルド直後以外は `dist/` を手作業で編集しないでください。

## 4. 検証、PR、問い合わせ

```bash
python3 scripts/validate.py  # 必須
python3 scripts/build.py     # データ変更後は必須
```

検証の失敗時には、重複 id、無効な参照、言語キーの不足などが表示されます。一つずつ修正してください。PR には明確なタイトル、変更内容、出典を記載し、1 つのテーマに絞ってください。大規模な追加は複数の PR に分けるとレビューしやすくなります。

参加により [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) に従うことに同意したものとします。翻訳に関する意見の相違は、感情ではなく確認可能な出典に基づいて解決してください。誤ったデータを見つけた場合は、修正 PR を出すか、項目 id と公式リンク・スクリーンショットなどの根拠を添えて Issue を作成してください。
