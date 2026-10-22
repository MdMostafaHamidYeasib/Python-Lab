def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
total = 0
for num in range(2, 1000):
    if is_prime(num):
        total = total + num
print("Sum of primes below 1000 =", total)