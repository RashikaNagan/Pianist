import cv2
import numpy as np

background = cv2.imread("Lesson 9/bg2.png")

#resizing the image
resize = background.shape

pianist = cv2.imread("Lesson 9/pianist.png")
resize = pianist.shape

newsize = cv2.resize(background, (1280,720)) 


HSV = cv2.cvtColor(pianist, cv2.COLOR_BGR2HSV)



lowerrange = np.array([45,50,50]) 
upperrange = np.array([80,255,255]) 
mask = cv2.inRange(HSV, lowerrange, upperrange)

reverse = cv2.bitwise_not(mask)

combine = cv2.bitwise_and(pianist, pianist, mask = reverse )
bg = cv2.bitwise_and(newsize, newsize, mask = mask)
final = cv2.addWeighted(combine, 1, bg, 0.8, 0)
cv2.imshow("display", final)

cv2.waitKey(0)
