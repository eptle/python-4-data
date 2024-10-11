from PIL import Image, ImageFont, ImageDraw


if __name__ == "__main__":
    src = 'lab2/src/nature.jpg'
    image = Image.open(src)
    logo = Image.open('lab2/src/logo.png')
    
    watermark = Image.new('RGBA', (100, 100))
    watermark.paste(logo.resize((80, 80)), (10, 0))

    draw = ImageDraw.Draw(watermark)
    font = ImageFont.truetype("lab2/src/Merriweather-Italic.ttf", 22)
    draw.text((20, 70), "Eptel", font=font)
    
    image.paste(watermark, box=(image.width-100, image.height-100), mask=watermark)
    image.save('lab2/src/new.jpg')
    image.show()