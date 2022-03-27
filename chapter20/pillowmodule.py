"""
    CHAPTER 21
    TUTORIAL NO. 230
    EDIT IMAGES USING PYTHON
        Installation of pillow library
        change the image extension
        resize image fiels
        resize mulitiple images using for loop
        sharpness
        brightness
        color
        contrast
        Image Blur, GaussianBlurS
"""
from PIL import Image, ImageEnhance
import os
# img = Image.open('image/img1.jpg')
# img.save('Cutedog.png')  # chage image extension
# img.show()  # to open image

# maxsize = (100, 100)
# img.thumbnail(maxsize)
# img.save('image/small_image_of_dog.jpeg')

# how to change all images extensions with os and image module
# for item in os.listdir():
#     if item.endswith('.png'):
#         img = Image.open(item)
#         filename, extension = os.path.splitext(item)
#         img.save(f"{filename}.jpg")


# ---------- increase sharpness of image ----------------
img = Image.open('Cutedog.jpg')
enhancer = ImageEnhance.Color(img)
enhancer.enhance(5).save('enhance.jpg')
# 0 : Blurr
# 1 : Original image
# 2 : image with increased sharpness
img = Image.open('enhance.jpg')
img.show()
