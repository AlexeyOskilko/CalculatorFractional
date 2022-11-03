import fractions
from core import Calculator

while True:

    user_input = input('Введите выражение для вычисления через пробел\n')
    user_input = user_input.strip().split(" ")

    user_number1 = fractions.Fraction(user_input[0])
    desicion = user_input[1]
    user_number2 = fractions.Fraction(user_input[2])

    calc = Calculator(user_number1, user_number2)
    result = calc.desicion(desicion)
    print(result)

    next_calculation = input('Ввести ещё одно выражение? y - Да, n - нет')
    if next_calculation.lower()[0] == 'y':
        continue
    else:
        print('Хорошего дня!')
        break
