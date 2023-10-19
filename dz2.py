# Задача 1
day_number = int(input("Введите номер дня недели (1-7): "))

if day_number == 1:
    print("Понедельник")
elif day_number == 2:
    print("Вторник")
elif day_number == 3:
    print("Среда")
elif day_number == 4:
    print("Четверг")
elif day_number == 5:
    print("Пятница")
elif day_number == 6:
    print("Суббота")
elif day_number == 7:
    print("Воскресенье")
else:
    print("Неверный номер дня недели. Пожалуйста, введите число от 1 до 7.")

# Задание 4

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

# Проверяем, равны ли числа
if a == b:
    print("Введенные числа равны.")
else:
    min_number = min(a, b)
    max_number = max(a, b)
    print(f"Введенные числа в порядке возрастания: {min_number}, {max_number}")







