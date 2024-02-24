"""Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно),
распознает, преобразует и выводит на экран лексемы по определенному правилу.
Лексемы разделены пробелами. Преобразование делать по возможности через словарь.
Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
Регулярные выражения использовать нельзя.

Нечетные восьмиричные числа, не превышающие 409610, у которых вторая справа цифра равна 7.
Выводит на экран цифры числа, исключая семерки.
Вычисляется среднее число между минимальным и максимальным и выводится прописью.
"""
digit_to_word = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть',
                 '7': 'семь', '8': 'восемь', '9': 'девять'}
min_num = 0
max_num = 10000
num_filtered = []
num_remove_seven = []
file = open("input.txt", "r", encoding="utf-8")

while True:
    str_txt = file.readline().split()
    if not str_txt:
        print("\nФайл input.txt в директории проекта закончился")
        break
    else:
        for num in str_txt:
            flag_negative = False
            symb_punct = '''!()[]{};:'"\\,<>./?@#$%^&*_~'''
            if num.startswith('-'):
                flag_negative = True
                num = num[1:]
            if all(val not in symb_punct and not val.isalpha() and '0' <= val <= '7' for val in num) and len(num) > 1:
                if int(num) % 2 != 0 and len(num) < 5 and num[-2] == '7':
                    if flag_negative:
                        num = -int(num)
                    num_filtered.append(int(num))
if num_filtered:
    print("Список чисел, удовлетворяющих условию:\n",num_filtered)
    min_num = min(num_filtered)
    max_num = max(num_filtered)
    
    print("Цифры чисел, исключая семерки:")
    for num in num_filtered:
        num_remove_seven = ''.join([digit for digit in str(abs(num)) if digit != '7'])
        print(num_remove_seven)

    avg_num = (min_num + max_num) // 2
    avg_num_words = ' '.join([digit_to_word[digit] for digit in str(abs(avg_num))])
    print(f"Среднее число между минимальным ({min_num}) и максимальным ({max_num}): {avg_num_words}")

else:
    print("Нет чисел для обработки.")
