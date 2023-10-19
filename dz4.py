# Задание 1

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

sum_even = 0
sum_odd = 0
sum_div_9 = 0
count_even = 0
count_odd = 0
count_div_9 = 0

for num in range(start, end + 1):
    if num % 2 == 0:  # Проверка на четность
        sum_even += num
        count_even += 1
    else:
        sum_odd += num
        count_odd += 1
    if num % 9 == 0:  # Проверка на кратность 9
        sum_div_9 += num
        count_div_9 += 1

if count_even > 0:
    avg_even = sum_even / count_even
else:
    avg_even = 0

if count_odd > 0:
    avg_odd = sum_odd / count_odd
else:
    avg_odd = 0

if count_div_9 > 0:
    avg_div_9 = sum_div_9 / count_div_9
else:
    avg_div_9 = 0

print(f"Сумма четных чисел: {sum_even}")
print(f"Сумма нечетных чисел: {sum_odd}")
print(f"Сумма чисел, кратных 9: {sum_div_9}")
print(f"Среднеарифметическое четных чисел: {avg_even}")
print(f"Среднеарифметическое нечетных чисел: {avg_odd}")
print(f"Среднеарифметическое чисел, кратных 9: {avg_div_9}")

# Задание 2

length = int(input("Введите длину линии: "))
symbol = input("Введите символ для заполнения линии: ")

# Отображаем вертикальную линию
for i in range(length):
    print(symbol)

# Задание 3

while True:
    number = float(input("Введите число: "))
    
    if number > 0:
        print("Number is positive")
    elif number < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")
    
    if number == 7:
        print("Good bye!")
        break

# Задание 4

sum_numbers = 0
max_number = float('-inf')
min_number = float('inf')

while True:
    number = float(input("Введите число: "))
    
    if number == 7:
        print("Good bye!")
        break
    
    sum_numbers += number
    
    if number > max_number:
        max_number = number
    
    if number < min_number:
        min_number = number

# Выводим результаты
print(f"Сумма введенных чисел: {sum_numbers}")
print(f"Максимальное число: {max_number}")
print(f"Минимальное число: {min_number}")

