import sys

def PANIC(message):
    print(message)
    sys.exit(0)

class GameLogicError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)