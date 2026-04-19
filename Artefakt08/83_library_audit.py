import json
from pathlib import Path

requirements_file = Path("requirements.txt")
output_file = Path("83_vulnerabilities.json")

fake_cve_db = {
    "com.google.android.gms:10.0.1": {
        "cve": "CVE-2018-1234",
        "severity": "CRITICAL",
        "issue": "Stary framework usług Google z luką bezpieczeństwa"
    },
    "com.squareup.okhttp:2.7.5": {
        "cve": "CVE-2016-2402",
        "severity": "HIGH",
        "issue": "Podatność na MitM w starej wersji OkHttp"
    },
    "org.apache.commons:1.0.0": {
        "cve": "CVE-2015-9999",
        "severity": "CRITICAL",
        "issue": "Znana biblioteka zdalnego wykonania kodu (RCE)"
    },
    "com.android.support:25.0.0": {
        "cve": "CVE-2018-9543",
        "severity": "MEDIUM",
        "issue": "Stara biblioteka support z lukami kompatybilności i wyciekami"
    }
}

if not requirements_file.exists():
    raise FileNotFoundError("Brak requirements.txt")

libs = [line.strip() for line in requirements_file.read_text(encoding="utf-8").splitlines() if line.strip()]
results = []

print(">>> ZADANIE 8.3: ANALIZA ŁAŃCUCHA DOSTAW <<<")

for lib in libs:
    if lib in fake_cve_db:
        item = {"library": lib, **fake_cve_db[lib]}
        results.append(item)
        print(f"[{item['severity']}] {lib} -> {item['cve']} | {item['issue']}")
    else:
        print(f"[OK] {lib} -> BRAK ZNANEJ PODATNOŚCI")

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)

print(f"[OK] Zapisano raport JSON: {output_file}")