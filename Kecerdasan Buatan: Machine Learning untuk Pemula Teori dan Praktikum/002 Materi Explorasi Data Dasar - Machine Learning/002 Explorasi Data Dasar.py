# %% [markdown]
# # Menggunakan Pandas untuk Mengenal Data Anda
#
# Langkah pertama dalam proyek pembelajaran mesin apa pun adalah membiasakan diri Anda dengan data. Anda akan menggunakan perpustakaan Pandas untuk ini. Pandas adalah alat utama yang digunakan para ilmuwan data untuk mengeksplorasi dan memanipulasi data. Kebanyakan orang menyingkat panda dalam kodenya menjadi `pd`. Saya melakukan ini dengan perintah

# %% [code] {"jupyter":{"outputs_hidden":true}}
import pandas as pd

# %% [markdown]
# Bagian terpenting dari perpustakaan Pandas adalah DataFrame. DataFrame menampung tipe data yang mungkin Anda anggap sebagai tabel. Ini mirip dengan lembar di Excel, atau tabel di database SQL.
#
# Pandas memiliki metode ampuh untuk sebagian besar hal yang ingin Anda lakukan dengan jenis data ini.
#
# Sebagai contoh, kita akan melihat [data tentang harga rumah](https://www.kaggle.com/dansbecker/melbourne-housing-snapshot) di Melbourne, Australia. Dalam latihan praktis, Anda akan menerapkan proses yang sama pada kumpulan data baru, yang berisi harga rumah di Iowa.
#
# Contoh data (Melbourne) ada di jalur file **`../input/melbourne-housing-snapshot/melb_data.csv`**.
#
# Kami memuat dan menjelajahi data dengan perintah berikut:

# %% [code] {"jupyter":{"outputs_hidden":true}}
# save filepath to variable for easier access
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)
# print a summary of the data in Melbourne data
melbourne_data.describe()

# Hasilnya menunjukkan 8 angka untuk setiap kolom di dataset asli Anda. Angka pertama, **hitungan**, menunjukkan berapa banyak baris yang memiliki nilai yang tidak ada.
#
# Nilai yang hilang muncul karena berbagai alasan. Misalnya, ukuran kamar tidur ke-2 tidak akan dikumpulkan saat mensurvei rumah dengan 1 kamar tidur. Kami akan kembali ke topik data yang hilang.
#
# Nilai kedua adalah **mean**, yaitu rata-rata. Di bawahnya, **std** adalah deviasi standar, yang mengukur seberapa tersebar nilai secara numerik.
#
# Untuk menafsirkan nilai **min**, **25%**, **50%**, **75%** dan **max**, bayangkan mengurutkan setiap kolom dari nilai terendah hingga tertinggi. Nilai pertama (terkecil) adalah min. Jika Anda menelusuri seperempat daftar, Anda akan menemukan angka yang lebih besar dari 25% nilai dan lebih kecil dari 75% nilai. Itu adalah nilai **25%** (diucapkan "persentil ke-25"). Persentil ke-50 dan ke-75 didefinisikan secara analog, dan **maks** adalah angka terbesar.
#
#
# Get started with your **[first coding exercise](https://www.kaggle.com/kernels/fork/1258954)**
# # Your Turn
# %% [markdown]
# ---
#
#
#
#
