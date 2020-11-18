
def selection_sort(arr):
    n = len(arr)
    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if arr[i] < arr[min_index]:
                min_index = i
        if arr[j] > arr[min_index]:
            aux = arr[j]
            arr[j] = arr[min_index]
            arr[min_index] = aux
# 1 + (n-1)[5 + X] = 1 + 5(n-1) + X*(n-1)
# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)
