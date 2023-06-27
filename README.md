# UAS_PAA_F55121088_Dendy_Kurniawan_C
Analisis Algoritma: no1

1. Bubble Sort:
   - Kasus Terburuk (Worst Case): O(n^2)
     Pada kasus terburuk, Bubble Sort akan melakukan iterasi sebanyak n kali untuk setiap elemen dalam array. Dalam setiap iterasi, elemen akan dibandingkan dengan elemen-elemen sebelumnya dan akan ditukar jika diperlukan. Dengan demikian, pada setiap iterasi, elemen terbesar akan "mengapung" ke posisi terakhir secara bertahap. Jumlah iterasi yang dilakukan adalah sebanyak n kali untuk setiap elemen dalam array. Oleh karena itu, dalam kasus terburuk, kompleksitas waktu Bubble Sort adalah O(n^2).

   - Kasus Terbaik (Best Case): O(n)
     Pada kasus terbaik, jika array sudah terurut secara membesar, maka dalam satu iterasi pertama, Bubble Sort akan membandingkan semua pasangan elemen dan tidak akan ada pertukaran yang terjadi. Dengan demikian, algoritma akan berhenti setelah satu iterasi, karena tidak ada lagi elemen yang perlu ditukar. Oleh karena itu, dalam kasus terbaik, kompleksitas waktu Bubble Sort adalah O(n).

   - Kasus Rata-rata (Average Case): O(n^2)
     Pada kasus rata-rata, Bubble Sort akan melakukan sekitar n^2/2 perbandingan elemen dan pertukaran dalam array yang tidak terurut secara sempurna. Jumlah iterasi yang dilakukan adalah sebanyak n kali untuk setiap elemen dalam array. Oleh karena itu, dalam kasus rata-rata, kompleksitas waktu Bubble Sort adalah O(n^2).

2. Insertion Sort:
   - Kasus Terburuk (Worst Case): O(n^2)
     Pada kasus terburuk, jika array sudah terurut secara terbalik, Insertion Sort akan memerlukan waktu yang maksimal untuk memindahkan setiap elemen ke posisi yang benar. Dalam setiap iterasi, algoritma akan membandingkan elemen dengan elemen-elemen sebelumnya dan memindahkan elemen tersebut ke posisi yang sesuai. Oleh karena itu, dalam kasus terburuk, kompleksitas waktu Insertion Sort adalah O(n^2).

   - Kasus Terbaik (Best Case): O(n)
     Pada kasus terbaik, jika array sudah terurut secara membesar, Insertion Sort hanya akan memerlukan satu perbandingan untuk setiap elemen dan tidak ada perpindahan yang perlu dilakukan. Dalam kasus terbaik, kompleksitas waktu Insertion Sort adalah O(n).

   - Kasus Rata-rata (Average Case): O(n^2)
     Pada kasus rata-rata, Insertion Sort akan melakukan sekitar n^2/4 perbandingan elemen dan perpindahan dalam array yang tidak terurut secara sempurna. Oleh karena itu, dalam kasus rata-rata, kompleksitas waktu Insertion Sort adalah O(n^2).

Dalam kode yang diberikan, terdapat sebuah menu utama dengan pilihan untuk melakukan Bubble Sort, Insertion Sort, melihat Analisis Algoritma, atau keluar dari program. Kode ini menggunakan fungsi `bubble_sort` dan `insertion_sort` untuk mengurutkan array yang diber

ikan menggunakan masing-masing algoritma. Fungsi `print_iterations` digunakan untuk mencetak 5 iterasi pertama dan 5 iterasi terakhir dari hasil pengurutan. Fungsi `print_before_after` digunakan untuk mencetak array sebelum dan setelah pengurutan. Fungsi `analyze_algorithm` mencetak analisis kompleksitas waktu untuk masing-masing algoritma.

Analisis algoritma no 2
1. Algoritma TSP (Travelling Salesman Problem):
   - Fungsi `tsp` menerima graf sebagai argumen dan titik awal dari perjalanan.
   - Variabel `n` digunakan untuk menyimpan jumlah simpul dalam graf.
   - Variabel `vertex` adalah daftar yang berisi semua simpul kecuali simpul awal.
   - Variabel `shortest_path` dan `shortest_dist` digunakan untuk menyimpan jalur terpendek dan jarak terpendek saat ini.
   - Fungsi rekursif `tsp_util` mengimplementasikan pencarian rekursif untuk mencari jalur terpendek. Ini mempertimbangkan setiap kemungkinan jalur dengan mengunjungi semua simpul yang belum dikunjungi.
   - Jika semua simpul telah dikunjungi, maka jalur yang ditemukan diperiksa apakah kembali ke simpul awal, dan jika jaraknya lebih pendek dari `shortest_dist` saat ini, maka jalur dan jarak terpendek diperbarui.
   - Fungsi utama `main` digunakan untuk menerima masukan dari pengguna dan memanggil fungsi `tsp` dengan graf dan titik awal yang sesuai.
   - Output dari algoritma ini adalah jalur terpendek yang ditemukan dan jarak terpendek.

2. Algoritma Dijkstra:
   - Fungsi `dijkstra` juga menerima graf sebagai argumen dan titik awal perjalanan.
   - Variabel `n` menyimpan jumlah simpul dalam graf.
   - Variabel `dist` menyimpan jarak terpendek saat ini antara titik awal dan setiap simpul.
   - Variabel `shortest_path` awalnya berisi simpul awal.
   - Algoritma Dijkstra dilakukan dengan menemukan simpul dengan jarak terpendek yang belum termasuk dalam `shortest_path` dan memperbarui jarak terpendek untuk simpul-simpul tetangganya.
   - Fungsi utama `main` digunakan untuk menerima masukan dari pengguna dan memanggil fungsi `dijkstra` dengan graf dan titik awal yang sesuai.
   - Output dari algoritma ini adalah jalur terpendek yang ditemukan dan jarak terpendek.

Kedua algoritma ini digunakan untuk mencari jalur terpendek dalam graf dengan bobot. Pilihan menu dalam fungsi `main` memungkinkan pengguna untuk memilih algoritma yang ingin digunakan, dan juga menyediakan beberapa kasus uji khusus seperti kasus terburuk, kasus terbaik, dan kasus rata-rata.

Dalam analisis kompleksitas waktu, algoritma TSP menggunakan pendekatan brute force yang mencoba semua kemungkinan jalur, sehingga kompleksitasnya adalah O(n!) di mana n adalah jumlah simpul dalam graf. Algoritma Dijkstra memiliki kompleksitas waktu O(V^2) di mana V adalah jumlah simpul dalam graf. Namun, jika digunakan implementasi optimasi seperti heap biner, kompleksitasnya dapat dikurangi menjadi O((V + E) log V), di mana E adalah jumlah tepi dalam graf.

Kode ini juga
