from ib111 import week_03  # noqa


# V úloze ‹02/fraction.py› jsme se již setkali s řetězovými zlomky.
# Řetězový zlomek je forma reprezentace čísla jako součet celého
# čísla ⟦a₀⟧ a převrácené hodnoty jiného čísla, které opět
# reprezentujeme součtem celého čísla ⟦a₁⟧ a další převrácené
# hodnoty. Celá čísla ⟦aₙ⟧ postupně tvoří řadu koeficientů
# řetězového zlomku.

# Například řetězový zlomek ⟦4 + (1 / (2 + 1 / (6 + (1/7))))⟧
# reprezentuje číslo ⟦415/93⟧ a jeho koeficienty jsou 4, 2, 6 a 7.

# Koeficienty řetězového zlomku pro číslo ⟦n⟧ můžete získat
# iterativním postupem:
#
#  1. Rozdělte číslo ⟦n⟧ na jeho celočíselnou část ⟦p⟧ a zlomkovou
#     část ⟦q⟧. Číslo ⟦p⟧ přímo udává první koeficient posloupnosti,
#     tzn. ⟦a₀⟧, zbytek koeficientů je odvozen od ⟦q⟧ (viz další krok).
#     Posloupnost má tedy tvar: ⟦p; a₁, a₂, a₃,…⟧.
#
#  2. Pro získání dalšího koeficientu opakujte 1. krok s převrácenou
#     hodnotou zlomkové části ⟦(1/q)⟧.

# V této úloze s řetězovým zlomky budeme pokračovat. Tentokrát implementujeme
# převod opačným směrem, na vstupu bude seznam koeficientů řetězového zlomku
# a výstupem bude zlomek klasický.

# Naprogramujte tedy čistou funkci ‹continued_fraction›, která dostane jako
# parametr seznam koeficientů a vrátí zlomek ve tvaru ‹(numerator,
# denominator)›.

def continued_fraction(coefficients):
    denom = coefficients[len(coefficients) - 2]
    nom = coefficients[len(coefficients) - 1]
    remain = 1
    for i in range(len(coefficients), 1, -1):

        denom = denom * nom + remain
        remain = nom
        nom = denom
        denom = coefficients[i - 3]

    return nom, remain


def main():
    assert continued_fraction([4, 2, 6, 7]) == (415, 93)
    assert continued_fraction([3, 4, 12, 4]) == (649, 200)
    assert continued_fraction([0, 2, 4]) == (4, 9)


if __name__ == "__main__":
    main()
