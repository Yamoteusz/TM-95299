import xml.etree.ElementTree as ET
import glob
import json
import os

def analyze_a11y(path):
    gaps = []
    ns = '{http://schemas.android.com/apk/res/android}'
    
    for file in glob.glob(path + "/**/*.xml", recursive=True):
        try:
            tree = ET.parse(file)
            for elem in tree.iter():
                node_text = elem.get(f'{ns}text')
                node_desc = elem.get(f'{ns}contentDescription')
                node_id = elem.get(f'{ns}id', 'no-id')
                
                if node_text and not node_desc:
                    gaps.append({
                        "file": os.path.basename(file),
                        "id": node_id.split('/')[-1],
                        "text": node_text,
                        "issue": "Brak atrybutu contentDescription"
                    })
        except:
            continue
            
    with open('a11y_report.json', 'w') as f:
        json.dump(gaps, f, indent=4)
        
analyze_a11y("../Artefakt02/decompiled_apk/res/layout")