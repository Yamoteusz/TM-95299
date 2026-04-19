import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Test API",
    "body": "To jest test POST",
    "userId": 1
}

print("=== TEST 9.2: CREATE (POST) ===")

response = requests.post(url, json=data)

print(f"[INFO] Status Code: {response.status_code}")
print(f"[DEBUG] Response: {response.json()}")

if response.status_code == 201:
    print("[SUCCESS] Zasób stworzony pomyślnie!")
else:
    print("[ERROR] Nie udało się utworzyć zasobu!")