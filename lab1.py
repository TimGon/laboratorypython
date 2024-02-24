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

num_filtered = []
max_num = 0
min_num = 0


def is_number(value):
    symb_punct = '''!()[]{};:'"\\,<>./?@#$%^&*_~'''
    fil_num = ''
    for num_str in value:
        if num_str not in symb_punct and not num_str.isalpha():
            fil_num += num_str

    return fil_num


with open("input.txt", "r", encoding='utf-8') as file:
    for line in file:

        characters = line.split()

        for char in characters:
            num_fil = is_number(char)
            is_negative = False

            if num_fil.startswith('-'):
                is_negative = True
                num_fil = num_fil[1:]

            if len(num_fil) > 1 and all('0' <= char <= '7' for char in num_fil):
                num = int(num_fil)
                if num % 2 != 0 and num < 4096 and str(num)[-2] == '7':
                    if is_negative:
                        num = -num
                    num_filtered.append(num)
if num_filtered:
    print("Список чисел, удовлетворяющих условию:")
    print(num_filtered)
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
    print("Нет чисел для обработки/файл был пустым.")
