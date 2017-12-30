import matplotlib.pyplot as plt
from skimage import data,color,morphology,filters,feature,segmentation,measure,io
import numpy as np
from matplotlib import patches as mpatches
from PIL import Image
import os

cwd=os.getcwd()
image=io.imread('IMG_0494.JPG')
# image=data.coins()
image_grey=color.rgb2grey(image)
rows,cols=image_grey.shape

image_=Image.open('IMG_0494.JPG')
w,h=image_.size

for i in range(rows):
    for j in range(cols):
        if(image_grey[i,j]<=0.5):
            image_grey[i,j]=0
        else:
            image_grey[i,j]=1

edgs=feature.canny(image_grey)
label_image=measure.label(image_grey,connectivity=1,background=1)
fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(8, 6))
ax0.imshow(image_grey, plt.cm.gray)
ax1.imshow(image)
print('regions number:',label_image.max()+1)

i=0
for region in measure.regionprops(label_image):  # 循环得到每一个连通区域属性集

    # 忽略小区域
    if region.area < 50:
        continue

    # 绘制外包矩形
    minr, minc, maxr, maxc = region.bbox
    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='red', linewidth=1)
    box=(minr-3,minc-3,maxr+3,maxc+3)
    print(box)
    roi=image_.crop(box)
    roi.save(cwd+'/rapeseed/'+str(i)+'.jpg')
    i +=1
    ax1.add_patch(rect)

fig.tight_layout()
plt.show()
