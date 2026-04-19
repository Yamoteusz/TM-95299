import subprocess
import sys

def run_command(command, description, stop_on_error=True):
    print(f"\n=== {description} ===")
    print(f"[CMD] {command}")

    result = subprocess.run(command, shell=True)

    if result.returncode != 0:
        print(f"[WARN] Problem w kroku: {description} (kod: {result.returncode})")
        if stop_on_error:
            sys.exit(result.returncode)
        return result.returncode

    print(f"[SUCCESS] {description}")
    return result.returncode


def main():
    test_exit_code = 0

    # 1. infrastruktura
    run_command(
        r'cd ..\Artefakt03 && docker compose up -d',
        "Uruchamianie infrastruktury Docker",
        stop_on_error=True
    )

    # 2. testy - tutaj NIE przerywamy pipeline nawet jeśli są failed
    test_exit_code = run_command(
        r'pytest test_101_allure_init.py test_102_meta_reporting.py test_103_attachments.py --alluredir=allure-results',
        "Uruchamianie testów pytest + Allure",
        stop_on_error=False
    )

    # 3. generowanie raportu - ma się wykonać nawet gdy testy failed
    run_command(
        r'allure generate allure-results -o allure-report --clean',
        "Generowanie raportu Allure HTML",
        stop_on_error=True
    )

    # 4. sprzątanie
    run_command(
        r'cd ..\Artefakt03 && docker compose down',
        "Zamykanie infrastruktury Docker",
        stop_on_error=False
    )

    print("\n=== PIPELINE ZAKOŃCZONY ===")
    if test_exit_code == 0:
        print("[FINAL] Wszystkie testy przeszły poprawnie.")
    else:
        print("[FINAL] Pipeline zakończony, ale część testów była FAIL — raport został wygenerowany.")
        print("[INFO] To jest OK dla BLOKU 10, bo raport ma pokazywać Passed + Failed.")

    print(r"[INFO] Otwórz plik: allure-report\index.html")


if __name__ == "__main__":
    main()