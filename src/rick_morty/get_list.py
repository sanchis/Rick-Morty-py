from menu import Menu, MenuElement
from rick_morty.character import Character
from rick_morty.http_client import RickMortyClient
from terminal_table import TerminalTable


class RickyMortyList:
    def __init__(self) -> None:
        pass

    def list(self):
        self.__print_list()

    def search(self, name: str):
        self.__print_list(1, name)

    def __move_next_page(self, current_page: int, name: str):
        self.__print_list(current_page + 1, name)

    def __move_previus_page(self, current_page: int, name: str):
        self.__print_list(current_page - 1, name)

    def __print_list(self, current_page: int = 1, name: str = None):
        response = RickMortyClient.list(current_page, name)
        if not response:
            return

        characters = list(
            map(lambda char: str(Character(char)), response.get("results"))
        )

        TerminalTable.print(characters)
        self.__print_menu(current_page, response.get("info").get("count"), name)

    def __print_menu(self, current_page: int, max_pages: int, name: str) -> None:
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
                MenuElement("Página anterior", self.__move_previus_page)
            )

        pagination_elements.append(MenuElement("Volver al menu", lambda *_,: _))

        menu_element = Menu(pagination_elements).print()
        menu_element.fn(current_page, name)
