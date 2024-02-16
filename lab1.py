"""Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно),
распознает, преобразует и выводит на экран лексемы по определенному правилу.
Лексемы разделены пробелами. Преобразование делать по возможности через словарь.
Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
Регулярные выражения использовать нельзя.

Нечетные восьмиричные числа, не превышающие 409610, у которых вторая справа цифра равна 7.
Выводит на экран цифры числа, исключая семерки.
Вычисляется среднее число между минимальным и максимальным и выводится прописью.
"""

num_files = []
num_filtered = []
num_remove_seven = []
max_num = 0
min_num = 0

with open("input.txt", "r") as file:
    for line in file:
        string_files = line.strip()
        numbers = string_files.split()

        if numbers != '':
            for num_str in numbers:
                num = int(num_str)
                num_files.append(num)
            print("Список входных чисел из файла:", num_files)
            for num in num_files:
                if num % 2 != 0 and num < 4096 and str(num)[1] == '7' in str(num):
                    num_filtered.append(num)
            print("Список удовлетворяющих условию числа:", num_filtered)

            if num_filtered:

                min_num = min(num_filtered)
                max_num = max(num_filtered)

                print("Цифры чисел, исключая семерки:")
                for num in num_filtered:
                    num_remove_seven = ' '.join([digit for digit in str(num) if digit != '7'])
                    print(num_remove_seven)

                avg_num = (min_num + max_num) // 2
                print(f"Среднее число между минимальным ({min_num}) и максимальным ({max_num}): {avg_num}")
            else:
                print("Нет подходящих чисел в последовательности.")

            num_files = []
            num_filtered = []
        else:
            print("\nФайл пустой. Добавьте непустой файл в директорию или переименуйте существующий *.txt файл")
