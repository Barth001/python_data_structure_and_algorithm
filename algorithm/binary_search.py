def linear_search(number_list, number_to_find):
    for index, element in enumerate(number_list):
        if element == number_to_find:
            return index
    return -1


def binary_search(number_list, number_to_find):
    left_side = 0
    right_side = len(number_list) - 1
    mid_index = 0
    while left_side <= right_side:
        mid_index = (left_side + right_side) // 2
        mid_number = number_list[mid_index]
        if mid_number == number_to_find:
            return mid_index
        if number_to_find < mid_number:
            right_side = mid_index - 1

        else:
            left_side = mid_index + 1
    return -1


def recursive_binary_search(number_list, number_to_find, left_index, right_index):
    mid_index = (left_index + right_index) // 2
    mid_number = number_list[mid_index]
    if left_index > right_index:
        return -1

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1

    if mid_number > number_to_find:
        right_index = mid_index - 1

    return recursive_binary_search(number_list, number_to_find, left_index, right_index)


def find_all_index_of(numbers, number_to_find):
    index_list = []
    for index, element in enumerate(numbers):
        if element == number_to_find:
            index_list.append(index)
    return index_list


def binary_search_find_index_of(numbers, number_to_find):
    left_index = 0
    mid_index = 0
    right_index = len(numbers) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1

        else:
            right_index = mid_index - 1
    return -1


def find_index(numbers, number_to_find):
    index = binary_search_find_index_of(numbers, number_to_find)
    index_list = [index]

    # for left side of the binary
    i = index - 1
    while i >= 0:
        if numbers[i] == number_to_find:
            index_list.append(i)
        else:
            break
        i = i - 1

        # for right hand side

    i = index + 1
    while i < len(numbers):
        if numbers[i] == number_to_find:
            index_list.append(i)
        else:
            break
        i = i + 1
    return sorted(index_list)


numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
number_to_find = 1

index = find_index(numbers, number_to_find)
print(index)

# number_list = [56, 67, 72, 75, 76, 79, 82, 84, 87, 90, 96]

# index = recursive_binary_search(number_list, 79, 0, len(number_list) - 1)
# index = binary_search(number_list, 799)
# index = linear_search(number_list, 560)
# print(index)
