import cv2
import random

faceData = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#image = cv2.imread('npc_face.jpeg')
video = cv2.VideoCapture(0)

while True:
    frameRead, frame = video.read()

    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faceCoords = faceData.detectMultiScale(grayscale)

    for(x, y, w, h) in faceCoords:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (random.randrange(128, 256), random.randrange(128, 256), random.randrange(128, 256)), 2)

    cv2.imshow('face detector', frame)
    cv2.waitKey(1)

'''
faceCoords = faceData.detectMultiScale(grayscale)

for(x, y, w, h) in faceCoords:
    cv2.rectangle(video, (x, y), (x + w, y + h), (random.randrange(128, 256), random.randrange(128, 256), random.randrange(128, 256)), 2)

#print(faceCoords)

cv2.imshow('face detector', video)
cv2.waitKey()
'''