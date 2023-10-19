# Задание первое
print(eval(input("Введите первое число : ") + input("Введите действие : ") + input("Введите второе число : ") ))

# Задача 2
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

print((a + b + c) / 3)


# Задача 3
meters = float(input("Введите количество метров: "))

unit = input("Введите 'мили', 'дюймы' или 'ярды' для выполнения соответствующего преобразования: ")

METERS_TO_MILES = 0.000621371
METERS_TO_INCHES = 39.3701
METERS_TO_YARDS = 1.09361

if unit == 'мили':
    result = meters * METERS_TO_MILES
    print(f"{meters} метров = {result} миль")
elif unit == 'дюймы':
    result = meters * METERS_TO_INCHES
    print(f"{meters} метров = {result} дюймов")
elif unit == 'ярды':
    result = meters * METERS_TO_YARDS
    print(f"{meters} метров = {result} ярдов")
else:
    print("Неверный выбор единицы измерения. Пожалуйста, введите 'мили', 'дюймы' или 'ярды'.")


