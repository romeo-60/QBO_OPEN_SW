#!/usr/bin/python3 
from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv
print ("ok")
print("----------")
#-------------------------
eye_01= cv.imread("O25.png")
cv.imshow("image", eye_01) 
#-------------------------
# conversione gray scale
img= cv.cvtColor(eye_01, cv.COLOR_BGR2GRAY)
#-----------------------
rows, cols = img.shape
print ("dimensioni in pixel", "rows ",rows, "cols ",cols)
print ("-----------" )
data = np.asarray(img)
print("####################")
print (data)
print ("###################")
#k=[]
# for i in range(0,img.shape[0]):
#     for j in range(0,img.shape[1]):
#         k.append(img[i,j])
#         pixel = img.item(i, j)
#         print ("i ", i, "j ", j, "pixel ", pixel)
# print ("**************")
#print ("lista K", k)
#-------------------
print("gray_image")
cv.imshow("image_gray", img)
cv.imwrite("eye_G.png", img)
#----------------------
fig, ax =plt.subplots(1,1) 
plt.title("matrice")
column_labels=[]
ax.axis('tight')
ax.axis('off')
ax.table(cellText=data, loc = "center")
plt.show() 
#---------------
cv.waitKey(0)
cv.destroyAllWindows()
