def heap_down(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heap_down(arr, n, largest)

def build_heap(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        heap_down(arr, n, i)

def heapsort(arr):
    n = len(arr)

    build_heap(arr, n)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap_down(arr, i, 0)