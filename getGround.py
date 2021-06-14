import cv2
import numpy as np
import random as rand

src = cv2.imread('./src_Arrow/rtd.jpg')
#print('shape: ', src.shape)

B = G = R = 0
for randSelect in range(10):
     rPixel = rand.randint(0, src.shape[1]-1)
     #print('cursor: ', src.shape[0]-3, rPixel)
     bgColor = src[src.shape[0]-3, rPixel]
     B += bgColor[0]
     G += bgColor[1]
     R += bgColor[2]
     #print('aveBGR: ', B, G, R)
B /= 10
G /= 10
R /= 10
print('aveBGR: ', B, G, R)

crit = B+G+R
if crit > 270:
     bgRes = True
else:
     bgRes = False
print('bgRes: ', bgRes)
