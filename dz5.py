# Задание 1

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

prime_numbers = find_primes(start, end)

print("Простые числа в указанном диапазоне:")
for prime in prime_numbers:
    print(prime)

# Задание 2

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")

# Задание 3

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

for i in range(start, end + 1):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}", end="\t")
    print()


