# Задание 4:
# Дан список  целых чисел:
# numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
# Создайте новый лист и замените отрицательные числа на -1, положительные на число 1, ноль оставить без изменения.

numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
new_numbers = []
for i in numbers:
    if i < -1:
        i = -1
        new_numbers.append(i)
    elif i > 1:
        i = 1
        new_numbers.append(i)
    else:
        i = i
        new_numbers.append(i)
print(new_numbers)