import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
path = "C://Users//HP//Downloads//pt.jpg"
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
desired_width = 800
desired_height = 600
img_resized = cv2.resize(imgGray, (desired_width, desired_height))
cv2.imshow("Img Blur",img_resized)
cv2.waitKey(0)
