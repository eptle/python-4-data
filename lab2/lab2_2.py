from PIL import Image


if __name__ == "__main__":
    src = 'lab2/src/nature.jpg'
    image = Image.open(src)
    width = image.width
    height = image.height

    r, g, b = 0, 0, 0

    for i in range(width):
        for j in range(height):
            cur_r, cur_g, cur_b = image.getpixel((i, j))
            r += cur_r
            g += cur_g
            b += cur_b

    max_color = max(r, g, b)

    if r == max_color:
        print('dominate color is red')
    if g == max_color:
        print('dominate color is green')
    if b == max_color:
        print('dominate color is blue')