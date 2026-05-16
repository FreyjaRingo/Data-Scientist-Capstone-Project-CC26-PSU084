# Final Package - NutriMatch Data Science

Folder ini adalah paket akhir Data Science NutriMatch yang ringan untuk GitHub. Dataset mentah tidak disimpan sebagai file di sini; sumbernya dicatat sebagai link agar repository tidak berat.

## Struktur Folder

```text
final/
├── dataset_sources/
│   └── raw_dataset_links.md
├── docs/
│   ├── contribution_matrix.md
│   ├── report_ready_summary.md
│   ├── data_science_plan_nutrimatch.md
│   ├── Project Plan - CC26-PSU084 (2).pdf
│   └── todolist.txt
├── final_datasets/
│   ├── train_ready_dataset.csv
│   ├── user_profile_features_schema.csv
│   ├── food_master_standardized.csv
│   ├── merge_summary.csv
│   ├── merge_metadata.json
│   └── README_merge_orang_a_b.md
├── notebooks/
│   ├── orang_a/
│   └── orang_b_and_merge/
├── scripts_python/
├── MANIFEST.csv
└── README.md
```

## Pembagian Kerja

Ringkasan siapa mengerjakan apa ada di:

```text
final/docs/contribution_matrix.md
```

## Dataset Mentah

Link sumber dataset mentah ada di:

```text
final/dataset_sources/raw_dataset_links.md
```

Dataset mentah sengaja tidak disimpan di folder `final` agar aman untuk push ke GitHub. Jika reviewer ingin reproduksi pipeline, unduh dataset dari link tersebut dan letakkan sesuai path yang dijelaskan di dokumen sumber dataset.

## Dataset Final

Dataset utama untuk AI Engineer:

```text
final/final_datasets/train_ready_dataset.csv
```

Schema fitur profil user:

```text
final/final_datasets/user_profile_features_schema.csv
```

## Notebook dan Script

- Notebook Orang A: `final/notebooks/orang_a/`
- Notebook Orang B dan merge: `final/notebooks/orang_b_and_merge/`
- Script pipeline: `final/scripts_python/`

## Catatan Keamanan Alergi

Untuk kasus alergi, data yang tidak punya bukti cukup tidak dianggap aman. Baris yang tidak berhasil dipetakan diberi `contains_unknown=True` pada mode conservative agar sistem rekomendasi dapat memfilternya sebelum makanan ditampilkan ke pengguna.
