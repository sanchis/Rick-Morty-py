from rick_morty.character import Character
from rick_morty.http_client import RickMortyClient
from terminal_table import TerminalTable


class RickMortyGetOne:
    def __init__(self) -> None:
        pass

    def get(self, id: str):
        response = RickMortyClient.get_by_id(id)
        if not response:
            return

        character = str(Character(response))
        TerminalTable.print([character])
        input("Pulsa cualquier letra para volver...")
