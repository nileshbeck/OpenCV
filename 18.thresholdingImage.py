import cv2 as cv
photo=cv.imread('image/mountain.jpg',cv.IMREAD_GRAYSCALE)# open and read image
if photo is not None:
    image=cv.resize(photo,(400,400))# resize image to 400x400 width,height
    ret,thresh1=cv.threshold(image,127,255,cv.THRESH_BINARY)# apply binary thresholding
    ret,thresh2=cv.threshold(image,127,255,cv.THRESH_BINARY_INV)# apply binary inverse thresholding
    ret,thresh3=cv.threshold(image,127,255,cv.THRESH_TRUNC)# apply truncation thresholding
    ret,thresh4=cv.threshold(image,127,255,cv.THRESH_TOZERO)# apply tozero thresholding
    ret,thresh5=cv.threshold(image,127,255,cv.THRESH_TOZERO_INV)# apply tozero inverse thresholding
    print(ret)
    cv.imshow('Original Image', image)  # display original image
    cv.imshow('Binary Thresholding', thresh1)  # display binary thresholded image
    cv.imshow('Binary Inverse Thresholding', thresh2)  # display binary inverse thresholded image
    cv.imshow('Truncation Thresholding', thresh3)  # display truncation thresholded image
    cv.imshow('Tozero Thresholding', thresh4)  # display tozero thresholded
    cv.imshow('Tozero Inverse Thresholding', thresh5)  # display tozero inverse thresholded image
    cv.imwrite('image/Binary_Thresholding.jpg', thresh1)  # write binary thresholded image to a file
    cv.imwrite('image/Binary_Inverse_Thresholding.jpg', thresh2)  # write binary inverse thresholded image to a file
    cv.imwrite('image/Truncation_Thresholding.jpg', thresh3)  # write truncation thresholded image to a file
    cv.imwrite('image/Tozero_Thresholding.jpg', thresh4)  # write tozero thresholded image to a file
    cv.imwrite('image/Tozero_Inverse_Thresholding.jpg', thresh5)  # write tozero inverse thresholded image to a file
    cv.waitKey(0)  # wait for a key press to close the window
    cv.destroyAllWindows()  # close all windows
else:
    print('image not found ')