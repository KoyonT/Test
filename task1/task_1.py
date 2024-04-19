import itertools

n = int(input('Введите количество элементов в массиве: '))
m = int(input('Введите интервал длины: '))

arr = [i + 1 for i in range(n)]

count = 0
answer_array = [1]  #т.к. путь в ответе всегда будет начинаться с 1
gen = (x for x in itertools.cycle(arr))  #Зацикливаю массив чтобы выйти из него при определенном условии
for x in gen:
    count += 1
    if count == m:
        if x == 1:
            break
        answer_array.append(x)
        count = 1

print(answer_array)
