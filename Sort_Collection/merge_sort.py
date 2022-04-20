def mergeSort(arr, left, right):
    if left < right:
        mid = (left+right)//2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)
        merge(arr, left, right, mid)


def merge(arr, left, right, mid):
    L, R = arr[left:mid+1], arr[mid+1:]
    i = left
    while(L and R):
        if L[0] < R[0]:
            arr[i] = L.pop(0)
        else:
            arr[i] = R.pop(0)
        i += 1
    if L:
        arr[i:right+1] = L
    else:
        arr[i:right+1] = R


def main():
    arr = [10, 7, 8, 9, 1, 5, 101, 77, 99, 56]
    n = len(arr)
    mergeSort(arr, 0, n-1)
    for i in range(n):
        print("%d" % arr[i])


if __name__ == "__main__":
    main()
