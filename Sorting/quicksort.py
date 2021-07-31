def partition(arr, low, high):
    i = high + 1    # index of highest element
    pivot = arr[low]    # pivot is the lowest element

    for j in range(i-1, low, -1):
        if arr[j] > pivot:
            i -= 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i-1], arr[j] = arr[j], arr[i-1]
    return i - 1


def quicksort(arr, low, high):
    if low >= high:
        # print(arr)
        return
    i = partition(arr, low, high)
    quicksort(arr, low, i - 1)
    quicksort(arr, i + 1, high)


# arr = [5, 8, 1, 3, 7, 9, 2]
arr = [6, 5, 9, 3, 2, 1]
quicksort(arr, 0, len(arr) - 1)
print(arr)
