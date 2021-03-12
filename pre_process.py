import cv2 as cv
import numpy as np
import os
from PIL import Image

def make_binary(src):

    img = cv.imread(src)
    img = cv.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    thresh = 127
    img = cv.threshold(img, thresh, 255, cv.THRESH_BINARY_INV)[1]
    img = cv.dilate(img, np.ones((5,5)),iterations=2)
    img = cv.erode(img, np.ones((5,5)),iterations=1)
    img = cv.resize(img,(21,21), interpolation=cv.INTER_AREA)
    return img
    

path= os.path.abspath("input")

extensions= ['PNG']

if __name__ == "__main__":

    for f in os.listdir(path):

        if os.path.isfile(os.path.join(path,f)):

            f_text, f_ext= os.path.splitext(f)

            f_ext= f_ext[1:].upper()

            if f_ext in extensions:

                print (f)
                img = make_binary(os.path.join(path,f))
                cv.imwrite(os.path.join(path,f), img)
                

