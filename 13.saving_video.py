import cv2 as cv
cap = cv.VideoCapture(0)  # 0 means default camera, 1 means external camera 
frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))  # get width of the frame
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))  # get height of the frame

fourcc = cv.VideoWriter_fourcc(*'XVID')  # define the codec
out = cv.VideoWriter('image\output.avi', fourcc, 20.0, (frame_width, frame_height))  # create VideoWriter object

print(fourcc)
print(frame_width)
print(frame_height)
while True:
    ret, frame = cap.read()  # ret means return    ret=True/False  frame=image
    if not ret:
        print("Could not read frame")
        break
    out.write(frame)  # write the frame to the output file
    cv.imshow('Webcam recording...', frame)  # display frame in a window
    if cv.waitKey(1) & 0xFF == ord('q'):  # wait for 'q' key to quit
        print("Quitting....")
        break