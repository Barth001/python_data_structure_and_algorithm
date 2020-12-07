def swapper(num1, num2, lst):
    if num1 != num2:
        temp = lst[num1]
        lst[num1] = lst[num2]
        lst[num2] = temp


def partition(elements, start, end):
    pivort_index = start
    pivort = elements[pivort_index]

    while start < end:

        while start < len(elements) and elements[start] <= pivort:
            start += 1

        while elements[end] > pivort:
            end -= 1

        if start < end:
            swapper(start, end, elements)

    swapper(pivort_index, end, elements)

    return end


def quick_sort(elements, start,  end):
    if start < end:

        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)  # left
        quick_sort(elements, pi+1, end)  # left


elements = [11, 9, 29, 7, 2, 15, 28]

quick_sort(elements, 0, len(elements)-1)
print(elements)
