import random
import shutil
import time
import os

# Characters used in the Matrix rain
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"

# Get the size of the terminal window
columns, rows = shutil.get_terminal_size()
columns = columns // 2  # Adjust for character width

# Create drops for each column
drops = [0 for _ in range(columns)]

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

try:
    while True:
        print("\033[1;32m")  # Set text to bright green
        for i in range(rows):
            line = ""
            for j in range(columns):
                char = random.choice(chars) if random.random() > 0.9 else " "
                if drops[j] < i:
                    char = " "
                line += char + " "
            print(line)
        drops = [drop + 1 if random.random() > 0.1 else 0 for drop in drops]
        time.sleep(0.1)
        clear_screen()
except KeyboardInterrupt:
    clear_screen()
    print("Matrix effect stopped.")
