#dendy kurniawan
#f55121088
#kelas: c

import sys
import time

# Fungsi untuk mencari shortest path menggunakan algoritma TSP
def tsp(graph, start):
    # Inisialisasi variabel
    n = len(graph)
    vertex = [i for i in range(n) if i != start]
    shortest_path = []
    shortest_dist = sys.maxsize

    # Rekursi untuk mencari shortest path
    def tsp_util(curr_vertex, visited, curr_path, curr_dist):
        nonlocal shortest_dist, shortest_path

        if len(curr_path) == n:
            if graph[curr_vertex][start] != 0 and curr_dist + graph[curr_vertex][start] < shortest_dist:
                shortest_dist = curr_dist + graph[curr_vertex][start]
                shortest_path = curr_path + [start]
        else:
            for next_vertex in vertex:
                if not visited[next_vertex] and graph[curr_vertex][next_vertex] != 0:
                    visited[next_vertex] = True
                    tsp_util(next_vertex, visited, curr_path + [next_vertex], curr_dist + graph[curr_vertex][next_vertex])
                    visited[next_vertex] = False

    # Panggil fungsi rekursi untuk mencari shortest path
    visited = [False] * n
    visited[start] = True
    tsp_util(start, visited, [], 0)

    return shortest_path, shortest_dist

# Fungsi untuk mencari shortest path menggunakan algoritma Dijkstra
def dijkstra(graph, start):
    # Inisialisasi variabel
    n = len(graph)
    dist = [sys.maxsize] * n
    dist[start] = 0
    shortest_path = [start]

    # Looping untuk mencari shortest path
    while len(shortest_path) < n:
        min_dist = sys.maxsize
        next_vertex = None

        for v in range(n):
            if v not in shortest_path and dist[v] < min_dist:
                min_dist = dist[v]
                next_vertex = v

        if next_vertex is None:
            break

        shortest_path.append(next_vertex)
        for v in range(n):
            if v not in shortest_path and graph[next_vertex][v] != 0:
                new_dist = dist[next_vertex] + graph[next_vertex][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist

    return shortest_path, dist[start]

# Fungsi untuk menampilkan graph
def display_graph(graph):
    for i, row in enumerate(graph):
        for j, dist in enumerate(row):
            print(f'Distance from {chr(65 + i)} to {chr(65 + j)}: {dist}')
        print()

# Fungsi utama
def main():
    # Graph dalam bentuk matriks adjacency
    graph = [[0, 12, 10, 0, 0, 0, 0],
             [0, 0, 8, 12, 0, 0, 0],
             [0, 0, 0, 11, 3, 0, 0],
             [0, 0, 0, 0, 0, 6, 0],
             [0, 0, 0, 11, 0, 9, 0],
             [0, 0, 0, 0, 0, 0, 7],
             [12, 0, 0, 0, 0, 0, 0]]

    while True:
        # Pilihan pengguna
        print("\nPilihan algoritma:")
        print("1. TSP (Travelling Salesman Problem)")
        print("2. Dijkstra")
        print("3. Worst Case (TSP)")
        print("4. Best Case (Dijkstra)")
        print("5. Average Case (TSP)")
        print("6. Exit")
        choice = input("Pilih opsi (1-6): ")

        if choice == '1':
            start = int(input("Masukkan titik awal (0-6): "))
            start_time = time.time()
            shortest_path, shortest_dist = tsp(graph, start)
            end_time = time.time()

            print(f"\nShortest Path (TSP): {' -> '.join(chr(65 + v) for v in shortest_path)}")
            print(f"Shortest Distance: {shortest_dist}")
            print(f"Waktu komputasi: {end_time - start_time} detik")

        elif choice == '2':
            start = int(input("Masukkan titik awal (0-6): "))
            start_time = time.time()
            shortest_path, shortest_dist = dijkstra(graph, start)
            end_time = time.time()

            print(f"\nShortest Path (Dijkstra): {' -> '.join(chr(65 + v) for v in shortest_path)}")
            print(f"Shortest Distance: {shortest_dist}")
            print(f"Waktu komputasi: {end_time - start_time} detik")

        elif choice == '3':
            worst_case_graph = [[0, 1, 1, 1, 1, 1, 1],
                                [1, 0, 1, 1, 1, 1, 1],
                                [1, 1, 0, 1, 1, 1, 1],
                                [1, 1, 1, 0, 1, 1, 1],
                                [1, 1, 1, 1, 0, 1, 1],
                                [1, 1, 1, 1, 1, 0, 1],
                                [1, 1, 1, 1, 1, 1, 0]]

            start = int(input("Enter the starting vertex (0-6): "))
            start_time = time.time()
            shortest_path, shortest_dist = tsp(worst_case_graph, start)
            end_time = time.time()

            print(f"\nShortest Path (Worst Case - TSP): {' -> '.join(chr(65 + v) for v in shortest_path)}")
            print(f"Shortest Distance: {shortest_dist}")
            print(f"Execution Time: {end_time - start_time} seconds")

        elif choice == '4':
            best_case_graph = [[0, 1, 0, 0, 0, 0, 0],
                               [0, 0, 1, 0, 0, 0, 0],
                               [0, 0, 0, 1, 0, 0, 0],
                               [0, 0, 0, 0, 1, 0, 0],
                               [0, 0, 0, 0, 0, 1, 0],
                               [0, 0, 0, 0, 0, 0, 1],
                               [0, 0, 0, 0, 0, 0, 0]]

            start = int(input("Enter the starting vertex (0-6): "))
            start_time = time.time()
            shortest_path, shortest_dist = dijkstra(best_case_graph, start)
            end_time = time.time()

            print(f"\nShortest Path (Best Case - Dijkstra): {' -> '.join(chr(65 + v) for v in shortest_path)}")
            print(f"Shortest Distance: {shortest_dist}")
            print(f"Execution Time: {end_time - start_time} seconds")

        elif choice == '5':
            # Average case graph
            avg_case_graph = [[0, 12, 10, 0, 0, 0, 0],
                              [0, 0, 8, 12, 0, 0, 0],
                              [0, 0, 0, 11, 3, 0, 0],
                              [0, 0, 0, 0, 0, 6, 0],
                              [0, 0, 0, 11, 0, 9, 0],
                              [0, 0, 0, 0, 0, 0, 7],
                              [12, 0, 0, 0, 0, 0, 0]]

            start = int(input("Enter the starting vertex (0-6): "))
            start_time = time.time()
            shortest_path, shortest_dist = tsp(avg_case_graph, start)
            end_time = time.time()

            print(f"\nShortest Path (Average Case - TSP): {' -> '.join(chr(65 + v) for v in shortest_path)}")
            print(f"Shortest Distance: {shortest_dist}")
            print(f"Execution Time: {end_time - start_time} seconds")

        elif choice == '6':
            break

        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
