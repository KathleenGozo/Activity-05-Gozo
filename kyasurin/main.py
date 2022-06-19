import cv2 as cv
import numpy as np

def imgpixelcount(img):
    setpixelcount = 100000
    size = img.size

    if size < setpixelcount:
        print("The currently loaded image is higher than the set pixel count.")
    else:
        print("The currently loaded image is lower than the set pixel count.")

    getImageType(img)

def getImageType(img):
    dataType =img.dtype
    print("The image datatype is ", dataType)

def dimentionValildation(img):
    size = img.shape

    x = 900
    y = 900

    if size[0] > x and size[1] > y:
        print("The currently loaded image is not within the boundaries")
    else:
        print("The currently loaded image is within the boundaries")

    imgpixelcount(img)

def accesspx(img):
    x = int(input("Enter x coordinate: "))
    y = int(input("Enter y coordinate: "))
    c = int(input("Enter attribute color 0 for blue, 1 for green and 2 for red: "))

    px = img.item(x,y,c)
    print("Pixel value: ", px)

    img.itemset((x,y,c), 100)
    px = img.item(x,y,c)
    print("After modify: ",px)

    dimentionValildation(img)


img = cv.imread('picture.jpg')

if(len(img.shape) < 3):
      print("Grayscale image is not allowed")
else:
    accesspx(img)


