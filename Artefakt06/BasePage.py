import json
from pathlib import Path

class BasePage:
    def __init__(self, selectors_file="../Artefakt05/53_selectors.json"):
        self.selectors_file = Path(selectors_file)

        if not self.selectors_file.exists():
            raise FileNotFoundError(f"Brak pliku mapy selektorów: {self.selectors_file}")

        with open(self.selectors_file, "r", encoding="utf-8") as f:
            self.selectors = json.load(f)

        print(f"[BASE_PAGE] Pomyślnie zainicjalizowano mapę: {len(self.selectors)} elementów.")

    def get_selector(self, business_name):
        return self.selectors.get(business_name)

    def find_id(self, business_name):
        selector = self.get_selector(business_name)
        if selector:
            return selector
        raise KeyError(f"Nie znaleziono klucza biznesowego: {business_name}")

if __name__ == "__main__":
    page = BasePage()
    print(f"Weryfikacja klucza 'ADD': {page.get_selector('ADD')}")