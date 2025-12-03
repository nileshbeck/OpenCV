import cv2 as cv
face_cascade=cv.CascadeClassifier('Opencv2/haarcascade_frontalface_default.xml')# load the pre-trained Haar Cascade classifier for face detection
if face_cascade.empty():
    print("error in loading face")
eye_cascade=cv.CascadeClassifier('Opencv2/haarcascade_eye.xml')
if eye_cascade.empty():
    print("error in loading eye")
smile_cascade=cv.CascadeClassifier('Opencv2/haarcascade_smile.xml')
if smile_cascade.empty():
    print("error in loading smile")

cap=cv.VideoCapture(0)# open the default camera (0)
while True:
    ret, frame=cap.read()#
    if not ret:
        break
    
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)# convert the frame to grayscale

    faces=face_cascade.detectMultiScale(gray,1.1,5)# detect faces in the grayscale frame
    
    for (x,y,w,h) in faces:# iterate over detected faces
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)# draw rectangles around detected faces

        roigray=gray[y:y+h, x:x+w]#
        #gray[150:150+80,100:100+80]
        roi_color=frame[y:y+h, x:x+w]#
 
        eyes=eye_cascade.detectMultiScale(roigray, 1.1, 10)#
        if len(eyes)>0:
            cv.putText(frame,"eye detected",(x,y-30), cv.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
        else:
            print("eye not detected")
        smile=smile_cascade.detectMultiScale(roi_color,1.1,10)
        if len(smile)>0:
            cv.putText(frame,"smile detected",(x,y-20), cv.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
        else:
            print("not detected smile")
    cv.imshow("face_eye_smile Detected",frame)
    if cv.waitKey(1)&0xFF==ord('q'):
        break
cap.release()
cv.destroyAllWindows()
    