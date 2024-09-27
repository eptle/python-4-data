from pathlib import Path


def create_from_file(path = '', missing_files='lab1/missing.txt'):
    if path == '':
        dir = Path.cwd()
    else:
        dir = Path(path)

    with open(missing_files, 'r') as missing:
        for new_file in missing:
            Path(path, new_file).touch(exist_ok=True)


if __name__ == '__main__':
    create_from_file()