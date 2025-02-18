import os
from pathlib import Path
from icecream import ic

# dir = r'C:\Users\Vanoha\Downloads'
directory = Path('C:/Users/Vanoha/downloads')
# print(dir)
# for i in directory.iterdir():
#     ic(i)
ic(directory.stat().st_size)
# [ic(i) for i in directory.stat()]
# help(os.stat_result)