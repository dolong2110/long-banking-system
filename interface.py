import os


def clean_terminal_screen():
    """
    Cleans the terminal screen by performing a system
    clear command. Cls on windows and Clear on UNIX ones.
    """

    os.system('cls' if os.name == 'nt' else 'clear')

def display_horizontal_line():
    """
    A pretty decorative horizontal line.
    """

    print("───────────────────────────────────────────────────────────────")