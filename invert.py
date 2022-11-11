import cv2;
import math;
import numpy as np;


src = cv2.imread('NTIRE2021_Test_Hazy/8.png');
src = ~src;
cv2.imshow('I',src);
cv2.imwrite("NTIRE2021_Test_Hazy/8.png",src);
cv2.waitKey();