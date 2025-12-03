import cv2 as cv
image=cv.imread('image/traffic.jpg')# open and read image
if image is not None:
    (h, w) = image.shape[:2]  # get dimensions
    center = (w // 2, h // 2)  # calculate center

    # Rotate the image by 45 degrees
    M = cv.getRotationMatrix2D(center, 45, 1.0)
    rotated = cv.warpAffine(image, M, (w, h))#
    flipped_horizontally = cv.flip(image, 1)  # flip the image horizontally
    flipped_vertically = cv.flip(image, 0)    # flip the image vertically
    flip_both = cv.flip(image, -1)          # flip the image both horizontally and vertically
    cv.imshow('Original Image', image)  # display original image
    cv.imshow('Rotated Image', rotated)  # display rotated image
    cv.imshow('Flipped Horizontally', flipped_horizontally)  # display horizontally flipped image
    cv.imshow('Flipped Vertically', flipped_vertically)      # display vertically flipped image
    cv.imshow('Flipped Both', flip_both)                    # display both flipped image
    cv.imwrite('image/traffic_rotated.jpg', rotated)  # write rotated image to a file
    cv.waitKey(0)  # wait for a key press to close the window    
    cv.destroyAllWindows()  # close all windows
else:
    print('image not found ')