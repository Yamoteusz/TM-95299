# TM-95299 — Testowanie aplikacji mobilnych

Repozytorium dokumentuje realizację pełnego cyklu laboratoriów z testowania aplikacji mobilnych. Projekt obejmuje przygotowanie środowiska, analizę aplikacji APK, budowę frameworka testowego, testy API, raportowanie Allure oraz prosty pipeline automatyzujący wykonanie testów.

## Cel projektu
Celem repozytorium było praktyczne przejście przez kolejne etapy pracy testera automatyzującego aplikacje mobilne — od analizy statycznej i konfiguracji Appium, przez selektory i Page Object Model, aż po raportowanie i portfolio projektowe.

## Technologie użyte w projekcie
- Python
- Docker / Docker Compose
- Appium
- Pytest
- Allure Report
- Requests
- JSON Schema
- Git / GitHub
- ADB / APKTool / AAPT
- XML / JSON / Markdown

---

## Blok 1 — Środowisko, struktura projektu i Git
W pierwszym etapie przygotowano repozytorium, strukturę folderów artefaktów oraz podstawowy workflow pracy z Git i GitHub. Celem było zbudowanie stabilnej bazy pod wszystkie kolejne laboratoria.

**Zakres prac:**
- utworzenie repozytorium,
- organizacja katalogów Artefakt01–Artefakt10,
- pierwsze commity i push do GitHub.

---

## Blok 2 — ADB i statyczna analiza APK
W tym bloku przeprowadzono analizę pliku APK. Zrealizowano dekompilację aplikacji, odczyt manifestu oraz sprawdzenie uprawnień, SDK i podstawowych parametrów pakietu.

**Zakres prac:**
- analiza `AndroidManifest.xml`,
- badanie minimalnej i docelowej wersji SDK,
- odczyt uprawnień,
- przygotowanie zdekompilowanej struktury APK.

---

## Blok 3 — Docker Compose i serwer Appium
Celem było uruchomienie serwera Appium w kontenerze Docker oraz potwierdzenie poprawności działania środowiska testowego.

**Zakres prac:**
- stworzenie `docker-compose.yml`,
- uruchomienie Appium,
- weryfikacja portu 4723,
- analiza logów serwera,
- sprawdzenie wersji Appium.

---

## Blok 4 — Inspektor i lokalizatory
W tym etapie przygotowano skrypty do analizy layoutów XML i oceny jakości lokalizatorów wykorzystywanych w automatyzacji.

**Zakres prac:**
- wydobycie identyfikatorów z layoutów,
- analiza stabilności selektorów,
- weryfikacja unikalności par ID + TAG,
- analiza luk dostępności (`contentDescription`),
- generowanie raportów JSON i TXT.

---

## Blok 5 — Pierwszy skrypt automatyczny
Blok był poświęcony przygotowaniu pierwszych elementów frameworka automatyzującego oraz połączeniu danych z manifestu, map selektorów i konfiguracji sesji.

**Zakres prac:**
- generowanie desired capabilities,
- analiza manifestu,
- mapowanie selektorów UI,
- budowa prostego session managera,
- przygotowanie raportu XML z wynikiem walidacji.

---

## Blok 6 — Page Object Model (POM)
W tym bloku zbudowano podstawową architekturę POM, rozdzielając warstwę techniczną od logiki testowej.

**Zakres prac:**
- implementacja `BasePage`,
- implementacja `MainPage`,
- stworzenie prostego scenariusza testowego,
- przygotowanie audytu modularności i spójności,
- walidacja frameworka i raport XML.

---

## Blok 7 — Testy przerwań, gesty i stan urządzenia
Celem było odwzorowanie bardziej realistycznych sytuacji mobilnych: gestów, zmian orientacji, synchronizacji dynamicznej i przerwań systemowych.

**Zakres prac:**
- logika scroll/swipe,
- symulacja przerwania połączeniem,
- zarządzanie stanem i orientacją urządzenia,
- synchronizacja dynamiczna z użyciem waitów,
- raport stabilności testów.

---

## Blok 8 — Statyczna analiza bezpieczeństwa
W tym bloku skupiono się na bezpieczeństwie aplikacji Android — zarówno od strony konfiguracji, jak i zależności.

**Zakres prac:**
- analiza ryzykownych uprawnień,
- wyszukiwanie hardcoded secrets,
- audyt bibliotek z podatnościami,
- obliczanie security score,
- przygotowanie końcowego raportu bezpieczeństwa.

---

## Blok 9 — Testowanie API dla Mobile
Blok 9 rozszerzył testy mobilne o warstwę backendową. Zaimplementowano testy API, walidację odpowiedzi i prosty przepływ hybrydowy API + Appium.

**Zakres prac:**
- test połączenia z endpointem API,
- testy CRUD (POST/GET),
- walidacja schematu JSON,
- testy negatywne i obsługa kodów błędów,
- prosty test hybrydowy łączący API i UI.

---

## Blok 10 — Raportowanie i automatyzacja (CI/CD)
Ostatni blok był poświęcony raportowaniu wyników i prezentacji projektu w formie portfolio.

**Zakres prac:**
- konfiguracja Pytest + Allure,
- implementacja metadanych Epic / Feature / Story,
- dołączanie attachmentów do błędów,
- przygotowanie prostego `pipeline.py`,
- budowa README jako wizytówki projektu.

---

## Struktura repozytorium
Repozytorium zawiera osobne foldery dla każdego artefaktu laboratoryjnego:

- `Artefakt01`
- `Artefakt02`
- `Artefakt03`
- `Artefakt04`
- `Artefakt05`
- `Artefakt06`
- `Artefakt07`
- `Artefakt08`
- `Artefakt09`
- `Artefakt10`

Dodatkowo w repo znajdują się pliki pomocnicze, takie jak `.gitignore` oraz `app.apk`, wykorzystywany do analizy aplikacji. Repo w tej chwili rzeczywiście zawiera te katalogi i pliki. :contentReference[oaicite:1]{index=1}

---

## Wnioski końcowe
Projekt pokazuje pełny przekrój pracy z automatyzacją testów mobilnych:
- analiza aplikacji,
- budowa środowiska testowego,
- przygotowanie lokalizatorów,
- implementacja frameworka,
- testy UI i API,
- analiza bezpieczeństwa,
- raportowanie i pipeline.

Repozytorium może być traktowane jako materiał portfolio pokazujący praktyczne podstawy pracy testera automatyzującego mobile.

## Autor
Brajan S. pseud. Yamoteusz / TM-95299