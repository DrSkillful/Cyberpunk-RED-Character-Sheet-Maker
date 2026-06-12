# This file is for testing code, before putting it in the main file


from PIL import Image, ImageDraw, ImageFont

image_first_page = Image.open("assets/1-1.png")
image_second_page = Image.open("assets/1-2.png")
image_third_page = Image.open("assets/1-3.png")

draw = ImageDraw.Draw(image_first_page)
position_y = 196
position_start = (625, position_y)

for i in range(10):
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    print(position_start)
    position_y += 120 - i
    position_start = (625, position_y)

    if i == 0:
        position_y = 196
        position_start = (625, position_y)

    if i == 6 or i == 9:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
        position_y += 20
        position_start = (670, position_y)

    draw.text(position_start, "10", font=font)


image_first_page.show()