class Alert:
    @staticmethod
    def error(msg: str) -> None:
        print(f"\033[1;31;40m {msg}  \033[0m \n")
