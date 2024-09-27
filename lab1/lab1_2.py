import argparse
from pathlib import Path


def list_of_strings(arg):
    return arg.split(',')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Привет, это парсер командной строки на python')
    parser.add_argument('-d', '--dirpath', type=str, default=Path.cwd())
    parser.add_argument('-f', '--files', type=list_of_strings)
    args = parser.parse_args()

    dir = Path(args.dirpath)
    files = list(dir.iterdir())
    print(files)

    if args.files != None:
        filenames = list(file.name for file in files)
        Path('lab1/missing.txt').touch(exist_ok=True)
        Path('lab1/contained.txt').touch(exist_ok=True)
        with open(r'lab1/missing.txt', 'w') as missing, open(r'lab1/contained.txt', 'w') as contained:
            for file in args.files:
                contained.write(file + '\n') if file in filenames else missing.write(file + '\n')
    else:
        print(*zip([file.name for file in files], [file.stat().st_size for file in files]), sep='\n')


# /home/eptel/Documents/GitHub/flask-todo
