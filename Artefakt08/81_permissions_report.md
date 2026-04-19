# RAPORT AUDYTU: ANALIZA UPRAWNIEŃ APLIKACJI

## 1. Zakres Analizy
Analiza została przeprowadzona na podstawie pliku `AndroidManifest.xml`. Proces obejmował identyfikację uprawnień sklasyfikowanych jako **dangerous** (ryzykowne) oraz weryfikację krytycznych flag konfiguracyjnych, w tym atrybutu `android:debuggable`.

---

## 2. Ocena Ryzyka i Interpretacja
Nadmiarowe uprawnienia bezpośrednio zwiększają tzw. powierzchnię ataku (attack surface). Podczas analizy szczególną uwagę zwrócono na:
* **Uprawnienia wrażliwe:** Dostęp do SMS, rejestru połączeń, kontaktów oraz lokalizacji (GPS). Ich obecność jest dopuszczalna wyłącznie, gdy wynika bezpośrednio z kluczowej logiki biznesowej aplikacji.
* **Zasada minimalnych uprawnień:** Każde zezwolenie wykraczające poza niezbędne minimum stanowi potencjalne zagrożenie dla prywatności danych użytkownika.

---

## 3. Wnioski i Rekomendacje Inżynierskie
* **Kontekstualizacja:** Każde uprawnienie musi być uzasadnione funkcjonalnością. Uprawnienia nieużywane powinny zostać niezwłocznie usunięte z manifestu.
* **Bezpieczeństwo konfiguracji:** Flaga `debuggable="true"` w środowisku produkcyjnym jest krytycznym uchybieniem, umożliwiającym nieautoryzowany dostęp do danych i debugowanie procesu przez osoby trzecie.
* **Analiza skumulowana:** Nawet uprawnienia o niskim priorytecie (np. `INTERNET`) w połączeniu z innymi lukami mogą zostać wykorzystane do eksfiltracji danych. Należy monitorować przepływ informacji wychodzących.

---

**Status końcowy:** *Analiza zakończona. Wymagana weryfikacja uprawnień z mapą drogową produktu.*