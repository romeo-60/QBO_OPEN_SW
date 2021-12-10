#!/usr/bin/python3 
# esempio iterazione
# su matrice 25*12 (colonne * righe)
import numpy as np
import cv2 as cv
righe = 25
colonne = 12
maxVal = 254
risposta1 = "no"
risposta2 = "no"
Num_Diff = 0
matrix1 = np.random.randint(maxVal, size =(colonne,righe))
print ("matrix1", "\n", matrix1)
print("--------")
#----------------------
matrix2 = matrix1.copy() # non si modifica
#-----------------
if matrix1.all() == matrix2.all():
    risposta1 = "si"
print ("le matrici sono uguali?", risposta1)
print("_________________")
#----------------------
print ("matrix2", "\n", matrix2)
#modifica
print(matrix1[0,1])
matrix1[0,1] = matrix1[0,1]+1
#----------------------------
print("----modifica di matrix1-----")
print ("matrix1", "\n", matrix1)
print("---------------")
print ("matrix2", "\n", matrix2)
print("-------------")
if matrix1.all() == matrix2.all:
    risposta2 = "si"
print ("le matrici sono uguali?", risposta2)
print("_________________")
for i in range(colonne):
    for j in range(righe):
        x = matrix1[i,j]
        y = matrix2[i,j]
        if x != y:
            Num_Diff+=1
print("riscontrati N_pixel differenti = ", Num_Diff)
#---------------------------------------------------
array1 = np.uint8(matrix1)
array2 = np.uint8(matrix2)
cv.imshow("image_Modif_gray", array1)
cv.imshow("image_orig_gray", array2)
cv.waitKey(0)
cv.destroyAllWindows()
