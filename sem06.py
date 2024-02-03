# Задача.
# Написать программу на любом языке в любой парадигме для бинарного поиска.
# На вход подаётся целочисленный массив и число.
# На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.

def binary_search(arr_list, element):
    left = 0
    right = len(arr_list) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr_list[mid] == element:
            return mid
        elif arr_list[mid] > element:
            right = mid - 1
        else:
            left = mid + 1

    return -1


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 19
    result = binary_search(arr, target) + 1
    if result != -1:
        print(f"Элемент {target} найден в позиции {result}.")
    else:
        print(f"Элемент {target} не найден в массиве.")
