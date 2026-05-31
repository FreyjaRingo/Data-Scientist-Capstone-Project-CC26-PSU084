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
5. Memfilter item agar rekomendasi berisi makanan/menu yang layak dimakan, bukan bahan mentah.
6. Menambahkan status halal berbasis rule dari nama makanan dan ingredient text.
7. Menghasilkan dataset final siap pakai untuk AI Engineer dan Fullstack.

## Dataset Tambahan yang Dipakai

Dataset baru berada di:

```text
raw_datasets/Dataset/archive/Indonesian_Food_Recipes.csv
raw_datasets/Dataset/archive (1)/dataset-*.csv
raw_datasets/Dataset/archive (2)/nutrition.csv
raw_datasets/Dataset/archive (3)/1_Recipe_csv.csv
../new datasets/extracted/archive (1)/Multi_Cuisine_Recipe_Dataset.csv
../new datasets/extracted/archive (2)/recipes_master.csv
../new datasets/extracted/archive (2)/recipe_ingredients.csv
../new datasets/extracted/archive (4)/NutritionalFacts_Fruit_Vegetables_Seafood.csv
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
- `menu_reference_match`
- `recommendation_item_type`
- `is_recommendable_food`
- `halal_status`
- `is_halal_candidate`
- `contains_non_halal_ingredient`

## Output Final

```text
final_datasets/train_ready_dataset.csv
final_datasets/train_ready_dataset_full_audit.csv
final_datasets/user_profile_features_schema.csv
final_datasets/feature_enrichment_summary.csv
final_datasets/feature_enrichment_metadata.json
final_datasets/menu_ready_filter_summary.csv
final_datasets/menu_ready_filter_metadata.json
```

`train_ready_dataset.csv` adalah file utama untuk training/rekomendasi. File ini sudah difilter agar berisi menu/makanan siap rekomendasi, buah, sayur, snack, minuman, dan staple yang layak dimakan. Bahan mentah, bumbu, kondimen, tepung, beras mentah, serta protein hewani mentah dipindahkan ke `train_ready_dataset_full_audit.csv` dengan flag dan alasan eksklusi.

Kolom halal yang dipakai:

- `halal_status`: `halal_candidate`, `non_halal`, atau `needs_review`.
- `is_halal_candidate`: aman untuk mode halal-only jika bernilai `True`.
- `contains_non_halal_ingredient`: `True` untuk keyword eksplisit seperti babi, anjing, atau alkohol.
- `non_halal_ingredient_tags`: alasan keyword eksplisit, misalnya `pork`, `dog`, atau `alcohol`.
- `halal_review_reason`: item yang perlu review manual, misalnya hewan sensitif/eksotik seperti penyu, paniki, katak, keong, atau kura-kura.

Catatan: `halal_candidate` bukan sertifikasi halal resmi, melainkan hasil rule-based filtering agar AI Engineer punya guardrail rekomendasi.

## Script Penting

```text
scripts_python/orang_b_allergen_pipeline.py
scripts_python/merge_orang_a_b.py
scripts_python/enrich_ready_dataset_features.py
scripts_python/build_menu_ready_train_dataset.py
```

Untuk menjalankan ulang enrichment fitur konteks:

```bash
python scripts_python/enrich_ready_dataset_features.py
```

Untuk menjalankan ulang filter real-food/menu-ready:

```bash
python scripts_python/build_menu_ready_train_dataset.py
```

## Catatan

Raw dataset tidak perlu dipush ke GitHub karena ukurannya besar. Folder `new datasets/` juga hanya disimpan lokal dan digunakan sebagai referensi menu/nutrisi tambahan. Yang perlu dibagikan ke AI/Fullstack adalah isi `final_datasets/`.
