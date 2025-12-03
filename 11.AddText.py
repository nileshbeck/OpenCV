import cv2 as cv
image=cv.imread('image/mountain.jpg')# open and read image
if image is not None:
    resized=cv.resize(image,(800,800))# resize  image to 800x600 width,height
    cv.putText(resized, 'mountain\'s forest', (100, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3) # add text
    cv.imshow('Mountain Image', resized) # display image in a window
    cv.waitKey(0) # wait for a key press to close the window
    cv.destroyAllWindows()# close all windows