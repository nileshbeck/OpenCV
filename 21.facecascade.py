import cv2 as cv
face_cascade=cv.CascadeClassifier('Opencv2/haarcascade_frontalface_default.xml')# load the pre-trained Haar Cascade classifier for face detection

cap=cv.VideoCapture(0)# open the default camera (0)
while True:
    ret,frame=cap.read()# read a frame from the camera
    if ret is True:
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)# convert the frame to grayscale
        faces=face_cascade.detectMultiScale(gray,1.1,5)# detect faces in the grayscale frame
        """
        detectMultiScale()-scan and detect face
        1.1 balance,not too slow,blind
        minNeighbors=5  test 5 time more than 5 strict checking
        """
        for (x,y,w,h) in faces: # iterate over detected faces
            cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)# draw rectangles around detected faces
            """
            x=how far from left
            y=how far from top
            w=width of face
            h=height of face
            """
        cv.imshow('Face Detection',frame)# display the frame with detected faces
        if cv.waitKey(1) & 0xFF==ord('q'):# wait for 'q' key to exit
            break
    else:
        print('Failed to capture frame from camera')    
cap.release()# release the camera
cv.destroyAllWindows()# close all windows   