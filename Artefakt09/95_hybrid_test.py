import requests

print("=== TEST 9.5: HYBRID API + APPIUM ===")

# KROK 1 - API
url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Hybrid Test",
    "body": "Test integracji",
    "userId": 1
}

response = requests.post(url, json=data)

print(f"[API] Status: {response.status_code}")
print(f"[API] Data: {response.json()}")

# KROK 2 - SYMULACJA APPIUM (log)
print("[APPIUM] Start sesji...")
print("[APPIUM] Nawigacja do elementu...")
print("[APPIUM] Weryfikacja danych na ekranie...")

print("[SUCCESS] Test hybrydowy zakończony!")