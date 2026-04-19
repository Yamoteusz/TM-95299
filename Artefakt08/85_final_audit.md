# RAPORT KOŃCOWY Z AUDYTU BEZPIECZEŃSTWA: APIDEMOS

**Data:** 18.04.2026  
**Audytor:** Brajan Sieroń 95299  
**Projekt:** ApiDemos

---

## 1. OCENA KOŃCOWA (SECURITY SCORE)

> **WYNIK:** **0/100**  
> **STATUS:** **REJECTED**

---

## 2. KLUCZOWE OBSZARY RYZYKA

### A. Konfiguracja Systemowa i Uprawnienia
* **Zidentyfikowany problem:** Aplikacja żąda dostępu do ryzykownych uprawnień (*dangerous permissions*), co wymaga rygorystycznej oceny pod kątem rzeczywistego zapotrzebowania biznesowego (Zasada Najmniejszego Uprzywilejowania).
* **Wektor zagrożenia:** Znaczne poszerzenie powierzchni ataku (*attack surface*) oraz wysokie prawdopodobieństwo nadużycia uprawnień w przypadku kompromitacji aplikacji.

### B. Wycieki Danych Wrażliwych (Secrets Leakage)
* **Zidentyfikowany problem:** W kodzie źródłowym oraz plikach zasobów (XML) wykryto wzorce sugerujące obecność zahardkodowanych danych uwierzytelniających, kluczy API oraz adresów URL środowisk testowych.
* **Wektor zagrożenia:** Bezpośrednie ryzyko ujawnienia architektury backendowej, nieautoryzowanego dostępu do usług zewnętrznych lub ułatwienie inżynierii wstecznej i dalszego rekonesansu atakującemu.

### C. Bezpieczeństwo Zależności (Łańcuch Dostaw)
* **Zidentyfikowany problem:** Analiza wykazała obecność przestarzałych bibliotek zewnętrznych, które posiadają publicznie znane luki bezpieczeństwa sklasyfikowane w bazie podatności CVE.
* **Wektor zagrożenia:** Aplikacja bezpośrednio dziedziczy ryzyka z niezabezpieczonego łańcucha dostaw oprogramowania (*Supply Chain Vulnerabilities*), co otwiera drogę do wykorzystania znanych exploitów.

---

## 3. MAPA DROGOWA NAPRAWCZA (REMEDIATION ROADMAP)

1. **[PRIORYTET 1 - KRYTYCZNY] Aktualizacja zależności:** Natychmiastowa aktualizacja podatnych bibliotek i usunięcie/zastąpienie komponentów oznaczonych poziomami ryzyka `CRITICAL` oraz `HIGH`.
2. **[PRIORYTET 1 - KRYTYCZNY] Audyt uprawnień:** Przegląd pliku `AndroidManifest.xml`, usunięcie nadmiarowych deklaracji oraz wyłączenie flag testowych (np. `debuggable="true"`).
3. **[PRIORYTET 2 - WYSOKI] Zarządzanie sekretami:** Usunięcie *hardcoded secrets* z repozytorium kodu i przeniesienie konfiguracji z poświadczeniami do bezpiecznych, zewnętrznych mechanizmów zarządzania kluczami (np. systemowe Keystore, zmienne środowiskowe CI/CD).

---

## 4. WNIOSKI KOŃCOWE

Aplikacja w obecnym stanie **wymaga wdrożenia pilnych działań naprawczych** przed uznaniem jej za bezpieczną do wdrożenia na środowiska produkcyjne. Największe zidentyfikowane ryzyko wynika ze skumulowanego efektu przestarzałych bibliotek z lukami CVE, nadużywania ryzykownych uprawnień w systemie Android oraz pozostawienia potencjalnych punktów zaczepienia (wycieki danych) dla atakujących. Weryfikacja powdrożeniowa jest obligatoryjna.