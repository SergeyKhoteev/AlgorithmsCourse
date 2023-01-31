sum_list = [i for i in range(int(input('Введите число A: ')), int(input('Введите число B: ')) + 1) if i % 3 == 0]
print(f'Сумма кратных 3-м чисел равна: {sum(sum_list)}')
print(f'Среднее арифметическое кратных 3-м чисел равно: {sum(sum_list) / len(sum_list)}')