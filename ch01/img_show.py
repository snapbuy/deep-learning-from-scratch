# coding: utf-8
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('ch01/images/fig 1-1.png') # 이미지 읽어오기
plt.imshow(img)

plt.show()
