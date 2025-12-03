import cv2

image=cv2.imread('image/mountai.jpg')# open and read image
if image is None:
    print("Could not open or find the image.")
else:
    cv2.imshow('Mountain Image', image) # display image in a window
    cv2.waitKey(0) # wait for a key press to close the window
    cv2.destroyAllWindows()# close all windows