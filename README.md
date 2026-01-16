# Galunggung Green Glory Dashboard

Dashboard interaktif untuk analisis penjualan kopi Galunggung Green Glory menggunakan teknologi Big Data dan Machine Learning.

## Deskripsi

Dashboard ini dibuat sebagai bagian dari proyek analisis big data untuk Galunggung Green Glory, sebuah bisnis kopi lokal. Aplikasi ini menyajikan berbagai analisis termasuk trend penjualan, preferensi pelanggan, dan proyeksi finansial berdasarkan data transaksi 951 entri dari 6 jenis kopi yang berbeda.

## Fitur Utama

- **Analisis Trend Penjualan**: Menggunakan Linear Regression untuk mengidentifikasi produk-produk yang sedang naik daun (rising stars) vs produk-produk yang menurun (declining products)
- **Analisis Preferensi Pelanggan**: Menggunakan Logistic Regression untuk memahami preferensi pelanggan berdasarkan demografi
- **Visualisasi Interaktif**: Grafik interaktif menggunakan Plotly untuk memahami data dengan lebih baik
- **Proyeksi Finansial**: Proyeksi pendapatan berdasarkan data historis dengan target pertumbuhan 20% dalam 6 bulan

## Teknologi yang Digunakan

- **Streamlit**: Framework untuk membuat dashboard interaktif
- **Apache PySpark**: Processing data besar dengan efisiensi komputasi paralel
- **Scikit-learn**: Model machine learning (Linear Regression & Logistic Regression)
- **Plotly**: Visualisasi interaktif
- **Pandas**: Processing data
- **Matplotlib**: Visualisasi statis

## Instalasi

1. Clone repository ini:
```bash
git clone <url-repository-ini>
```

2. Install dependensi:
```bash
pip install -r requirements.txt
```

3. Jalankan aplikasi:
```bash
streamlit run app.py
```

## Struktur Proyek

- `app.py`: File utama aplikasi Streamlit
- `requirements.txt`: Daftar dependensi yang diperlukan
- `constants.py`: Konstanta-konstanta yang digunakan dalam aplikasi
- `utils.py`: Fungsi-fungsi utilitas
- `Transaksi Penjualan 2025.csv`: Data transaksi penjualan
- `trend_analysis_results.csv`: Hasil analisis trend
- `preference_analysis_results.csv`: Hasil analisis preferensi pelanggan

## Data yang Digunakan

Dataset berisi 951 transaksi dari 6 jenis kopi Galunggung Green Glory:
- Java Halu
- Bunar
- Parentas
- Taraju
- Gunung Puntang
- Regional

## Tujuan Bisnis

- Meningkatkan value penjualan secara signifikan dan berkelanjutan dalam 6 bulan ke depan
- Menganalisis apakah perlu menambahkan produk kopi baru atau fokus pada optimasi portfolio saat ini
- Memberikan insight berbasis data untuk mendukung pengambilan keputusan strategis

## Target Kinerja

- **Revenue Growth**: Rp 176.5M → Rp 212M/bulan (+20%)
- **ROI Year 1**: 48%
- **Payback Period**: 2.1 tahun
- **Market Share**: +5% (target 35%)

## Kontribusi

Silakan fork repository ini dan kirimkan pull request untuk kontribusi Anda.