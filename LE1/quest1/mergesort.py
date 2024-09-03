import random
import time

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def mergesort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = mergesort(arr[:middle])
    right = mergesort(arr[middle:])

    return merge(left, right)

def generate_random_arr(size):
    return random.sample(range(size * 10), size)

def measure_func(func, data):
    start_time = time.time()
    func(data)
    end_time = time.time()
    return end_time - start_time


size_arr = 100000
arr = generate_random_arr(size_arr)
time = measure_func(mergesort, arr)
print(f"Tempo de execução do Mergesort para {size_arr} elementos: {time:.5f} segundos")