from pathlib import Path
import shutil


def copy_small_files(path = '', size = 2048):
    if path == '':
        dir = Path.cwd()
    else:
        dir = Path(path)

    files = list(dir.iterdir())
    small_files = [file for file in files if file.stat().st_size <= size and file.is_file()]
    if len(small_files) == 0:
        return None
    
    small_dir = Path('lab1/small')
    small_dir.mkdir(exist_ok=True)

    for file in small_files:
        shutil.copy(str(file), str(small_dir))
        print(file.name)


if __name__ == '__main__':
    copy_small_files('/home/eptel/Documents/GitHub/flask-todo')
