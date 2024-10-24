import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
1. Read the image
img = cv.imread('image.jpg')
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')
plt.show()
2. Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()
3. Rotate by 90 degrees
rotated_90 = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
plt.imshow(cv.cvtColor(rotated_90, cv.COLOR_BGR2RGB))
plt.title('Rotated 90 Degrees Clockwise')
plt.axis('off')
plt.show()
Rotate by 180 degrees
rotated_180 = cv.rotate(img, cv.ROTATE_180)
plt.imshow(cv.cvtColor(rotated_180, cv.COLOR_BGR2RGB))
plt.title('Rotated 180 Degrees Clockwise')
plt.axis('off')
plt.show()
4. Write the image to a file
cv.imwrite('output_image.jpg', img)
saved_img = cv.imread('output_image.jpg')
plt.imshow(cv.cvtColor(saved_img, cv.COLOR_BGR2RGB))
plt.title('Saved Image')
plt.axis('off')
plt.show()
5. Extracting image properties
height, width, channels = img.shape
print(f'Height: {height}, Width: {width}, Channels: {channels}')
6. Accessing pixel value at (100, 100)
pixel_value = img[100, 100]
print(f'Pixel Value at (100, 100): {pixel_value}')
img[100, 100] = [0, 255, 0]
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title('Modified Pixel Value')
plt.axis('off')
plt.show()
7. Color mixing
blue_img = np.zeros_like(img)
blue_img[:, :, 0] = 255
red_img = np.zeros_like(img)
red_img[:, :, 2] = 255
mixed_img = cv.addWeighted(blue_img, 0.5, red_img, 0.5, 0)
plt.imshow(cv.cvtColor(mixed_img, cv.COLOR_BGR2RGB))
plt.title('Color Mixing (Blue and Red)')
plt.axis('off')
plt.show()
