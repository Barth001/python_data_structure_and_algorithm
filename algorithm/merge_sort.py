# def merge_sort(arr):
#     if len(arr) <= 1:
#         return

#     mid = len(arr) // 2

#     left = arr[:mid]
#     right = arr[mid:]
#     merge_sort(left)
#     merge_sort(right)
#     merge_two_sorted_list(left, right, arr)

#     return arr


# def merge_two_sorted_list(a, b, arr):
#     index_a = len(a)
#     index_b = len(b)

#     i = j = k = 0

#     while i < index_a and j < index_b:
#         if a[i] <= b[j]:
#             arr[k] = a[i]
#             i += 1
#         else:
#             arr[k] = b[j]
#             j += 1
#         k += 1
#     while i < index_a:
#         arr[k] = a[i]
#         i += 1
#         k += 1

#     while j < index_b:
#         arr[k] = b[j]
#         j += 1
#         k += 1


def merge(left_list, right_list, key, descending=False):
    merged = []
    if descending:
        if len(left_list) > 0 and len(right_list) > 0:
            if left_list[0][key] >= right_list[0][key]:
                merged.append(left_list.pop(0))
            else:
                merged.append(right_list.pop(0))

    else:
        while len(left_list) > 0 and len(right_list) > 0:
            if len(left_list) > 0 and len(right_list) > 0:
                if left_list[0][key] <= right_list[0][key]:
                    merged.append(left_list.pop(0))
                else:
                    merged.append(right_list.pop(0))

    merged.extend(left_list)
    merged.extend(right_list)
    return merged


def merge_sort(elements, key, descending=False):
    size = len(elements)
    if len(elements) == 1:
        return elements

    left_list = merge_sort(elements[:size//2], key, descending)
    right_list = merge_sort(elements[size//2:], key, descending)
    sorted_list = merge(left_list, right_list, key, descending)

    return sorted_list


elements = [
    {'name': 'vedanth',   'age': 17, 'time_hours': 1},
    {'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
    {'name': 'rajab', 'age': 12,  'time_hours': 3},
    {'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
]

sort = merge_sort(elements, key='name')
print(sort)

# elements = [
#     {'name': 'rajab', 'age': 12, 'time_hours': 3},
#     {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
#     {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
#     {'name': 'vedanth', 'age': 17, 'time_hours': 1},
# ]

# merge_sort(elements, key='name')

# elements = [
#     {'name': 'chinmay',   'age': 24, 'time_hours': 1.5},
#     {'name': 'rajab', 'age': 12,  'time_hours': 3},
#     {'name': 'vedanth',  'age': 17,  'time_hours': 1},
#     {'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
# ]


# arr = [10, 3, 15, 7, 8, 23, 98, 29]


# print(merge_sort(arr))
