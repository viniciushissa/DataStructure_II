def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        smallers, biggers = [], []
        
        for x in arr[:-1]:
            if x <= pivot:
                smallers.append(x)
            else:
                biggers.append(x)
        
        return quicksort(smallers) + [pivot] + quicksort(biggers)