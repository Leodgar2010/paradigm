# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(numbers):
    for i in range(len(numbers)):
        highest_value_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[highest_value_index]:
                highest_value_index = j
        numbers[i], numbers[highest_value_index] = numbers[highest_value_index], numbers[i]


if __name__ == '__main__':
    random_list_of_nums = [12, 8, 3, 20, 11]
    sort_list_imperative(random_list_of_nums)
    print(random_list_of_nums)
