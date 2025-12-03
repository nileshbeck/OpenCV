import cv2 as cv
image=cv.imread('image/traffic.jpg')# open and read image
if image is not None:
    median_blurred=cv.medianBlur(image,5)# apply Median blur with a 15x15 kernel
    cv.imshow('Original Image', image)  # display original image
    cv.imshow('Median Blurred Image', median_blurred)  # display blurred image
    cv.imwrite('image/traffic_median_blurred.jpg', median_blurred)  # write blurred image to a file
    cv.waitKey(0)  # wait for a key press to close the window    
    cv.destroyAllWindows()  # close all windows

else:
    print('image not found ')