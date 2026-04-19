import requests

url = "https://jsonplaceholder.typicode.com/posts/9999"

print("=== TEST 9.4: NEGATIVE ===")

response = requests.get(url)

print(f"[INFO] Status Code: {response.status_code}")

if response.status_code == 404:
    print("[SUCCESS] API poprawnie zwróciło 404 Not Found")
else:
    print("[ERROR] API nie obsłużyło błędu poprawnie")