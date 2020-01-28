#!/usr/bin/python3
var_a = int(input('Введите a: '))
var_b = int(input('Введите b: '))
var_day = 0
while var_a < var_b:
    print(var_day, "й день:", var_a)
    var_a *= 1.1
    var_day += 1
print('Ваш результат достигнут на ', var_day, " день")
