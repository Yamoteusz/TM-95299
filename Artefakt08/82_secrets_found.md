# RAPORT AUDYTU: ANALIZA WYCIEKU DANYCH WRAŻLIWYCH (SECRETS)

**Audytor:** Brajan Sieroń  
**Numer indeksu:** 95299

---

## 1. Krytyczne Zagrożenia (Top 3)

1. **Plik `res/layout/mapview.xml` (słowo kluczowe: `apiKey`)**  
   * **Uzasadnienie:** Potencjalne ujawnienie zaszytego w kodzie (hardcoded) klucza API do usług map (np. Google Maps API). Wyciek takiego klucza pozwala na jego nieautoryzowane użycie przez osoby trzecie, co może skutkować kradzieżą limitów i wygenerowaniem kosztów na koncie chmurowym organizacji.

2. **Plik `smali/io/appium/.../DatabaseHelper.smali` (słowo kluczowe: `KEY`)**  
   * **Uzasadnienie:** Wykryty ciąg w klasie obsługującej bazę danych sugeruje obecność zahardkodowanych kluczy kryptograficznych (np. do bazy SQLCipher) lub poświadczeń dostępowych. Stanowi to bezpośrednie ryzyko deszyfracji lokalnych danych użytkownika.

3. **Plik `res/values/strings.xml` (URL: `http://www.example.com/lala/foobar@example.com`)**  
   * **Uzasadnienie:** Niestandardowy adres URL połączony z adresem e-mail. Może on ujawniać zapomniane deweloperskie punkty końcowe (staging endpoints) lub ścieżki komunikacji, co umożliwia precyzyjny rekonesans struktury backendowej i planowanie dalszych wektorów ataku.

---

## 2. Analiza Wyników Fałszywie Pozytywnych (False Positives)

1. **Pliki XML, m.in. `AndroidManifest.xml`, `animator.xml` (URL: `http://schemas.android.com/apk/res/android`)**  
   * **Uzasadnienie:** Zidentyfikowany adres to standardowa deklaracja przestrzeni nazw (namespace) wymagana przez system Android w plikach konfiguracyjnych i widokach. Występuje masowo we wszystkich aplikacjach i nie niesie żadnego ryzyka.

2. **Pliki `res/values/strings.xml` oraz `ids.xml` (słowa kluczowe: `password`, `login`)**  
   * **Uzasadnienie:** Skaner bezkontekstowo oflagował słowa "password", jednak w plikach zasobów (`strings.xml`) są to jedynie publiczne etykiety tekstowe (np. "Wpisz hasło") lub identyfikatory pól interfejsu (UI). Nie są to rzeczywiste dane uwierzytelniające.

3. **Pliki bibliotek, np. `smali/androidx/collection/LruCache.smali` (słowo kluczowe: `key`)**  
   * **Uzasadnienie:** Słowo kluczowe zostało błędnie dopasowane przez algorytm skanera w standardowych bibliotekach AndroidX. W tym kontekście "key" oznacza po prostu strukturę danych (klucz-wartość w mapach/słownikach), a nie klucz autoryzacyjny czy kryptograficzny.

---

## 3. Podsumowanie i Wnioski
Zastosowanie automatycznych narzędzi do skanowania kodu pozwala na szybką identyfikację potencjalnych luk, generuje jednak znaczny stopień szumu informacyjnego (np. masowe raportowanie przestrzeni nazw XML). Kluczowym etapem audytu bezpieczeństwa pozostaje **manualna weryfikacja ekspercka**, która pozwala oddzielić błędy konfiguracji (np. `apiKey` w widokach) od nieszkodliwych artefaktów programistycznych. 

**Rekomendacja:** Należy wdrożyć mechanizmy *pre-commit hooks*, aby zapobiegać wysyłaniu sekretów do repozytorium na etapie wytwarzania oprogramowania, oraz zoptymalizować reguły skanera, aby wykluczyć pliki bibliotek (np. `androidx/*`).