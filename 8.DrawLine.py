import cv2 as cv
image=cv.imread('image/mountain.jpg')# open and read image
if image is not None:
    print(image.shape)
    (h, w) = image.shape[:2] # get width and height
    print(f"Width: {w}, Height: {h}")

    cv.line(image, (100, 100), (100, 500), (255, 0, 0), 5) # draw a blue line from top-left to (250,250) with thickness 5
    cv.imshow('Mountain Image', image) # display image in a window
    cv.waitKey(0) # wait for a key press to close the window
    cv.destroyAllWindows()# close all windows   
else:
    print('image not found ')
