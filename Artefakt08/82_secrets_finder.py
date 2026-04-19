import re
from pathlib import Path

root_dir = Path("../Artefakt02/decompiled_apk")
output_path = Path("82_secrets_found.txt")

patterns = {
    "URL": re.compile(r"https?://[^\s\"'<>]+", re.IGNORECASE),
    "IP": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "KEYWORD": re.compile(r"\b(password|passwd|token|secret|apikey|api_key|auth|login|key)\b", re.IGNORECASE),
}

text_extensions = {".xml", ".txt", ".smali", ".json", ".properties"}

if not root_dir.exists():
    raise FileNotFoundError(f"Brak folderu: {root_dir}")

findings = []

for file in root_dir.rglob("*"):
    if file.is_file() and file.suffix.lower() in text_extensions:
        try:
            content = file.read_text(encoding="utf-8", errors="ignore")
            for label, pattern in patterns.items():
                for match in pattern.findall(content):
                    value = match if isinstance(match, str) else str(match)
                    findings.append(f"[{label}] {file}: {value}")
        except Exception:
            continue

with open(output_path, "w", encoding="utf-8") as f:
    if findings:
        f.write("\n".join(findings))
    else:
        f.write("BRAK ZNALEZISK\n")

print(">>> URUCHOMIENIE SKANERA HARDICODED SECRETS <<<")
if findings:
    for item in findings[:20]:
        print(item)
else:
    print("BRAK ZNALEZISK")
print(f"[OK] Zapisano raport do: {output_path}")