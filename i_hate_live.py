def euler_phi(n):
    result = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
        i += 1
    if n > 1:
        result -= result // n
    return result

def count_coprime_pairs(n):
    pairs_count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            pairs_count += euler_phi(i) * (n // i)

    return pairs_count // 2

n = int(input())

result = count_coprime_pairs(n)

print(result)

# second

def sum_of_divisors(n):
    divisor_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:
                divisor_sum += n // i
    return divisor_sum

def find_friendly_numbers(k):
    friendly_pairs = []
    for n in range(2, k + 1):
        m = sum_of_divisors(n)
        if m > n and sum_of_divisors(m) == n:
            friendly_pairs.append((n, m))
    return friendly_pairs

k = int(input())

friendly_numbers = find_friendly_numbers(k)
for pair in friendly_numbers:
    print(*pair)
