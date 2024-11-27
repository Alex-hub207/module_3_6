new_list = []


def calculate_structure_sum(arg):
    sum_elements = 0
    for i in arg:
        if isinstance(i, (int, str)):
            global new_list
            new_list.append(i)
        elif isinstance(i, dict):
            new_list.extend(i.keys())
            new_list.extend(i.values())
        else:
            calculate_structure_sum(i)
    for j in new_list:
        if isinstance(j, int):
            sum_elements = sum_elements + j
        else:
            sum_elements = sum_elements + len(j)
    return sum_elements


data_structure = [

    [1, 2, 3],

    {'a': 4, 'b': 5},

    (6, {'cube': 7, 'drum': 8}),

    "Hello",

    ((), [{(2, 'Urban', ('Urban2', 35))}])

]

result = calculate_structure_sum(data_structure)

print(result)


#   Не нравится мне то, что получилось.
#   Считает правильно,
#   и структуру нормально на части разбирает рекурсией.
#   Но два цикла...
#   И пустой список пришлось объявлять до функции.
#   Может что посоветуете?
