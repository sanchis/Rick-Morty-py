from typing import Callable, List
from helpers import Alert

from helpers import Terminal
from helpers import TerminalTable


class MenuElement:
    def __init__(self, name: str, fn: Callable) -> None:
        self.name = name
        self.fn = fn


class Menu:
    def __init__(self, menu_items: List[MenuElement]) -> None:
        self.__menu_items = menu_items

    def print(self) -> MenuElement:
        elements = list(
            map(
                lambda value: f"{self.__menu_items.index(value)+1}. {value.name}",
                self.__menu_items,
            )
        )
        TerminalTable.print(elements)
        option = input("Introduce la opción: ")
        if (
            not option.isdigit()
            or int(option) <= 0
            or int(option) > len(self.__menu_items)
        ):
            Terminal.clear()
            Alert.error("Opción incorrecta vuelva a intentarlo.")
            return self.print()
        else:
            option_selected = self.__menu_items[int(option) - 1]
            return option_selected
