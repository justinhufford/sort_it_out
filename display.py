import os
import sys

def logo():
    print("""
 ▄▄                      ▄▄         ▄
█  ▀        █      █    █  █     █  █
 ▀▀▄  ▄   ▄ █▀   ▀ █▀   █  █ ▄ ▄ █▀ █
█  █ █ █ █  █    █ █    █  █ █ █ █  ▀
 ▀▀   ▀  ▀  ▀▀   ▀ ▀▀    ▀▀   ▀▀ ▀▀ ▀
""")
    
def clear():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Unix-based systems
    else:
        os.system('clear')

def clear_lines(num_lines=1):
    for _ in range(num_lines):
        sys.stdout.write("\033[F\033[K")

def color_text(text, color):
    """
    Colors the given text using ANSI escape codes.
    
    color: str - The color name ('red', 'green', 'yellow', 'blue', etc.)
    """
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    
    return f"{colors.get(color, colors['reset'])}{text}{colors['reset']}"
