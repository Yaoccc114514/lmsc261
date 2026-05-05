import time, json, subprocess
from datetime import datetime
from pynput import keyboard, mouse

work_time = idle_time = distraction_time = 0
last_input_time = time.time()

check_interval = 5
idle_threshold = 30

work_apps = [
    "Code", "Live", "Logic Pro", "Notion", "Unity",
    "Unity Hub", "Wwise Launcher", "Wwise2019",
    "Microsoft Word", "Sibelius"
]

work_web_keywords = [
    "notion", "docs", "google docs", "github", "figma",
    "canvas", "lecture", "assignment", "python", "unity",
    "wwise", "google translate", "study", "music", "track"
]

def on_input(*args):
    global last_input_time
    last_input_time = time.time()

def run_script(script):
    try:
        return subprocess.check_output(["osascript", "-e", script]).decode().strip()
    except:
        return ""

def get_active_app():
    return run_script('''
    tell application "System Events"
        name of first application process whose frontmost is true
    end tell
    ''')

def get_page_title(app_name):
    if app_name == "Google Chrome":
        return run_script('''
        tell application "Google Chrome"
            if windows is not {} then
                return title of active tab of front window
            end if
        end tell
        ''')
    if app_name == "Safari":
        return run_script('''
        tell application "Safari"
            if windows is not {} then
                return name of current tab of front window
            end if
        end tell
        ''')
    return ""

def has_keyword(text, keywords):
    text = text.lower()
    for word in keywords:
        if word.lower() in text:
            return True
    return False

def is_work_context(app_name, page_title):
    if app_name in work_apps:
        return True

    if app_name in ["Google Chrome", "Safari"]:
        if has_keyword(page_title, work_web_keywords):
            return True

    return False

def format_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h}h {m}m {s}s"


def calculate_percentages():
    total = work_time + idle_time + distraction_time
    if total == 0:
        return 0, 0, 0, 0
    work_percent = work_time / total * 100
    idle_percent = idle_time / total * 100
    distraction_percent = distraction_time / total * 100
    efficiency_percent = 100 - idle_percent - distraction_percent
    return work_percent, idle_percent, distraction_percent, efficiency_percent

def get_distraction_level(efficiency_percent):
    if efficiency_percent > 90:
        return "高效"
    if efficiency_percent > 80:
        return "良好"
    if efficiency_percent > 70:
        return "中等"
    return "严重走神"

def print_summary():
    _, _, _, efficiency_percent = calculate_percentages()
    print("\nToday's Summary:")
    print("Work Time:", format_time(work_time))
    print("Idle Time:", format_time(idle_time))
    print("Distraction Time:", format_time(distraction_time))
    print("\nEfficiency:")
    print(f"Efficiency %: {efficiency_percent:.2f}%")
    print("Distraction Level:", get_distraction_level(efficiency_percent))

keyboard_listener = keyboard.Listener(on_press=on_input)
mouse_listener = mouse.Listener(on_move=on_input, on_click=on_input, on_scroll=on_input)
keyboard_listener.start()
mouse_listener.start()

try:
    while True:
        app_name = get_active_app()
        page_title = get_page_title(app_name)

        if time.time() - last_input_time < idle_threshold:
            if is_work_context(app_name, page_title):
                work_time += check_interval
                print("Working:", app_name, "|", page_title)
            else:
                distraction_time += check_interval
                print("Distraction:", app_name, "|", page_title)
        else:
            idle_time += check_interval
            print("Idle... no computer use detected")

        time.sleep(check_interval)

except KeyboardInterrupt:
    print("\nStopped tracking.")
    print_summary()

finally:
    keyboard_listener.stop()
    mouse_listener.stop()
