from utils.cursor import *

cprint("hello p1: ")
cp1 = record()
cprint("\nhello p2: ")
cp2 = record()
goto(cp1)
cprint("<- p1")
goto(cp2)
cprint("<- p2")