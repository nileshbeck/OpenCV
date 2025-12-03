import cv2 as cv
image=cv.imread('image/ice_mountian.jpg')# open and read image
if image is not None:
    cropped=image[200:500,200:500]
    print(f"croppedImage: {cropped}")
    cv.imshow("cropped",cropped)
    cv.imshow('original',image)
    cv.imwrite('image/croped_iceMountain.jpg',cropped)
    cv.waitKey(0)
    cv.destroyAllWindows()