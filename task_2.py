"""
Задание 2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""
lst_2 = input("Введите числа через пробел:").split(' ')
a, b = 0, 1
while len(lst_2) > b:
    lst_2[a], lst_2[b] = lst_2[b], lst_2[a]
    a += 2
    b += 2
    print('Резултат:', *lst_2)
