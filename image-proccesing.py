import matplotlib.pyplot as plt
import cv2
import os

path = os.getcwd()
print(path)
image = cv2.imread(path +'/data/images/train.jpg')

image = cv2.GaussianBlur(image, (1001, 1001), 1)
image = cv2.filter2D(image, -1, 1)
cv2.imshow('gaussian', image)

cv2.waitKey(0)