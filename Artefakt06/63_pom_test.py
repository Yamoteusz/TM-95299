from MainPage import MainPage

def run_pom_test():
    print("=== ZADANIE 6.3: URUCHOMIENIE TESTU W ARCHITEKTURZE POM ===")

    page = MainPage()

    print("\n--- PRZEBIEG SCENARIUSZA TESTOWEGO ---")

    step1 = page.check_text_visibility()
    print(f"KROK 1: {step1}")

    step2 = page.click_add_button()
    print(f"KROK 2: {step2}")

    step3 = page.open_content_section()
    print(f"KROK 3: {step3}")

    with open("63_pom_audit.log", "w", encoding="utf-8") as f:
        f.write("PRZEBIEG SCENARIUSZA TESTOWEGO\n")
        f.write(f"KROK 1: {step1}\n")
        f.write(f"KROK 2: {step2}\n")
        f.write(f"KROK 3: {step3}\n")
        f.write("STATUS: Scenariusz wykonany pomyślnie.\n")

    print("\n[OK] Scenariusz wykonany. Log audytu zapisany w 63_pom_audit.log")

if __name__ == "__main__":
    run_pom_test()