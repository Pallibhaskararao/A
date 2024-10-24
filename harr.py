import cv2
import matplotlib.pyplot as plt

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +              
                      'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +  
                                      'haarcascade_eye.xml')
img = cv2.imread('image.jpg')
print(img.shape)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray.shape)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, 
                          minNeighbors=5, minSize=(30, 30))
print("Faces : ", faces)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print("Face rectangle:", x, y, w, h)
    face_region = gray[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(face_region, scaleFactor=1.1, minNeighbors=5, minSize=(10, 10))
    print("Eyes:", eyes)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(img, (x+ex, y+ey), (x+ex+ew, y+ey+eh), 
                                             (0, 0, 255), 2)
        print("Eye rectangle:", x+ex, y+ey, ew, eh)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
