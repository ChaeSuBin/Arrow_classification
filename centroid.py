import cv2
import numpy as np
import getGround as bg
#1
img = bg.src
if bg.bgRes == False:
    src = 255 - img
    print('---------------')
else:
    src = img
    print('_______________')
#cv2.imshow('src',  src)

src = src[5:src.shape[0]-5, 5:src.shape[1]-5]

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, bImage = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
#cv2.imshow('gray',  bImage)
print('shape: ', src.shape)
#2
mode = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
contours, hierarchy = cv2.findContours(bImage, mode, method)

dst = src.copy()
cv2.drawContours(dst, contours, -1, (0,255,0), 2)
#cv2.imshow('cnt',  dst)
#print(contours)
#3
for cnt in contours:
    try:
        M = cv2.moments(cnt, True)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.circle(dst, (cx, cy), 5, (0,0,255), 2)
        print('x, y: ',cx, cy)
    except ZeroDivisionError as e:
        continue

cv2.imshow('dst',  dst)
cv2.waitKey()
cv2.destroyAllWindows()
