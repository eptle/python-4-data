from pathlib import Path
import skimage as ski
import numpy as np


def image_transformation(images, num, dir_to_save=Path.cwd()):
    img_ln = len(images)
    match num:
        case '1':
            for i, img in enumerate(images):
                path = str(dir_to_save) + '/' + f'{i + img_ln}.jpg'.rjust(8, '0')

                new_img = ski.exposure.adjust_gamma(img, 3)
                ski.io.imsave(path, new_img)
        case '2':
            for i, img in enumerate(images):
                path = str(dir_to_save) + '/' + f'{i + img_ln}.jpg'.rjust(8, '0')

                new_img = np.flip(img)
                ski.io.imsave(path, new_img)
        case '3':
            for i, img in enumerate(images):
                path = str(dir_to_save) + '/' + f'{i + img_ln}.jpg'.rjust(8, '0')
                img = img / 255.0
                new_img = ski.util.random_noise(img)
                ski.io.imsave(path, (new_img * 255).astype(np.uint8))
        case '4':
            for i, img in enumerate(images):
                path = str(dir_to_save) + '/' + f'{i + img_ln}.jpg'.rjust(8, '0')

                img = img / 255.0
                new_img = ski.transform.rotate(img, 30)
                ski.io.imsave(path, (new_img * 255).astype(np.uint8))
        case '5':
            for i, img in enumerate(images):
                path = str(dir_to_save) + '/' + f'{i + img_ln}.jpg'.rjust(8, '0')

                new_img = img[:, :, (2, 0, 1)]
                ski.io.imsave(path, new_img)
        case '6':
            for i, img in enumerate(images):
                path = str(dir_to_save) + '/' + f'{i + img_ln}.jpg'.rjust(8, '0')

                new_img = img[:, :, (2, 0, 1)]
                new_img = ski.exposure.adjust_gamma(img, 3)

                img = img / 255.0
                new_img = ski.util.random_noise(img)
                ski.io.imsave(path, (new_img * 255).astype(np.uint8))
        case _:
            print('неправильный номер :(')


def transform_image(path = ''):
    if path == '':
        dir = Path.cwd()
    else:
        dir = Path(path)

    dir_to_save = dir

    images = sorted(list(dir.iterdir()))
    np_images = ski.io.imread_collection(images)

    print(*images, sep='\n')
    # print(np_images, sep='\n')

    print('Выберите преобразование:')
    print('1) Повысить контрастность')
    print('2) Отразить по горизонтали')
    print('3) Добавить шум')
    print('4) Повернуть на 30 градусов по часовой стрелке (фон черный)')
    print('5) Смена каналов (RGB -> BRG)')
    print('6) Комплексное (контрастность, смена каналов, шум)')

    num_of_transformation = '6'

    image_transformation(np_images, num_of_transformation, dir_to_save)


if __name__ == '__main__':
    transform_image('/home/eptel/Documents/GitHub/python-4-data/lab3/plates/train/cleaned')