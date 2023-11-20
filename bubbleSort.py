def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        already_sorted = True
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                already_sorted = False
        if already_sorted:
            break
    return arr

print(bubbleSort([20, 10, 14, 82, 56, 43]))