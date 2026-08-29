# Contributing Guide

Languages: [English](CONTRIBUTING.en.md) · [简体中文](CONTRIBUTING.md) · [繁體中文](CONTRIBUTING.zh-TW.md) · [日本語](CONTRIBUTING.ja.md)

Welcome, contributors from around the world! Thank you for helping to grow and improve this database.

---

## 1. Ways to Contribute

| Type | Description |
|------|-------------|
| **Add models** | Add current or discontinued models (the most common contribution — welcome!) |
| **Fix translations** | Correct outdated/incorrect Chinese (Simplified/Traditional) or Japanese names |
| **Add brands** | Add brands not yet in the database (all 4 language names required) |
| **Expand glossary** | Add missing automotive terms |
| **Cross-market aliases** | Document name differences for the same model across markets |
| **Improve docs** | Improve README, translations, examples |
| **Improve tooling** | Improve `scripts/build.py`, `scripts/validate.py`, etc. |

---

## 2. Quick Start

1. **Fork** this repository and clone it locally.
2. Create a branch: `git checkout -b add-xxx-models`.
3. Edit data files under `data/` (see §3).
4. Validate: `python3 scripts/validate.py` (**must pass**).
5. Build: `python3 scripts/build.py`, and commit the regenerated `dist/` outputs.
6. Commit, push, and open a **Pull Request**.

> No account registration or CLA signing required. By submitting, you agree to license your contribution under [CC BY-SA 4.0](../LICENSE).

---

## 3. Data Editing Rules

### 3.1 Adding a Model

Append to the matching brand file under `data/models/`:

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
  "note": "Best-selling nameplate worldwide; Levin is the FAW sibling name in China",
  "verified": "verified"
}
```

Field requirements:

- `id`: `model:{brand_lowercase}:{model_lowercase}`, globally unique.
- `brand`: must match the English name in `data/brands.json`.
- `names`: must contain all four keys `en` / `zh-CN` / `zh-TW` / `ja`.
- `segment` / `body_style` / `powertrain`: must be existing ids from `data/vehicle_classes.json`.
- `status`: `current` / `discontinued` / `concept`.
- `years`: production years, e.g. `1995–2012` or `1995–present`.
- If a name in a language is unknown: use "—" or the English name as placeholder, set `verified: "pending"`, and register it in `pending_verification.json`.

### 3.2 Adding a Brand

Append to `data/brands.json` with fields: `id`, `country`, `names{en,zh-CN,zh-TW,ja}`, `note`.

### 3.3 Adding a Term

Append to `glossary.terms` in `data/glossary.json` under one of the 10 existing categories: `id`, `category`, `names`, `abbr`, `note`.

### 3.4 General Rules

- **Single source of truth**: edit only `data/`, then run `scripts/build.py` to regenerate `dist/` — the two stay in sync.
- **Cite sources**: record the source in `note` (official site / Wikipedia / standard number).
- **Never guess silently**: mark unconfirmed entries `verified: "pending"`.
- **Keep sorted**: models are ordered by `id` for diff-friendly reviews.
- **Do not hand-edit** `dist/` files unless you have just run `build.py`.

---

## 4. Validate & Build

```bash
# Validate (required)
python3 scripts/validate.py

# Build (required after data changes)
python3 scripts/build.py
```

Validation failures list concrete errors (duplicate ids, invalid references, missing language keys, etc.). Fix them one by one.

---

## 5. Pull Request Guidelines

- Clear PR title, e.g. `add: Toyota bZ4X` or `fix: Mazda Japanese spelling`.
- Describe what you changed and your sources.
- Keep one PR focused on one topic.
- For very large additions, split into multiple PRs for easier review.

---

## 6. Code of Conduct

By participating you agree to [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Be respectful; resolve translation disputes with cited evidence, not heated arguments.

---

## 7. FAQ

**Q: I don't know the Taiwan/Japanese name of a model.**
A: Fill in the languages you know, use the English name as placeholder for the rest, set `verified: "pending"`, and note it in the PR description. Other contributors will help complete it.

**Q: Can I submit many models at once?**
A: Yes, but group by brand, keep ids unique and references valid. Passing `validate.py` is the baseline requirement.

**Q: How do I report wrong data?**
A: Submit a fixing PR, or open an Issue with the entry id and evidence (official link/screenshot).
