Customer Churn Dashboard – Streamlit App

Project ini merupakan dashboard interaktif untuk menganalisis pola customer churn menggunakan data bank customer. Dashboard dibuat dengan Streamlit agar hasil analisis lebih mudah dipahami oleh stakeholder non-teknis dan dapat digunakan sebagai alat bantu pengambilan keputusan bisnis.

================================================
Tujuan Project
================================================
Dashboard ini bertujuan untuk:
- Memahami distribusi customer churn
- Mengidentifikasi segmen pelanggan yang berisiko churn
- Membantu tim bisnis menentukan strategi retensi yang lebih tepat sasaran
- Menyajikan insight data secara interaktif, bukan hanya dalam bentuk notebook

================================================
Dataset
================================================
Dataset yang digunakan:
Bank Customer Churn Dataset

File:
- bank_churn_data.csv

Beberapa kolom utama:
- customer_age
- gender
- education_level
- income_category
- months_on_book
- months_inactive_12_mon
- total_trans_ct
- attrition_flag (label churn)

Kolom churn dibuat dari attrition_flag:
- Attrited Customer → churn = 1
- Existing Customer → churn = 0

================================================
Fitur Dashboard
================================================
Dashboard menyediakan beberapa fitur utama:

1. Filter Interaktif (Sidebar)
   - Filter berdasarkan gender
   - Filter rentang usia customer

2. Key Metrics (KPI)
   - Total Customers
   - Churn Rate (%)
   - Average Age

3. Visualisasi Data
   - Distribusi churn (Churn vs Not Churn)
   - Perbandingan churn berdasarkan gender
   - Visualisasi berubah secara real-time saat filter digeser

4. Data Preview
   - Menampilkan sebagian data hasil filter untuk validasi cepat

================================================
Tools & Library
================================================
- Python
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn (untuk preprocessing ringan)

================================================
Cara Menjalankan Aplikasi (Local)
================================================
1. Pastikan Python sudah terinstall
2. Install dependency:
   pip install -r requirements.txt
3. Jalankan aplikasi:
   streamlit run app.py
4. Dashboard akan terbuka otomatis di browser

================================================
Catatan
================================================
Project ini dibuat sebagai bagian dari portfolio Data Science / Data Analyst untuk menunjukkan pemahaman:
- Data understanding
- Exploratory analysis
- Penyajian insight dalam bentuk dashboard interaktif
- Pembelajaran dalam pembuatan Portofolio menggunakan Streamlit

note : Dashboard ini bersifat eksploratif dan dapat dikembangkan lebih lanjut dengan model prediksi churn pada tahap berikutnya.