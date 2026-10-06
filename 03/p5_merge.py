from ib111 import week_03  # noqa


# Naprogramujte (čistou) funkci, která ze dvou vzestupně seřazených
# seznamů čísel ‹a›, ‹b› vytvoří nový vzestupně seřazený seznam,
# který bude obsahovat všechny prvky z ‹a› i ‹b›. Nezapomeňte, že
# nesmíte modifikovat vstupní seznamy (jinak by funkce nebyla
# čistá). Pokuste se funkci naprogramovat «efektivně».

def merge(a, b):
    result = []
    index_a = 0
    index_b = 0

    for i in range(len(a)+len(b)):
        if index_a == len(a):
            result.append(b[index_b])
            index_b += 1
            continue

        if index_b == len(b):
            result.append(a[index_a])
            index_a += 1
            continue

        if a[index_a] <= b[index_b]:
            result.append(a[index_a])
            index_a += 1
        else:
            result.append(b[index_b])
            index_b += 1

    return result


def main():
    assert merge([1, 2, 3], [1, 2, 3]) == [1, 1, 2, 2, 3, 3]
    assert merge([0, 2, 4, 6, 8], [1, 3, 5, 7, 9]) \
        == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert merge([], []) == []
    assert merge([], [1, 2]) == [1, 2]
    assert merge([1, 2], []) == [1, 2]
    assert merge([1, 5, 10], [-1, 2, 3, 4, 6, 10, 11]) \
        == [-1, 1, 2, 3, 4, 5, 6, 10, 10, 11]


if __name__ == "__main__":
    main()
