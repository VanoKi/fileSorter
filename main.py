from pathlib import Path
from icecream import ic
from time import time

start = time()
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
dict = {}
for i in directory.iterdir():
    if i.is_file():
        key = i.suffix
        size = i.stat().st_size
        if key in dict:
            dict[key][0] += 1
            dict[key][1] += size
        else:
            dict[key] = [1, size]

end = time()
ic(end - start)
ic([f'{dict[i][0]} files have extension {i} and total size {round(dict[i][1] / 1048576, 2)}mb' for i in dict])
