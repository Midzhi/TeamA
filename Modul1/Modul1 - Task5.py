# Задание №5:
# Какое слово нужно сложить 5 раз чтобы получить число 5?
# Какое слово нужно умножить на 7 чтобы получить 7?

while True:
    word = input('Введите слово от одной буквы: ')
    total_word = 0
    for i in range(5):
        total_word += len(word)
    answer1 = total_word
    print(answer1)

    answer2 = len(word) * 7
    print(answer2)

    if answer1 == 5 and answer2 == 7:
        print('Вы подобрали нужное слово!')
        break
    else:
        print('Нужно слово покороче')
        print()

