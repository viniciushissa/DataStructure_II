import random
import time

def insertionsort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket

def bucketsort(arr):
    n = len(arr)
    B = [[] for _ in range(10)]

    for i in range(n):
        index = int(10 * arr[i])
        B[index].append(arr[i])

    for i in range(10):
        B[i] = insertionsort(B[i])

    sorted_array = []
    for i in range(10):
        sorted_array.extend(B[i])

    return sorted_array

def generate_random_arr(size):
    return [random.random() for _ in range(size)]

size_arr = 25000
arr = generate_random_arr(size_arr)
# print(arr)
print(f'Ordenação Iniciada!')
sorted_arr = bucketsort(arr)
# print(sorted_arr)
print(f'Ordenação finalizada!')

# def measure_func(func, data):
#     start_time = time.time()
#     result = func(data)
#     end_time = time.time()
#     return result, end_time - start_time

# size_arr = 25
# arr = generate_random_arr(size_arr)
# print(arr)
# sorted_arr, exec_time = measure_func(bucketsort, arr)
# print(sorted_arr)
# print(f"Tempo de execução do BucketSort para {size_arr} elementos: {exec_time:.5f} segundos")