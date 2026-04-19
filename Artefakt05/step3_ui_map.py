import json
import xml.etree.ElementTree as ET
from pathlib import Path

ANDROID_NS = "{http://schemas.android.com/apk/res/android}"
layout_dir = Path("../Artefakt02/decompiled_apk/res/layout")
output_path = Path("53_selectors.json")

if not layout_dir.exists():
    raise FileNotFoundError(f"Brak folderu: {layout_dir}")

ui_map = {}

for xml_file in layout_dir.rglob("*.xml"):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for elem in root.iter():
            res_id = elem.attrib.get(ANDROID_NS + "id")
            if res_id:
                clean_id = res_id.split("/")[-1]
                business_name = clean_id.upper()
                ui_map[business_name] = clean_id
    except Exception:
        continue

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(ui_map, f, indent=4, ensure_ascii=False, sort_keys=True)

print(f"Zmapowano {len(ui_map)} unikalnych elementów UI.")
print(f"Zapisano plik: {output_path}")