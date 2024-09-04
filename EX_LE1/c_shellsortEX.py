import random
import time

def shellsort(arr):
    h = 1
    n = len(arr)
    while h <= (n - 1)/3:
        h = 3 * h + 1
    while h > 0:
        for j in range(h, n):
            print(arr)
            key = arr[j]
            i = j
            while i - h >= 0 and key <= arr[i - h]:
                arr[i] = arr[i - h]
                i -= h
            arr[i] = key
        h = (h - 1)//3

def generate_random_arr(size):
    return random.sample(range(size * 10), size)

def measure_func(func, data):
    start_time = time.time()
    func(data)
    end_time = time.time()
    return end_time - start_time


size_arr = 10
arr = generate_random_arr(size_arr)
time = measure_func(shellsort, arr)
print(arr)
print(f"Tempo de execução do Shellsort para {size_arr} elementos: {time:.5f} segundos")