def shell_sort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:

        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2
    return arr


# elemeents = [21, 38, 29, 17, 4, 25, 11, 32, 9]
elemeents = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
print(shell_sort(elemeents))
