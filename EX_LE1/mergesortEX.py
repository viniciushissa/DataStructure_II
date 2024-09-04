import random
import time

def merge(arr, p, q, r):
    left_arr = []
    right_arr = []

    n1 = q - p + 1
    n2 = r - q

    for i in range(0, n1 - 1):
        left_arr.append(arr[i])
    print(left_arr) 

    for j in range(0, n2 - 1):
        right_arr.append(arr[j])
    print(right_arr)

    i = j = 0

    for k in range(p, r):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1

def mergesort(arr, p, r):
    if p < r:
        q = (p + r)//2
        mergesort(arr, p, q)
        mergesort(arr, q+1, r)
        merge(arr, p, q, r)

def generate_random_arr(size):
    return random.sample(range(size * 10), size)

def measure_func(func, *data):
    start_time = time.time()
    func(*data)
    end_time = time.time()
    return end_time - start_time


size_arr = 10
arr = generate_random_arr(size_arr)
print(arr)
time = measure_func(mergesort, arr, 0, size_arr)
print(arr)
print(f"Tempo de execução do Mergesort para {size_arr} elementos: {time:.5f} segundos")