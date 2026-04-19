import json
import xml.etree.ElementTree as ET
from pathlib import Path

ANDROID_NS = "{http://schemas.android.com/apk/res/android}"

caps_path = Path("51_caps.json")
selectors_path = Path("53_selectors.json")
manifest_path = Path("../Artefakt02/decompiled_apk/AndroidManifest.xml")
output_path = Path("55_result.xml")

if not caps_path.exists():
    raise FileNotFoundError("Brak 51_caps.json")
if not selectors_path.exists():
    raise FileNotFoundError("Brak 53_selectors.json")
if not manifest_path.exists():
    raise FileNotFoundError("Brak AndroidManifest.xml")

with open(caps_path, "r", encoding="utf-8") as f:
    caps_data = json.load(f)

with open(selectors_path, "r", encoding="utf-8") as f:
    selectors = json.load(f)

tree = ET.parse(manifest_path)
root = tree.getroot()
manifest_package = root.attrib.get("package", "")

caps_package = caps_data.get("appium:appPackage") or caps_data.get("appPackage", "")
target_element = "ACCESSIBILITY"

testsuite = ET.Element("testsuite", name="Artefakt05", tests="2", failures="0")
failures = 0

# Test 1: package match
tc1 = ET.SubElement(testsuite, "testcase", name="package_match")
if caps_package == manifest_package:
    print(f"[PASS] Package OK: {caps_package}")
else:
    failures += 1
    fail = ET.SubElement(tc1, "failure", message="Package mismatch")
    fail.text = f"caps={caps_package}, manifest={manifest_package}"
    print(f"[FAIL] Package mismatch: caps={caps_package}, manifest={manifest_package}")

# Test 2: selector exists
tc2 = ET.SubElement(testsuite, "testcase", name="selector_exists")
if target_element in selectors:
    print(f"[PASS] Selektor {target_element} istnieje w mapie.")
else:
    failures += 1
    fail = ET.SubElement(tc2, "failure", message="Selector missing")
    fail.text = f"Brak klucza {target_element} w 53_selectors.json"
    print(f"[FAIL] Brak selektora {target_element} w mapie.")

testsuite.set("failures", str(failures))
xml_tree = ET.ElementTree(testsuite)
xml_tree.write(output_path, encoding="utf-8", xml_declaration=True)

if failures == 0:
    print("[OK] Wszystkie testy przeszły poprawnie.")
else:
    print("[WARN] Część testów nie przeszła.")

print(f"[OK] Raport zapisano do: {output_path}")