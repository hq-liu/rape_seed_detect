import matplotlib.pyplot as plt
from skimage import data,color,morphology,filters,feature,segmentation,measure,io
import numpy as np
from matplotlib import patches as mpatches

image=io.imread('IMG_0462.JPG')
# image=data.coins()
image_grey=color.rgb2grey(image)
rows,cols=image_grey.shape

for i in range(rows):
    for j in range(cols):
        if(image_grey[i,j]<=0.5):
            image_grey[i,j]=0
        else:
            image_grey[i,j]=1

edgs=feature.canny(image_grey)
plt.imshow(edgs)
plt.show()
