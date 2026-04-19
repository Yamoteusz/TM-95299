import json
import socket
from pathlib import Path

caps_path = Path("51_caps.json")
selectors_path = Path("53_selectors.json")
output_path = Path("54_session.log")

if not caps_path.exists():
    raise FileNotFoundError("Brak 51_caps.json")
if not selectors_path.exists():
    raise FileNotFoundError("Brak 53_selectors.json")

with open(caps_path, "r", encoding="utf-8") as f:
    caps_data = json.load(f)

with open(selectors_path, "r", encoding="utf-8") as f:
    ui_map = json.load(f)

app_package = caps_data.get("appium:appPackage") or caps_data.get("appPackage")
app_activity = caps_data.get("appium:appActivity") or caps_data.get("appActivity")
device_name = caps_data.get("appium:deviceName") or caps_data.get("deviceName", "Android Emulator")

server_ok = False
try:
    sock = socket.create_connection(("127.0.0.1", 4723), timeout=2)
    sock.close()
    server_ok = True
except Exception:
    server_ok = False

if app_package and app_activity and server_ok:
    status = "READY TO CONNECT"
else:
    status = "NOT READY"

report_lines = [
    "=== ZADANIE 5.4: SESSION READINESS REPORT ===",
    f"Target App : {app_package}",
    f"Main Activity : {app_activity}",
    f"Device : {device_name}",
    f"UI Elements : {len(ui_map)} loaded",
    f"Appium Port 4723 : {'OK' if server_ok else 'NOT AVAILABLE'}",
    f"Status : {status}"
]

report_text = "\n".join(report_lines)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(report_text)

print(report_text)
print(f"\n[OK] Zapisano do: {output_path}")