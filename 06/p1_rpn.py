from ib111 import week_06  # noqa


# Napište (čistou) funkci, která na vstupu dostane:
#
#  • neprázdný výraz ‹expr› složený z proměnných a z aritmetických
#    operátorů, zapsaný v postfixové notaci, a
#  • slovník, přiřazující proměnným číselnou hodnotu (můžete se
#    spolehnout, že všechny proměnné použité v daném výrazu jsou
#    v tomto slovníku obsaženy),
#
# a vrátí číslo, na které se daný výraz vyhodnotí. Každý operátor
# nebo proměnná je samostatný řetězec, celý výraz je pak tvořen
# posloupností těchto řetězců. Povolené operátory jsou pouze ‹+› a
# ‹*›. Vstupní podmínkou je, že výraz ‹expr› je správně utvořený.

# Postfixová notace funguje následovným způsobem:
#
#  • výraz čteme zleva doprava, přitom si každou hodnotu zapíšeme,
#  • narazíme-li na operátor, např. ‹+›:
#    ◦ v hlavě sečteme poslední dvě hodnoty, které jsme napsali,
#    ◦ tyto hodnoty smažeme,
#    ◦ zapíšeme místo nich součet, který jsme si zapamatovali.
#
# Tento postup opakujeme, až dokud nepřečteme celý výraz. Je-li
# výraz správně utvořený, na konci tohoto procesu máme zapsané
# jediné číslo. Toto číslo je výsledkem vyhodnocení zadaného výrazu.

def rpn_eval(expr: list[str], variables: dict[str, int]) -> int:
    num_list = []

    for i in expr:

        if i != "+" and i != "*":
            num_list.append(variables[i])
        else:
            num_list_len = len(num_list)

            if i == "+":
                new_num = num_list[num_list_len - 1] +\
                    num_list[num_list_len - 2]

            elif i == "*":
                new_num = num_list[num_list_len - 1] *\
                    num_list[num_list_len - 2]

            num_list.pop()
            num_list.pop()
            num_list.append(new_num)

    return num_list[0]


def main() -> None:
    assert rpn_eval(["a"], {"a": 5}) == 5
    assert rpn_eval(["a", "b", "+"], {"a": 1, "b": -4}) == -3
    assert rpn_eval(["x", "y", "+"], {"x": 1, "y": 2}) == 3
    assert rpn_eval(["x", "y", "+", "y", "*", "z", "+"],
                    {"x": 5, "y": 2, "z": 25}) == 39
    assert rpn_eval(["x", "x", "*", "x", "*"],
                    {"x": 5}) == 125
    assert rpn_eval(["a", "a", "a", "a", "a", "a", "+", "+", "+",
                     "+", "+"], {"a": 1}) == 6


if __name__ == '__main__':
    main()
