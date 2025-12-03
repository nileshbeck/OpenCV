import cv2

image=cv2.imread('image/mountain.jpg')# open and read image
if image is not None:
    success=cv2.imwrite('image/mountain_copy.jpg', image) # write image to a file

    if success:
        print("Image written successfully.")
        image.shape
    else:
        print("Failed to write the image.")
else:
    print("Could not open or find the image to write.")