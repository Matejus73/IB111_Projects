from ib111 import week_01  # noqa
import math

# Napište funkci ‹largest_triple›, která najde pythagorejskou
# trojici ⟦(a, b, c)⟧ – totiž takovou, že ⟦a⟧, ⟦b⟧ a ⟦c⟧ jsou
# přirozená čísla a platí ⟦a² + b² = c²⟧ (tzn. tvoří pravoúhlý
# trojúhelník). Hledáme trojici, která:
#
#  1. má největší možný součet ⟦a + b + c⟧,
#  2. hodnoty ⟦a⟧, ⟦b⟧ jsou menší než ‹max_side›.
#
# Výsledkem funkce bude součet ⟦a + b + c⟧, tedy největší možný
# obvod pravoúhlého trojúhelníku, jsou-li obě jeho odvěsny kratší
# než ‹max_side›. Předpokládejte, že ‹max_side› bude vždy alespoň 5.


def largest_triple(max_side):
    max_o = 0

    for a in range(max_side - 1, 1, -1):
        for b in range(max_side - 1, a + 1, -1):
            c = math.sqrt(a ** 2 + b ** 2)
            if max(a, b, c) < max_side:
                break
            if round(c) == c and a + b + c > max_o:
                max_o = a + b + c
    return max_o


def main():
    assert largest_triple(10) == 24
    assert largest_triple(25) == 72
    assert largest_triple(100) == 288
    assert largest_triple(150) == 490
    assert largest_triple(1000) == 3290


if __name__ == "__main__":
    main()