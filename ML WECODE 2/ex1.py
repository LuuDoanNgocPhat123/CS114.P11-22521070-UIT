import math 
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_goldbach_pairs(n):
    if n <= 2 or n % 2 != 0:
        return 0 
    count = 0
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            count += 1
    return count

n = int(input())

result = count_goldbach_pairs(n)

print(result)

    