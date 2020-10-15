# a = int(input('введите число: '))
# b = int(input('введите число: '))
# sign = input('введите знак: ')
# if sign == '+':
#     print(a + b)
# elif sign == '-':
#     print(a - b)
# elif sign == '*':
#     print(a * b)
# elif sign == '/':
#     print(a / b)
# elif sign == 'mod':
#     print(a % b)
# elif sign == 'pow':
#     print(a ** b)
# elif sign == 'div':
#     print(a // b)
# else:
#     print('err')

# form = input('введите форму квартиры: ')
# if form == 'треугольник':
#     a = int(input('введите основание: '))
#     h = int(input('введите высоту: '))
#     print((a * h) / 2)
# elif form == 'круг':
#     r = int(input('введите радиус: '))
#     print(3.14 * r * r)

# passwd = input('введите пароль: ')
# if len(passwd) >= 8:
#     print('надёжный пароль')
# elif len(passwd) >= 5 or len(passwd) <= 7:
#     print('средний')
# else:
#     print('слабый пароль')

# ticket = int(input('введите номера билета: '))
# if ticket >= 100000 and ticket <= 999999:
#     a6 = ticket % 10
#     ticket = ticket // 10
#     a5 = ticket % 10
#     ticket = ticket // 10
#     a4 = ticket % 10
#     ticket = ticket // 10
#     a3 = ticket % 10
#     ticket = ticket // 10
#     a2 = ticket % 10
#     ticket = ticket // 10
#     a1 = ticket
#     if a1+a2+a3 == a4+a5+a6:
#         print('счастливый')
#     else:
#         print('несчастливый')
# else:
#     print('err')

'''
задача: 
вывести число 123 5 раз

стандартный синтаксис для повторения чего-то 5 раз
'''
# i = 0
# while i < 5:
#     print(123)
#     i = i + 1

'''
бесконечный цикл:
'''
# i = 0
# while True:
#     print(i)
#     i = i + 1

'''
цикл "до тех пор, пока"

задача:
пользователь вводит числа, до тех пор, пока не введёт 0
'''

a = int(input())
while a != 0:
    a = int(input())

'''
задача 1:
вывести все числа от 0 до 7 включительно

задача 2:
пользователь вводит число, с которого начать и которым закончить
вывести все числа в этом диапазоне

задача 3:
вывести все нечетные числа от 5 до 55 включительно
'''







# while (true)
#     alert('вас взломали')