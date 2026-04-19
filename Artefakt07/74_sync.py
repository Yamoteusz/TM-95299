import sys
import time
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

sys.path.append(str(Path("../Artefakt06").resolve()))
from MainPage import MainPage

class DummyDriver:
    pass

class SyncManager(MainPage):
    def __init__(self):
        super().__init__()
        self.driver = DummyDriver()

    def wait_for_ui_element(self, business_id, timeout=10, simulated_delay=1.5):
        selector = self.get_selector(business_id)
        if not selector:
            raise KeyError(f"Brak klucza '{business_id}' w mapie!")

        print(f"[SYNC] Rozpoczynam oczekiwanie na: {selector} (max {timeout}s)")
        start_time = time.time()

        try:
            WebDriverWait(self.driver, timeout, poll_frequency=0.5).until(
                lambda d: (time.time() - start_time) >= simulated_delay
            )
            duration = round(time.time() - start_time, 3)
            print(f"SUKCES: Element '{selector}' odnaleziony i kliknięty po {duration}s.")
        except TimeoutException:
            duration = round(time.time() - start_time, 3)
            print(f"TIMEOUT: Element '{selector}' nie pojawił się w ciągu {duration}s.")

if __name__ == "__main__":
    page = SyncManager()
    print(">>> ZADANIE 7.4: TESTY SYNCHRONIZACJI DYNAMICZNEJ <<<")

    page.wait_for_ui_element("ADD", timeout=10, simulated_delay=1.5)

    try:
        page.wait_for_ui_element("NON_EXISTENT_BUTTON", timeout=3, simulated_delay=1.0)
    except KeyError as e:
        print(f"BŁĄD: {e}")

    page.wait_for_ui_element("CONTENT", timeout=1, simulated_delay=2.0)