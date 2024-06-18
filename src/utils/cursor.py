from others.singleton import singleton

class CursorPosition:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        
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

@singleton
class CursorManager:
    def __init__(self):
        self.cursor_x = 0
        self.cursor_y = 0

    def position(self):
        return CursorPosition(self.cursor_x, self.cursor_y)
    
    def offset(self, cp: CursorPosition):
        return cp.pos_x - self.cursor_x, cp.pos_y - self.cursor_y
    
    def set(self, cp: CursorPosition):
        self.cursor_x = cp.pos_x
        self.cursor_y = cp.pos_y
        
def goto(cp: CursorPosition):
    cm = CursorManager()
    offset_x, offset_y = cm.offset(cp)
    
    if offset_x > 0:
        move_cursor_down(offset_x)       
    elif offset_x < 0:
        move_cursor_up(-offset_x)
        
    if offset_y > 0:
        move_cursor_right(offset_y)
    elif offset_y < 0:
        move_cursor_left(-offset_y)
        
    cm.set(cp)
        
def record():
    cm = CursorManager()
    return cm.position()
        
def cprint(message: str):
    lines = message.split("\n")
    line_count = len(lines)
    enter_count = line_count - 1
    if line_count == 0:
        return
    if len(lines[line_count-1]) == 0:
        lines.pop(line_count-1)

    cur_enter_count = 0
    for line in lines:
        cprintline(line)
        if cur_enter_count < enter_count:
            cnewline(1)
            cur_enter_count += 1

def cprintline(message: str):
    length = len(message)
    cm = CursorManager()
    cm.cursor_y += length
    print(message, end="")
    
def cnewline(n: int):
    cm = CursorManager()
    cm.cursor_x += n
    cm.cursor_y = 0
    print("\n" * n, end="")
    