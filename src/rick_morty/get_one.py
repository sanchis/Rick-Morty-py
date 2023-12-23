from typing import Dict
from rick_morty.character import Character
from rick_morty.http_client import RickMortyClient
from helpers.table.module import TerminalTable


class RickMortyGetOne:
    def __init__(self) -> None:
        pass

    def get(self, id: str):
        try:
            response: Dict = RickMortyClient.get_by_id(id)
            character = str(Character(response))
            TerminalTable.print([character])

        except Exception:
            return

        input("Pulsa cualquier letra para volver...")
