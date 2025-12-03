import cv2

image=cv2.imread('image/mountain.jpg')# open and read image   
if image is not None:

    height, width, channels = image.shape # get dimensions
    print(f"Image Dimensions: Height={height}, Width={width}, Channels={channels}")
    dimension=image.ndim # get number of dimensions
    print(f"Number of Dimensions: {dimension}")
    
    print(dimension.shape[:2])#
else:
    print('image not found ')