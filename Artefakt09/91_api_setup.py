import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

headers = {
    "Content-Type": "application/json"
}

print("=== TEST 9.1: POŁĄCZENIE Z API ===")

response = requests.get(url, headers=headers)

print(f"[INFO] Status Code: {response.status_code}")
print(f"[DEBUG] Response Body: {response.json()}")

if response.status_code == 200:
    print("[SUCCESS] API działa poprawnie!")
else:
    print("[ERROR] API nie odpowiada poprawnie!")