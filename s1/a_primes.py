from ib111 import week_01
from math import isqrt


# Napište čistou funkci ‹nth_smallest_prime_divisor›, která vrátí ‹index›-té
# nejmenší prvočíslo vyskytující se v prvočíselném rozkladu čísla ‹num›.
# Pokud se v rozkladu vyskytuje některé prvočíslo vícekrát, počítáme všechny
# jeho výskyty, tedy např. v čísle ⟦2 · 2 · 3 · 3 · 3 · 5 = 540⟧ je třetím
# nejmenším prvočíslem číslo 3. Pokud má ‹num› méně než ‹index› prvočísel
# v rozkladu, funkce vrátí ‹None›.
#
# Předpokládejte, že ‹num› i ‹index› jsou kladná celá čísla.
# Zde indexujeme od 1, tedy první prvočíslo v rozkladu má ‹index› 1.
#
# Je potřeba, aby vaše funkce fungovala rozumně rychle i pro velmi velká
# čísla, u nichž je hledané prvočíslo malé. (Není třeba vymýšlet zvláště
# chytrá řešení, jen je třeba nedělat zbytečnou práci navíc.)

def nth_smallest_prime_divisor(num, index):
    i = 2
    curent_index = 0
    while i <= num:
        is_prime = True
        square = isqrt(i) + 1
        for j in range(2, square):
            if i % j == 0:
                is_prime = False
                break

        if is_prime and num % i == 0:
            num //= i
            curent_index += 1
            if curent_index == index:
                return i
            i = 2
        else:
            i += 1
    return None


def main():
    # print(nth_smallest_prime_divisor(20, 1))
    assert nth_smallest_prime_divisor(20, 1) == 2
    assert nth_smallest_prime_divisor(42350, 2) == 5
    assert nth_smallest_prime_divisor(42350, 3) == 5
    assert nth_smallest_prime_divisor(42350, 4) == 7
    assert nth_smallest_prime_divisor(42350, 7) is None


if __name__ == '__main__':
    main()
