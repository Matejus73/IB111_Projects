from ib111 import week_02  # noqa


# Napište funkci, která najde celé číslo ‹x›, které leží mezi
# hodnotami ‹low› a ‹high› (včetně), a pro které vrátí funkce ‹poly›
# maximální hodnotu (tzn. libovolné ⟦x⟧ takové, že pro všechny ⟦x'⟧
# platí ⟦f(x) ≥ f(x')⟧, kde ⟦f⟧ je funkce, kterou počítá podprogram
# ‹poly›).
# Pozor: definice funkce ‹poly› se může změnit! Vaše řešení by tedy
# nemělo nijak záviset na konkrétní definici funkce ‹poly›.

def poly(x):
    return 10 + 30 * x - 15 * x ** 3 + x ** 5


def maximum(low, high):
    top = low
    for i in range(low, high + 1):
        if poly(i) > poly(top):
            top = i

    return top


def main():
    assert maximum(0, 5) == 5
    assert maximum(0, 2) == 1
    assert maximum(-5, -1) == -3
    assert maximum(-2, 2) == -2
    assert maximum(-10, 10) == 10


if __name__ == "__main__":
    main()
