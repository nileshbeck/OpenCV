import cv2 as cv
image=cv.imread('image/mountain.jpg')# open and read image
if image is not None:
    
    resized=cv.resize(image,(1920,1024))# resize image to 300x300 width,height
    cv.rectangle(resized, (100, 100), (400,400), (0, 255, 0), 5) # draw rectangle
    cv.imshow('Mountain Image', resized) # display image in a window
    cv.waitKey(0) # wait for a key press to close the window
    cv.destroyAllWindows()# close all windows
else:
    print('image not found ')