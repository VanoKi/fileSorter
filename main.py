import os
from pathlib import Path
from icecream import ic
import humanize

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

ic(humanize.naturalsize(directory_size(directory)))
