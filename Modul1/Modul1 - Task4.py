# Задание №4:
# Создайте input() который принимает от пользователя дату в формате: "2020-10-24 18:30" и возвращает dictionary разделённую по значениям даты:

# date = {
# "year": "2020",
# "month": "10",
# .....
# }

import re
today = input('Введите дату в формате "yyyy-mm-dd hh:mm": ')

today = re.split('[- ]', today)
print(today)
format_today = ['year', 'month', 'day', 'hour']
date = dict(zip(format_today, today))
print(date)
