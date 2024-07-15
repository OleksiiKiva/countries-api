from typing import Dict, Any
from urllib.parse import urljoin

import requests

BASE_URL = "https://restcountries.com/v3.1/all"
HOME_URL = urljoin(BASE_URL, "?fields=name,capital,flags")


class CountryAPI:
    """A class that interacts with the API on https://restcountries.com"""

    def __init__(self):
        self.url = HOME_URL

    def __get_data(self) -> Dict[str, Any]:
        """A method that receives data from a third party API and converts it to json"""

        try:
            response = requests.get(url=self.url)
            if not response:
                print(
                    "The web-address was not entered or was entered incorrectly. Try again"
                )
            else:
                return response.json()

        except requests.ConnectionError:
            print("Connection error")

        except requests.Timeout:
            print("Timeout error")

        except requests.RequestException:
            print("Request error")
