import cv2
from PIL import Image, ImageFilter
import os
from matplotlib import pyplot as plt

image = Image.open("./clean.jpg")
img = cv2.imread("./clean.jpg")
(h, w) = img.shape[:2]
print((h,w))
box = (int(w*.1), int(h*.01), int(w-w*.1), int(h-h*.01))
box1 = (0,0,int(w*.1), int(h-h*.01)) #left
box2 = (int(w-w*.1), 0, int(w), int(h)) #right
box3 = (0,0, int(w), int(h*.01)) #top
box4 = (0, int(h-h*.01), int(w), int(h)) #botton
#print(box)
img = image.copy()
#crop_img = image.crop(box2)
# Use GaussianBlur directly to blur the image 10 times. 
for each1 in box1, box2, box3, box4:
    each = image.crop(each1)
    yyy = (each.filter(ImageFilter.ModeFilter(size=71)))
    img.paste(yyy, each1[:2])
img.show()

#blur_image = crop_img.filter(ImageFilter.ModeFilter(size=71))
#image.paste(blur_image, box)
#blur_image.show()
