from ib111 import week_02  # noqa


# Napište predikát ‹is_visa›, který je pravdivý, reprezentuje-li
# číslo ‹number› platné číslo platební karty VISA, tj. začíná
# cifrou 4, má 13, 16, nebo 19 cifer a zároveň je platným číslem
# platební karty. Číslo platební karty ověříte podle Luhnova
# algoritmu (stejně jako v příkladu p5_credit):
#
#  1. zdvojnásobte hodnotu každé druhé cifry zprava; je-li výsledek
#     větší než 9, odečtěte od něj hodnotu 9,
#  2. sečtěte všechna takto získaná čísla a cifry na lichých
#     pozicích zprava (kromě první cifry zprava, která slouží jako
#     kontrolní součet),
#  3. číslo karty je platné právě tehdy, je-li po přičtení kontrolní
#     cifry celkový součet dělitelný 10.
#
# Například pro číslo 28316 je kontrolní cifra 6 a součet je: ⟦2 +
# (2⋅8 - 9) + 3 + 2⋅1 = 2 + 7 + 3 + 2 = 14⟧. Po přičtení kontrolní
# cifry je celkový součet ⟦20⟧. Protože je beze zbytku dělitelný
# deseti, číslo karty je platné.

def is_visa(number):
    pass


# Dále napište predikát ‹is_mastercard›, který je pravdivý,
# reprezentuje-li číslo ‹number› platné číslo platební karty
# MasterCard, tj. začíná prefixem 50–55, nebo 22100–27209, má 16
# cifer a zároveň je platným číslem platební karty.

def is_mastercard(number):
    pass


def main():
    assert is_visa(4111111111111111)
    assert is_visa(4012888888881881)
    assert is_visa(4988438843884305)
    assert is_visa(4646464646464644)
    assert is_visa(4199350000000002)
    assert is_visa(4222222222222)
    assert is_visa(4111111111111111110)

    assert not is_visa(411111111111116)
    assert not is_visa(5500000000000004)
    assert not is_visa(4929300836739328)

    assert is_mastercard(5500000000000004)
    assert is_mastercard(5555555555554444)
    assert is_mastercard(5105105105105100)
    assert is_mastercard(5424000000000015)
    assert is_mastercard(2223520443560010)
    assert is_mastercard(5101180000000007)
    assert is_mastercard(2222400070000005)

    assert not is_mastercard(4012888888881881)
    assert not is_mastercard(22004000700000003)
    assert not is_mastercard(5624000000000013)
    assert not is_mastercard(2721000030000016)
    assert not is_mastercard(5101180000000000003)


if __name__ == "__main__":
    main()
