# TODO Написать свою реализацию функции для подсчёта числа вхождение элементов в список
def my_count(l: list, item):
    counts = 0
    for i in l:
        if i == item:
            counts += 1
    return counts


# Пример работы

A = [1, 3, 1, 1, 3]

print(my_count(A, 3))