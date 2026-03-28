import xml.etree.ElementTree as ET
import glob
import json
import os

def mine_selectors(path):
    results = []
    # Przeszukiwanie wszystkich plików XML
    for file in glob.glob(path + "/**/*.xml", recursive=True):
        try:
            tree = ET.parse(file)
            for elem in tree.iter():
                res_id = elem.get('{http://schemas.android.com/apk/res/android}id')
                if res_id:
                    results.append({
                        "file": os.path.basename(file),
                        "id": res_id.split('/')[-1],
                        "tag": elem.tag
                    })
        except Exception:
            continue
            
    # Zapis do pliku JSON
    with open('miner_report.json', 'w') as f:
        json.dump(results, f, indent=4)
    print(f"[OK] Extracted {len(results)} IDs")

mine_selectors("../Artefakt02/decompiled_apk/res/layout")