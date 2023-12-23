import os


class Terminal:
    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")
