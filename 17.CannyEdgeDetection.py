import cv2 as cv
image=cv.imread('image/mountain.jpg',cv.IMREAD_GRAYSCALE)# open and read image in grayscale
if image is not None:
    edge=cv.Canny(image,100,255)# apply Canny edge detection
    cv.imshow('Original Image', image)  # display original image
    cv.imshow('canny edge detection Image', edge)  # display blurred image
    cv.imwrite('image/CannyEdgeDetection.jpg', edge)  # write blurred image to a file
    cv.waitKey(0)  # wait for a key press to close the window    
    cv.destroyAllWindows()  # close all windows
else:
    print('image not found ')