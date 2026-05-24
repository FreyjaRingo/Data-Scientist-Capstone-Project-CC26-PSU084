from __future__ import annotations

import json
import re
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATASET_PATH = PROJECT_ROOT / "final_datasets" / "train_ready_dataset.csv"
SUMMARY_PATH = PROJECT_ROOT / "final_datasets" / "feature_enrichment_summary.csv"
METADATA_PATH = PROJECT_ROOT / "final_datasets" / "feature_enrichment_metadata.json"

ADDED_COLUMNS = [
    "food_category",
    "food_category_source",
    "base_ingredient",
    "base_ingredient_tags",
    "suitable_breakfast",
    "suitable_lunch",
    "suitable_dinner",
    "meal_time_tags",
    "primary_meal_time",
    "feature_rule_version",
]


def normalize_text(value: object) -> str:
    if pd.isna(value):
        return ""
    text = str(value).lower()
    text = re.sub(r"[^a-z0-9\s-]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def has_any(text: str, keywords: list[str]) -> bool:
    padded = f" {text} "
    return any(re.search(r"(?<![a-z0-9])" + re.escape(keyword) + r"(?![a-z0-9])", padded) for keyword in keywords)


CATEGORY_RULES: list[tuple[str, list[str]]] = [
    ("minuman", ["air", "teh", "kopi", "susu", "jus", "sirup", "es ", "cendol", "dawet", "minuman", "wedang"]),
    ("berkuah", ["kuah", "sop", "sup", "soto", "rawon", "gulai", "lodeh", "opor", "laksa", "bakso", "kaldu", "kari", "semur"]),
    ("gorengan", ["goreng", "bakwan", "perkedel", "rempeyek", "peyek", "kerupuk", "keripik", "emping"]),
    ("sayuran", ["sayur", "bayam", "kangkung", "sawi", "kol", "kubis", "wortel", "buncis", "brokoli", "tauge", "taoge", "daun", "labu", "terong", "terung", "tomat", "timun", "mentimun", "selada", "andewi", "kacang panjang"]),
    ("buah", ["apel", "pisang", "alpukat", "anggur", "jeruk", "mangga", "pepaya", "nanas", "semangka", "melon", "jambu", "durian", "rambutan", "salak", "sirsak", "belimbing", "nangka", "kelapa", "markisa", "stroberi"]),
    ("karbohidrat_pokok", ["nasi", "beras", "ketan", "lontong", "ketupat", "bubur", "mie", "mi ", "bihun", "kwetiau", "roti", "jagung", "singkong", "ubi", "kentang", "talas", "sagu", "tepung"]),
    ("lauk_hewani", ["ayam", "sapi", "daging", "kambing", "kerbau", "ikan", "udang", "cumi", "kepiting", "kerang", "telur", "bebek", "itik", "angsa", "hati", "paru", "limpa", "usus", "abon", "bakso"]),
    ("lauk_nabati", ["tahu", "tempe", "oncom", "kedelai", "kacang hijau", "kacang merah", "kacang tanah", "kacang kedelai"]),
    ("bumbu_sambal", ["sambal", "cabai", "cabe", "kecap", "saus", "terasi", "bumbu", "andaliman", "lada", "merica", "garam"]),
    ("snack_dessert", ["kue", "bolu", "biskuit", "cookies", "wafer", "dodol", "puding", "agar-agar", "permen", "coklat", "cokelat", "manisan", "selai"]),
]


BASE_INGREDIENT_RULES: list[tuple[str, list[str]]] = [
    ("telur", ["telur"]),
    ("ayam", ["ayam"]),
    ("sapi", ["sapi", "daging sapi", "abon"]),
    ("daging_lain", ["babi", "kerbau"]),
    ("ikan", ["ikan", "haruan", "haruwan", "bandeng", "lele", "tongkol", "tuna", "salmon", "teri", "kembung", "gabus", "patin", "nila", "gurame", "gurami", "mujair", "kakap"]),
    ("seafood", ["udang", "cumi", "kepiting", "kerang", "lobster", "rajungan"]),
    ("kedelai", ["kedelai", "tahu", "tempe", "oncom", "ampas tahu"]),
    ("kacang", ["kacang", "almond", "mete", "kenari"]),
    ("beras", ["beras", "nasi", "ketan", "lontong", "ketupat", "bubur"]),
    ("jagung", ["jagung"]),
    ("umbi", ["singkong", "ubi", "kentang", "talas", "sagu", "ganyong", "sukun"]),
    ("gandum", ["gandum", "terigu", "roti", "mie", "mi ", "bihun", "kwetiau", "tepung"]),
    ("susu", ["susu", "keju", "yogurt", "yoghurt", "mentega"]),
    ("sayuran", ["sayur", "bayam", "kangkung", "sawi", "kol", "wortel", "buncis", "brokoli", "daun", "labu", "terong", "terung", "tomat", "timun", "selada"]),
    ("buah", ["apel", "pisang", "alpukat", "anggur", "jeruk", "mangga", "pepaya", "nanas", "semangka", "melon", "jambu", "durian", "rambutan", "salak", "sirsak", "belimbing", "nangka", "kelapa"]),
    ("kambing", ["kambing"]),
    ("unggas_lain", ["bebek", "itik", "angsa"]),
    ("bumbu_rempah", ["sambal", "cabai", "cabe", "kecap", "saus", "terasi", "bumbu", "andaliman", "lada", "merica"]),
]


def infer_food_category(name: str) -> tuple[str, str]:
    for category, keywords in CATEGORY_RULES:
        if has_any(name, keywords):
            return category, "keyword"
    return "lainnya", "fallback"


def infer_base_ingredient(name: str) -> tuple[str, str]:
    matches = [ingredient for ingredient, keywords in BASE_INGREDIENT_RULES if has_any(name, keywords)]
    if matches:
        return matches[0], "|".join(matches)
    return "unknown", ""


def infer_meal_time(row: pd.Series) -> tuple[bool, bool, bool, str, str]:
    name = row["food_name_clean"]
    category = row["food_category"]
    calories = float(row.get("calories_100g", 0) or 0)
    fat = float(row.get("fat_100g", 0) or 0)

    breakfast = False
    lunch = False
    dinner = False

    if category in {"buah", "minuman", "snack_dessert"} and calories <= 450:
        breakfast = True
    if has_any(name, ["bubur", "roti", "telur", "susu", "pisang", "apel", "oat"]):
        breakfast = True
    if category == "karbohidrat_pokok" and calories <= 450:
        breakfast = True

    if category in {"karbohidrat_pokok", "lauk_hewani", "lauk_nabati", "sayuran", "berkuah", "gorengan"}:
        lunch = True
    if 120 <= calories <= 750:
        lunch = True

    if category in {"berkuah", "sayuran", "lauk_hewani", "lauk_nabati"} and calories <= 650:
        dinner = True
    if category == "karbohidrat_pokok" and calories <= 400 and fat <= 20:
        dinner = True

    if not (breakfast or lunch or dinner):
        lunch = True

    tags = []
    if breakfast:
        tags.append("breakfast")
    if lunch:
        tags.append("lunch")
    if dinner:
        tags.append("dinner")

    if breakfast and category in {"buah", "minuman", "snack_dessert"}:
        primary = "breakfast"
    elif breakfast and has_any(name, ["bubur", "roti", "telur", "susu", "oat"]):
        primary = "breakfast"
    elif dinner and category in {"berkuah", "sayuran"}:
        primary = "dinner"
    elif lunch:
        primary = "lunch"
    elif dinner:
        primary = "dinner"
    else:
        primary = "breakfast"

    return breakfast, lunch, dinner, "|".join(tags), primary


def enrich_dataset(path: Path = DATASET_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    stale_columns = [
        col
        for col in df.columns
        if col in ADDED_COLUMNS or any(col.startswith(f"{added_col}.") for added_col in ADDED_COLUMNS)
    ]
    df = df.drop(columns=stale_columns)
    df["food_name_clean"] = df["food_name_clean"].fillna(df["food_name"].map(normalize_text))

    category_results = df["food_name_clean"].map(infer_food_category)
    df["food_category"] = category_results.map(lambda item: item[0])
    df["food_category_source"] = category_results.map(lambda item: item[1])

    base_results = df["food_name_clean"].map(infer_base_ingredient)
    df["base_ingredient"] = base_results.map(lambda item: item[0])
    df["base_ingredient_tags"] = base_results.map(lambda item: item[1])

    meal_results = df.apply(infer_meal_time, axis=1, result_type="expand")
    meal_results.columns = [
        "suitable_breakfast",
        "suitable_lunch",
        "suitable_dinner",
        "meal_time_tags",
        "primary_meal_time",
    ]
    df = pd.concat([df, meal_results], axis=1)
    df["feature_rule_version"] = "food_context_rules_v1"

    df.to_csv(path, index=False)
    return df


def write_summary(df: pd.DataFrame) -> None:
    rows = []
    for column in ["food_category", "base_ingredient", "primary_meal_time"]:
        counts = df[column].value_counts(dropna=False)
        for value, count in counts.items():
            rows.append({"feature": column, "value": value, "count": int(count)})
    for column in ["suitable_breakfast", "suitable_lunch", "suitable_dinner"]:
        rows.append({"feature": column, "value": "true", "count": int(df[column].sum())})
    pd.DataFrame(rows).to_csv(SUMMARY_PATH, index=False)

    metadata = {
        "rule_version": "food_context_rules_v1",
        "dataset_path": str(DATASET_PATH),
        "rows": int(len(df)),
        "added_columns": ADDED_COLUMNS,
        "notes": [
            "Features are rule-based and intended to improve recommendation diversity.",
            "Meal time is represented as both multilabel booleans and a primary class.",
            "contains_unknown should still be used as an allergy safety guardrail.",
        ],
    }
    METADATA_PATH.write_text(json.dumps(metadata, indent=2), encoding="utf-8")


if __name__ == "__main__":
    enriched = enrich_dataset()
    write_summary(enriched)
    print(f"Updated: {DATASET_PATH}")
    print(f"Rows: {len(enriched)}")
    print(f"Summary: {SUMMARY_PATH}")
    print(f"Metadata: {METADATA_PATH}")
