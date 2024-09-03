import random
import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
        print(arr)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)
        print(arr)

def generate_random_arr(size):
    return random.sample(range(size * 10), size)

def measure_func(func, data):
    start_time = time.time()
    func(data)
    end_time = time.time()
    return end_time - start_time


size_arr = 10
arr = generate_random_arr(size_arr)
print(arr)
time = measure_func(heapsort, arr)
print(arr)
print(f"Tempo de execução do Heapsort para {size_arr} elementos: {time:.5f} segundos")