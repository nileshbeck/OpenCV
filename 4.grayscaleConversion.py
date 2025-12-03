import cv2

image=cv2.imread('image/mountain.jpg')
if image is not None:
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)# convert to grayscale

    cv2.imshow('Grayscale Image', gray) # display grayscale image
    cv2.waitKey(0) # wait for a key press to close the window   
    cv2.destroyAllWindows()# close all windows
else:
    print('image not found ')