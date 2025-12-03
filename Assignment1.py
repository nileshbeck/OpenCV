import cv2 as cv
image=cv.imread('image/mountain.jpg')# open and read image
if image is not None:
    gray=cv.cvtColor(image, cv.COLOR_BGR2GRAY)# convert to grayscale
    cv.imshow('Grayscale Image', gray) # display grayscale image
    cv.imwrite('image/mountain_gray.jpg', gray) # write grayscale image to a file
    cv.waitKey(0) # wait for a key press to close the window    
    cv.destroyAllWindows()# close all windows
else:
    print('image not found ')