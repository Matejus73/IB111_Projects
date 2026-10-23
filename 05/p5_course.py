from ib111 import week_05  # noqa

# Známky studentů z jednoho předmětu jsou uloženy ve slovníku, kde
# klíčem je UČO studenta a hodnotou je známka zadaná jako písmeno nebo '-'.
# Možná hodnocení jsou 'A' až 'F', dále, 'N', 'P', 'X', 'Z' a '-'.

# Napište čistou funkci ‹modus›, jejímž vstupem bude slovník známek
# a výstupem bude jejich modus, tedy nejčastější hodnota.
# Předpokládejte, že známek se stejnou četností může být více, takže
# funkce bude vždy vracet množinu známek, a to i v případě, že je
# nejčastější hodnota určena jednoznačně. V případě, že je vstupní
# slovník prázdný, bude výstupem prázdná množina.


def modus(marks: dict[int, str]) -> set[str]:
    mod_set: set[str] = set()
    max_count = 0
    for mark in marks.values():
        count = 0
        for mark_check in marks.values():
            if mark_check == mark:
                count += 1

        if count > max_count:
            max_count = count
            mod_set = set()
            mod_set.add(mark)
        elif count == max_count:
            mod_set.add(mark)

    return mod_set

# Dále napište predikát ‹check›, který ověří, že známky jsou
# smysluplné, tedy že odpovídají buďto předmětu ukončenému zkouškou
# (známky 'A' - 'F', nebo 'X'), kolokviem (známky 'P' nebo 'N'),
# anebo zápočtem (známky 'Z' nebo 'N'). Hodnocení '-' je možné
# u jakéhokoliv způsobu hodnocení. Klasifikované zápočty
# neuvažujeme.


def check(marks: dict[int, str]) -> bool:
    zk_marks = ["A", "B", "C", "D", "E", "F", "X", "-"]
    kol_marks = ["P", "N", "-"]
    zap_marks = ["Z", "N", "-"]
    zk_count = 0
    kol_count = 0
    zap_count = 0
    for mark in marks.values():
        for i in zk_marks:
            if i == mark:
                zk_count += 1

        for i in kol_marks:
            if i == mark:
                kol_count += 1

        for i in zap_marks:
            if i == mark:
                zap_count += 1

    return zk_count == len(marks) or\
        kol_count == len(marks) or\
        zap_count == len(marks)


def main() -> None:
    assert modus({}) == set()
    assert modus({100000: 'P'}) == {'P'}
    assert modus({100000: 'A', 100001: 'B', 100002: 'A'}) == {'A'}
    assert modus({100000: 'A', 100001: 'B', 100002: 'A', 100003: 'B'}) \
           == {'A', 'B'}
    assert check({})
    assert check({100000: 'P'})
    assert check({100000: '-'})
    assert check({100000: 'A', 100001: 'B', 100002: 'A'})
    assert check({100000: 'A', 100001: 'B', 100002: 'A', 100003: 'B'})
    assert not check({100000: 'A', 100001: 'B', 100002: 'A', 100003: 'N'})
    assert not check({100000: 'P', 100001: 'N', 100002: 'Z', 100003: '-'})


if __name__ == "__main__":
    main()
