import cv2 as cv
import numpy as np
img1=np.zeros((400,400,3),dtype='uint8')# create a black image of size 400x400
img2=np.zeros((400,400,3),dtype='uint8')# create another black image of size 400x400
cv.circle(img2,(200,200),100,(255,255,255),-1)# draw a white circle on img1
cv.rectangle(img1,(100,100),(300,300),(255,255,255),-1)# draw a filled white rectangle on img2
bitwise_and=cv.bitwise_and(img1,img2)# perform bitwise AND operation
bitwise_or=cv.bitwise_or(img1,img2)# perform bitwise OR operation
bitwise_xor=cv.bitwise_xor(img1,img2)# perform bitwise XOR operation
bitwise_not_img1=cv.bitwise_not(img1)# perform bitwise NOT operation on img
bitwise_not_img2=cv.bitwise_not(img2)# perform bitwise NOT operation on img2
cv.imshow('Image 1',img1)# display img1
cv.imshow('Image 2',img2)# display img2
cv.imshow('Bitwise AND',bitwise_and)# display bitwise AND result
cv.imshow('Bitwise OR',bitwise_or)# display bitwise OR result
cv.imshow('Bitwise XOR',bitwise_xor)# display bitwise XOR result
cv.imshow('Bitwise NOT Image 1',bitwise_not_img1)# display bitwise
cv.imshow('Bitwise NOT Image 2',bitwise_not_img2)# display bitwise NOT result
cv.waitKey(0)# wait for a key press to close the window
cv.destroyAllWindows()# close all windows

