import cv2 as cv
img=cv.imread('image/ll_shape.jpg')# read the image
if img is not None:
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)# convert to grayscale
    _,thresh=cv.threshold(gray,100,150,cv.THRESH_BINARY)# apply binary thresholding      
    #   //   _ underscore is used to ignore the first return value
    # find contours
    contours, hierarchy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)# find contours

    # draw all contours on the original image
    img_contours=cv.drawContours(img.copy(),contours,-1,(0,255,0),5)# draw all contours in green color with thickness 5
    for contour in contours:
        epsilon=0.01*cv.arcLength(contour,True)# calculate epsilon for contour approximation 
        print(epsilon)  
        approx=cv.approxPolyDP(contour,epsilon,True)# approximate the contour
        print(approx)
        print('Number of vertices:', len(approx))# print number of vertices of the approxim
        corners=len(approx)
        if corners==3:
            shape_name='Triangle'
        elif corners==4:
            shape_name='Quadrilateral'
        elif corners==5:
            shape_name='Pentagon'
        elif corners==6:
            shape_name='Hexagon'
        else:
            shape_name='Circle'
        cv.drawContours(img_contours,[approx],0,(255,0,0),3)# draw the approximated contour in blue color with thickness 3 
        x=approx.ravel()[0]# get x coordinate of the first vertex   reval() flattens the array
        y=approx.ravel()[1]-10# get y coordinate of the first vertex
        cv.putText(img_contours,shape_name,(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)# put shape name near the first vertex 



        print(shape_name)
    cv.imshow('Original Image', img)  # display original image
    cv.imshow('Contours', img_contours)  # display image with contours
    cv.imwrite('image/shapes_contours.png', img_contours)  # write image with contours to a file
    cv.waitKey(0)  # wait for a key press to close the window    
    cv.destroyAllWindows()  # close all windows