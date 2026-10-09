from ib111 import week_03  # noqa


# «FreeCell¹» je pasiánsová karetní hra, kterou možná znáte jako součást
# operačních systémů jisté společnosti se sídlem v Redmondu. Ve hře se používá
# klasický balíček 52 karet se čtyřmi barvami (suits) a třinácti hodnotami
# (ranks) od esa po krále. Hrací pole obsahuje:
#
# • volná pole (cells) – typicky čtyři, ve variantách jedno až deset,
# • domácí pole (foundations) – vždy přesně čtyři, do každého z nich se
#   odkládají karty ve stejné barvě, postupně od esa po krále,
# • sloupce (cascades) – typicky osm, ve variantách čtyři až deset;
#   do sloupců se na začátku rozdají všechny karty.
#
# ¹ ‹https://en.wikipedia.org/wiki/FreeCell›
#
# Povolené přesuny karet jsou následující:
#
# • je možno přesouvat karty z volných polí a spodní karty sloupců;
# • na prázdné volné pole a do prázdného sloupce je možno položit libovolnou
#   kartu;
# • na prázdné domácí pole je možno položit eso libovolné barvy;
# • na kartu v domácím poli je možno položit kartu stejné barvy s hodnotou
#   přesně o jednu vyšší;
# • na spodní kartu sloupce je možno položit další kartu, pokud je její
#   hodnota přesně o jednu nižší a pokud se její barva liší (ve smyslu
#   červená / černá).
#
# Karty budeme reprezentovat jako dvojice ‹(rank, suit)›, kde rank je
# jedno z čísel 1 až 13 (pro karty s hodnotami 1, 11, 12, 13 máme níže
# zavedeny konstanty) a suit je jedno z čísel 0 až 3 (postupně reprezentující
# srdce, kára, piky a kříže; níže opět reprezentované konstantami).
# Zde uvedené konstanty nijak neměňte.

ACE, JACK, QUEEN, KING = 1, 11, 12, 13
HEARTS, DIAMONDS, CLUBS, SPADES = 0, 1, 2, 3


# Implementujte predikát ‹can_move›, tj. jestli je v zadané situaci možné
# provést přesun nějaké karty. Situace je reprezentována třemi seznamy,
# jejichž prvky jsou buď karty nebo ‹None›.
#
# • ‹cascades› je seznam spodních karet sloupců (‹None› je prázdný sloupec),
# • ‹cells› je seznam karet na volných polích (‹None› je prázdné pole),
# • ‹foundation› je seznam horních karet na domácích polích (‹None› je opět
#   prázdné pole).
#
# Předpokládejte, že vstupní situace je skutečnou situací ve hře (např. není
# možné, aby se někde objevila stejná karta dvakrát).


def can_move(cascades, cells, foundation):

    # check for emptys
    has_any_card = False
    for i in cascades:
        if i is not None:
            has_any_card = True
            break

    if not has_any_card:
        for i in cells:
            if i is not None:
                has_any_card = True
                break

    for i in cascades:
        if i is None and has_any_card:
            return True

    for i in cells:
        if i is None and has_any_card:
            return True

    # checkin for aces
    for i in foundation:
        if i is None:
            for j in cascades:
                if j is not None:
                    rank, suit = j
                    if rank == ACE:
                        return True

            for j in cells:
                if j is not None:
                    rank, suit = j
                    if rank == ACE:
                        return True

    # check the cascades
    for i in cascades:
        if i is not None:
            rank_cascades, suit_cascades = i
            for j in cells:
                if j is not None:
                    rank_cells, suit_cells = j
                    if rank_cascades - rank_cells == 1:
                        if (suit_cascades == HEARTS or
                            suit_cascades == DIAMONDS) and\
                                (suit_cells == SPADES or
                                 suit_cells == CLUBS):
                            return True
                        elif (suit_cascades == SPADES or
                              suit_cascades == CLUBS) and\
                                (suit_cells == HEARTS or
                                 suit_cells == DIAMONDS):
                            return True

        for j in cascades:
            if j is not None:
                rank_cascades2, suit_cascades2 = j
                if rank_cascades - rank_cascades2 == 1:
                    if (suit_cascades == HEARTS or
                        suit_cascades == DIAMONDS) and\
                            (suit_cascades2 == SPADES or
                             suit_cascades2 == CLUBS):
                        return True
                    elif (suit_cascades == SPADES or
                          suit_cascades == CLUBS) and\
                            (suit_cascades2 == HEARTS or
                             suit_cascades2 == DIAMONDS):
                        return True

    # check the foundation
    for i in foundation:
        if i is not None:
            rank_foundation, suit_foundation = i
            for j in cells:
                if j is not None:
                    rank_cells, suit_cells = j
                    if rank_cells - rank_foundation == 1 and\
                            suit_foundation == suit_cells:
                        return True

            for j in cascades:
                if j is not None:
                    rank_cascades, suit_cascades = j
                    if rank_cascades - rank_foundation == 1 and\
                            suit_foundation == suit_cascades:
                        return True

    return False


def main():
    cascades = [(2, HEARTS), (3, HEARTS), (7, CLUBS), (8, CLUBS)]
    cells = [(2, CLUBS), (3, CLUBS), (7, CLUBS)]
    foundations = [None, None, None, None]
    assert can_move(cascades, cells, foundations)

    cells = [(2, DIAMONDS), (3, DIAMONDS), (4, DIAMONDS)]
    assert not can_move(cascades, cells, foundations)


if __name__ == '__main__':
    main()
