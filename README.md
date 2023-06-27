# UAS_PAA_F55121088_Dendy_Kurniawan_C
Analisis Algoritma:

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
