import os
from pathlib import Path
from icecream import ic
import humanize

directory = Path('C:/Users/Vanoha/downloads')
total_size = 0
items = 0
for i in directory.iterdir():
    total_size += i.stat().st_size
    items += 1

ic(items)
ic(total_size)
ic(humanize.naturalsize(total_size))

