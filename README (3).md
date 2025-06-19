# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus. Untuk itulah Jaya Jaya Institut memerlukan sebuah alat untuk mendeteksi siswa yang berpotensi untuk melakukan dropout berdasarkan beberapa fitur atau demografi yang dimiliki oleh siswa itu sendiri, dengan deteksi yang lebih dini Jaya Jaya Institute mempunyai harapan untuk membantu siswa berubah pikiran.

### Permasalahan Bisnis
Untuk membantu perusahaan mengatasi masalah ini akan dilakukan:
1. Tingginya tingkat droput oleh para siswa, setelah dilakukan identifikasi diketahui bahwa siswa yang dropout sangat tinggi.
2. Mengidentifikasi faktor-faktor yang membuat siswa memiliki potensi dropout
3. Berdasarkan faktor yang telah diketahui, diifentifikasi kembali faktor mana yang menjadi potensi tinggi siswa untuk dropout.

### Cakupan Proyek
1. Memulai dari memahami data
2. Menggunakan analisis korelasi (heatmap) untuk mengetahui faktor-faktor yang mengindikasikan siswa melakukan dropout
3. Menyediakan dashboard untuk membantu Jaya Jaya Institut memahami faktor - faktor siswa melakukan dropout
4. Menyediakan alat untuk melakukan prediksi terhadap siswa yang akan melaksanakan dropout

### Persiapan
Data bersumber dari [dicoding](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md), dataset ini berisi demografi, kondisi gender, nationality, pekerjaan dan pendidikan orangtua, serta fitur lainnya

Setup environment:
Sebelum mengkases file ipnyb diperlukan setup einvornment untuk python

```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

Untuk mengakses file ipynb perlu diperhatikan
1. Memiliki jaringan internet
2. Sebelum menjalankan file ipnyb anda harus sudah memiliki seluruh library yang digunakan
3. Jangan lupa untuk menjalankan semua isi dari file ipnyb

Untuk mengakses Business Dashboard anda bisa melalui tautan berikut: [Business Dashboard](https://public.tableau.com/views/das2_17502973115640/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)


## Business Dashboard
Business Dashboard dapat di lihat menggunakan [link](https://public.tableau.com/views/das2_17502973115640/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link) ini.
Berikut Beberapa hal yang di tampilkan di dalam dashboard
- Jumlah siswa berdasarkan status
- Visualisasi dari beberapa faktor yang mempengaruhi siswa melakukan dropout
- Pada visualisasi ditampilkan perbandingan antara siswa yang droput, graduate dan enroled dalam satu kategori dalam satu fitur

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
streamlit run (nama file.py)
```
Selain menyediakan dashboard pada proyek ini disediakan tools yang berupa alat prediksi untuk mengetahui potensi siswa drop out, untuk mengakses alat itu dapat melalui [link](https://datascience2-j8azzafc9rg5zaprbsooce.streamlit.app/) berikut


## Conclusion
Ditemukan beberapa faktor yang mempengaruhi siswa melakukan dropout, diantaranya adalah Previous_qualification_grade, Admission_grade, Displaced, Tuition_fees_up_to_date, Scholarship_holder, Curricular_units_1st_sem_approved, Curricular_units_1st_sem_grade, Curricular_units_2nd_sem_approved, Curricular_units_2nd_sem_grade, dari sebagian besar siswa yang dropout dari perusahaan ditemukan faktor terbesar adalah dikarenakan Curricular_units_2nd_sem_approved dimana mereka yang tidak mengambil curricular units pada semester 2 (0) berpotensi untuk melakukan dropout


### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- Pihak institusi perlu memberikan edukasi atau pendekatan untuk  siswa mengambil atau menyetujui curricular units pada semester kedua
- Setelah semester selesai hendaknya pihak institusi memberikan pembaljaran yang lebih intens pada siswa yang memiliki grade rendah pada kualifikasi sebelumnya
- Pihak institusi dapat melaksanakan penyelidikan lebih lanjut mengapa pada semester 2 banyak siswa tidak mengambil curricular units
