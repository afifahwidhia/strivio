# Strivio

## Link Aplikasi
https://afifah-widhia-strivio.pbp.cs.ui.ac.id/

## Step by Step Implementasi
1. Membuat project baru di PWS.
2. Membuat direktori baru di git dan lokal.
4. Membuat project Django baru.
5. Membuat aplikasi `main` dengan `python manage.py startapp main`.
6. Menambahkan aplikasi `main` ke `INSTALLED_APPS` di `settings.py`.
7. Menambahkan routing di `urls.py` agar `main` bisa diakses.
8. Membuat model `Product` dengan atribut `name, price, description, thumbnail, category, is_featured, stock, size`.
9. Membuat fungsi di `views.py` untuk menampilkan nama aplikasi, nama saya, dan kelas saya.
10. Membuat routing di `main/urls.py` untuk fungsi tersebut.
11. Melakukan migrasi database (`makemigrations` dan `migrate`).
12. Melakukan push ke git dan deploy project ke PWS.
13. Membuat `README.md` berisi link aplikasi dan jawaban pertanyaan.

## Bagan Request Client ke Web
Client (Browser)
     │
     ▼
 urls.py  →  views.py  →  models.py
     │          │
     │          └────> proses logika & pengambilan data
     │
     ▼
 Template HTML  <── context (data dari views)
     │
     ▼
  Response (dikirim kembali ke Client)

Penjelasan Komponen
- urls.py
Menyimpan daftar pola URL. Ketika client mengakses http://domain/halaman/, Django mencari kecocokan URL pada urls.py. Jika cocok, URL diarahkan ke fungsi/class pada views.py.
- views.py
Berisi logika aplikasi (controller). Menerima request, memproses data (opsional menggunakan models.py), lalu menyiapkan context untuk dikirim ke template. Memanggil template HTML agar data bisa ditampilkan.
- models.py
Berfungsi sebagai representasi database dalam bentuk class Python. Digunakan views.py untuk query data (misalnya ambil semua pengguna).
- Template HTML
Berisi tampilan interface untuk user. Menggunakan Django Template Language (DTL) agar bisa menampilkan data ({{ variable }}) yang dikirim dari views.py.
- Response ke Client
Setelah template di-render, hasil akhirnya adalah HTML murni yang dikirim balik ke browser user.

## Peran settings.py
settings.py merupakan pusat konfigurasi Django project. Berisi pengaturan penting seperti:
- Database (engine, nama DB, user, password).
- Installed apps (daftar aplikasi Django yang aktif).
- Middleware (pengatur request/response).
- Template settings.
- Static files & media files.
- Konfigurasi keamanan (DEBUG, ALLOWED_HOSTS).
Bisa dibilang, tanpa settings.py Django tidak tahu bagaimana project dijalankan.

## Cara Kerja Migrasi di Django
Migrasi database di Django bekerja dengan cara mendefinisikan atau mengubah struktur tabel melalui models.py sebagai blueprint database, lalu dijalankan perintah python manage.py makemigrations untuk membuat file migrasi yang merekam perubahan model, dan python manage.py migrate untuk mengeksekusi perubahan tersebut pada database nyata. Proses ini dipantau melalui tabel khusus bernama django_migrations sehingga Django tahu migrasi mana saja yang sudah atau belum diterapkan.

## Framework Django untuk Pemula
Django cocok dijadikan framework awal karena memiliki konsep batteries included dengan banyak fitur bawaan seperti ORM, admin panel, dan autentikasi sehingga pemula bisa langsung fokus pada logika aplikasi tanpa repot melakukan konfigurasi dasar, menggunakan arsitektur MVT yang memudahkan pemahaman alur request–response, didukung dokumentasi resmi yang lengkap dan rapi, menerapkan best practices sehingga pengguna Django dapat terbiasa dengan pola kode yang bersih, terstruktur, dan aman.

## Feedback Tutorial 1
Menurut saya, asisten dosen pada tutorial 1 sudah menjelaskan materi dengan cukup runtut dan membantu mahasiswa memahami alur kerja Django dari awal hingga praktik langsung. Penyampaian yang sistematis memudahkan mengikuti setiap langkah, mulai dari struktur proyek, peran file utama, hingga proses migrasi database.