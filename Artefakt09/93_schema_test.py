import requests
from jsonschema import validate

url = "https://jsonplaceholder.typicode.com/todos/1"

schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "completed": {"type": "boolean"}
    },
    "required": ["userId", "id", "title", "completed"]
}

print("=== TEST 9.3: WALIDACJA JSON ===")

response = requests.get(url)
data = response.json()

validate(instance=data, schema=schema)

print("[SUCCESS] JSON poprawny!")
print(f"[DEBUG] Dane: {data}")