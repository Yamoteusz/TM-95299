import xml.etree.ElementTree as ET
from pathlib import Path

ANDROID_NS = "{http://schemas.android.com/apk/res/android}"

manifest_path = Path("../Artefakt02/decompiled_apk/AndroidManifest.xml")
output_path = Path("RiskyPermission.xml")

risky_permissions_catalog = {
    "android.permission.READ_SMS": "HIGH",
    "android.permission.SEND_SMS": "HIGH",
    "android.permission.READ_CONTACTS": "MEDIUM",
    "android.permission.WRITE_CONTACTS": "MEDIUM",
    "android.permission.ACCESS_FINE_LOCATION": "MEDIUM",
    "android.permission.RECORD_AUDIO": "MEDIUM",
    "android.permission.CAMERA": "MEDIUM",
    "android.permission.READ_CALL_LOG": "HIGH",
    "android.permission.WRITE_EXTERNAL_STORAGE": "LOW",
    "android.permission.READ_EXTERNAL_STORAGE": "LOW",
    "android.permission.INTERNET": "LOW",
}

if not manifest_path.exists():
    raise FileNotFoundError(f"Brak pliku: {manifest_path}")

tree = ET.parse(manifest_path)
root = tree.getroot()

package_name = root.attrib.get("package", "UNKNOWN")
application = root.find("application")

debuggable = "false"
if application is not None:
    debuggable = application.attrib.get(ANDROID_NS + "debuggable", "false").lower()

found_permissions = []
for perm in root.findall("uses-permission"):
    perm_name = perm.attrib.get(ANDROID_NS + "name", "")
    if perm_name in risky_permissions_catalog:
        found_permissions.append((perm_name, risky_permissions_catalog[perm_name]))

report_root = ET.Element("security_audit")
ET.SubElement(report_root, "package").text = package_name
ET.SubElement(report_root, "debuggable").text = debuggable

perms_node = ET.SubElement(report_root, "risky_permissions")
for perm_name, severity in found_permissions:
    p = ET.SubElement(perms_node, "permission", severity=severity)
    p.text = perm_name

ET.ElementTree(report_root).write(output_path, encoding="utf-8", xml_declaration=True)

print(">>> URUCHOMIENIE ANALIZY MANIFESTU <<<")
print(f"[INFO] Pakiet: {package_name}")
print(f"[INFO] Flaga debuggable: {debuggable}")
print(f"[INFO] Wykryto {len(found_permissions)} ryzykownych uprawnień.")
print(f"[OK] Zapisano raport XML: {output_path}")