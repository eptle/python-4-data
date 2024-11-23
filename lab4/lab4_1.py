from pathlib import Path
from moviepy import *
import numpy as np
import argparse

def main():
    parser = argparse.ArgumentParser(prog='Video cutter')
    parser.add_argument('-i', '--input', help='Путь до файла')
    parser.add_argument('-o', '--output', help='Путь и имя конечного файла')
    parser.add_argument('-s', '--start', type=int, help='Начало фрагмента')
    parser.add_argument('-e', '--end', type=int, help='Конец фрагмента')

    args = parser.parse_args()
    video = VideoFileClip(args.input)

    if args.input == None:
        print('Введите имя файла')
        return None
    if args.input == args.output:
        print('Имя конечного файла должно отличаться от исходного')
        return None
    if args.start == None:
        args.start = 0
    if args.output == None:
        args.output = 'cropped.mp4'
    if (args.start > video.duration) or (args.end > video.duration) or (args.start > args.end):
        print('Неверные данные')
        return None

    video.with_subclip(args.start, args.end).write_videofile(args.output)


if __name__ == '__main__':
    main()

# python3 lab4/lab4_1.py -i lab4/video.mp4 -s 0 -e 4