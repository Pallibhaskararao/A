import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('virat1.jpg',0)
img2 = cv2.imread('virat2.jpg',0)
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
bf = cv2.BFMatcher()
matches = bf.match(des1,des2)
similarity_score = 0
for match in matches:
    similarity_score += match.distance
threshold = 50
if similarity_score > threshold:
    print("The images are similar.")
else:
    print("The images are dissimilar.")
matches = sorted(matches, key=lambda val: val.distance)
out = cv2.drawMatches(img1, kp1, img2, kp2, matches[:20], None, flags=2)
plt.imshow(out)
plt.show()
