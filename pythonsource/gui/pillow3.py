from PIL import Image, ImageFilter

image = Image.open("d:\JJH\py\jarong.jpg")

# Thumbnail 이미지 생성
size = (64, 64)
image.thumbnail(size)

image.save("d:\JJH\py\jarong.jpg-thumb.jpg")


# 크기 조정
image2 = Image.open("d:\JJH\py\jarong.jpg")
image2 = image.resize((600, 600))
image2.save("d:\JJH\py\jarong.jpg-resize.jpg")


# 회전
image3 = Image.open("d:\JJH\py\jarong.jpg")
image3.rotate(90).save("d:\JJH\py\jarong.jpg-rotate.jpg")


# blur
image4 = Image.open("d:\JJH\py\jarong.jpg")
image4.filter(ImageFilter.BLUR).save("d:\JJH\py\jarong.jpg-blur.jpg")
