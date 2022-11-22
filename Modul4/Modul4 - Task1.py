# Задание 1:
    # Нужно создать обычный калькулятор состоящий из знаков +,-,*,/
    # 1. У пользователя просят выбрать знак
    # 2. Просят ввести 1-ое число
    # 3. Просят ввести 2-ое число
    # 4. Вывести результат
    # 5. После результата спросить у пользователя хочет он закончить или нет,
    # если нет то калькулятор должен запускатся сначала
    # 6. Учесть то что деление на ноль невозможно

answer = 0
while True:
    operator = input('Введите операцию (+, -, *, /): ')
    num1 = int(input('Введите 1ое число: '))
    num2 = int(input('Введите 2ое число: '))

    if operator == '+':
        answer = num1 + num2
        print('Ответ:', answer)
        repeat = int(input('Хотите продолжить вычисления (1-да или 0-нет)? '))
        print()
        if repeat == 0:
            print('Программа завершает работу\nСпасибо, что воспользовались нашим калькулятором ^_-')
            break

    elif operator == '-':
        answer = num1 - num2
        print('Ответ:', answer)
        repeat = int(input('Хотите продолжить вычисления (1-да или 0-нет)? '))
        print()
        if repeat == 0:
            print('Программа завершает работу\nСпасибо, что воспользовались нашим калькулятором ^_-')
            break

    elif operator == '*':
        answer = num1 * num2
        print('Ответ:', answer)
        repeat = int(input('Хотите продолжить вычисления (1-да или 0-нет)? '))
        print()
        if repeat == 0:
            print('Программа завершает работу\nСпасибо, что воспользовались нашим калькулятором ^_-')
            break

    elif operator == '/':
        if num2 != 0:
            answer = num1 / num2
            print('Ответ:', answer)
            repeat = int(input('Хотите продолжить вычисления (1-да или 0-нет)? '))
            print()
            if repeat == 0:
                print('Программа завершает работу\nСпасибо, что воспользовались нашим калькулятором ^_-')
                break
        else:
            print('На 0 делить нельзя')
            repeat = int(input('Хотите продолжить вычисления (1-да или 0-нет)? '))
            print()
            if repeat == 0:
                print('Программа завершает работу\nСпасибо, что воспользовались нашим калькулятором ^_-')
                break

    else:
        print("Ошибка! Введите правильный оператор: не '0', '+', '-', '*', '/'")
        print()
