import math


def prime_num(n):
    for i in range(1, n + 1):
        if is_prime(i):
            print(f"{i} is a prime number")


def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


# lambda where x: is an argument and x * x is a return expression. This is a lambda function.
