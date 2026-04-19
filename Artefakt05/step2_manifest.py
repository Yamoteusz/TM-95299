import xml.etree.ElementTree as ET
from pathlib import Path

ANDROID_NS = "{http://schemas.android.com/apk/res/android}"

manifest_path = Path("../Artefakt02/decompiled_apk/AndroidManifest.xml")
output_path = Path("52_inspection.log")

if not manifest_path.exists():
    raise FileNotFoundError(f"Brak pliku: {manifest_path}")

tree = ET.parse(manifest_path)
root = tree.getroot()

package_name = root.attrib.get("package", "BRAK")

permissions = [
    elem.attrib.get(ANDROID_NS + "name", "BRAK")
    for elem in root.findall("uses-permission")
]

activities = []
application = root.find("application")
if application is not None:
    for activity in application.findall("activity"):
        name = activity.attrib.get(ANDROID_NS + "name", "BRAK")
        activities.append(name)

uses_sdk = root.find("uses-sdk")
min_sdk = uses_sdk.attrib.get(ANDROID_NS + "minSdkVersion", "BRAK") if uses_sdk is not None else "BRAK"
target_sdk = uses_sdk.attrib.get(ANDROID_NS + "targetSdkVersion", "BRAK") if uses_sdk is not None else "BRAK"

report_lines = [
    "=== RAPORT ANALIZY ===",
    f"Pakiet główny: {package_name}",
    f"Liczba activity: {len(activities)}",
    f"minSdkVersion: {min_sdk}",
    f"targetSdkVersion: {target_sdk}",
    "",
    "Kluczowe uprawnienia:",
]

for perm in permissions:
    report_lines.append(f"- {perm}")

report_lines.append("")
report_lines.append("Przykładowe activity:")
for act in activities[:10]:
    report_lines.append(f"- {act}")

report_text = "\n".join(report_lines)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(report_text)

print(report_text)
print(f"\n[OK] Sukces! Artefakt zapisany jako: {output_path}")