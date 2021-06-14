import cv2
import numpy as np
import math
import centroid as ct

#detectConerPoints
gray = ct.bImage
K = 4
corners = cv2.goodFeaturesToTrack(gray, maxCorners=K,
              qualityLevel=0.05, minDistance=10)
print('corners.shape=',corners.shape)
print('corners=',corners)

corners = corners.reshape(-1, 2)
for x, y in corners:
    cv2.circle(ct.src, (x, y), 3, (0,0,255), -1)
    
cv2.imshow('Corners', ct.src)

#distance of two points
lineC = [0, 0, 0, 0]
center = [ct.cx, ct.cy]
for fori in range(4):
     lineC[fori] = math.sqrt(math.pow(center[0] - corners[fori][0], 2)
                             + math.pow(center[1] - corners[fori][1], 2))
#select lowest distance
comp = lineC
lineC = sorted(lineC)
lowest = 0
for fori in range(4):
     if lineC[0] == comp[fori]:
          lowest = fori
          break
     
#if corners[lowest]
cv2.waitKey()
cv2.destroyAllWindows()
