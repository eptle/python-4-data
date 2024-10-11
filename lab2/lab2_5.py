import argparse
from pathlib import Path
from PIL import Image


def list_of_strings(arg):
    return arg.split(',')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Привет, это просмотрщик картинок на питоне!')
    parser.add_argument('-ft', '--ftype', type=str)
    args = parser.parse_args()

    dir = Path('lab2/src/')

    if args.ftype != None:
        image = Image.open(str(dir) + '/' + args.ftype)
        image.resize((50, 50)).show()
    else:
        print('А где картинка? :(')


# /home/eptel/Documents/GitHub/flask-todo
