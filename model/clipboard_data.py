from pyperclip import copy
from pyperclip import paste


class ClipboardData:
    def __init__(self):
        pass

    def copy_wallet(self, wallet):
        copy(wallet)

    def clipboard_content(self):
        return paste()
