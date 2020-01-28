#!/usr/bin/python3
var_number = int(input('Введите целое положительное число: '))
var_max = 0

while var_number>1:
    var_let=var_number %10
    var_number //= 10
    if var_let > var_max:
        var_max = var_let

print(var_max)