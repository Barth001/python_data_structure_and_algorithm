def swapper(a, b, lst):
    if a != b:
        first_num = lst[a]
        lst[a] = lst[b]
        lst[b] = first_num


def quick_sort(element, start, end):
    if len(elements) == 1:
        return
    if start < end:
        pi = partitioning(element, start, end)
        quick_sort(elements, start, pi-1)  # left side
        quick_sort(elements, pi+1, end)  # Right side


def partitioning(element, start, end):
    pivort = elements[end]
    p_index = start

    for i in range(start, end):
        if elements[i] <= pivort:
            swapper(i, p_index, elements)
            p_index += 1

    swapper(p_index, end, elements)

    return p_index


if __name__ == '__main__':

    elements = [11, 9, 29, 7, 2, 15, 28]

    quick_sort(elements, 0, len(elements)-1)
    print(elements)
