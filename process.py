from PIL import Image
import sys
#import pygame
import math
import algorithmSearch
import numpy as np
import scipy.misc as smp
from queue import PriorityQueue
import cv2
def Preprocess() :
    image = cv2.imread('floorPlan.jpeg')                                                                                           
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                                                                                 
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]                                               

    # Morph open to remove noise                                                                                                   
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))                                                                      
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)                                                       

    # Find contours and remove small noise                                                                                         
    cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)                                                   
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]                                                                                  
    for c in cnts:                                                                                                                 
        area = cv2.contourArea(c)                                                                                                  
        if area < 50:                                                                                                              
            cv2.drawContours(opening, [c], -1, 0, -1)                                                                              
    # Invert and apply slight Gaussian blur                                                                                        
    result = 255 - opening      
    cv2.imwrite("foo.png", result)

Preprocess()    
r = Image.open("foo.png")
fn = lambda x : 255 if x > 200 else 0
r = r.convert('L').point(fn, mode='1')
imageArray_path = np.array(r, dtype=np.uint8)

start_row, start_col, end_row, end_col = 160, 170, 400, 400 
sequence =  algorithmSearch.search(imageArray_path, start_row, start_col, end_row, end_col)
print(sequence)

#creating a new image
# Create a 1024x1024x3 array of 8 bit unsigned integers
floorPlanImage = Image.open("floorPlan.jpeg")
floorPlanImage = floorPlanImage.convert('L').point(fn, mode='1')
imageArray = np.array(floorPlanImage)
n_cols = len(imageArray[0])
n_rows = len(imageArray)
data = np.zeros((n_rows, n_cols, 3), dtype=np.uint8)

for row in range(n_rows):
    for col in range(n_cols):
        if(imageArray[row][col] == 0):
            data[row][col] = [0,0,0]
        else:
            data[row][col] = [255,255,255]

curr_row, curr_col = start_row, start_col

for i in range (len(sequence)):
    data[curr_row+1][curr_col+1] = [255, 0, 0]
    data[curr_row][curr_col] = [255, 0, 0]
    data[curr_row-1][curr_col-1] = [255, 0, 0]
    if(sequence[i] == 'D'):
        curr_row = curr_row - 1;
    elif(sequence[i] == 'R'):
        curr_col = curr_col + 1;
    elif(sequence[i] == 'U'):
        curr_row = curr_row +1;
    elif(sequence[i] == 'L'):
        curr_col = curr_col -1;

image = Image.fromarray(data)
image.show()
