from typing import List


def binary_search(arr: List[int], number: int) -> int:

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == number:
            return mid
        elif arr[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    arr = [1, 3, 9, 12, 21, 35, 57]
    print(f"Исходный список: {arr}")
    number = int(input("Введите элемент: "))
    result = binary_search(arr, number)

    if result == -1:
        print("Данного элемента нет в списке")
    else:
        print(f"Данный элемент: {number} найден по индексу: {result}")


if __name__ == "__main__":
    main()
