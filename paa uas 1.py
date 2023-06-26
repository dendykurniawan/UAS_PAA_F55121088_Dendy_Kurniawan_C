#dendy Kurniawan
#f55121088
#kelas:C

import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    end_time = time.time()
    return arr, end_time - start_time

def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    end_time = time.time()
    return arr, end_time - start_time

def print_iterations(iterations):
    print("5 iterasi pertama:")
    for i in range(5):
        print(iterations[i])
    print("5 iteraterasi kedua:")
    for i in range(len(iterations)-5, len(iterations)):
        print(iterations[i])

def print_before_after(before, after):
    print("Sebelum sorting:", before)
    print("Setelah sorting:", after)

def analyze_algorithm():
    print("Analysis of sorting algorithms:")
    print("Worst case:")
    print("Bubble Sort: O(n^2)")
    print("Insertion Sort: O(n^2)")
    print("Best case:")
    print("Bubble Sort: O(n)")
    print("Insertion Sort: O(n)")
    print("Average case:")
    print("Bubble Sort: O(n^2)")
    print("Insertion Sort: O(n^2)")

def main_menu():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
           26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
           17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59,
           40, 7, 41, 81]

    while True:
        print("\nOptions:")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Analysis of Sorting Algorithms")
        print("4. Keluar")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Bubble Sort")
            before_sort, bubble_time = bubble_sort(arr.copy())
            print_iterations(before_sort)
            print("Eksekusi Waktu Bubble Sort :", bubble_time)
            print_before_after(arr, before_sort)
        elif choice == 2:
            print("Insertion Sort")
            before_sort, insertion_time = insertion_sort(arr.copy())
            print_iterations(before_sort)
            print("Eksekusi waktu Insertion Sort :", insertion_time)
            print_before_after(arr, before_sort)
        elif choice == 3:
            analyze_algorithm()
        elif choice == 4:
            break
        else:
            print("uopsss salah input gess.")

main_menu()
