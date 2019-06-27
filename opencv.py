import cv2 as cv
import os
from pynput.keyboard import Key,Controller

keyboard = Controller()
detector=cv.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv.VideoCapture(0)
d,e = 0,0
# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")
while True:
    ret, frame = cap.read()

    frame = cv.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)

    faces = detector.detectMultiScale(frame, 1.3, 5)

    if (len(faces) > 0):
        e = e + 1
        d = 0
        if e == 1:
            keyboard.press(Key.space)
            keyboard.release(Key.space)

        x, y, w, h = faces[0]
        if w > 100 and h > 100:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
    else:
        d = d + 1

        if d == 30:
            print("No Face Detected")
            d = 0
            cmd = """osascript -e 'tell application "ScreenSaverEngine" to activate'"""
            e = 0
            os.system(cmd.format())

    cv.imshow('Face Detection', frame)

    c = cv.waitKey(1)
    if c == 27:
        break
    # print(d)
cap.release()
cv.destroyAllWindows()

