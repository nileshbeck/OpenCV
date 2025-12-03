import cv2 as cv
image=cv.imread('image/mountain.jpg')# open and read image
if image is not None:
    blurred=cv.GaussianBlur(image,(59,59),5)# apply Gaussian blur with a 15x15 kernel
    cv.imshow('Original Image', image)  # display original image
    cv.imshow('Gaussian Blurred Image', blurred)  # display blurred image
    cv.imwrite('image/forest_blurred.jpg', blurred)  # write blurred image to a file
    cv.waitKey(0)  # wait for a key press to close the window    
    cv.destroyAllWindows()  # close all windows
else:
    print('image not found ')