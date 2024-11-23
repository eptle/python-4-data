from PIL import Image
from moviepy import *
import argparse


def main():
    parser = argparse.ArgumentParser(prog='Video cutter')
    parser.add_argument('-i', '--input', help='Путь до файла')
    parser.add_argument('-o', '--output', help='Папка с кадрами')
    parser.add_argument('-b', '--begin', type=int, help='Начало фрагмента')
    parser.add_argument('-e', '--end', type=int, help='Конец фрагмента')
    parser.add_argument('-s', '--step', type=int, help='Шаг в кадрах в секунду')

    args = parser.parse_args()

    if args.step == None:
        args.step = 10
    if args.input == None:
        print('Введите имя файла')
        return None
    if args.input == args.output:
        print('Имя конечного файла должно отличаться от исходного')
        return None
    if args.begin == None:
        args.begin = 0
    if args.output == None:
        args.output = 'cropped.mp4'

    video = VideoFileClip(args.input)
    if (args.begin > video.duration) or (args.end > video.duration) or (args.begin > args.end):
        print('Неверные данные')
        return None

    cropped = video.with_subclip(args.begin, args.end)
    cur_frame = 0
    while cur_frame / cropped.fps < cropped.duration:
        img = Image.fromarray(cropped.get_frame(cur_frame / cropped.fps)).resize((250, 250))
        img.save(f'{args.output}/{cur_frame}.jpg')
        cur_frame += args.step


if __name__ == '__main__':
    main()

# python3 lab4/lab4_2.py -i lab4/video.mp4 -b 0 -e 4 -o lab4/output