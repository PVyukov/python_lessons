# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

var_list = []
print("Введите элементы списка, когда закончите, наберите 'exit'")
var_stop = 1
while var_stop:
    new_append = input()
    if new_append == 'exit':
        var_stop = 0
    else:
        var_list.append(new_append)
print(var_list)
var_iter = (len(var_list))//2
i = 0
while var_iter:
    var_x = var_list[i]
    var_list[i] = var_list[i+1]
    var_list[i+1]= var_x
    i += 2
    var_iter -=1

print(var_list)