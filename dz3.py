# Задание 1
number = int(input("Введите число от 1 до 100: "))

if 1 <= number <= 100:
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
else:
    print("Ошибка: введите число от 1 до 100.")

# Задание 2


base = float(input("Введите число: "))

power = int(input("Введите степень (от 0 до 7): "))

if 0 <= power <= 7:
    result = base ** power
    print(f"Результат: {result}")
else:
    print("Ошибка: введите степень от 0 до 7.")

# Задание 4

sales_manager1 = float(input("Введите уровень продаж для первого менеджера: $"))
sales_manager2 = float(input("Введите уровень продаж для второго менеджера: $"))
sales_manager3 = float(input("Введите уровень продаж для третьего менеджера: $"))

def calculate_salary(sales):
    if sales <= 500:
        return 200 + 0.03 * sales
    elif 500 < sales <= 1000:
        return 200 + 0.05 * sales
    else:
        return 200 + 0.08 * sales

salary_manager1 = calculate_salary(sales_manager1)
salary_manager2 = calculate_salary(sales_manager2)
salary_manager3 = calculate_salary(sales_manager3)

print(f"Зарплата первого менеджера: ${salary_manager1:.2f}")
print(f"Зарплата второго менеджера: ${salary_manager2:.2f}")
print(f"Зарплата третьего менеджера: ${salary_manager3:.2f}")

best_manager = max(salary_manager1, salary_manager2, salary_manager3)
bonus = 200
best_manager += bonus

print(f"\nЛучший менеджер получает премию и его зарплата составляет ${best_manager:.2f}")

