import cv2 as cv
import numpy as np
image=cv.imread('image/forest_blurred.jpg')# open and read image  
if image is not None:
    # Create sharpening kernel
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    # Apply the sharpening kernel to the image
    sharpened = cv.filter2D(image, -1, kernel)
    cv.imshow('Original Image', image)  # display original image
    cv.imshow('Sharpened Image', sharpened)  # display sharpened image
    cv.imwrite('image/mountain_sharpened.jpg', sharpened)  # write sharpened image to a file
    cv.waitKey(0)  # wait for a key press to close the window    
    cv.destroyAllWindows()  # close all windows
else:
    print('image not found ') 