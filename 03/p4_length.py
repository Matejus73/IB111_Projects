from ib111 import week_03  # noqa
from math import isclose, sqrt


# Napište čistou funkci, která dostane na vstup seznam bodů v rovině
# (tj. seznam dvojic čísel) a vrátí délku lomené čáry, která těmito
# body prochází (tzn. takové, která vznikne spojením každých dvou
# sousedních bodů seznamu úsečkou). Souřadnice i délky
# reprezentujeme čísly s plovoucí desetinnou čárkou (typ ‹float›).

# Například seznam ‹[(0, 0), (1, 0), (1, 1), (2, 1)]› definuje tuto
# lomenou čáru:
#
#       (1, 1) ┌───▶(2, 1)
#              │
#    (0, 0)╶───┘(1, 0)
#
# složenou ze tří segmentů (úseček) velikosti 1. Její délka je 3.

def length(points):
    line = 0

    if len(points) != 0:
        previous = points[0]

        for i in range(1, len(points)):
            x1, y1 = previous
            x2, y2 = points[i]

            if x2 == x1:
                line += abs(y2 - y1)
            elif y2 == y1:
                line += abs(x2 - x1)
            else:
                x2 -= x1
                y2 -= y1
                line += sqrt(x2 ** 2 + y2 ** 2)

            previous = points[i]

    return line


def main():
    assert isclose(length([(0.0, 0.0), (1.0, 0.0)]), 1.0)
    assert isclose(length([(3.0, 0.0), (0.0, 4.0)]), 5.0)
    assert isclose(length([(0.0, 1.0), (1.0, 1.0), (1.0, 2.0)]), 2.0)
    assert isclose(length([(0.0, 0.0)]), 0.0)
    assert isclose(length([]), 0.0)
    assert isclose(length([(3.0, 5.0), (3.0, 15.0), (4.0, 15.0),
                           (4.0, 0.0), (0.0, 0.0)]), 30.0)
    assert isclose(length([(0.0, 0.0), (3.0, 4.0)]), 5.0)
    assert isclose(length([(0.0, 0.0), (3.0, 4.0), (3.0, 7.0)]), 8.0)


if __name__ == "__main__":
    main()
