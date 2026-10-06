from ib111 import week_03  # noqa


# Napište (čistou) funkci, která pro zadaný seznam nezáporných čísel
# ‹data› vrátí nový seznam obsahující dvojice – číslo a jeho
# četnost. Výstupní seznam musí být seřazený vzestupně dle první
# složky. Můžete předpokládat, že v ‹data› se nachází pouze celá
# čísla z rozsahu [0, 100] (včetně).

def histogram(data):
    result = []
    counted_nums = 0
    instances = 0

    for i in range(0, 101):
        for j in data:
            if j == i:
                instances += 1
                counted_nums += 1

        if instances != 0:
            package = i, instances
            result.append(package)
            instances = 0

        if counted_nums == len(data):
            break

    return result


def main() -> None:
    assert histogram([1, 2, 3, 2, 1]) == [(1, 2), (2, 2), (3, 1)]
    assert histogram([7, 1, 7, 1, 5]) == [(1, 2), (5, 1), (7, 2)]
    assert histogram([1, 1, 1]) == [(1, 3)]
    assert histogram([]) == []


if __name__ == "__main__":
    main()
