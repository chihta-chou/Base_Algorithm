
def insertionSort(arr):
    for i in range(1, len(arr)):
        preIndex = i-1
        for j in range(preIndex, -1, -1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def main():
    arr = [10, 7, 8, 9, 1, 5, 101, 77, 99, 56]
    n = len(arr)
    # arr = insertionSort(arr)
    arr = bubbleSort(arr)
    for i in range(n):
        print("%d" % arr[i])


if __name__ == "__main__":
    main()
