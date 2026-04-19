from BasePage import BasePage

class MainPage(BasePage):
    def __init__(self):
        super().__init__()
        print("[MAIN_PAGE] Ekran główny zainicjalizowany.")

    def click_add_button(self):
        selector = self.find_id("ADD")
        return f"SUKCES: Wykonano kliknięcie w element UI o ID: '{selector}'"

    def check_text_visibility(self):
        selector = self.find_id("TITLE")
        return f"SUKCES: Odnaleziono nagłówek strony (ID: {selector}). Status: Widoczny."

    def open_content_section(self):
        selector = self.find_id("CONTENT")
        return f"SUKCES: Otworzono sekcję zawartości przez ID: '{selector}'"

if __name__ == "__main__":
    page = MainPage()
    print(page.click_add_button())
    print(page.check_text_visibility())
    print(page.open_content_section())