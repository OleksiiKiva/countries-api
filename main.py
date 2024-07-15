from typing import Dict, Any
from urllib.parse import urljoin

import requests
from prettytable import PrettyTable, SINGLE_BORDER

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

    def __parse_data(self) -> list[list]:
        """A method that receives data in json format and converts it into a nested list"""

        if self.__get_data():
            result = self.__get_data()
            list_for_table = []
            for country in result:
                name = country.get("name", {}).get("common", {})
                capital = ", ".join(country.get("capital", {}))
                flags = country.get("flags", {}).get("png", {})
                list_for_table.append([name, capital, flags])

            return list_for_table

    def print_data(self) -> None:
        """A method that receives a nested list and prints it in the console as a table"""

        if self.__parse_data():
            table = PrettyTable(
                [
                    "Country name",
                    "Capital",
                    "Flag_URL",
                ]
            )
            table.add_rows(rows=self.__parse_data())
            table.align = "l"
            table.set_style(SINGLE_BORDER)

            print(table.get_string(sortby="Country name", end=90))
