# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
def sort_list_declarative (numbers):
    return sorted (numbers, reverse=True)

if __name__ == '__main__':
    random_list_of_nums = [12, 8, 3, 20, 11]
    print (sort_list_declarative(random_list_of_nums))