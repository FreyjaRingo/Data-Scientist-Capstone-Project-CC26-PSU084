# Raw Dataset Sources

Dokumen ini menggantikan penyimpanan dataset mentah di repository. Dataset mentah perlu diunduh dari sumber berikut jika ingin menjalankan ulang pipeline dari awal.

## Dataset Utama Project

| Nama dataset | File lokal yang dipakai | Sumber | Fungsi |
|---|---|---|---|
| Indonesian Food & Drink Nutrition Dataset | `nutrition.csv` | https://www.kaggle.com/datasets/anasfikrihanif/indonesian-food-and-drink-nutrition-dataset | Master makanan Indonesia dan kandungan kalori/makro. |
| Food Ingredients and Allergens | `food_ingredients_and_allergens.csv` | https://www.kaggle.com/datasets/uom190346a/food-ingredients-and-allergens | Mapping produk/bahan makanan ke daftar alergen. |
| Food Allergens and Allergies | `FoodData.csv` | https://www.kaggle.com/datasets/boltcutters/food-allergens-and-allergies | Taksonomi makanan dan kategori alergi. |
| Comprehensive Weight Change Prediction | `weight_change_dataset.csv` | https://www.kaggle.com/datasets/abdullah0a/comprehensive-weight-change-prediction | Validasi formula BMR/TDEE dan fitur profil pengguna. |

## Dataset Tambahan Awal

| Nama dataset | File lokal yang dipakai | Sumber | Fungsi |
|---|---|---|---|
| Open Food Facts data export | `en.openfoodfacts.org.products.csv` | https://world.openfoodfacts.org/data | Ingredient text, allergen tag, traces, dan nutrisi produk nyata. |
| USDA FoodData Central Foundation Foods | Folder `FoodData_Central_foundation_food_csv_2026-04-30/` | https://fdc.nal.usda.gov/download-datasets/ | Referensi nutrisi resmi untuk enrichment dan validasi. |
| Ingredients with 17 Allergen Tags | `allergies_10k.csv` | https://www.kaggle.com/datasets/khochawongwat/ingredients-with-17-allergen-tags | Dataset ingredient text dengan tag alergen untuk training klasifikasi teks. |
| Global Food & Nutrition Database 2026 | `foods_allergens.csv`, `foods_dietary_restrictions.csv`, `foods_health_scores_allergens.csv`, `healthy_foods_database.csv`, `comprehensive_foods_usda.csv` | https://www.kaggle.com/datasets/ahsanneural/global-food-and-nutrition-database-2026 | Enrichment boolean alergen, nutrisi, kategori makanan, dan health score. |

## Dataset Tambahan Baru untuk Enrichment Konteks

| Nama dataset | File lokal yang dipakai | Sumber | Fungsi |
|---|---|---|---|
| Indonesian Food Recipes Dataset | `archive/Indonesian_Food_Recipes.csv` | https://www.kaggle.com/datasets/albertnathaniel12/food-recipes-dataset | Memperkuat kategori makanan dan bahan dasar dari title dan ingredients resep Indonesia. |
| Indonesian Food Recipes by Main Ingredient | `archive (1)/dataset-*.csv` | https://baselight.app/u/kaggle/dataset/canggih_indonesian_food_recipes | Memperkuat bahan dasar seperti ayam, ikan, sapi, kambing, tahu, telur, tempe, dan udang. |
| Global Cuisine Meals with Diet Labels | `archive (2)/nutrition.csv` | https://www.kaggle.com/datasets/himanshikushwaha/global-cuisine-meals-with-diet-labels | Referensi label meal type: breakfast, lunch, dinner. |
| Recipes Dataset 64k Dishes | `archive (3)/1_Recipe_csv.csv` | https://www.kaggle.com/datasets/prashantsingh001/recipes-dataset-64k-dishes | Referensi tambahan category, subcategory, dan ingredients untuk title matching. |

## Struktur Lokal untuk Reproduksi

Jika ingin menjalankan notebook/script dari awal, letakkan file mentah ke folder:

```text
orang_b/raw_datasets/Dataset/
  nutrition.csv
  food_ingredients_and_allergens.csv
  FoodData.csv
  weight_change_dataset.csv
  allergies_10k.csv
  foods_allergens.csv
  foods_dietary_restrictions.csv
  foods_health_scores_allergens.csv
  healthy_foods_database.csv
  comprehensive_foods_usda.csv
  en.openfoodfacts.org.products.csv
  FoodData_Central_foundation_food_csv_2026-04-30/
  archive/
  archive (1)/
  archive (2)/
  archive (3)/
```

## Catatan Lisensi dan Ukuran

- Open Food Facts berukuran sangat besar, sekitar 12 GB setelah diekstrak.
- Dataset mentah tidak direkomendasikan untuk commit Git biasa.
- Jika dataset harus disertakan di remote, gunakan Git LFS atau cloud storage, lalu cantumkan link unduhan di README.
