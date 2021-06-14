import cv2
import math
import numpy as np
import centroid as ct

src = ct.src
mask = np.zeros(src.shape, dtype = np.uint8)
center = [ct.cx, ct.cy]
print('------45------')
print('shape2: ', src.shape)
cv2.circle(mask, (center[0], center[1]), 1, (0,0,255), 2)

rows, cols, _ = src.shape
zeroX = rows / 2
zeroY = cols / 2
a = center[0] - zeroX
b = center[1] - zeroY

radian = 60 * (math.pi / 180)
rx = math.cos(radian) * a - math.sin(radian) * b
ry = math.sin(radian) * a + math.cos(radian) * b
ix = round(rx)
iy = round(ry)
#cv2.circle(mask, (ix, iy), 2, (0,255,0), 2)

result_x = ix + zeroX
result_y = iy + zeroY

print('rotate: ', result_x, result_y)
cv2.circle(mask, (int(result_x), int(result_y)), 1, (255,255,0), 2)
cv2.imshow('mask',  mask)

if result_x <= zeroX and result_y < zeroY:
     print('left')
elif result_x > zeroX and result_y <= zeroY:
     print('up')
elif result_x >= zeroX and result_y > zeroY:
     print('right')
elif result_x < zeroX and result_y >= zeroY:
     print('down')
else:
     print('N/A')
     
cv2.waitKey()
cv2.destroyAllWindows()
