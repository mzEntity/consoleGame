def cursor_up(n: int) -> str:
    return f"\033[{n}A"

def cursor_down(n: int) -> str:
    return f"\033[{n}B"

def cursor_right(n: int) -> str:
    return f"\033[{n}C"

def cursor_left(n: int) -> str:
    return f"\033[{n}D"

def move_cursor_up(n: int):
    print(cursor_up(n), end="")
    
def move_cursor_down(n: int):
    print(cursor_down(n), end="")
    
def move_cursor_right(n: int):
    print(cursor_right(n), end="")

def move_cursor_left(n: int):
    print(cursor_left(n), end="")