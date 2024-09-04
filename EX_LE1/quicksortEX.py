import random
import time

def quicksort(arr):


def generate_random_arr(size):
    return random.sample(range(size * 10), size)

def measure_func(func, data):
    start_time = time.time()
    func(data)
    end_time = time.time()
    return end_time - start_time


size_arr = 10
arr = generate_random_arr(size_arr)
left = i for i in range(0, size_arr//2 - 1)
print(arr)
time = measure_func(quicksort, arr, left, right)
print(arr)
print(f"Tempo de execução do Quicksort para {size_arr} elementos: {time:.5f} segundos")