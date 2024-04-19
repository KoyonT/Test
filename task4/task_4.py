import numpy as np


def main():
    file_path = input('Введите путь к файлу: ')

    with open(file_path, 'r') as file:
        numbers = [int(line) for line in file]
    import random

    def quickselect_median(l, pivot_fn=random.choice):  #Алгоритм Тони Хоара для нахождения медианы
        if len(l) % 2 == 1:
            return quickselect(l, len(l) / 2, pivot_fn)
        else:
            return 0.5 * (quickselect(l, len(l) / 2 - 1, pivot_fn) +
                          quickselect(l, len(l) / 2, pivot_fn))

    def quickselect(l, k, pivot_fn):
        """
        Выбираем k-тый элемент в списке l (с нулевой базой)
        :param l: список числовых данных
        :param k: индекс
        :param pivot_fn: функция выбора pivot, по умолчанию выбирает случайно
        :return: k-тый элемент l
        """
        if len(l) == 1:
            assert k == 0
            return l[0]

        pivot = pivot_fn(l)

        lows = [el for el in l if el < pivot]
        highs = [el for el in l if el > pivot]
        pivots = [el for el in l if el == pivot]

        if k < len(lows):
            return quickselect(lows, k, pivot_fn)
        elif k < len(lows) + len(pivots):
            return pivots[0]
        else:
            return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)

    moves = sum(abs(num - quickselect_median(numbers)) for num in numbers)  #сумма количества шагов к медиане

    print(moves)


if __name__ == "__main__":
    main()
