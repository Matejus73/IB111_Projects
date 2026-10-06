from ib111 import week_03  # noqa


# Napište (čistou) funkci, která simuluje jeden krok výpočtu
# jednorozměrného buněčného automatu (cellular automaton). My se
# omezíme na «binární» (buňky nabývají hodnot 0 a 1) «jednorozměrný»
# automat s «konečným stavem»: stav takového automatu je seznam
# jedniček a nul, například:
#
#   ┌───┬───┬───┬───┬───┬───┬───┐
#   │ 0 │ 1 │ 1 │ 1 │ 0 │ 0 │ 1 │
#   └───┴───┴───┴───┴───┴───┴───┘
#
# Protože obecný automat tohoto typu je stále relativně složitý,
# budeme implementovat automat s fixní sadou pravidel:
#
# │‹old[i - 1]›│‹old[i]›│‹old[i + 1]›│‹new[i]›│
# ├┄┄┄┄┄┄┄┄┄┄┄┄┼┄┄┄┄┄┄┄┄┼┄┄┄┄┄┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄│
# │     0      │    0   │      1     │    1   │
# │     1      │    0   │      0     │    1   │
# │     1      │    0   │      1     │    1   │
# │     1      │    1   │      0     │    0   │
# │     1      │    1   │      1     │    0   │
#
# Pravidla určují, jakou hodnotu bude mít buňka v následujícím
# stavu, v závislosti na několika okolních buňkách stavu nynějšího
# (konkrétní indexy viz tabulka). Neexistuje-li pro danou vstupní
# kombinaci pravidlo, do nového stavu přepíšeme stávající hodnotu
# buňky. Na krajích stavu interpretujeme chybějící políčko vždy
# jako nulu.
#
# Výpočet s touto sadou pravidel tedy funguje takto:
#
#   ┌───┬───┬───┬───┬───┬───┐ 001 → 1 ┌───┬───┬───┬───┬───┬───┐
#   │░0░│░1░│ 1 │ 0 │ 0 │ 1 │────────▶│░1 │   │   │   │   │   │
#   └───┴───┴───┴───┴───┴───┘         └───┴───┴───┴───┴───┴───┘
#   ┌───┬───┬───┬───┬───┬───┐ 011 → ? ┌───┬───┬───┬───┬───┬───┐
#   │░0░│░1░│░1░│ 0 │ 0 │ 1 │────────▶│ 1 │░1 │   │   │   │   │
#   └───┴───┴───┴───┴───┴───┘         └───┴───┴───┴───┴───┴───┘
#   ┌───┬───┬───┬───┬───┬───┐ 110 → 0 ┌───┬───┬───┬───┬───┬───┐
#   │ 0 │░1░│░1░│░0░│ 0 │ 1 │────────▶│ 1 │ 1 │░0░│   │   │   │
#   └───┴───┴───┴───┴───┴───┘         └───┴───┴───┴───┴───┴───┘
#   ┌───┬───┬───┬───┬───┬───┐ 100 → 1 ┌───┬───┬───┬───┬───┬───┐
#   │ 0 │ 1 │░1░│░0░│░0░│ 1 │────────▶│ 1 │ 1 │ 0 │░1░│   │   │
#   └───┴───┴───┴───┴───┴───┘         └───┴───┴───┴───┴───┴───┘
#   ┌───┬───┬───┬───┬───┬───┐ 001 → 1 ┌───┬───┬───┬───┬───┬───┐
#   │ 0 │ 1 │ 1 │░0░│░0░│░1░│────────▶│ 1 │ 1 │ 0 │ 1 │░1░│   │
#   └───┴───┴───┴───┴───┴───┘         └───┴───┴───┴───┴───┴───┘
#   ┌───┬───┬───┬───┬───┬───┐ 010 → ? ┌───┬───┬───┬───┬───┬───┐
#   │ 0 │ 1 │ 1 │ 0 │░0░│░1░│────────▶│ 1 │ 1 │ 0 │ 1 │ 1 │░1░│
#   └───┴───┴───┴───┴───┴───┘         └───┴───┴───┴───┴───┴───┘
#
# Na vstupu dostanete stav (konfiguraci) ‹state›, výstupem funkce je
# nový seznam, který obsahuje stav vzniklý aplikací výše uvedených
# pravidel na ‹state›. Výpočet celého nového stavu považujeme za
# jeden krok výpočtu.

def cellular_step(state):
    old_state = [0]

    for _, i in enumerate(state):
        old_state.append(i)
    old_state.append(0)
    new_state = []

    for i in range(1, len(old_state) - 1):

        if old_state[i] == 0:
            if old_state[i - 1] == 1 or old_state[i + 1] == 1:
                new_state.append(1)
            else:
                new_state.append(0)
        else:
            if old_state[i - 1] == 1:
                new_state.append(0)
            else:
                new_state.append(1)

    return new_state


def main() -> None:
    assert cellular_step([0, 1, 0]) == [1, 1, 1]
    assert cellular_step([0, 0, 1]) == [0, 1, 1]
    assert cellular_step([1, 0, 1]) == [1, 1, 1]
    assert cellular_step([1, 1, 1]) == [1, 0, 0]
    assert cellular_step([1, 0, 1, 1, 0, 1, 1]) == [1, 1, 1, 0, 1, 1, 0]
    assert cellular_step([1, 1, 1, 0, 1]) == [1, 0, 0, 1, 1]
    assert cellular_step([0, 0, 1, 1, 1, 0, 1]) == [0, 1, 1, 0, 0, 1, 1]


if __name__ == "__main__":
    main()
