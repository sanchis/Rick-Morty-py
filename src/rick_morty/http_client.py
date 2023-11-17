import requests
from urllib3.exceptions import InsecureRequestWarning, NewConnectionError
from urllib3 import disable_warnings
from alert import Alert


disable_warnings(InsecureRequestWarning)


# https://rickandmortyapi.com/documentation
class RickMortyClient:
    __base_url = "https://rickandmortyapi.com/api"

    @staticmethod
    def list(page: int = 0, name: str = None) -> dict:
        try:
            response = requests.get(
                RickMortyClient.__base_url + "/character",
                params={"page": page, "name": name},
            )
        except requests.exceptions.ConnectionError as error:
            Alert.error("Error conectando con el servidor intentalo otra vez.")
        except Exception as error:
            Alert.error(
                "Error desconocido con el servidor, intentalo otra vez." + str(error)
            )
            Alert.error(f"Detalle del error: {error}")
        else:
            if response.status_code != 200:
                return Alert.error(
                    f"Rick and morty get by id api response {response.status_code}"
                )
            return response.json()

    @staticmethod
    def get_by_id(id: str) -> dict:
        try:
            response = requests.get(RickMortyClient.__base_url + f"/character/{id}")

        except requests.exceptions.ConnectionError as error:
            Alert.error("Error conectando con el servidor intentalo otra vez.")
        except Exception as error:
            Alert.error(
                "Error desconocido con el servidor, intentalo otra vez." + str(error)
            )
            Alert.error(f"Detalle del error: {error}")
        else:
            if response.status_code != 200:
                return Alert.error(
                    f"Rick and morty get by id api response {response.status_code}"
                )
            return response.json()
