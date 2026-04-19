import json
import xml.etree.ElementTree as ET
from pathlib import Path

xml_file = Path("RiskyPermission.xml")
json_file = Path("83_vulnerabilities.json")
output_file = Path("84_risk_score.txt")

if not xml_file.exists():
    raise FileNotFoundError("Brak RiskyPermission.xml")
if not json_file.exists():
    raise FileNotFoundError("Brak 83_vulnerabilities.json")

score = 100
deductions = []

# XML z uprawnieniami
tree = ET.parse(xml_file)
root = tree.getroot()

debuggable = root.findtext("debuggable", default="false").lower()
permissions = root.findall("./risky_permissions/permission")

if debuggable == "true":
    score -= 30
    deductions.append("Debuggable flag: -30")

score -= len(permissions) * 5
if permissions:
    deductions.append(f"Ryzykowne uprawnienia ({len(permissions)} x -5): -{len(permissions)*5}")

# JSON z bibliotekami
vulns = json.loads(json_file.read_text(encoding="utf-8"))

severity_penalties = {
    "CRITICAL": 40,
    "HIGH": 30,
    "MEDIUM": 15,
    "LOW": 5
}

for v in vulns:
    sev = v.get("severity", "LOW").upper()
    penalty = severity_penalties.get(sev, 5)
    score -= penalty
    deductions.append(f"{v.get('library')} [{sev}]: -{penalty}")

if score < 0:
    score = 0

status = "REJECTED" if score < 50 else "NEEDS FIX" if score < 80 else "APPROVED"

report = []
report.append(">>> ZADANIE 8.4: OBLICZANIE SECURITY SCORE <<<")
report.append(f"WYNIK KOŃCOWY: {score}/100")
report.append(f"STATUS: {status}")
report.append("")
report.append("DEDUKCJE:")
report.extend(deductions)

text = "\n".join(report)
print(text)

output_file.write_text(text, encoding="utf-8")
print(f"\n[OK] Zapisano wynik do: {output_file}")