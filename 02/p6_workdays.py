from ib111 import week_02  # noqa


# Napište funkci, která zjistí, kolik bude pracovních dnů v roce
# ‹year›. Dny v týdnu mají hodnoty 0–6 počínaje pondělím s hodnotou 0.
# Předpokládejte, že ‹year› je větší než 1600.

# České státní svátky jsou:
#
# │  datum │ svátek                                         │
# ├┄┄┄┄┄┄┄▻┼◅┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄│
# │   1.1. │ Den obnovy samostatného českého státu          │
# │      — │ Velký pátek                                    │
# │      — │ Velikonoční pondělí                            │
# │   1.5. │ Svátek práce                                   │
# │   8.5. │ Den vítězství                                  │
# │   5.7. │ Den slovanských věrozvěstů Cyrila a Metoděje   │
# │   6.7. │ Den upálení mistra Jana Husa                   │
# │  28.9. │ Den české státnosti                            │
# │ 28.10. │ Den vzniku samostatného československého státu │
# │ 17.11. │ Den boje za svobodu a demokracii               │
# │ 24.12. │ Štědrý den                                     │
# │ 25.12. │ 1. svátek vánoční                              │
# │ 26.12. │ 2. svátek vánoční                              │

# Přestupné roky: v některých letech se na konec února přidává 29.
# den. Jsou to roky, které jsou dělitelné čtyřmi, s výjimkou těch,
# které jsou zároveň dělitelné 100 a nedělitelné 400.

# Čistou funkci ‹first_day› můžete použít k tomu, abyste zjistili,
# na který den v týdnu padne 1. leden daného roku. Např.
# ‹first_day(2001)› vrátí nulu, protože rok 2001 začínal pondělím.

def first_day(year):
    assert 1601 <= year
    years = year - 1601
    offset = years + years // 4 - years // 100 + years // 400
    return offset % 7


def workdays(year):
    day = first_day(year)
    work = 0
    for i in range(1, 13):
        if i == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            month_day = 29
        elif i == 2:
            month_day = 28
        elif i == 4 or i == 6 or i == 9 or i == 11:
            month_day = 30
        else:
            month_day = 31

        for j in range(1, month_day + 1):
            if (day <= 4
                and (j != 1 or i != 1)
                and (j != 1 or i != 5)
                and (j != 8 or i != 5)
                and (j != 5 or i != 7)
                and (j != 6 or i != 7)
                and (j != 28 or i != 9)
                and (j != 28 or i != 10)
                and (j != 17 or i != 11)
                and (j != 24 or i != 12)
                and (j != 25 or i != 12)
                and (j != 26 or i != 12)
            ):
                work += 1
            if day < 6:
                day += 1
            else:
                day = 0
    return work - 2


def main():
    assert workdays(2020) == 251
    assert workdays(2021) == 252
    assert workdays(2016) == 252
    assert workdays(2004) == 253
    assert workdays(1993) == 252
    assert workdays(1991) == 251
    assert workdays(1990) == 250
    assert workdays(1900) == 250
    assert workdays(2000) == 250
    assert workdays(1996) == 252


if __name__ == "__main__":
    main()
