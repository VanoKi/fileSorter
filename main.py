import os
from pathlib import Path
from icecream import ic
import humanize
import time

start = time.time()
directory = Path('C:/Users/Vanoha/downloads')
def directory_size(folder):
    total_size = 0
    for i in folder.iterdir():
        if i.is_dir():
            total_size += directory_size(i)
        else:
            # ic(i.stat().st_size)
            total_size += i.stat().st_size
    return total_size
# ic(humanize.naturalsize(directory_size(directory)))
dict = {}
for i in directory.iterdir():
    if i.is_file():
        # ic(i.suffix)
        key = i.suffix
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1

end = time.time()
ic(end - start)
ic(dict)