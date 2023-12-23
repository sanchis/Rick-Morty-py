class Character:
    def __init__(self, character: dict) -> None:
        self.__name = character.get("name")
        self.__id = character.get("id")
        self.__species = character.get("species")
        self.__gender = character.get("gender")

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def species(self):
        return self.__species

    @property
    def gender(self):
        return self.__gender

    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}, species: {self.species}"
