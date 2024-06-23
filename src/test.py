import msvcrt

def getch():
    return msvcrt.getch()

print("Press any key:")
char = getch()
print(f"You pressed: {char.decode('utf-8')}")
