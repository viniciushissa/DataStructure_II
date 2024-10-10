def shellsort(arr):
    h = 1  
    n = len(arr)  
    while h <= (n - 1)/3:
        h = 3 * h + 1  
    while h > 0:  
        for j in range(h, n):  
            key = arr[j]  
            i = j  
            while i - h >= 0 and key <= arr[i - h]:
                arr[i] = arr[i - h]  
                i -= h  
            arr[i] = key  
        h = (h - 1)//3