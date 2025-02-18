import os
from pathlib import Path
from icecream import ic
import humanize

# dir = r'C:\Users\Vanoha\Downloads'
directory = Path('C:/Users/Vanoha/downloads')
# print(dir)
# for i in directory.iterdir():
#     ic(i)
# ic(directory.stat().st_size)
ic(humanize.naturalsize(directory.stat().st_size, binary=True))
# [ic(i) for i in directory.stat()]
# help(os.stat_result)