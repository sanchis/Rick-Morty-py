from typing import Any, Optional
from rick_morty_py.helpers import Menu, MenuElement, TerminalTable
from .character import Character
from .http_client import RickMortyClient


class RickyMortyList:
    def __init__(self) -> None:
        pass

    def list(self):
        self.__print_list()

    def search(self, search_name: str):
        self.__print_list(1, search_name)

    def __move_next_page(self, current_page: int, search_name: str):
        self.__print_list(current_page + 1, search_name)

    def __move_previous_page(self, current_page: int, search_name: str):
        self.__print_list(current_page - 1, search_name)

    def __print_list(self, current_page: int = 1, search_name: Optional[str] = None):
        try:
            # TODO type the response to the correct one
            response: Any = RickMortyClient.list(current_page, search_name)
            result = response.get("results")
            characters = list(map(lambda char: str(Character(char)), result))

            TerminalTable.print(characters)
            self.__print_menu(
                current_page, response.get("info").get("count"), search_name
            )
        except Exception:
            return

    def __print_menu(
        self, current_page: int, max_pages: int, search_name: Optional[str] = None
    ) -> None:
        pagination_elements = []

        if current_page + 1 <= max_pages:
            pagination_elements.append(
                MenuElement(
                    "Página siguiente",
                    self.__move_next_page,
                ),
            )
        if current_page - 1 > 0:
            pagination_elements.append(
                MenuElement("Página anterior", self.__move_previous_page)
            )

        pagination_elements.append(MenuElement("Volver al menu", lambda *_,: _))

        menu_element = Menu(pagination_elements).print()
        menu_element.fn(current_page, search_name)
