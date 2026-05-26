# Orang B - Alergen, Merge, dan Enrichment Dataset

Folder ini berisi pekerjaan Data Science bagian Orang B, yaitu preprocessing alergen, ingredient mapping, merge dengan output Orang A, dan enrichment dataset agar rekomendasi makanan lebih bervariasi.

## Struktur

```text
orang_b/
  raw_datasets/
    Dataset/
      archive/
      archive (1)/
      archive (2)/
      archive (3)/
  dataset_sources/
  docs/
  notebooks/
  scripts_python/
  final_datasets/
  outputs/
```

## Alur Kerja

1. Membersihkan dataset alergen dan ingredient.
2. Membuat label multi-label alergen.
3. Menggabungkan label alergen dengan food master dari Orang A.
4. Menambahkan fitur konteks makanan dari nama makanan dan dataset resep tambahan.
5. Menghasilkan dataset final siap pakai untuk AI Engineer dan Fullstack.

## Dataset Tambahan yang Dipakai

Dataset baru berada di:

```text
raw_datasets/Dataset/archive/Indonesian_Food_Recipes.csv
raw_datasets/Dataset/archive (1)/dataset-*.csv
raw_datasets/Dataset/archive (2)/nutrition.csv
raw_datasets/Dataset/archive (3)/1_Recipe_csv.csv
```

Dataset tersebut dipakai untuk memperkuat:

- `food_category`
- `base_ingredient`
- `suitable_breakfast`
- `suitable_lunch`
- `suitable_dinner`
- `primary_meal_time`
- `recipe_reference_match`
- `recipe_reference_source`

## Output Final

```text
final_datasets/train_ready_dataset.csv
final_datasets/user_profile_features_schema.csv
final_datasets/feature_enrichment_summary.csv
final_datasets/feature_enrichment_metadata.json
```

## Script Penting

```text
scripts_python/orang_b_allergen_pipeline.py
scripts_python/merge_orang_a_b.py
scripts_python/enrich_ready_dataset_features.py
```

Untuk menjalankan ulang enrichment fitur konteks:

```bash
python scripts_python/enrich_ready_dataset_features.py
```

## Catatan

Raw dataset tidak perlu dipush ke GitHub karena ukurannya besar. Yang perlu dibagikan ke AI/Fullstack adalah isi `final_datasets/`.
