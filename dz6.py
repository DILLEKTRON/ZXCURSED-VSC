# Задание 1

x = int(input("Введите целое число x: "))
y = int(input("Введите целое число y: "))

result = x ** y

print(f"{x} в степени {y} равно {result}")

# Задание 2

count = 0

for x in range(1, 10):
    for y in range(0, 10):
        if x != y:
            count += 3

print(f"Количество чисел с двумя одинаковыми цифрами: {count}")

# Задание 3

count = 0

for i in range(100, 10000):
    digits = set(str(i))  
    if len(digits) == len(str(i)):  
        count += 1

print(f"Количество чисел с разными цифрами: {count}")

# Задание 4

def remove_digits(number):
    result = ""
    for digit in str(number):
        if digit not in ['3', '6']:
            result += digit
    return result

user_input = int(input("Введите любое целое число: "))

new_number = remove_digits(user_input)

print(f"Число после удаления цифр 3 и 6: {new_number}")
