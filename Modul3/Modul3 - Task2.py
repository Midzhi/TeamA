# Задание 2:
# 1. Спросите у пользователя предложение и поделите его по пробелам.
    # Если пользователь ввёл меньше шести слов спросите снова, Не принимайте предложения если оно короче 6 символов, спрашивайте снова и снова.
# 2. Поделите полученный лист на 2 равные части (Если число элементов листа нечетное, то длина первой части должна быть на один жлемент больше)
# 3. Переставьте эти две части местами и запишите в лист.
while True:
    text = input('Введите предложение: ')
    text = text.split(" ")
    if len(text) < 6:
        print('Ваше предложение слишком короткое, нужно предложение минимум из 6 слов')
        continue
    else:
        middle_index = len(text) // 2

        first_half = text[:middle_index]
        second_half = text[middle_index:]
        if len(second_half) > len(first_half):
            first_half = text[:middle_index + 1]
            second_half = text[middle_index + 1:]

    text = []
    text.extend(second_half)
    text.extend(first_half)
    print(text)
    print(middle_index)