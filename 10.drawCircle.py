import cv2 as cv

image=cv.imread('image/mountain.jpg')# open and read image
if image is not None:
    rezized=cv.resize(image,(1000,1000))# resize image to 300x300 width,height

    height, width = rezized.shape[:2]
    center = (width // 2, height // 2  )
    print(f"Center of the image: {center} ,latitude: {height//2}, longitude: {width//2}")
    cv.circle(rezized, center, 200, (0, 0, 255), -1) # draw a red circle at the center with radius 100 and thickness 5
    cv.imshow('Mountain Image', rezized) # display image in a window
    cv.waitKey(0) # wait for a key press to close the window
    cv.destroyAllWindows()# close all windows
else:
    print('image not found ')