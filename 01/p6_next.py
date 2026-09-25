from ib111 import week_01  # noqa
import math

# Napište funkci, která pro zadané celé číslo ‹number›
# najde nejbližší větší číslo, které je násobkem kladného
# celého čísla ‹k›.


def next_multiple(number, k):
    return (number // k + 1) * k

# Dále napište funkci, která pro zadané kladné celé číslo
# ‹number› najde nejbližší větší prvočíslo.


def prime(number):
    if number < 2:
        return False
    elif number == 2 or number == 3:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, math.isqrt(number) + 1, 2):
            if number % i == 0:
                return False
    return True


def next_prime(number):
    if number < 2:
        return 2
    number += 1
    if number > 2 and number % 2 == 0:
        number += 1
    while not prime(number):
        number += 2
    return number


def main():
    assert next_multiple(1, 2) == 2
    assert next_multiple(10, 7) == 14
    assert next_multiple(10, 5) == 15
    assert next_multiple(54, 6) == 60
    assert next_multiple(131, 29) == 145
    assert next_multiple(123, 112) == 224
    assert next_multiple(423, 90) == 450

    assert next_prime(1) == 2
    assert next_prime(2) == 3
    assert next_prime(3) == 5
    assert next_prime(4) == 5
    assert next_prime(11) == 13
    assert next_prime(12) == 13
    assert next_prime(13) == 17


if __name__ == "__main__":
    main()