#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate.py — 数据完整性校验
=============================

用法:
    python3 scripts/validate.py [--fix]

检查项:
  1. 所有文件均可解析为合法 JSON。
  2. 车型条目:id 唯一、字段齐全、4 语言键齐全。
  3. 车型引用的 segment / body_style / powertrain 必须存在于 vehicle_classes。
  4. 车型 brand 必须存在于 brands(英文名匹配)。
  5. 品牌 id 唯一;术语 id 唯一;跨市场异名 id 唯一。
  6. 车型 status 取值限 current / discontinued / concept。
  7. 待核实清单条目编号唯一。

退出码: 0 = 全部通过;1 = 存在错误。

许可: 本仓库整体采用 CC BY-SA 4.0;本脚本额外可按 MIT 使用。
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
MODELS_DIR = os.path.join(DATA_DIR, "models")
LANGS = ("en", "zh-CN", "zh-TW", "ja")
VALID_STATUS = ("current", "discontinued", "concept")

_DIACRITICS = str.maketrans(
    {"ë": "e", "é": "e", "è": "e", "ü": "u", "ç": "c", "ä": "a", "ö": "o", "š": "s", "ß": "ss"}
)


def normalize_id(s):
    """品牌名 → id 前缀:小写、空格转连字符、去变音符(如 Citroën → citroen)。"""
    return s.strip().lower().replace(" ", "-").translate(_DIACRITICS)

errors = []
warnings = []


def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:  # noqa: BLE001
        errors.append(f"JSON 解析失败: {os.path.relpath(path, ROOT)} -> {e}")
        return None


def build_id_sets():
    """收集可引用的 class/body/pt id。"""
    vc = load_json(os.path.join(DATA_DIR, "vehicle_classes.json"))
    refs = set()
    for section in vc.values():
        if isinstance(section, list):
            for item in section:
                if isinstance(item, dict) and item.get("id"):
                    refs.add(item["id"])
    return refs


def main():
    ref_ids = build_id_sets()
    meta = load_json(os.path.join(DATA_DIR, "meta.json"))
    brands = load_json(os.path.join(DATA_DIR, "brands.json"))
    glossary = load_json(os.path.join(DATA_DIR, "glossary.json"))
    pending = load_json(os.path.join(DATA_DIR, "pending_verification.json"))
    cross = load_json(os.path.join(MODELS_DIR, "cross_market.json"))

    if None in (meta, brands, glossary, pending, cross):
        sys.exit(1)

    # 品牌
    brand_ids = set()
    brand_en = {}
    for b in brands:
        if b["id"] in brand_ids:
            errors.append(f"品牌 id 重复: {b['id']}")
        brand_ids.add(b["id"])
        brand_en[b["names"]["en"].lower()] = b["id"]
        missing = [l for l in LANGS if l not in b["names"]]
        if missing:
            errors.append(f"品牌 {b['id']} 缺少语言键: {missing}")

    # 术语
    term_ids = set()
    for t in glossary["terms"]:
        if t["id"] in term_ids:
            errors.append(f"术语 id 重复: {t['id']}")
        term_ids.add(t["id"])
        if t.get("category") not in {c["id"] for c in glossary["categories"]}:
            errors.append(f"术语 {t['id']} 类别无效: {t.get('category')}")

    # 车型
    model_ids = set()
    n_models = 0
    for fname in sorted(os.listdir(MODELS_DIR)):
        if not fname.endswith(".json") or fname == "cross_market.json":
            continue
        data = load_json(os.path.join(MODELS_DIR, fname))
        if data is None:
            continue
        models = data["models"] if isinstance(data, dict) else data
        for m in models:
            n_models += 1
            mid = m.get("id", "")
            if mid in model_ids:
                errors.append(f"车型 id 重复: {mid}")
            model_ids.add(mid)

            if not mid.startswith("model:"):
                errors.append(f"车型 id 格式错误: {mid}")
            for field in ("segment", "body_style", "powertrain"):
                if field not in m:
                    errors.append(f"车型 {mid} 缺少字段 {field}")
                elif m[field] not in ref_ids:
                    errors.append(f"车型 {mid} 引用不存在的 {field}: {m[field]}")
            if "brand" not in m:
                errors.append(f"车型 {mid} 缺少 brand")
            elif m["brand"].lower() not in brand_en:
                warnings.append(f"车型 {mid} 的品牌 {m['brand']} 不在 brands 列表(检查是否需补充品牌)")
            if "names" not in m:
                errors.append(f"车型 {mid} 缺少 names")
            else:
                missing = [l for l in LANGS if l not in m["names"]]
                if missing:
                    errors.append(f"车型 {mid} 缺少语言键: {missing}")
            if "status" in m and m["status"] not in VALID_STATUS:
                errors.append(f"车型 {mid} status 非法: {m['status']}")
            if "years" in m and not re.match(
                r"^(\d{4}\s*[-–—~]\s*(\d{4}|present|至今|現行)(\s*[,;]\s*\d{4}\s*[-–—~]\s*(\d{4}|present|至今|現行))*|\d{4}|—)$",
                str(m["years"]).strip(),
            ):
                warnings.append(f"车型 {mid} years 格式待规范: {m['years']}")
            # id 需与 brand 一致(小写英文名,忽略大小写与变音符,如 Citroën→citroen)
            expected_prefix = "model:" + normalize_id(m.get("brand", "")) + ":"
            if mid.startswith("model:") and not mid.startswith(expected_prefix):
                warnings.append(f"车型 {mid} 的 id 前缀与 brand 不一致(期望 {expected_prefix}*)")

    # 跨市场异名
    alias_ids = set()
    for a in cross:
        if a["id"] in alias_ids:
            errors.append(f"异名 id 重复: {a['id']}")
        alias_ids.add(a["id"])

    # 待核实
    pv_ids = set()
    for p in pending:
        if p["id"] in pv_ids:
            errors.append(f"待核实 id 重复: {p['id']}")
        pv_ids.add(p["id"])

    print(f"检查完成: 品牌 {len(brands)} · 车型 {n_models} · 术语 {len(glossary['terms'])} · 异名 {len(cross)}")
    for w in warnings:
        print("WARN:", w)
    for e in errors:
        print("ERROR:", e)
    if errors:
        print("校验未通过。")
        sys.exit(1)
    if warnings:
        print("校验通过(含警告)。")
    else:
        print("校验全部通过。")
    sys.exit(0)


if __name__ == "__main__":
    main()
