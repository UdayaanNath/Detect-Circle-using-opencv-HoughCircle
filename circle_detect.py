import cv2
import psutil, os
import numpy as np

dp = 1
mindist = 600 # distance between center of circles
param1 = 50 # hyteresis threshold max
param2 = 30 # hyteresis threshold min
minRadius = 0 
maxRadius = 0
path = "imagesforimageprocessing/C1.jpg"

if __name__ == "__main__":

    p = psutil.Process(os.getpid())
    p.nice(19)

    img  = cv2.imread(path)
    output = img.copy()
    img = cv2.medianBlur(img,5)
    
    g = cv2.Laplacian(img,ddepth=5)

    g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(g, cv2.HOUGH_GRADIENT, dp,mindist,
    param1=param1,param2=param2,minRadius=minRadius,maxRadius=maxRadius)

    output = cv2.imread(path)
    
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)

        # show the output image, Press ESC to close
        cv2.imshow("output", output)
        cv2.waitKey(0)
    
    # [x-coordinate of center, y-coordinate of center, radius]
    print(circles)