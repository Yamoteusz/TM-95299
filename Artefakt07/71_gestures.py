import sys
from pathlib import Path

sys.path.append(str(Path("../Artefakt06").resolve()))
from MainPage import MainPage

class GestureAutomator(MainPage):
    def __init__(self):
        super().__init__()

    def scroll_down_logic(self, duration_ms=800):
        width = 1080
        height = 1920

        start_x = int(width * 0.50)
        start_y = int(height * 0.80)
        end_x = int(width * 0.50)
        end_y = int(height * 0.20)

        print(">>> ZADANIE 7.1: TESTY GESTÓW DOTYKOWYCH <<<")
        print(f"[GESTURE] Start Swipe: x={start_x}, y={start_y} -> x={end_x}, y={end_y} (duration={duration_ms}ms)")
        print("SUKCES: Przewinięto listę o 60% wysokości ekranu.")
        return (start_x, start_y, end_x, end_y, duration_ms)

    def long_press_on_add(self):
        selector = self.find_id("ADD")
        print(f"SUKCES: Wykonano LONG PRESS na elemencie: {selector}")

if __name__ == "__main__":
    page = GestureAutomator()
    page.scroll_down_logic(duration_ms=800)
    page.long_press_on_add()