#!/usr/bin/python3
var_time = int(input('Введите время в секундах: '))
#print(type(var_time))
var_hours = var_time // 3600
var_minutes = (var_time % 3600) // 60
var_seconds = (var_time % 3600) % 60
#print(var_time)
#print(var_hours)
#print(var_minutes)
#print(var_seconds)
print(f'Ваше время {var_hours} часа(ов) {var_minutes} минут(ы) {var_seconds} секунд(ы)')

