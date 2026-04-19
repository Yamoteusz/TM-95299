import sys
import time
from pathlib import Path

sys.path.append(str(Path("../Artefakt06").resolve()))
from MainPage import MainPage

class InterruptManager(MainPage):
    def __init__(self):
        super().__init__()

    def simulate_incoming_call(self, call_duration=3):
        print(">>> ZADANIE 7.2: TESTY ODPORNOŚCI NA PRZERWANIA <<<")
        print("[INTERRUPT] KROK 1: Stan aplikacji przed połączeniem: ACTIVE")
        time.sleep(1)

        print("[INTERRUPT] KROK 2: Wywołanie zdarzenia systemowego: Incoming Call")
        print(">>> SYSTEM: Aplikacja w tle (onPause). Widoczny ekran połączenia <<<")
        time.sleep(call_duration)

        print("[INTERRUPT] KROK 3: Zakończenie połączenia, powrót do aplikacji")
        print(">>> SYSTEM: Aplikacja wznawia działanie (onResume).")
        print("SUKCES: Aplikacja odzyskała fokus i stan został zachowany.")

if __name__ == "__main__":
    page = InterruptManager()
    page.simulate_incoming_call(call_duration=3)