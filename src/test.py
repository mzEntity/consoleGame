import os
import shutil

# 获取终端窗口的大小
size = shutil.get_terminal_size()
columns = size.columns
lines = size.lines

print(f"终端窗口宽度: {columns} 列")
print(f"终端窗口高度: {lines} 行")