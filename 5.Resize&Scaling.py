import cv2
image=cv2.imread('image/leafs.png')# open and read image
if image is None:
    print('Image not found')
else:
    print("Image loaded")
    print(image.shape)

    resized=cv2.resize(image,(300,300))# resize image to 300x300 width,height
    print(f"resized image size:{resized.shape}")
    cv2.imwrite("image/leafs_resized.png",resized)
    cv2.imshow("original",image)
    cv2.imshow("resized", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()