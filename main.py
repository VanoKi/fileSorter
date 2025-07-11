from shutil import copy2
from loguru import logger
from pathlib import Path
from time import time
from datetime import datetime

def setup_loger():
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = f'sorter_{now}.log'
    log_format = "<green>{time}</green> | <level>{level}</level> | <cyan>{message}</cyan>"
    logger.add(lambda msg: print(msg, end=''), colorize=True, format=log_format)
    logger.add(log_file, level='INFO', format=log_format)
    logger.info(Path.cwd())

directory = Path('C:/Users/Vanoha/downloads/Telegram Desktop')
destination = Path('E:/SORTED')
def directory_size(folder):
    total_size = 0
    dict = {}
    for i in folder.iterdir():
        if i.is_dir():
            total_size += directory_size(i)
        else:
            # ic(i.stat().st_size)
            total_size += i.stat().st_size
    return total_size

def show_total_size():
    start = time()
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
    logger.info(end - start)
    [logger.info(f'{dict[i][0]} files have extension {i} and total size {round(dict[i][1] / 1048576, 2)}mb') for i in dict]
# show_total_size()

GROUPS = {
    "Documents": ['.pdf', '.epub', '.mobi', '.txt', '.doc', '.docx', '.djvu', '.fb2'],
    "Images": ['.jpg', '.jpeg', '.png', '.gif'],
    "Audio": ['.mp3', '.wav', '.ogg'],
    "Video": ['.mp4', '.avi', '.mkv'],
    "Archives": ['.zip', '.rar', '.7z', '.gz'],
    "Executables": ['.exe', '.msi', '.apk'],
    "Torrents" : ['.torrent'],
    "Figma" : ['.fig']
}

def main():
    setup_loger()
    start = time()
    for file in directory.iterdir():
        file: Path
        if file.is_file():
            for folder in GROUPS:
                if file.suffix.lower() in GROUPS[folder]:
                    path_to_file = destination / folder
                    Path(path_to_file).mkdir(exist_ok=True, parents=True)
                    copy2(file, f'{destination}/{folder}')
                    logger.info(f'file {file.suffix}: {file.stem} copied to dir: {path_to_file}')
                    file.unlink()
                    logger.info(f'file {file.suffix}: {file.stem} deleted from {directory}')
                    break
                # else:
                #     path_to_other = f'{destination}/Other'
                #     Path(path_to_other).mkdir(exist_ok=True, parents=True)
                #     logger.info(f'file{file.suffix}: {file.stem} copied to dir: {path_to_other}')
                #     copy2(file, path_to_other)
    logger.info(time() - start)

if __name__ == "__main__":
    main()

