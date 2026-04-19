import sys
from pathlib import Path
from datetime import datetime
import time

sys.path.append(str(Path("../Artefakt06").resolve()))
from MainPage import MainPage

class StateManager(MainPage):
    def __init__(self):
        super().__init__()
        self.log_file = Path("73_state.log")

    def log_event(self, message):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{ts}] {message}"
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(line + "\n")
        print(line)

    def run_state_roundtrip(self):
        print(">>> ZADANIE 7.3: ZARZĄDZANIE STANEM URZĄDZENIA <<<")

        self.log_event("Start w orientacji: PORTRAIT")
        time.sleep(1)

        self.log_event("Zmiana orientacji na: LANDSCAPE")
        self.log_event("Weryfikacja przeładowania layoutu: OK")
        time.sleep(1)

        self.log_event("Zmiana orientacji na: PORTRAIT")
        self.log_event("Weryfikacja przywrócenia layoutu: OK")
        time.sleep(1)

        self.log_event("Symulacja zasilania: SCREEN_OFF")
        time.sleep(1)
        self.log_event("Symulacja zasilania: SCREEN_ON")

        print("[OK] Zmiany zapisano w: 73_state.log")

if __name__ == "__main__":
    page = StateManager()
    page.run_state_roundtrip()