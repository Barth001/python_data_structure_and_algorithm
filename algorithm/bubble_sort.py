def bubble_sort(element):
    size = len(element)

    for i in range(size-1):
        swapper = False
        for j in range(size-1-i):
            if element[j] > element[j+1]:
                tmp = element[j]
                element[j] = element[j+1]
                element[j+1] = tmp
                swapper = True
        if not swapper:
            break


if __name__ == '__main__':
    # element = [4, 7, 12, 9, 13, 2, 18, 22, 78]
    element = [1, 2, 3, 4]

    bubble_sort(element)
    print(element)


def bubble_sort(elements, key=None):
    size = len(elements)
    for i in range(size-1):
        swapper = False
        for j in range(size-1-i):
            x = elements[j][key]
            y = elements[j+1][key]
            if x > y:
                first_element = elements[j+1][key]
                elements[j+1][key] = elements[j][key]
                elements[j][key] = first_element
                swapper = True

        if not swapper:
            break


elements = [
    {'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    {'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
    {'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
    {'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
]

# print(elements[0]['transaction_amount'])
bubble_sort(elements, key='transaction_amount')
print(elements)
