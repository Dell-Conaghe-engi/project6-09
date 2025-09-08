Git init# Задание 1
'''temperature = int(input("Введите температуру целое число"))
if temperature <= 0:
    print('очень холодно')
elif temperature <= 20 and temperature > 0:
    print('прохладно')
else:
    print('тепло')'''
# задание 2
a = int(input('введите  час в формате целого числа от 0 до 23'))
if a<=11 and a>5:
    print('«утро »')
elif a<=17 and a>11:
    print('«день »')
elif a<=22 and a>17:
    print('«вечер »')
else:
    print('«ночь »')