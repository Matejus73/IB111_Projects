from ib111 import week_06  # noqa


# Dané přirozené číslo je «b–šťastné» platí-li, že nahradíme-li jej
# součtem druhých mocnin jeho cifer, vyjádřených v poziční soustavě
# se základem ‹b›, a tento postup budeme dále opakovat na takto
# vzniklém čísle, po konečném počtu kroků dostaneme číslo 1.

# Například číslo 3 je 4–šťastné, protože:
#
#  • ⟦3 = (3)₄⟧
#  • ⟦3² = 9 = (21)₄⟧
#  • ⟦2² + 1² = 5 = (11)₄⟧
#  • ⟦1² + 1² = 2 = (2)₄⟧
#  • ⟦2² = 4 = (10)₄⟧
#  • ⟦1² + 0² = 1⟧.
#
# Číslo 2 není 5–šťastné:
#
#  • ⟦2 = (2)₅⟧
#  • ⟦2² = 4 = (4)₅⟧
#  • ⟦4² = 16 = (31)₅⟧
#  • ⟦3² + 1² = 10 = (20)₅⟧
#  • ⟦2² + 0² = 4⟧
#
# a protože se nám ve výpočtu číslo 4 zopakovalo, nemůžeme již dojít
# k výsledku 1.

# Napište predikát, který o číslu ‹number› rozhodne, je-li
# ‹base›-šťastné.

def to_base(number, base) -> list[int]:
    num_in_base = []
    while number > 0:
        num_in_base.append(number % base)
        number //= base
    return num_in_base


def digit_sqr(num_in_base) -> int:
    suma = 0
    for i in num_in_base:
        suma += i ** 2

    return suma


def is_b_happy(number: int, base: int) -> bool:
    current_num = to_base(number, base)
    check_set = []

    while current_num != [1]:
        check_set.append(current_num)
        current_num = to_base(digit_sqr(current_num), base)
        if current_num in check_set:
            return False
    return True


def main() -> None:
    assert is_b_happy(3, 4)
    assert is_b_happy(11, 11)
    assert is_b_happy(19, 10)
    assert is_b_happy(347, 6)
    assert is_b_happy(123456, 4)
    assert is_b_happy(7, 10)

    assert not is_b_happy(2, 5)
    assert not is_b_happy(20, 6)
    assert not is_b_happy(100, 5)
    assert not is_b_happy(125, 10)
    assert not is_b_happy(40, 10)
    assert not is_b_happy(8, 6)
    assert not is_b_happy(15, 16)


if __name__ == '__main__':
    main()
