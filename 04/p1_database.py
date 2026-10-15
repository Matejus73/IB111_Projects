from ib111 import week_04  # noqa

# V této úloze budete pracovat s databázovou tabulkou. Tabulka je
# dvojice složená z «hlavičky» a seznamu «záznamů». «Hlavička»
# obsahuje seznam názvů sloupců. Jeden záznam je tvořen seznamem
# hodnot pro jednotlivé sloupce tabulky (pro jednoduchost uvažujeme
# jenom hodnoty typu řetězec). Ne všechny hodnoty v záznamech musí
# být vyplněny – v tom případě mají hodnotu ‹None›.


# Vaším úkolem bude nyní otypovat a implementovat následující
# funkce. Funkce ‹get_header› vrátí hlavičku tabulky ‹table›.

Records = list[list[str | None]]
Header = list[str]
Table = tuple[Header, Records]


def get_header(table: Table) -> Header:
    header, _ = table
    return header


# Funkce ‹get_records› vrátí seznam záznamů z tabulky ‹table›.

def get_records(table: Table) -> Records:
    _, records = table
    return records


# Procedura ‹add_record› přidá záznam ‹record› na konec tabulky
# ‹table›. Můžete předpokládat, že záznam ‹record› bude mít stejný
# počet sloupců jako tabulka. Návratovou hodnotou ať je ‹None›.

def add_record(record: list[str | None], table: Table) -> None:
    get_records(table).append(record)
    return None


# Predikát ‹is_complete› je pravdivý, neobsahuje-li tabulka ‹table›
# žádnou hodnotu ‹None›.

def is_complete(table: Table) -> bool:
    for record in get_records(table):
        for item in record:
            if item is None:
                return False
    return True


# Funkce ‹index_of_column› vrátí index sloupce se jménem ‹name›.
# Můžete předpokládat, že sloupec s jménem ‹name› se v tabulce
# nachází. První sloupec má index 0.

def index_of_column(name: str, header: Header) -> int:
    for index, item in enumerate(header):
        if item == name:
            return index
    return index

# Funkce ‹values› vrátí seznam platných hodnot (tzn. takových, které
# nejsou ‹None›) v sloupci se jménem ‹name›. Můžete předpokládat, že
# sloupec se jménem ‹name› se v tabulce nachází.


def values(name: str, table: Table) -> list[str]:
    result = []
    for record in get_records(table):
        value = record[index_of_column(name, get_header(table))]
        if value is not None:
            result.append(value)

    return result


# Procedura ‹drop_column› smaže sloupec se jménem ‹name› z tabulky
# ‹table›. Můžete předpokládat, že sloupec se jménem ‹name› se
# v tabulce nachází. Návratovou hodnotou ať je ‹None›.

def drop_column(name: str, table: Table) -> None:
    index_to_drop = index_of_column(name, get_header(table))
    header = get_header(table)
    records = get_records(table)

    new_record = []
    new_records = []
    for record in records:
        for item_i, item in enumerate(record):
            if item_i != index_to_drop:
                new_record.append(item)
        new_records.append(new_record)
        new_record = []

    new_header = []
    for item_i, item in enumerate(header):
        if item_i != index_to_drop:
            new_header.append(item)

    while len(header) > 0:
        header.pop()

    while len(records) > 0:
        records.pop()

    for item in new_header:
        header.append(item)

    for record in new_records:
        records.append(record)

    return None


# Konečně otypujte následující dvě testovací funkce (jejich
# implementaci neměňte, pouze přidejte typové anotace).


def make_empty() -> Table:
    return ["A", "B", "C", "D"], []


def make_table() -> Table:
    return (["A", "B", "C"],
            [["a1", "b1", None],
             ["a2", "b2", "c2"],
             ["a3", None, "c3"]])


def main() -> None:

    # header test
    assert get_header(make_empty()) == ['A', 'B', 'C', 'D']
    assert get_header(make_table()) == ['A', 'B', 'C']

    # records test
    assert get_records(make_empty()) == []
    assert get_records(make_table()) == [["a1", "b1", None],
                                         ["a2", "b2", "c2"],
                                         ["a3", None, "c3"]]

    # add_record test
    tab_1 = make_empty()
    add_record(["a", "b", "c", "d"], tab_1)
    assert tab_1 == (['A', 'B', 'C', 'D'], [['a', 'b', 'c', 'd']])

    tab_2 = make_table()
    add_record(["a4", None, None], tab_2)
    assert tab_2 == (['A', 'B', 'C'],
                     [['a1', 'b1', None], ['a2', 'b2', 'c2'],
                      ['a3', None, 'c3'], ['a4', None, None]])

    # is_complete test
    assert is_complete(make_empty())
    assert not is_complete(make_table())
    assert is_complete((["A", "B", "C"],
                        [["a1", "b1", "c1"], ["a2", "b2", "c2"]]))
    #
    # # index_of_column test
    header = ['A', 'C', 'B']
    assert index_of_column('A', header) == 0
    assert index_of_column('C', header) == 1
    assert index_of_column('B', header) == 2
    #
    tab_v = make_table()
    assert values("A", tab_v) == ["a1", "a2", "a3"]
    assert values("B", tab_v) == ["b1", "b2"]
    assert values("C", tab_v) == ["c2", "c3"]
    assert values("B", make_empty()) == []
    #
    # drop_column test
    tab_3 = make_table()
    drop_column("A", tab_3)
    assert tab_3 == (['B', 'C'],
                     [['b1', None], ['b2', 'c2'], [None, 'c3']])

    tab_4 = make_table()
    drop_column("B", tab_4)
    assert tab_4 == (['A', 'C'],
                     [['a1', None], ['a2', 'c2'], ['a3', 'c3']])

    tab_5 = make_empty()
    drop_column("D", tab_5)
    assert tab_5 == (['A', 'B', 'C'], [])


if __name__ == "__main__":
    main()