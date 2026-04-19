import json
import xml.etree.ElementTree as ET
from pathlib import Path

ANDROID_NS = "{http://schemas.android.com/apk/res/android}"

manifest_path = Path("../Artefakt02/decompiled_apk/AndroidManifest.xml")
output_path = Path("51_caps.json")

if not manifest_path.exists():
    raise FileNotFoundError(f"Brak pliku: {manifest_path}")

tree = ET.parse(manifest_path)
root = tree.getroot()

package_name = root.attrib.get("package", "")
launch_activity = None

application = root.find("application")
if application is not None:
    for activity in application.findall("activity"):
        activity_name = activity.attrib.get(ANDROID_NS + "name", "")

        for intent_filter in activity.findall("intent-filter"):
            has_main = False
            has_launcher = False

            for action in intent_filter.findall("action"):
                if action.attrib.get(ANDROID_NS + "name") == "android.intent.action.MAIN":
                    has_main = True

            for category in intent_filter.findall("category"):
                if category.attrib.get(ANDROID_NS + "name") == "android.intent.category.LAUNCHER":
                    has_launcher = True

            if has_main and has_launcher:
                if activity_name.startswith("."):
                    launch_activity = package_name + activity_name
                elif "." not in activity_name:
                    launch_activity = package_name + "." + activity_name
                else:
                    launch_activity = activity_name
                break

        if launch_activity:
            break

if not package_name or not launch_activity:
    raise ValueError("Nie udało się wykryć appPackage lub appActivity z manifestu.")

caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "Android Emulator",
    "appium:appPackage": package_name,
    "appium:appActivity": launch_activity,
    "appium:noReset": True
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(caps, f, indent=4, ensure_ascii=False)

print("Sukces! Wykryto:")
print(f"Package: {package_name}")
print(f"Activity: {launch_activity}")
print(f"Zapisano do: {output_path}")