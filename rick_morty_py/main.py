from rick_morty_py.helpers import Menu, MenuElement
from rick_morty_py.rick_morty.get_list import RickyMortyList
from rick_morty_py.rick_morty.get_one import RickMortyGetOne


class Main:
    @staticmethod
    def __init__() -> None:
        Main.__print_banner()
        Main.__print_menu()

    @staticmethod
    def __print_banner() -> None:
        print(
            """
      _____  _      _               __  __            _
     |  __ \\(_)    | |      ___    |  \\/  |          | |
     | |__) |_  ___| | __  ( _ )   | \\  / | ___  _ __| |_ _   _
     |  _  /| |/ __| |/ /  / _ \\/\\ | |\\/| |/ _ \\| '__| __| | | |
     | | \\ \\| | (__|   <  | (_>  < | |  | | (_) | |  | |_| |_| |
     |_|  \\_\\_|\\___|_|\\_\\  \\___/\\/ |_|  |_|\\___/|_|   \\__|\\__, |
                                                           __/ |
                                                          |___/  """
        )

    @staticmethod
    def __search_name():
        search_name = input("Introduce el nombre a buscar: ")
        RickyMortyList().search(search_name)

    @staticmethod
    def __search_by_id():
        id = input("Introduce el id a obtener: ")
        RickMortyGetOne().get(id)

    @staticmethod
    def __print_menu() -> None:
        option_selected = Menu(
            [
                MenuElement("Listar todos los personajes.", RickyMortyList().list),
                MenuElement("Buscar un personaje por nombre.", Main.__search_name),
                MenuElement("Buscar personaje por id.", Main.__search_by_id),
                MenuElement("Salir.", exit),
            ]
        ).print()
        option_selected.fn()
        Main.__print_menu()


Main()
