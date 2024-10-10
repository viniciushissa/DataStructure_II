def merge(arr, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]

    for j in range(n2):
        R[j] = arr[middle + 1 + j]

    i = 0  
    j = 0  
    k = left  

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergesort(arr, left, right):
    if left < right:
        middle = (left + right) // 2

        mergesort(arr, left, middle)
        mergesort(arr, middle + 1, right)

        merge(arr, left, middle, right)