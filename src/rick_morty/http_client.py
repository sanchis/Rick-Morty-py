from typing import Dict, Optional, Union
import requests
from urllib3.exceptions import InsecureRequestWarning, NewConnectionError
from urllib3 import disable_warnings
from alert import Alert


disable_warnings(InsecureRequestWarning)


# https://rickandmortyapi.com/documentation
class RickMortyClient:
    __base_url = "https://rickandmortyapi.com/api"

    @staticmethod
    def list(page: int = 0, name: Optional[str] = None) -> Union[Dict, Exception]:
        try:
            response = requests.get(
                RickMortyClient.__base_url + "/character",
                params={"page": page, "name": name},
            )
        except requests.exceptions.ConnectionError as error:
            Alert.error("Error conectando con el servidor intentalo otra vez.")
            return error
        except Exception as error:
            Alert.error(
                "Error desconocido con el servidor, intentalo otra vez." + str(error)
            )
            Alert.error(f"Detalle del error: {error}")
            raise error
        else:
            if response.status_code != 200:
                error_msg = (
                    f"Rick and morty get by id api response {response.status_code}"
                )
                Alert.error(error_msg)
                return Exception(error_msg)
            return response.json()

    @staticmethod
    def get_by_id(id: str) -> Dict:
        try:
            response = requests.get(RickMortyClient.__base_url + f"/character/{id}")

        except requests.exceptions.ConnectionError as error:
            Alert.error("Error conectando con el servidor intentalo otra vez.")
            raise Exception(error)
        except Exception as error:
            Alert.error(
                "Error desconocido con el servidor, intentalo otra vez." + str(error)
            )
            Alert.error(f"Detalle del error: {error}")
            raise Exception(error)
        else:
            if response.status_code != 200:
                error_msg = (
                    f"Rick and morty get by id api response {response.status_code}"
                )
                Alert.error(error_msg)
                raise Exception(error_msg)
            return response.json()
