from ib111 import week_02  # noqa


# Implementujte funkci ‹power_digit_sum›, která vrátí „speciální“
# ciferný součet čísla ‹number›, který se od běžného ciferného
# součtu liší tím, že každou cifru před přičtením umocníme na číslo
# její pozice. Pozice číslujeme zleva, přičemž první má číslo 1.
# Vstupem funkce ‹power_digit_sum› bude libovolné nezáporné celé
# číslo, na výstupu se očekává celé číslo. Výpočet budeme provádět
# v číselné soustavě se základem 7.

# Příklad: Číslo ⟦1234⟧ zapíšeme v sedmičkové soustavě jako
# ⟦(3412)₇⟧ – skutečně, ⟦3⋅7³ + 4⋅7² + 1⋅7¹ + 2⋅7⁰ = 1029 + 196 + 7
# + 2 = 1234⟧.  Proto ‹power_digit_sum(1234)› získáme jako ⟦3¹ + 4²
# + 1³ + 2⁴ = 36⟧.

# Napište funkci, která vytvoří číslo zřetězením ‹count› po sobě
# jdoucích kladných čísel počínaje zadaným číslem ‹start›.  Tato
# čísla zřetězte vyjádřená v binární soustavě. Například volání
# ‹joined(1, 3)› zřetězí sekvenci ⟦(1)₂ = 1⟧, ⟦(10)₂ = 2⟧, ⟦(11)₂ = 3⟧
# a vrátí číslo ⟦(11011)₂ = 27⟧. V Pythonu lze binární čísla přímo
# zapisovat v tomto tvaru: ‹0b11011› (podobně lze stejné číslo
# zapsat v šestnáctkové soustavě zápisem ‹0x1b› nebo osmičkové jako
# ‹0o33›).

def joined(start, count):
    result = 0

    for i in range(start, start + count):
        bitCount = 1
        bitNum = i
        while bitNum > 0:
            bitCount *= 2
            bitNum //= 2
        result = result * bitCount + i

    return result


def power_digit_sum(number):
    number7 = 0
    while number >= 1:
        number7 *= 10
        number7 += number % 7
        number //= 7

    i = 1
    suma = 0
    while number7 >= 1:
        suma += (number7 % 10) ** i
        number7 //= 10
        i += 1
    return suma


def main() -> None:
    assert power_digit_sum(7) == 1
    assert power_digit_sum(1234) == 36
    assert power_digit_sum(333) == 95
    assert power_digit_sum(52891) == 46693


if __name__ == "__main__":
    main()