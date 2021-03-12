import os, sys
from IPython.display import display
from IPython.display import Image as _Imgdis
from PIL import Image
import numpy as np
from time import time
from time import sleep

folder = "input"

onlyfiles = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

print("Working with {0} images".format(len(onlyfiles)))

from scipy import ndimage
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

train_files = []
y_train = []
i=0
for _file in onlyfiles:
    train_files.append(_file)
    label_in_file = _file.find(" ")
    y_train.append(int(_file[0:label_in_file]))
    
print("Files in train_files: %d" % len(train_files))

# Original Dimensions
image_width = 21  
image_height = 21
ratio = 1  #resizing factor

image_width = int(image_width / ratio)
image_height = int(image_height / ratio)

channels = 3
nb_classes = 1

dataset = np.ndarray(shape=(len(train_files), image_height, image_width, channels),
                     dtype=np.float32)

i = 0
for _file in train_files:
    img = load_img(folder + "/" + _file) 
    img.thumbnail((image_width, image_height))
    # Convert to Numpy Array
    x = img_to_array(img)  
    #x = x.reshape((3, 48, 48))
    # Normalize
    x = (x - 128.0) / 128.0
    dataset[i] = x
    i += 1
    if i % 250 == 0:
        print("%d images to array" % i)
print("All images to array!")
from sklearn.model_selection import train_test_split

print(np.shape(dataset))

Xtrain_monochrome = dataset.mean(axis=3)

Xtrain_monochrome[Xtrain_monochrome < 0 ] = 0
#Xtrain_monochrome = Xtrain_monochrome/3
print(np.shape(Xtrain_monochrome))
np.save("XtestNumta", Xtrain_monochrome)
import matplotlib.pyplot as plt
plt.imshow(Xtrain_monochrome[0])
plt.show()