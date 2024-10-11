from PIL import Image, ImageFont, ImageDraw
import copy


if __name__ == "__main__":
    folder = 'lab2/src/'

    image = Image.new('RGB', (100, 100))

    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0) + image.size, fill=None, width=5, outline='#0000ff')

    font = ImageFont.truetype("lab2/src/Merriweather-Italic.ttf", 70)
    
    for i in range(1, 3 + 1):
        im = copy.copy(image)
        print(im is image)
        im_draw = ImageDraw.Draw(im)
        im_draw.text((30, 10), text=str(i), font=font)
        im.save(folder + f'img_{i}.jpg')
        im.show()
