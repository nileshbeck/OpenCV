import cv2 as cv

cap=cv.VideoCapture(0)# 0 means default camera, 1 means external camera
while True:
    ret,frame=cap.read()#ret means return    ret=True/False  frame=image
    if not ret:
        print("Could not read frame")
        break
    flip = cv.flip(frame, 1)# flip the frame horizontally
    cv.imshow('Webcam Feed',flip)# display frame in a window
    print(ord('q'))# print ASCII value of 'q'
    if cv.waitKey(1) & 0xFF==ord('q'):# wait for 'q' key to quit
        
        print("Quitting....")
        break
cap.release()# release the camera
cv.destroyAllWindows()# close all windows

