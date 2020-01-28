#!/usr/bin/python3
var_cash = int(input('Введите выручку: '))
var_loss = int(input('Введите издержки: '))

if var_cash > var_loss:
    print("Фирма отработала с прибылью, рентабельность ", (var_cash-var_loss)/var_cash )
else:
    print("Looser!")


var_people = int(input('Введите численность сотрудников: '))
print("Прибыль в расчете на одного человека: ", (var_cash-var_loss)/var_people)