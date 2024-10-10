import random
import time
from shellsort import shellsort
from heapsort import heapsort
from mergesort import mergesort
from quicksort import quicksort

def generate_random_arr(size):
    return random.sample(range(size * 10), size)

def measure_func(func, *data):
    start_time = time.time()
    func(*data)
    end_time = time.time()
    return end_time - start_time

size_arr = 100000
arr1 = generate_random_arr(size_arr)
arr2, arr3, arr4 = arr1.copy(), arr1.copy(), arr1.copy() 

time1 = measure_func(shellsort, arr1)
time2 = measure_func(heapsort, arr2)
time3 = measure_func(mergesort, arr3, 0, size_arr - 1)
time4 = measure_func(quicksort, arr4)

print(f"Tempo de execução do ShellSort para {size_arr} elementos: {time1:.5f} segundos\n\
Tempo de execução do HeapSort  para {size_arr} elementos: {time2:.5f} segundos\n\
Tempo de execução do MergeSort para {size_arr} elementos: {time3:.5f} segundos\n\
Tempo de execução do QuickSort para {size_arr} elementos: {time4:.5f} segundos")

# print(arr1)
# shellsort(arr1)
# print(arr1)

# print(arr2)
# shellsort(arr2)
# print(arr2)

# print(arr3)
# shellsort(arr3)
# print(arr3)

# print(arr4)
# shellsort(arr4)
# print(arr4)