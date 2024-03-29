from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os

for pic in os.listdir('.'):
    if pic.endswith('.jpg'):
        img = Image.open(pic)
        fn, flext = os.path.splitext(pic)

        new = img.convert('L')
        new1 = new.filter(ImageFilter.DETAIL)
        new2 = new1.resize((1080, 1080))
        width, height = new2.size

        draw = ImageDraw.Draw(new2)
        text = "rime123!"
        title = "BLACK"
        font = ImageFont.truetype("arial.ttf", 80)
        textwidth, textheight = draw.textsize(text, font)

        m = 10
        x = width - textwidth - m
        y = height - textheight - m

        draw.text((x, y), text, title, font=font)
        
        new2.save('pic/{}{}'.format(fn, flext))
