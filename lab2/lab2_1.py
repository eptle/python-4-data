from PIL import Image


if __name__ == "__main__":
    image = Image.open('lab2/src/nature.jpg')
    width = image.width
    height = image.height

    r, g, b = image.split()
    channel_height = r.height // 3
    channel_width = r.width // 3
    r = r.resize((channel_width, channel_height))
    g = g.resize((channel_width, channel_height))
    b = b.resize((channel_width, channel_height))

    canvas = Image.new('RGB', (width + channel_width, height))
    canvas.paste(image, (0, 0))
    canvas.paste(r, (width, 0))
    canvas.paste(g, (width, channel_height))
    canvas.paste(b, (width, channel_height * 2))

    canvas.show()