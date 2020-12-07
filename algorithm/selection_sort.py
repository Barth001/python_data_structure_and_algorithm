def selection_sort(arr):
    size = len(arr)

    for i in range(0, size):
        k = i + 1
        while k < size:
            if arr[i] > arr[k]:
                sort_arr = arr[i]
                arr[i], arr[k] = arr[k], sort_arr
            k += 1
    return arr


# elements = [78, 12, 15, 8, 61, 53, 23, 27]
test = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [345, 678, 34, 12, 987, 0],
    [],
    [0, 100, 2, 3]
]
for elements in test:
    print(selection_sort(elements))
