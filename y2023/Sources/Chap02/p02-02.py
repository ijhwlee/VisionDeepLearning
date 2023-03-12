# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 04:49:20 2023

@author: hwlee

read and display images

"""
import cv2 as cv
import sys

file_name = './soccer.jpg'
img = cv.imread(file_name)

if img is None:
    sys.exit('파일({0})을 찾을 수 없습니다.'.format(file_name))
    
cv.imshow('Image Disply', img)
    
cv.waitKey()
cv.destroyAllWindows()    
