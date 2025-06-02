# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut adalah sebuah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Selama dua dekade terakhir, institut ini telah menghasilkan lulusan-lulusan berkualitas dan membangun reputasi yang baik di bidang pendidikan. Namun, di balik kesuksesan tersebut, terdapat tantangan besar yang perlu segera ditangani, yaitu tingginya tingkat dropout atau putus studi dari para siswa.

### Permasalahan Bisnis
- Tingginya jumlah siswa yang mengalami dropout.
- Belum adanya sistem prediksi untuk mengidentifikasi siswa yang berisiko tinggi dropout.
- Kurangnya visualisasi dan monitoring performa siswa secara menyeluruh.
  
### Cakupan Proyek
- Membuat dashboard untuk membantu Jaya Jaya Institut memantau performa siswa secara keseluruhan.
- Membangun model machine learning untuk memprediksi apakah seorang siswa berpotensi dropout atau tidak.
- Mengembangkan aplikasi prototype berbasis Streamlit yang memungkinkan pengguna melakukan prediksi dropout secara langsung menggunakan model tersebut.
- Memberikan rekomendasi tindakan berbasis data untuk mengurangi angka dropout.
  
### Persiapan

Sumber data: [student's performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

**Setup environment:**

Buka terminal atau command prompt, arahkan ke folder proyek:
```
cd path/to/project_folder
```
Buat virtual (opsional) 
```
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```
Instalasi dependensi
```
pip install -r requirements.txt
```

## Business Dashboard
Dashboard ini dirancang untuk membantu pihak manajemen Jaya Jaya Institut dalam:
- Memantau jumlah mahasiswa aktif, dropout, dan lulus.
- Mengidentifikasi faktor-faktor penting yang berhubungan dengan dropout rate.
- Mengambil keputusan strategis berdasarkan data performa dan latar belakang mahasiswa.

## Menjalankan Sistem Machine Learning di Lokal
Pastikan telah melakukan **Setup environment** lalu jalankan:
```
streamlit run app.py
```
Link prototype: https://do-app.streamlit.app/

## Conclusion
1. Dropout Rate Tinggi (32%) menjadi perhatian utama.
2. Mahasiswa dengan:
   - Nilai masuk rendah,
   - Usia lebih tua saat mendaftar,
   - Jumlah mata kuliah approved rendah,
   - Berstatus debtor, dan
   - Tidak memiliki beasiswa
   cenderung memiliki kemungkinan lebih tinggi untuk dropout.

### Rekomendasi Action Items
- Buat sistem early warning untuk mahasiswa dengan kombinasi profil: umur tua, nilai rendah, dan status debtor.
- Tingkatkan akses ke beasiswa untuk kelompok mahasiswa dengan potensi tinggi tapi kondisi finansial lemah.
- Terapkan mentoring wajib bagi mahasiswa debtor atau yang nilai ujian masuknya di bawah rata-rata.
