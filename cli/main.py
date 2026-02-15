from simple_term_menu import TerminalMenu
import sys

from cli.fetch_data import fetch_info

options = ["Get Random User Info", "Exit"]

menu = TerminalMenu(options, title="Random User Info Generator")
while True:
    menu.show()

    if menu.chosen_menu_index == 0:
        print("====================")
        print(fetch_info())
        print("====================")
    else:
        print("GoodBye!")
        sys.exit()