# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
print(my_list)
# print("Введите новый элемент рейтинга, когда закончите, наберите 'exit'")
# var_stop = 1
# while var_stop:
#     new_append = input()
#     if new_append == 'exit':
#         var_stop = 0
#     else:
#         var_list.append(new_append)
# print(var_list)
new_int = int(input("Новый элемент рейтинга: "))
new_list = my_list.copy()
new_list.append(new_int)
new_list.sort(reverse=True)

print(new_list)