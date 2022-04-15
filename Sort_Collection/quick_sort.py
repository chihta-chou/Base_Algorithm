def partition(arr, low, high):
    i, pivot = low-1, arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quickSort(arr, low, high):
    if low < high:
        q = partition(arr, low, high)
        quickSort(arr, low, q-1)
        quickSort(arr, q+1, high)


def main():
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quickSort(arr, 0, n-1)
    for i in range(n):
        print("%d" % arr[i])


if __name__ == "__main__":
    main()
