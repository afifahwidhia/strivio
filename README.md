# Strivio

## Link Aplikasi
https://afifah-widhia-strivio.pbp.cs.ui.ac.id/

## Tugas Individu 1
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
 urls.py  →  views.py  ←→  models.py
     │          
     │          
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

## Tugas Indisidu 2
## Step by Step Implementasi
1. **Membuat Model**  
   Pertama, saya membuat model bernama **`Product`** di file `models.py` untuk merepresentasikan data produk yang akan digunakan.  

2. **Menjalankan Migrasi**  
   Setelah model selesai dibuat, saya menjalankan perintah **`python manage.py makemigrations`** diikuti dengan **`python manage.py migrate`** agar perubahan pada model tersimpan ke dalam basis data.  

3. **Membuat Form**  
   Selanjutnya, saya membuat **form** bernama `ProductForm` di file `forms.py` untuk memudahkan proses input data produk melalui antarmuka pengguna.  

4. **Menambahkan Views**  
   Saya kemudian menambahkan beberapa **view** di file `views.py`, yaitu `show_main`, `create_product`, `show_product`, `show_json`, `show_xml`, `show_json_by_id`, dan `show_xml_by_id`. View-view ini bertugas menampilkan halaman utama, membuat produk baru, menampilkan detail produk, serta menyajikan data dalam format JSON dan XML.  

5. **Mengonfigurasi URL Routing**  
   Setelah view selesai dibuat, saya mengonfigurasi **URL routing** di file `urls.py` agar semua view dapat diakses melalui alamat URL yang sesuai.  

6. **Membuat Templates**  
   Selanjutnya, saya membuat beberapa **template** di folder `templates`, yaitu `main.html` untuk halaman utama, `create_product.html` untuk halaman pembuatan produk baru, dan `product_detail.html` untuk menampilkan detail produk.  

7. **Melakukan Commit dan Push**  
   Terakhir, setelah semua fitur berhasil diimplementasikan, saya melakukan **commit** terhadap perubahan tersebut dan melakukan **push** ke repository GitHub untuk menyimpan dan membagikan hasil implementasi proyek.


## Mengapa perlu data delivery?
Data delivery diperlukan untuk menghubungkan backend dan frontend atau layanan lain. Dengan mengirim data dalam format standar seperti JSON/XML, platform dapat:

* Menyediakan data untuk berbagai klien (web, mobile, pihak ketiga).
* Memisahkan tanggung jawab antara UI dan logika backend.
* Mempermudah integrasi, otomasi, dan pengujian.

## XML vs JSON
Menurut saya, JSON lebih baik dibandingkan XML karena JSON lebih ringkas, mudah dibaca, dan memiliki struktur yang lebih sederhana. JSON juga lebih mudah dipahami oleh manusia maupun diproses oleh mesin tanpa perlu tag penutup yang panjang seperti XML.  

JSON lebih populer dibandingkan XML karena:  
1. Lebih mudah dibaca dan ditulis, strukturnya menyerupai objek JavaScript sehingga lebih intuitif.  
2. Lebih ringan, tidak memerlukan tag pembuka dan penutup yang kompleks.  
3. Didukung luas oleh framework dan bahasa pemrograman modern, terutama untuk pengembangan web berbasis API.  
4. Kinerja parsing lebih cepat, yang penting untuk aplikasi real-time dan layanan berbasis web.  


## Fungsi `is_valid()` pada Django form
* Memvalidasi input pengguna sesuai field & aturan validator.
* Mencegah data invalid masuk ke database.
* Menyediakan `cleaned_data` jika valid.
* Membantu menampilkan error ke pengguna jika ada kesalahan input.

### Alasan penggunaan `{% csrf_token %}`
* Mencegah CSRF (Cross-Site Request Forgery).
* Token ini diverifikasi server untuk memastikan request POST berasal dari form sah.
* Tanpa token, penyerang bisa memanfaatkan sesi pengguna untuk mengirim permintaan berbahaya (misalnya menghapus data).

## Feedback Tutorial 2
Penjelasannya sudah jelas dan mudah diikuti. Namun, jika memungkinkan, akan lebih baik jika bagian terkait file HTML seperti `main.html` dan template lainnya dijelaskan sedikit lebih detail. Hal ini akan membantu memahami struktur dan peran masing-masing file HTML dalam keseluruhan proyek.

## Contoh Pengujian Postman
