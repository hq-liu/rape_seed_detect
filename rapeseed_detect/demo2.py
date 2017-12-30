from PIL import Image
import matplotlib.pyplot as plt
import os

cwd=os.getcwd()
image=Image.open('IMG_0462.JPG')
w,h=image.size
num=4000

for i in range(1,w,40):
    for j in range(1,h,40):
        roi=image.crop((i,j,i+40,j+40))
        roi.save(cwd+'/dataset/'+str(num)+'.jpg')
        num += 1


