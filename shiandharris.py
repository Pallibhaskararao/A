SHI THOMASI ALGORITHM : 
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('blog.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
corners = cv.goodFeaturesToTrack(gray,25,0.01,50)
corners = np.int0(corners)
for i in corners:
    x,y = i.ravel()
    cv.circle(img,(x,y),10,255,-1)
plt.imshow(img)
plt.show()


HARRIS CORNER ALGORITHM : 
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
filename = 'chessboard.png'
img = cv.imread(filename)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2, 3, 0.04)
dst = cv.dilate(dst, None)
img[dst > 0.01 * dst.max()] = [0, 0, 255]
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.figure(figsize=(10, 6))
plt.imshow(img_rgb)
plt.title('Corners Detected')
plt.axis('off')
plt.show()
