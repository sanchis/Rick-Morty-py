from typing import Dict
from .character import Character
from .http_client import RickMortyClient
from rick_morty_py.helpers import TerminalTable


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
