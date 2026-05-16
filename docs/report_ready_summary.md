# Report Ready Summary - Data Preparation NutriMatch

## 1. Tujuan Data Preparation

Tahap Data Science bertujuan menyiapkan dataset makanan, nutrisi, profil pengguna, dan label alergen agar siap digunakan oleh AI Engineer untuk membangun sistem rekomendasi makanan yang dipersonalisasi dan ramah alergi.

Fokus utama tahap ini adalah:

- membersihkan data nutrisi makanan,
- membuat fitur profil pengguna seperti BMR/TDEE dan target makro,
- membuat label alergen multi-label,
- menggabungkan data nutrisi dan alergen menjadi dataset final,
- mendokumentasikan sumber data, asumsi, dan risiko.

## 2. Dataset yang Digunakan

Dataset mentah berasal dari beberapa sumber: Indonesian Food & Drink Nutrition, Food Ingredients and Allergens, Food Allergens and Allergies, Comprehensive Weight Change Prediction, Open Food Facts, USDA FoodData Central, Ingredients with Allergen Tags, dan Global Food & Nutrition Database 2026.

Link lengkap dataset tersedia di:

```text
final/dataset_sources/raw_dataset_links.md
```

Dataset mentah tidak disimpan di folder final agar repository GitHub tetap ringan.

## 3. Metode Cleaning dan Feature Engineering

### Nutrisi dan Profil Pengguna

Orang A membersihkan data makanan, menstandarkan kolom nutrisi per 100 gram, membuat `food_id`, serta menambahkan flag kualitas seperti `zero_calorie_flag`, `calorie_inconsistent_flag`, dan `calorie_macro_diff`.

Untuk profil pengguna, Orang A membuat fitur:

- `age`
- `gender`
- `height_cm`
- `weight_kg`
- `activity_level`
- `goal`
- `bmr`
- `tdee`
- `target_calorie`
- `protein_target_g`
- `fat_target_g`
- `carb_target_g`
- `allergy_vector`

### Alergen dan Ingredient Mapping

Orang B membersihkan dataset alergen, menghapus duplikat, menstandarkan nama alergen, dan membuat label multi-label:

- `contains_gluten`
- `contains_dairy`
- `contains_nuts`
- `contains_peanut`
- `contains_seafood`
- `contains_egg`
- `contains_soy`
- `contains_celery`
- `contains_mustard`
- `contains_sesame`
- `contains_sulfite`
- `contains_other`
- `contains_unknown`

Setiap label diberi `confidence`:

- `high`: berasal dari tag/label eksplisit.
- `medium`: berasal dari keyword ingredient/product text.
- `low`: berasal dari sinyal lemah atau keyword fallback.
- `unknown`: tidak ada bukti cukup.

## 4. Hasil Merge Final

Dataset final:

```text
final/final_datasets/train_ready_dataset.csv
```

Ringkasan merge:

```text
food_master_rows      : 1332
train_ready_rows      : 1332
exact_name_rows       : 258
keyword_fallback_rows : 3
not_matched_rows      : 1071
conservative_unknown  : True
```

Interpretasi:

- `exact_name`: nama makanan cocok langsung dengan label alergen.
- `keyword_fallback`: tidak cocok langsung, tetapi terdeteksi dari keyword alergen.
- `not_matched`: tidak ada bukti alergen yang cukup, sehingga diberi `contains_unknown=True` pada mode conservative.

## 5. Prinsip Keamanan Alergi

Dalam konteks alergi, false negative lebih berbahaya daripada false positive. Karena itu, data kosong atau tidak terpetakan tidak dianggap aman. Baris dengan `contains_unknown=True` harus difilter atau diperiksa manual jika pengguna memiliki alergi kritis.

Sistem rekomendasi disarankan memakai dua lapisan:

- model AI untuk ranking/rekomendasi,
- rule-based guardrail untuk memastikan makanan berisiko alergen tidak lolos.

## 6. Output untuk AI Engineer

| File | Fungsi |
|---|---|
| `train_ready_dataset.csv` | Dataset makanan final berisi nutrisi, label alergen, confidence, dan status merge. |
| `user_profile_features_schema.csv` | Fitur profil user untuk perhitungan kebutuhan kalori dan target makro. |
| `merge_summary.csv` | Audit hasil penggabungan data Orang A dan Orang B. |
| `merge_metadata.json` | Metadata input dan output merge. |

## 7. Risiko dan Batasan

- Banyak makanan Indonesia tidak memiliki daftar ingredient eksplisit.
- Open Food Facts bersifat crowdsourced sehingga kualitas label perlu divalidasi.
- Sebagian besar makanan lokal masih `not_matched`, sehingga perlu manual review lanjutan untuk meningkatkan coverage alergen.
- Dataset final aman sebagai baseline training dan guardrail awal, tetapi belum cukup untuk klaim medis.
