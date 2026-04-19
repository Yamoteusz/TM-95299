import json
from pathlib import Path
from BasePage import BasePage
from MainPage import MainPage

def check_framework():
    print("=== ZADANIE 6.5: FRAMEWORK INTEGRITY CHECK ===")

    results = []

    # 1. Dziedziczenie POM
    try:
        page = MainPage()
        inheritance_ok = isinstance(page, BasePage)
        results.append(("POM Inheritance", inheritance_ok, "MainPage dziedziczy po BasePage"))
    except Exception as e:
        results.append(("POM Inheritance", False, f"Błąd inicjalizacji: {e}"))

    # 2. Dokumentacja Markdown
    audit_file = Path("64_audit_report.md")
    markdown_ok = False
    if audit_file.exists():
        content = audit_file.read_text(encoding="utf-8")
        if "# " in content or "## " in content:
            markdown_ok = True
    results.append(("Documentation_Doc", markdown_ok, "Raport audytu jest w formacie Markdown"))

    # 3. Mapa selektorów
    selectors_file = Path("../Artefakt05/53_selectors.json")
    selectors_ok = False
    selectors_count = 0
    if selectors_file.exists():
        with open(selectors_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            selectors_count = len(data)
            selectors_ok = selectors_count > 0
    results.append(("Data_Layer_Selectors", selectors_ok, f"Wczytano {selectors_count} selektorów z Bloku 5"))

    print("\n--- WYNIKI AUDYTU ARCHITEKTURY ---")
    for name, status, message in results:
        print(f"[{'PASSED' if status else 'FAILED'}] {name}: {message}")

    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<testsuite name="Framework_Audit" tests="3">\n'

    for name, status, message in results:
        xml_content += f'  <testcase name="{name}">'
        if not status:
            xml_content += f'<failure message="{message}">{message}</failure>'
        xml_content += '</testcase>\n'

    xml_content += '</testsuite>\n'

    with open("65_final_report.xml", "w", encoding="utf-8") as f:
        f.write(xml_content)

    print("\n[OK] Wygenerowano: 65_final_report.xml")

if __name__ == "__main__":
    check_framework()