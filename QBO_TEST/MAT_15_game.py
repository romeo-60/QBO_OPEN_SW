#!/usr/bin/python3 
# MAT 15 GAME
#Type "copyright", "credits" or "license()" for more information.
#---gestione matrice per inserimento dati---
#--- software by Romeo Ceccato ---
#---------------------------------
# gioco matrice 15
# quadrato 90x90
#
#-------------------
from turtle import *
from random import *
import time
#-------------------
sequence=False
answer = ''
#-----------------
counter_row1=0
row1_l=False
row1_m=False
row1_seq= {'c1':0, 'c2':0, 'c3':0}
#-----------------
counter_row2=0
row2_l=False
row2_m=False
row2_seq= {'c4':0, 'c5':0, 'c6':0}
#-----------------
counter_row3=0
row3_l=False
row3_m=False
row3_seq= {'c7':0, 'c8':0, 'c9':0}
#----------------
counter_ch1=0
ch1_l=False
ch1_m=False
ch1_seq= {'c1':0, 'c4':0, 'c7':0}
#-------------------
counter_ch2=0
ch2_l=False
ch2_m=False
ch2_seq= {'c2':0, 'c5':0, 'c8':0}
#-------------------
counter_ch3=0
ch3_l=False
ch3_m=False
ch3_seq= {'c3':0, 'c6':0, 'c9':0}
#--------------------
counter_dh1=0
d_h1l=False
dh1_m=False
dh1_seq= {'c1':0, 'c5':0, 'c9':0}
#--------------------
counter_dh2=0
d_h2l=False
dh2_m=False
dh2_seq= {'c3':0, 'c5':0, 'c7':0}
#-----var for player ------------
end_game = False
sel_number = None
sel_cell = None
#-----var for randomizer ------------
level = 0
counter=0
limit=150 # number for random sequence
sequence_counter=0
R_Cells=[]
R_Numbers=[]
Mem_numbers=[]
rc = ()
rn = ()
#----var for permutatons ---------
Mem_matrix={}
matrix_temp={}
Numbers=[1,2,3,4,5,6,7,8,9]
Sequences=[]
R_15_Seq=()
#----- var sequentializer ----
s_similar={}
temp_seq=[]
seq=[]
seq5 =  [(2, 5, 8), (7, 5, 3), (6, 5, 4), (9, 5, 1), (4, 5, 6),(3,5,7), (1, 5, 9), (8, 5, 2)]
# seq temporanea + sbloccare Romeo_Finds_Sequence
#seq=[[(6, 1, 8), (5, 1, 9), (9, 1, 5), (8, 1, 6)], [(6, 2, 7), (4, 2, 9), (8, 2, 5), (9, 2, 4), (5, 2, 8), (7, 2, 6)], [(8, 3, 4), (7, 3, 5), (4, 3, 8), (5, 3, 7)], [(6, 4, 5), (5, 4, 6), (8, 4, 3), (3, 4, 8), (9, 4, 2), (2, 4, 9)], [(2, 5, 8), (7, 5, 3), (6, 5, 4), (9, 5, 1), (4, 5, 6), (3, 5, 7), (1, 5, 9), (8, 5, 2)], [(8, 6, 1), (1, 6, 8), (2, 6, 7), (4, 6, 5), (5, 6, 4), (7, 6, 2)], [(6, 7, 2), (2, 7, 6), (5, 7, 3), (3, 7, 5)], [(5, 8, 2), (3, 8, 4), (1, 8, 6), (4, 8, 3), (6, 8, 1), (2, 8, 5)], [(1, 9, 5), (2, 9, 4), (5, 9, 1), (4, 9, 2)]]
#-------------------------------------
#Mem_seq [[(6, 1, 8), (5, 1, 9), (9, 1, 5), (8, 1, 6)], [(6, 2, 7), (4, 2, 9), (8, 2, 5), (9, 2, 4), (5, 2, 8), (7, 2, 6)], [(8, 3, 4), (7, 3, 5), (4, 3, 8), (5, 3, 7)], [(6, 4, 5), (5, 4, 6), (8, 4, 3), (3, 4, 8), (9, 4, 2), (2, 4, 9)], [(2, 5, 8), (7, 5, 3), (6, 5, 4), (9, 5, 1), (4, 5, 6), (3, 5, 7), (1, 5, 9), (8, 5, 2)], [(8, 6, 1), (1, 6, 8), (2, 6, 7), (4, 6, 5), (5, 6, 4), (7, 6, 2)], [(6, 7, 2), (2, 7, 6), (5, 7, 3), (3, 7, 5)], [(5, 8, 2), (3, 8, 4), (1, 8, 6), (4, 8, 3), (6, 8, 1), (2, 8, 5)], [(1, 9, 5), (2, 9, 4), (5, 9, 1), (4, 9, 2)]]
#-------------------------------------
colors=("green", "salmon", "purple", "violet","olive", "magenta", "maroon", "orange", "red")
Boxes=['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9']
cells = {'c1':0, 'c2':0, 'c3':0, 'c4':0, 'c5':0, 'c6':0,'c7':0, 'c8':0,'c9':0}
Cell_Pos = {'c1':[-30, 45],'c2':[0,45],'c3':[30,45],'c4':[-30,15],'c5':[0,15],'c6':[30,15],'c7':[-30,-15],'c8':[0,-15],'c9':[30,-15]}
# -------------------------
#  d_h1  ch1 ch2 ch3 d_h2  
#  r_l1  c1  c2  c3  rw1 
#  r_l2  c4  c5  c6  rw2
#  r_l3  c7  c8  c9  rw3
#  d_l2  c11 cl2 cl3 d_l1
#------------------------------------------------------------
# ----definitions----
start_romeo=False
start_player=False
#--------------------
romeo = Turtle()
romeo.shape("turtle")
romeo.color("yellow")
#turtle writer
writer = Turtle()
writer.shape("turtle")
writer.hideturtle()
#turtle player
player= Turtle()
player.shape("turtle")
player.hideturtle()
#---------------------
# turtle bea
bea = Turtle()
bea.shape("turtle")
bea.color('blue')
bea.hideturtle()
bea.penup()
#------------------
# yes turtle
Y = Turtle()
Y.shape('turtle')
Y.color('blue')
Y.hideturtle()
Y.penup()
#----------------
# no-turtle
N = Turtle()
N.shape('turtle')
N.color('red')
N.hideturtle()
N.penup()
#---------------
Tc_end = Turtle()
Tc_end.shape('square')
Tc_end.hideturtle()
Tc_end.penup()
#------------------
Tc1 = Turtle()
Tc1.shape('square')
Tc1.color('yellow')
Tc1.penup()
Tc1.hideturtle()
Tc2 = Turtle()
Tc2.shape('square')
Tc2.color('yellow')
Tc2.penup()
Tc2.hideturtle()
Tc3 = Turtle()
Tc3.shape('square')
Tc3.color('yellow')
Tc3.penup()
Tc3.hideturtle()
Tc4 = Turtle()
Tc4.shape('square')
Tc4.color('yellow')
Tc4.penup()
Tc4.hideturtle()
Tc5 = Turtle()
Tc5.shape('square')
Tc5.color('yellow')
Tc5.penup()
Tc5.hideturtle()
Tc6 = Turtle()
Tc6.shape('square')
Tc6.color('yellow')
Tc6.penup()
Tc6.hideturtle()
Tc7 = Turtle()
Tc7.shape('square')
Tc7.color('yellow')
Tc7.penup()
Tc7.hideturtle()
Tc8 = Turtle()
Tc8.shape('square')
Tc8.color('yellow')
Tc8.penup()
Tc8.hideturtle()
Tc9 = Turtle()
Tc9.shape('square')
Tc9.color('yellow')
Tc9.penup()
Tc9.hideturtle()
#----------------
Tn1 = Turtle()
Tn1.shape('square')
Tn1.color('yellow')
Tn1.penup()
Tn1.hideturtle()
Tn2 = Turtle()
Tn2.shape('square')
Tn2.color('yellow')
Tn2.penup()
Tn2.hideturtle()
Tn3 = Turtle()
Tn3.shape('square')
Tn3.color('yellow')
Tn3.penup()
Tn3.hideturtle()
Tn4 = Turtle()
Tn4.shape('square')
Tn4.color('yellow')
Tn4.penup()
Tn4.hideturtle()
Tn5 = Turtle()
Tn5.shape('square')
Tn5.color('yellow')
Tn5.penup()
Tn5.hideturtle()
Tn6 = Turtle()
Tn6.shape('square')
Tn6.color('yellow')
Tn6.penup()
Tn6.hideturtle()
Tn7 = Turtle()
Tn7.shape('square')
Tn7.color('yellow')
Tn7.penup()
Tn7.hideturtle()
Tn8 = Turtle()
Tn8.shape('square')
Tn8.color('yellow')
Tn8.penup()
Tn8.hideturtle()
Tn9 = Turtle()
Tn9.shape('square')
Tn9.color('yellow')
Tn9.penup()
Tn9.hideturtle()
#---------------
#-------------------
def Romeo_Fills_Square():
    romeo.showturtle()
    romeo.speed(0)
    romeo.begin_fill()
    romeo.goto(-45,70)
    romeo.goto(45,70)
    romeo.goto(45,-20)
    romeo.goto(-45,-20)
    romeo.goto(-45,70)
    romeo.end_fill()
    romeo.goto(0,0)
#--------------------------
def T_Fills_Square(turtle_name,x1,y1,x2,y2):
    t=turtle_name
    t.color('lightgrey')
    t.showturtle()
    t.penup()
    t.speed(0)
    t.begin_fill()
    t.goto(x1,y1)
    t.goto(x2,y1)
    t.goto(x2,y2)
    t.goto(x1,y2)
    t.goto(x1,y1)
    t.end_fill()
    t.goto(0,0)
    t.hideturtle()
#--------------------------
def T_Draws_Square(turtle_name, x, y):
    t=turtle_name
    t.color('blue')
    t.showturtle()
    t.speed(0)
    t.penup()
    #------
    if t.heading()==90:
        t.right(90)

    elif t.heading()==180:
        t.right(180)

    elif t.heading()==270:
        t.left(90)
    #---------
    t.goto (x,y)
    t.speed (10)
    t.right (0)
    t.pendown()
    t.forward(90)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.left(90)
    #end square
    t.forward(30)
    t.right(90)
    t.penup()
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.pendown()
    t.forward(30)
    t.left(90)
    t.forward(90)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.penup()
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.pendown()
    t.forward(30)
    t.left(90)
    t.forward(90)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.penup()
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.pendown()
    t.forward(30)
    t.left(90)
    t.forward(90)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.penup()
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.pendown()
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.penup()
    t.forward(30)
    t.right(90)
    t.pendown()
    t.forward(30)
    t.forward(90)
    t.forward(30)
    t.right(90)
    t.penup()
    t.forward(30)
    t.right(90)
    t.pendown()
    t.forward(30)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.forward(30)
    t.right(90)
    t.penup()
    t.forward(30)
    t.right(90)
    t.pendown()
    t.forward(30)
    t.forward(90)
    t.forward(30)
    t.right(90)
    t.penup()
    t.forward(30)
    t.right(90)
    t.pendown()
    t.forward(30)
    t.penup()
    t.goto(0,0)
    t.right(180)
    t.hideturtle()
#--------------------------
def T_Fills_S1_4Boxes(turtle_name):
    t=turtle_name
    t.showturtle()
    # ABCD-ABDC-ACBD-ACDB-ACBD-ADBC-ADCB
    #--- 1x4box ---
    t.color('pink')
    #--P1--S1--
    t.speed(0)
    t.begin_fill()
    t.goto(-180,140)
    t.goto(-150,140)
    t.goto(-150,110)
    t.goto(-180,110)
    t.goto(-180,140)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #-------------
    t.color('lime')
    #--P2--S2--
    t.speed(0)
    t.begin_fill()
    t.goto(-140,140)
    t.goto(-110,140)
    t.goto(-110,110)
    t.goto(-140,110)
    t.goto(-140,140)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #-------------
    t.color('magenta')
    #--P3--S3--
    t.speed(0)
    t.begin_fill()
    t.goto(-180,100)
    t.goto(-150,100)
    t.goto(-150,70)
    t.goto(-180,70)
    t.goto(-180,100)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #-------------
    t.color('orange')
    #--P4--S4--
    t.speed(0)
    t.begin_fill()
    t.goto(-140,100)
    t.goto(-110,100)
    t.goto(-110,70)
    t.goto(-140,70)
    t.goto(-140,100)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #---------------
    #--- 2x4 box ---
    t.color('pink')
    #--P1--S1--
    t.speed(0)
    t.begin_fill()
    t.goto(-35,140)
    t.goto(-5,140)
    t.goto(-5,110)
    t.goto(-35,110)
    t.goto(-35,140)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #-------------
    t.color('lime')
    #--P2--S2--
    t.speed(0)
    t.begin_fill()
    t.goto(5,140)
    t.goto(35,140)
    t.goto(35,110)
    t.goto(5,110)
    t.goto(5,140)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #-------------
    t.color('magenta')
    #--P4--S3--
    t.speed(0)
    t.begin_fill()
    t.goto(5,100)
    t.goto(35,100)
    t.goto(35,70)
    t.goto(5,70)
    t.goto(5,100)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #-------------
    t.color('orange')
    #--P3--S4--
    t.speed(0)
    t.begin_fill()
    t.goto(-35,100)
    t.goto(-5,100)
    t.goto(-5,70)
    t.goto(-35,70)
    t.goto(-35,100)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    
    #--- 3x4 Box ---
    t.color('pink')
    #--P1--S1--
    t.speed(0)
    t.begin_fill()
    t.goto(110,140)
    t.goto(140,140)
    t.goto(140,110)
    t.goto(110,110)
    t.goto(110,140)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #-------------
    t.color('lime')
    #--P3--S2--
    t.speed(0)
    t.begin_fill()
    t.goto(110,100)
    t.goto(140,100)
    t.goto(140,70)
    t.goto(110,70)
    t.goto(110,100)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #-------------
    t.color('magenta')
    #--P2--S3--
    t.speed(0)
    t.begin_fill()
    t.goto(150,140)
    t.goto(180,140)
    t.goto(180,110)
    t.goto(150,110)
    t.goto(150,140)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #-------------
    t.color('orange')
    #--P4--S4--
    t.speed(0)
    t.begin_fill()
    t.goto(150,100)
    t.goto(180,100)
    t.goto(180,70)
    t.goto(150,70)
    t.goto(150,100)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    
    #*************
    #--- 4x4box ---
    t.color('pink')
    #--P1--S1--
    t.speed(0)
    t.begin_fill()
    t.goto(-180,40)
    t.goto(-150,40)
    t.goto(-150,10)
    t.goto(-180,10)
    t.goto(-180,40)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #-------------
    t.color('magenta')
    #--P2--S3---
    t.speed(0)
    t.begin_fill()
    t.goto(-140,40)
    t.goto(-110,40)
    t.goto(-110,10)
    t.goto(-140,10)
    t.goto(-140,40)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #-------------
    t.color('lime')
    #--P4--S2--
    t.speed(0)
    t.begin_fill()
    t.goto(-140,0)
    t.goto(-110,0)
    t.goto(-110,-30)
    t.goto(-140,-30)
    t.goto(-140,0)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #--------------
    t.color('orange')
    #--P3--S4--
    t.speed(0)
    t.begin_fill()
    t.goto(-180,0)
    t.goto(-150,0)
    t.goto(-150,-30)
    t.goto(-180,-30)
    t.goto(-180,0)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #-------------
    
    #--- 5x4 box ---
    t.color('pink')
    #--P1--S1--
    t.speed(0)
    t.begin_fill()
    t.goto(-35,40)
    t.goto(-5,40)
    t.goto(-5,10)
    t.goto(-35,10)
    t.goto(-35,40)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #-------------
    t.color('magenta')
    #--P4--S3--
    t.speed(0)
    t.begin_fill()
    t.goto(5,0)
    t.goto(35,0)
    t.goto(35,-30)
    t.goto(5,-30)
    t.goto(5,0)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #-------------
    t.color('lime')
    #--P3--S2--
    t.speed(0)
    t.begin_fill()
    t.goto(-35,0)
    t.goto(-5,0)
    t.goto(-5,-30)
    t.goto(-35,-30)
    t.goto(-35,0)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #-------------
    t.color('orange')
    #--P2--S4--
    t.speed(0)
    t.begin_fill()
    t.goto(5,40)
    t.goto(35,40)
    t.goto(35,10)
    t.goto(5,10)
    t.goto(5,40)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #-------------
    
    #--- 6x4 Box ---
    t.color('pink')
    #--P1--S1--
    t.speed(0)
    t.begin_fill()
    t.goto(110,40)
    t.goto(140,40)
    t.goto(140,10)
    t.goto(110,10)
    t.goto(110,40)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #-------------
    t.color('lime')
    #--P4--S2--
    t.speed(0)
    t.begin_fill()
    t.goto(150,0)
    t.goto(180,0)
    t.goto(180,-30)
    t.goto(150,-30)
    t.goto(150,0)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #-------------
    t.color('magenta')
    #--P3--S3--
    t.speed(0)
    t.begin_fill()
    t.goto(110,0)
    t.goto(140,0)
    t.goto(140,-30)
    t.goto(110,-30)
    t.goto(110,0)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    #-------------
    t.color('orange')
    #--P2--S4--
    t.speed(0)
    t.begin_fill()
    t.goto(150,40)
    t.goto(180,40)
    t.goto(180,10)
    t.goto(150,10)
    t.goto(150,40)
    t.end_fill()
    t.penup()
    t.goto(0,-140)
    t.hideturtle()
    #-----------------
    #*****************
    
#--------------------------
def S1_1Combinations(turtle_name):
    t=turtle_name
    t.showturtle()
    t.speed(0)
    t.penup()
    t.color('blue')
    # ABCD-ABDC-ACBD-ACDB-ADBC-ADCB
    #-------------
    t.goto(-170,120)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(-130,120)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(-170,80)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    t.goto(-130,80)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    #---< 2 Seq >---
    t.goto(-25,120)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(15,120)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(-25,80)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    t.goto(15,80)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    #---< 3 Seq <---
    t.goto(120,120)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(160,120)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(120,80)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    t.goto(160,80)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    #---< 4 Seq >---
    #-------------
    t.goto(-170,20)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(-130,20)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(-170,-20)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    t.goto(-130,-20)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    #---< 5 Seq >---
    t.goto(-25,20)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(15,20)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(-25,-20)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    t.goto(15,-20)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    #---< 6Seq >---
    t.goto(120,20)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(160,20)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(120,-20)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    t.goto(160,-20)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    writer.hideturtle()
#--------------------------
def S1_2Combinations(turtle_name):
    t=turtle_name
    t.showturtle()
    t.speed(0)
    t.penup()
    t.color('blue')
    # BACD-BADC-BCBD-BCDB-BDBC-BDCB
    #-------------
    t.goto(-170,120)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(-130,120)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(-170,80)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    t.goto(-130,80)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    #---< 2 Seq >---
    t.goto(-25,120)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(15,120)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(-25,80)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    t.goto(15,80)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    #---< 3 Seq <---
    t.goto(120,120)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(160,120)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(120,80)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    t.goto(160,80)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    #---< 4 Seq >---
    #-------------
    t.goto(-170,20)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(-130,20)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(-170,-20)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    t.goto(-130,-20)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    #---< 5 Seq >---
    t.goto(-25,20)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(15,20)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(-25,-20)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    t.goto(15,-20)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    #---< 6Seq >---
    t.goto(120,20)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(160,20)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(120,-20)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    t.goto(160,-20)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    writer.hideturtle()
#--------------------------
def S1_3Combinations(turtle_name):
    t=turtle_name
    t.showturtle()
    t.speed(0)
    t.penup()
    t.color('blue')
    # CABD-CADB-CBAD-CBDA-CDAB-CDBA
    #-------------
    t.goto(-170,120)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    t.goto(-130,120)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(-170,80)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(-130,80)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    #---< 2 Seq >---
    t.goto(-25,120)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    t.goto(15,120)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(-25,80)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(15,80)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    #---< 3 Seq <---
    t.goto(120,120)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    t.goto(160,120)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(120,80)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(160,80)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    #---< 4 Seq >---
    #-------------
    t.goto(-170,20)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    t.goto(-130,20)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(-170,-20)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(-130,-20)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    #---< 5 Seq >---
    t.goto(-25,20)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    t.goto(15,20)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(-25,-20)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(15,-20)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    #---< 6Seq >---
    t.goto(120,20)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    t.goto(160,20)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(120,-20)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(160,-20)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    writer.hideturtle()
#--------------------------
def S1_4Combinations(turtle_name):
    t=turtle_name
    t.showturtle()
    t.speed(0)
    t.penup()
    t.color('blue')
    # CABD-CADB-CBAD-CBDA-CDAB-CDBA
    #-------------
    t.goto(-170,120)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    t.goto(-130,120)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(-170,80)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(-130,80)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    #---< 2 Seq >---
    t.goto(-25,120)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    t.goto(15,120)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(-25,80)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(15,80)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    #---< 3 Seq <---
    t.goto(120,120)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    t.goto(160,120)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(120,80)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(160,80)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    #---< 4 Seq >---
    #-------------
    t.goto(-170,20)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    t.goto(-130,20)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(-170,-20)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(-130,-20)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    #---< 5 Seq >---
    t.goto(-25,20)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    t.goto(15,20)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(-25,-20)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(15,-20)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    #---< 6Seq >---
    t.goto(120,20)
    t.write("S4")
    t.goto(0,-140)
    #-------------
    t.goto(160,20)
    t.write("S1")
    t.goto(0,-140)
    #-------------
    t.goto(120,-20)
    t.write("S2")
    t.goto(0,-140)
    #-------------
    t.goto(160,-20)
    t.write("S3")
    t.goto(0,-140)
    #-------------
    writer.hideturtle()
#--------------------------
#----------------------------
def S2_5Combinations(turtle_name):
    t=turtle_name
    t.showturtle()
    t.speed(0)
    t.penup()
    t.color('blue')
    # ABCD-ABDC-ACBD-ACDB-ACBD-ADBC-ADCB
    #-------------
    t.goto(-170,120)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(-130,120)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(-170,80)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    t.goto(-130,80)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    #---< 2 Seq >---
    t.goto(-25,120)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(15,120)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(-25,80)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    t.goto(15,80)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    #---< 3 Seq <---
    t.goto(120,120)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(160,120)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(120,80)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    t.goto(160,80)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    #---< 4 Seq >---
    #-------------
    t.goto(-170,20)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(-130,20)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(-170,-20)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    t.goto(-130,-20)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    #---< 5 Seq >---
    t.goto(-25,20)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(15,20)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(-25,-20)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    t.goto(15,-20)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    #---< 6Seq >---
    t.goto(120,20)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(160,20)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(120,-20)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    t.goto(160,-20)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    writer.hideturtle()
#----------------------------
def S2_6Combinations(turtle_name):
    t=turtle_name
    t.showturtle()
    t.speed(0)
    t.penup()
    t.color('blue')
    # BACD-BACD-BCAD-BCDA-BDAC-BDCA
    #-------------
    t.goto(-170,120)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(-130,120)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(-170,80)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    t.goto(-130,80)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    #---< 2 Seq >---
    t.goto(-25,120)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(15,120)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(-25,80)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    t.goto(15,80)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    #---< 3 Seq <---
    t.goto(120,120)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(160,120)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(120,80)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    t.goto(160,80)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    #---< 4 Seq >---
    #-------------
    t.goto(-170,20)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(-130,20)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(-170,-20)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    t.goto(-130,-20)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    #---< 5 Seq >---
    t.goto(-25,20)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(15,20)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(-25,-20)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    t.goto(15,-20)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    #---< 6Seq >---
    t.goto(120,20)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(160,20)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(120,-20)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    t.goto(160,-20)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    writer.hideturtle()
#----------------------------
def S2_7Combinations(turtle_name):
    t=turtle_name
    t.showturtle()
    t.speed(0)
    t.penup()
    t.color('blue')
    # CABD-CADB-CBAD-CBDA-CDAB-CDBA
    #-------------
    t.goto(-170,120)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    t.goto(-130,120)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(-170,80)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(-130,80)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    #---< 2 Seq >---
    t.goto(-25,120)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    t.goto(15,120)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(-25,80)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(15,80)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    #---< 3 Seq <---
    t.goto(120,120)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    t.goto(160,120)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(120,80)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(160,80)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    #---< 4 Seq >---
    #-------------
    t.goto(-170,20)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    t.goto(-130,20)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(-170,-20)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(-130,-20)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    #---< 5 Seq >---
    t.goto(-25,20)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    t.goto(15,20)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(-25,-20)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(15,-20)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    #---< 6Seq >---
    t.goto(120,20)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    t.goto(160,20)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(120,-20)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(160,-20)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    writer.hideturtle()
#----------------------------
def S2_8Combinations(turtle_name):
    t=turtle_name
    t.showturtle()
    t.speed(0)
    t.penup()
    t.color('blue')
    # CABD-CADB-CBAD-CBDA-CDAB-CDBA
    #-------------
    t.goto(-170,120)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    t.goto(-130,120)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(-170,80)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(-130,80)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    #---< 2 Seq >---
    t.goto(-25,120)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    t.goto(15,120)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(-25,80)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(15,80)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    #---< 3 Seq <---
    t.goto(120,120)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    t.goto(160,120)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(120,80)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(160,80)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    #---< 4 Seq >---
    #-------------
    t.goto(-170,20)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    t.goto(-130,20)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(-170,-20)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(-130,-20)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    #---< 5 Seq >---
    t.goto(-25,20)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    t.goto(15,20)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(-25,-20)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(15,-20)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    #---< 6Seq >---
    t.goto(120,20)
    t.write("S8")
    t.goto(0,-140)
    #-------------
    t.goto(160,20)
    t.write("S5")
    t.goto(0,-140)
    #-------------
    t.goto(120,-20)
    t.write("S6")
    t.goto(0,-140)
    #-------------
    t.goto(160,-20)
    t.write("S7")
    t.goto(0,-140)
    #-------------
    writer.hideturtle()
#--------------------------
#----------------------------
def First_Consideration():
    writer.clear()
    writer.penup()
    writer.goto(0,190)
    writer.color('blue')
    writer.write("I try to combine the second four sequences:", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,170)
    writer.write(seq[4], None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,150)
    writer.color('blue')
    writer.write("                                                      Seq. 5 - Seq. 6 - Seq. 7 - Seq. 8", None, align="center",font=("Arial",10,"normal"))
    bea.clear()
#----------------------------
def Second_Consideration():
    writer.clear()
    writer.penup()
    writer.goto(0,190)
    writer.color('blue')
    writer.write("and now the first four again with these variations  :", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,170)
    writer.write(seq[4], None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,150)
    writer.color('blue')
    writer.write("S(2-1-3-4);S(2-1-4-3);S(2-3-1-4);S(2-3-4-1);S(2-4-1-3);S(2-4-3-1)", None, align="center",font=("Arial",10,"normal"))
    bea.clear()
#----------------------------
def Third_Consideration():
    writer.clear()
    writer.penup()
    writer.goto(0,190)
    writer.color('blue')
    writer.write("and now the second four again with these variations  :", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,170)
    writer.write(seq[4], None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,150)
    writer.color('blue')
    writer.write("S(6-5-7-8);S(6-5-8-7);S(6-7-5-8);S(6-7-8-5);S(6-8-5-7);S(6-8-7-5)", None, align="center",font=("Arial",10,"normal"))
    bea.clear()
#----------------------------
def Fourth_Consideration():
    writer.clear()
    writer.penup()
    writer.goto(0,190)
    writer.color('blue')
    writer.write("and now the first four again with these variations  :", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,170)
    writer.write(seq[4], None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,150)
    writer.color('blue')
    writer.write("S(3-1-2-4);S(3-1-4-2);S(3-2-1-4);S(3-2-4-1);S(3-4-1-2);S(3-4-2-1)", None, align="center",font=("Arial",10,"normal"))
    bea.clear()
    #----------------------------
def Fifth_Consideration():
    writer.clear()
    writer.penup()
    writer.goto(0,190)
    writer.color('blue')
    writer.write("and now the second four again with these variations  :", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,170)
    writer.write(seq[4], None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,150)
    writer.color('blue')
    writer.write("S(7-5-6-8);S(7-5-8-6);S(7-6-5-8);S(767-8-5);S(7-8-5-6);S(7-8-6-5)", None, align="center",font=("Arial",10,"normal"))
    bea.clear()
    #----------------------------
def Sixth_Consideration():
    writer.clear()
    writer.penup()
    writer.goto(0,190)
    writer.color('blue')
    writer.write("Last combination for the first four sequences:", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,170)
    writer.write(seq[4], None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,150)
    writer.color('blue')
    writer.write("S(4-1-2-3);S(4-1-3-2);S(4-2-1-3);S(4-2-3-1);S(4-3-1-2);S(4-3-2-1)", None, align="center",font=("Arial",10,"normal"))
    bea.clear()
    #----------------------------   
##def Seventh_Consideration():
##    writer.clear()
##    writer.penup()
##    writer.goto(0,190)
##    writer.color('blue')
##    writer.write("Last combination for the second four sequences:", None, align="center",font=("Arial",10,"normal"))
##    writer.goto(0,170)
##    writer.write(seq[4], None, align="center",font=("Arial",10,"normal"))
##    writer.goto(0,150)
##    writer.color('blue')
##    writer.write("S(8-5-6-7);S(8-5-7-6);S(8-6-5-7);S(8-6-7-5);S(8-7-5-6);S(8-7-6-5)", None, align="center",font=("Arial",10,"normal"))
##    bea.clear()
##    #----------------------------    
def Show_Solutions():
    writer.clear()
    writer.penup()
    writer.goto(0,190)
    writer.color('blue')
    writer.write("As you saw, I checked many configurations:", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,170)
    writer.write("I divided the sequences into two complementary parts:", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,140) 
    writer.color('blue')
    writer.write("A  -  B  -  C  -  D  <>  !C  -  !B  -  !D  -  !A", None, align="center",font=("Arial",12,"bold"))
    # writer_fills_rectangle
    writer.showturtle()
    writer.color('red')
    writer.speed(0)
    writer.begin_fill()
    writer.goto(-200,140)
    writer.goto(200,140)
    writer.goto(200,-30)
    writer.goto(-200,-30)
    writer.goto(-200,140)
    writer.end_fill()
    writer.penup()
    writer.color('blue')
    writer.goto(0,120)
    writer.write(seq[4], None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,100)
    writer.write("The number of permutations of objects is equal to the factorial of n:", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,80)
    writer.write(" n!=n* (n-1)* (n-2)*...1", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,60)
    writer.write("in this case 8! = 40320 !!!", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,40)
    writer.write("but the multinominal coefficient of the sequences-positions is:", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,20)
    writer.write("8! / (4s! * 4p!)=70", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,0)
    writer.write("and ... the possible geometrical combinations are:", None, align="center", font=("Arial",12,"bold"))
    writer.goto(0,-20)
    T_Turns_Right(writer)
    romeo.goto(0,-20)
    T_Turns_Right(romeo)
    bea.goto(0,-20)
    T_Turns_Right(bea)

#----------------------------
#--------------------------
def T_Fills_8Boxes(turtle_name,x,y):
    t=turtle_name
    t.penup()
    t.showturtle()
    # -- A --
    #-- COLUMN 2 --
    t.color('lime')
    #--CH2--Pos H--
    t.speed(0)
    t.begin_fill()
    t.goto(x,y)
    t.goto((x+30),y)
    t.goto((x+30),(y-30))
    t.goto(x,(y-30))
    t.goto(x,y)
    t.end_fill()
    t.penup()
    t.goto(0,-180)
    #-- CH2--Pos L--
    t.speed(0)
    t.begin_fill()
    t.goto(x,y-120)
    t.goto((x+30),y-120)
    t.goto((x+30),(y-120-30))
    t.goto(x,(y-120-30))
    t.goto(x,y-120)
    t.end_fill()
    t.penup()
    t.goto(0,-180)
    #-- B --
    t.color('pink')
    #--row 2 .. Pos. Left --
    t.speed(0)
    t.begin_fill()
    rx=x-60
    ry=y-60
    t.goto(rx,ry)
    t.goto((rx+30),ry)
    t.goto((rx+30),(ry-30))
    t.goto(rx,(ry-30))
    t.goto(rx,ry)
    t.end_fill()
    t.penup()
    t.goto(0,-180)
    #--row 2 .. Pos. Right --
    t.speed(0)
    t.begin_fill()
    t.goto(rx+120,ry)
    t.goto((rx+120+30),ry)
    t.goto((rx+120+30),(ry-30))
    t.goto(rx+120,(ry-30))
    t.goto(rx+120,ry)
    t.end_fill()
    t.penup()
    t.goto(0,-180)
    #-- C --
    t.color('magenta')
    #--diagonal 1 .. Pos. Left --
    t.speed(0)
    t.begin_fill()
    xd1=x-60
    yd1=y-120
    t.goto(xd1,yd1)
    t.goto((xd1+30),yd1)
    t.goto((xd1+30),(yd1-30))
    t.goto(xd1,(yd1-30))
    t.goto(xd1,yd1)
    t.end_fill()
    t.penup()
    t.goto(0,-180)
    #-- diagonal 1 Pos. Right--
    t.speed(0)
    t.begin_fill()
    t.goto(xd1+120,yd1+120)
    t.goto((xd1+120+30),yd1+120)
    t.goto((xd1+120+30),(yd1+120-30))
    t.goto(xd1+120,(yd1+120-30))
    t.goto(xd1+120,yd1+120)
    t.end_fill()
    t.penup()
    t.goto(0,-180)
    #-- D --
    t.color('orange')
    #--diagonal 2 .. Pos. Left --
    t.speed(0)
    t.begin_fill()
    xd2=x-60
    yd2=y
    t.goto(xd2,yd2)
    t.goto((xd2+30),yd2)
    t.goto((xd2+30),(yd2-30))
    t.goto(xd2,(yd2-30))
    t.goto(xd2,yd2)
    t.end_fill()
    t.penup()
    t.goto(0,-180)
    #-- diagonal 2 Pos. Right--
    t.speed(0)
    t.begin_fill()
    t.goto(xd2+120,yd2-120)
    t.goto((xd2+120+30),yd2-120)
    t.goto((xd2+120+30),(yd2-120-30))
    t.goto(xd2+120,(yd2-120-30))
    t.goto(xd2+120,yd2-120)
    t.end_fill()
    t.penup()
    t.goto(0,-180)
    #----------------
    t.hideturtle()
#--------------------------
def Romeo_Writes_Names():
    #romeo write cells_name
    romeo.goto(-30,55)
    romeo.speed(0)
    romeo.color('grey')
    romeo.showturtle()

    for i in range (45):
        romeo.left(i)
    romeo.write("c1")
    romeo.forward(30)
    for i in range (45):
        romeo.left(i)
    romeo.right(-90)
    romeo.write("c2")
    romeo.forward(30)
    for i in range (45):
        romeo.left(i)
    romeo.write("c3")
    romeo.forward(30)
    for i in range (45):
        romeo.left(i)
    romeo.write("c6")
    romeo.forward(30)
    for i in range (45):
        romeo.left(i)
    romeo.write("c5")
    romeo.left(90)
    romeo.forward(30)
    for i in range (45):
        romeo.left(i)
    romeo.write("c4")
    romeo.right(180)
    romeo.forward(30)
    for i in range (45):
        romeo.left(i)
    romeo.write("c7")
    romeo.left(180)
    romeo.forward(30)
    for i in range (45):
        romeo.left(i)
    romeo.write("c8")
    romeo.right(-90)
    romeo.forward(30)
    for i in range (45):
        romeo.left(i)
    romeo.write("c9")
    romeo.forward(30)
    #end drowing names
    romeo.hideturtle()

#--------------------------
def Romeo_Turns():
    #romeo goes to the place
    romeo.goto (0,-140)
    romeo.color("green")
    romeo.showturtle()
    romeo.speed(0)
    for i in range (90):
        romeo.left(i)
    romeo.left(90)
    romeo.hideturtle()
#-------------------------
def Romeo_Turns_Right():
    romeo.showturtle()
    romeo.color("blue")
    romeo.speed(0)
    for i in range (45):
        romeo.right(i)
    romeo.left(90)
    romeo.hideturtle()
#----------------
def Romeo_Turns_Left():
    romeo.showturtle()
    romeo.color("red")
    romeo.speed(0)
    for i in range (45):
        romeo.left(i)
    romeo.left(90)
    romeo.hideturtle()
#--------------------------
def T_Turns_Right(turtle_name):
    t=turtle_name
    t.showturtle()
    t.color("blue")
    t.speed(0)
    for i in range (45):
        t.right(i)
    t.left(90)
    t.hideturtle()
#----------------
def T_Turns_Left(turtle_name):
    t=turtle_name
    t.showturtle()
    t.color("red")
    t.speed(0)
    for i in range (45):
        t.left(i)
    t.left(90)
    t.hideturtle()
#-------------------
def T_Turns_Turtles():
    for i in range (45):
        romeo.right(i)
        writer.left(i)
        bea.right(i)
    romeo.hideturtle()
    writer.hideturtle()
    bea.hideturtle()
#--------------------------
#--------------------------
def Romeo_Draws_R01():
    romeo.speed(0)
    romeo.color('blue')
    romeo.showturtle()            
    romeo.goto(-30,120)
    romeo.right(180)
    romeo.write('c1')
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c2")
    romeo.forward(30)
    romeo.write("c3")
    romeo.penup()
    romeo.forward(60)
    romeo.right(90)
    romeo.goto(90,60)
    romeo.write("c3")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c6")
    romeo.forward(30)
    romeo.write("c9")
    romeo.penup()
    romeo.forward(60)
    romeo.right(90)
    romeo.forward(60)
    romeo.write("c9")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c8")
    romeo.forward(30)
    romeo.write("c7")
    romeo.penup()
    romeo.forward(60)
    romeo.right(90)
    romeo.forward(60)
    romeo.write("c7")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c4")
    romeo.forward(30)
    romeo.write("c1")
    romeo.penup()
    romeo.forward(60)
    romeo.goto(0,-120)
    
#--------------------------
def Romeo_Draws_R02():
    romeo.speed(0)
    romeo.showturtle()
    romeo.goto(90,60)
    romeo.write('c1')
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c2")
    romeo.forward(30)
    romeo.write("c3")
    romeo.penup()
    romeo.forward(60)
    #---------------
    romeo.right(90)
    romeo.forward(60)
    romeo.write("c3")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c6")
    romeo.forward(30)
    romeo.write("c9")
    romeo.penup()
    #---------------
    romeo.forward(60)
    romeo.right(90)
    romeo.forward(60)
    romeo.write("c9")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c8")
    romeo.forward(30)
    romeo.write("c7")
    romeo.penup()
    romeo.forward(60)
    #----------------
    romeo.right(90)
    romeo.forward(60)
    romeo.write("c7")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c4")
    romeo.forward(30)
    romeo.write("c1")
    romeo.penup()
    romeo.forward(60)
    romeo.goto(0,-140)
#---------------------
def Romeo_Draws_R03():
    romeo.speed(0)
    romeo.showturtle()
    romeo.goto(30,-60)
    romeo.write('c1')
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c2")
    romeo.forward(30)
    romeo.write("c3")
    romeo.penup()
    romeo.forward(60)
    #---------------
    romeo.right(90)
    romeo.forward(60)
    romeo.write("c3")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c6")
    romeo.forward(30)
    romeo.write("c9")
    romeo.penup()
    #---------------
    romeo.forward(60)
    romeo.right(90)
    romeo.forward(60)
    romeo.write("c9")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c8")
    romeo.forward(30)
    romeo.write("c7")
    romeo.penup()
    romeo.forward(60)
    #----------------
    romeo.right(90)
    romeo.forward(60)
    romeo.write("c7")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c4")
    romeo.forward(30)
    romeo.write("c1")
    romeo.penup()
    romeo.forward(60)
    romeo.goto(0,-120)
#---------------------
def Romeo_Draws_R04():
    romeo.speed(0)
    romeo.showturtle()
    romeo.goto(-90,-0)
    romeo.write('c1')
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c2")
    romeo.forward(30)
    romeo.write("c3")
    romeo.penup()
    romeo.forward(60)
    #---------------
    romeo.right(90)
    romeo.forward(60)
    romeo.write("c3")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c6")
    romeo.forward(30)
    romeo.write("c9")
    romeo.penup()
    #---------------
    romeo.forward(60)
    romeo.right(90)
    romeo.forward(60)
    romeo.write("c9")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c8")
    romeo.forward(30)
    romeo.write("c7")
    romeo.penup()
    romeo.forward(60)
    #----------------
    romeo.right(90)
    romeo.forward(60)
    romeo.write("c7")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c4")
    romeo.forward(30)
    romeo.write("c1")
    romeo.penup()
    romeo.forward(60)
    romeo.goto(0,-120)
#---------------------
def Romeo_Draws_L01():
    romeo.speed(0)
    romeo.showturtle()
    romeo.goto(30,120)
    romeo.right(180)
    romeo.write('c1')
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c2")
    romeo.forward(30)
    romeo.write("c3")
    romeo.penup()
    romeo.forward(60)
    romeo.left(90)
    romeo.goto(-90,60)
    romeo.write("c3")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c6")
    romeo.forward(30)
    romeo.write("c9")
    romeo.penup()
    romeo.forward(60)
    #-----------------
    romeo.left(90)
    romeo.forward(60)
    romeo.write("c9")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c8")
    romeo.forward(30)
    romeo.write("c7")
    romeo.penup()
    romeo.forward(60)
    romeo.left(90)
    #---------------
    romeo.forward(60)
    romeo.write("c7")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c4")
    romeo.forward(30)
    romeo.write("c1")
    romeo.penup()
    romeo.forward(60)
    romeo.goto(0,-120)
#---------------------
def Romeo_Draws_L02():
    romeo.speed(0)
    romeo.showturtle()
    romeo.goto(-90,60)
    romeo.left(180)
    romeo.write('c1')
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c2")
    romeo.forward(30)
    romeo.write("c3")
    romeo.penup()
    romeo.forward(60)
    #---------------
    romeo.left(90)
    romeo.forward(60)
    romeo.write("c3")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c6")
    romeo.forward(30)
    romeo.write("c9")
    romeo.penup()
    #---------------
    romeo.forward(60)
    romeo.left(90)
    romeo.forward(60)
    romeo.write("c9")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c8")
    romeo.forward(30)
    romeo.write("c7")
    romeo.penup()
    romeo.forward(60)
    #----------------
    romeo.left(90)
    romeo.forward(60)
    romeo.write("c7")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c4")
    romeo.forward(30)
    romeo.write("c1")
    romeo.penup()
    romeo.forward(60)
    romeo.goto(0,-140)
#---------------------
def Romeo_Draws_L03():
    romeo.speed(0)
    romeo.showturtle()
    romeo.goto(-30,-60)
    romeo.left(180)
    romeo.write('c1')
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c2")
    romeo.forward(30)
    romeo.write("c3")
    romeo.penup()
    romeo.forward(60)
    #---------------
    romeo.left(90)
    romeo.forward(60)
    romeo.write("c3")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c6")
    romeo.forward(30)
    romeo.write("c9")
    romeo.penup()
    #---------------
    romeo.forward(60)
    romeo.left(90)
    romeo.forward(60)
    romeo.write("c9")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c8")
    romeo.forward(30)
    romeo.write("c7")
    romeo.penup()
    romeo.forward(60)
    #----------------
    romeo.left(90)
    romeo.forward(60)
    romeo.write("c7")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c4")
    romeo.forward(30)
    romeo.write("c1")
    romeo.penup()
    romeo.forward(60)
    romeo.goto(0,-120)    
#---------------------
def Romeo_Draws_L04():
    romeo.speed(0)
    romeo.showturtle()
    romeo.goto(90,-0)
    romeo.left(180)
    romeo.write('c1')
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c2")
    romeo.forward(30)
    romeo.write("c3")
    romeo.penup()
    romeo.forward(60)
    #---------------
    romeo.left(90)
    romeo.forward(60)
    romeo.write("c3")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c6")
    romeo.forward(30)
    romeo.write("c9")
    romeo.penup()
    #---------------
    romeo.forward(60)
    romeo.left(90)
    romeo.forward(60)
    romeo.write("c9")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c8")
    romeo.forward(30)
    romeo.write("c7")
    romeo.penup()
    romeo.forward(60)
    #----------------
    romeo.left(90)
    romeo.forward(60)
    romeo.write("c7")
    romeo.pendown()
    romeo.forward(30)
    romeo.write("c4")
    romeo.forward(30)
    romeo.write("c1")
    romeo.penup()
    romeo.forward(60)
    romeo.goto(0,-120)
#-----------------------
def Show_Vertical_Reflection():
    T_Fills_Square(romeo,-45,150,45,60)
    T_Draws_Square(romeo, -45, 150)
    #------------------
    romeo.color("green")
    romeo.goto(-30,125)
    romeo.write("C1",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(-0,125)
    romeo.write("C2",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(30,125)
    romeo.write("C3",None, align="center",font=("Arial",12,"normal"))
    #------------------
    romeo.color("magenta")
    romeo.goto(-30,95)
    romeo.write("C4",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(-0,95)
    romeo.write("C5",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(30,95)
    romeo.write("C6",None, align="center",font=("Arial",12,"normal"))
    #------------------
    romeo.color("orange")
    romeo.goto(-30,65)
    romeo.write("C7",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(-0,65)
    romeo.write("C8",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(30,65)
    romeo.write("C9",None, align="center",font=("Arial",12,"normal"))
    #************************************
    T_Fills_Square(romeo,-45,30,45,-60)
    T_Draws_Square(romeo, -45, 30)
    #------------------
    romeo.color("orange")
    romeo.goto(-30,5)
    romeo.write("C7",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(-0,5)
    romeo.write("C8",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(30,5)
    romeo.write("C9",None, align="center",font=("Arial",12,"normal"))
    #------------------
    romeo.color("magenta")
    romeo.goto(-30,-25)
    romeo.write("C4",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(-0,-25)
    romeo.write("C5",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(30,-25)
    romeo.write("C6",None, align="center",font=("Arial",12,"normal"))
    #------------------
    romeo.color("green")
    romeo.goto(-30,-55)
    romeo.write("C1",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(-0,-55)
    romeo.write("C2",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(30,-55)
    romeo.write("C3",None, align="center",font=("Arial",12,"normal"))

#**************************************
def Show_Horizontal_Reflection():
    T_Fills_Square(romeo,-150,115,-60,25)
    T_Draws_Square(romeo, -150, 115)
    #------------------
    romeo.color("green")
    romeo.goto(-135,90)
    romeo.write("C1",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(-135,60)
    romeo.write("C4",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(-135,30)
    romeo.write("C7",None, align="center",font=("Arial",12,"normal"))
    #------------------
    romeo.color("magenta")
    romeo.goto(-105,90)
    romeo.write("C2",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(-105,60)
    romeo.write("C5",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(-105,30)
    romeo.write("C8",None, align="center",font=("Arial",12,"normal"))
    #------------------
    romeo.color("orange")
    romeo.goto(-75,90)
    romeo.write("C3",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(-75,60)
    romeo.write("C6",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(-75,30)
    romeo.write("C9",None, align="center",font=("Arial",12,"normal"))
    #****************************************
    T_Fills_Square(romeo,50,115,140,25)
    T_Draws_Square(romeo, 50, 115)
    #------------------
    romeo.color("orange")
    romeo.goto(65,90)
    romeo.write("C3",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(65,60)
    romeo.write("C6",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(65,30)
    romeo.write("C9",None, align="center",font=("Arial",12,"normal"))
    #------------------
    romeo.color("magenta")
    romeo.goto(95,90)
    romeo.write("C2",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(95,60)
    romeo.write("C5",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(95,30)
    romeo.write("C8",None, align="center",font=("Arial",12,"normal"))
    #------------------
    romeo.color("green")
    romeo.goto(125,90)
    romeo.write("C1",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(125,60)
    romeo.write("C4",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(125,30)
    romeo.write("C7",None, align="center",font=("Arial",12,"normal"))
    
    
#-----------------------    
    
def Romeo_Fills_C5():
    romeo.showturtle()
    romeo.speed(0)
    romeo.begin_fill()
    romeo.goto(-15,40)
    romeo.goto(15,40)
    romeo.goto(15,10)
    romeo.goto(-15,10)
    romeo.goto(-15,40)
    romeo.end_fill()
    romeo.penup()
    romeo.goto(0,-130)
#---------------------------
def T_Fills_C5(turtle_name):
    t=turtle_name
    t.showturtle()
    t.color('red')
    t.speed(0)
    t.begin_fill()
    t.goto(-15,40)
    t.goto(15,40)
    t.goto(15,10)
    t.goto(-15,10)
    t.goto(-15,40)
    t.end_fill()
    t.penup()
    t.goto(0,-130)
       
#--------------------------
def Romeo_Draws_Boxes_01():
    romeo.showturtle()
    romeo.speed(0)
    romeo.penup()
    romeo.color("purple")
    romeo.begin_fill()
    romeo.goto(-115,160)
    romeo.goto(-85,160)
    romeo.goto(-85,130)
    romeo.goto(-115,130)
    romeo.goto(-115,160)
    romeo.end_fill()
    romeo.goto(-80,145)
    
    #-----------------
    romeo.color("blue")
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    romeo.right(90)
    romeo.forward(15)
    romeo.right(90)
    romeo.penup()
    romeo.forward(10)
    romeo.right(90)
    romeo.penup()
    romeo.forward(5)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    #-----------------
    romeo.color("green")
    romeo.begin_fill()
    romeo.goto(-55,160)
    romeo.goto(-25,160)
    romeo.goto(-25,130)
    romeo.goto(-55,130)
    romeo.goto(-55,160)
    romeo.end_fill()
    romeo.goto(-20,145)
    romeo.right(90)
    #----------------
    romeo.color("blue")
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    romeo.right(90)
    romeo.forward(15)
    romeo.right(90)
    romeo.penup()
    romeo.forward(10)
    romeo.right(90)
    romeo.penup()
    romeo.forward(5)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    #----------------
    romeo.color("violet")
    romeo.begin_fill()
    romeo.goto(5,160)
    romeo.goto(35,160)
    romeo.goto(35,130)
    romeo.goto(5,130)
    romeo.goto(5,160)
    romeo.end_fill()
    romeo.goto (50,150)
#-----------------------
    romeo.color("blue")
    romeo.right(90)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    romeo.right(90)
    romeo.forward(10)
    romeo.right(90)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
#-----------------------
    romeo.goto(100,160)
    romeo.color("red")
    romeo.begin_fill()
    romeo.circle(15)
    romeo.end_fill()
    romeo.goto (0,-140)
#-----------------------
def Romeo_Writes_Var_01():
    romeo.color("white")
    romeo.goto(-100,140)
    romeo.write("X", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    #-----------------
    romeo.goto(-40,140)
    romeo.write("Y", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    #-----------------
    romeo.goto(20,140)
    romeo.write("Z", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    #-----------------
    romeo.goto(100,140)
    romeo.write("R", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
#---------------------
def Romeo_Draws_Boxes_02():
    romeo.showturtle()
    romeo.speed(0)
    romeo.penup()
    romeo.color("violet")
    romeo.begin_fill()
    romeo.goto(-115,80)
    romeo.goto(-85,80)
    romeo.goto(-85,50)
    romeo.goto(-115,50)
    romeo.goto(-115,80)
    romeo.end_fill()
    romeo.goto(-80,65)
    
    #-----------------
    romeo.color("blue")
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    romeo.right(90)
    romeo.forward(15)
    romeo.right(90)
    romeo.penup()
    romeo.forward(10)
    romeo.right(90)
    romeo.penup()
    romeo.forward(5)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    #-----------------
    romeo.color("green")
    romeo.begin_fill()
    romeo.goto(-55,80)
    romeo.goto(-25,80)
    romeo.goto(-25,50)
    romeo.goto(-55,50)
    romeo.goto(-55,80)
    romeo.end_fill()
    romeo.goto(-20,65)
    romeo.right(90)
    #----------------
    romeo.color("blue")
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    romeo.right(90)
    romeo.forward(15)
    romeo.right(90)
    romeo.penup()
    romeo.forward(10)
    romeo.right(90)
    romeo.penup()
    romeo.forward(5)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    #----------------
    romeo.color("purple")
    romeo.begin_fill()
    romeo.goto(5,80)
    romeo.goto(35,80)
    romeo.goto(35,50)
    romeo.goto(5,50)
    romeo.goto(5,80)
    romeo.end_fill()
    romeo.goto (50,70)
#-----------------------
    romeo.color("blue")
    romeo.right(90)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    romeo.right(90)
    romeo.forward(10)
    romeo.right(90)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
#-----------------------
    romeo.goto(100,80)
    romeo.color("red")
    romeo.begin_fill()
    romeo.circle(15)
    romeo.end_fill()
    romeo.goto (0,-140)
#-----------------------
def Romeo_Writes_Var_02():
    romeo.color("white")
    romeo.goto(-100,60)
    romeo.write("Z", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    #-----------------
    romeo.goto(-40,60)
    romeo.write("Y", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    #-----------------
    romeo.goto(20,60)
    romeo.write("X", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    #-----------------
    romeo.goto(100,60)
    romeo.write("R", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)

#---------------------
def Romeo_Draws_Boxes_03():
    romeo.showturtle()
    romeo.speed(0)
    romeo.penup()
    romeo.color("green")
    romeo.begin_fill()
    romeo.goto(-115,40)
    romeo.goto(-85,40)
    romeo.goto(-85,10)
    romeo.goto(-115,10)
    romeo.goto(-115,40)
    romeo.end_fill()
    romeo.goto(-80,25)
    
    #-----------------
    romeo.color("blue")
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    romeo.right(90)
    romeo.forward(15)
    romeo.right(90)
    romeo.penup()
    romeo.forward(10)
    romeo.right(90)
    romeo.penup()
    romeo.forward(5)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    #-----------------
    romeo.color("violet")
    romeo.begin_fill()
    romeo.goto(-55,40)
    romeo.goto(-25,40)
    romeo.goto(-25,10)
    romeo.goto(-55,10)
    romeo.goto(-55,40)
    romeo.end_fill()
    romeo.goto(-20,25)
    romeo.right(90)
    #----------------
    romeo.color("blue")
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    romeo.right(90)
    romeo.forward(15)
    romeo.right(90)
    romeo.penup()
    romeo.forward(10)
    romeo.right(90)
    romeo.penup()
    romeo.forward(5)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    #----------------
    romeo.color("purple")
    romeo.begin_fill()
    romeo.goto(5,40)
    romeo.goto(35,40)
    romeo.goto(35,10)
    romeo.goto(5,10)
    romeo.goto(5,40)
    romeo.end_fill()
    romeo.goto (50,30)
#-----------------------
    romeo.color("blue")
    romeo.right(90)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    romeo.right(90)
    romeo.forward(10)
    romeo.right(90)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
#-----------------------
    romeo.goto(100,40)
    romeo.color("red")
    romeo.begin_fill()
    romeo.circle(15)
    romeo.end_fill()
    romeo.goto (0,-140)
#-----------------------
def Romeo_Writes_Var_03():
    romeo.color("white")
    romeo.goto(-100,20)
    romeo.write("Y", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    #-----------------
    romeo.goto(-40,20)
    romeo.write("Z", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    #-----------------
    romeo.goto(20,20)
    romeo.write("X", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    #-----------------
    romeo.goto(100,20)
    romeo.write("R", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
#---------------------
def Romeo_Draws_Boxes_04():
    romeo.showturtle()
    romeo.speed(0)
    romeo.penup()
    romeo.color("purple")
    romeo.begin_fill()
    romeo.goto(-115,0)
    romeo.goto(-85,0)
    romeo.goto(-85,-30)
    romeo.goto(-115,-30)
    romeo.goto(-115,0)
    romeo.end_fill()
    romeo.goto(-80,-15)
    
    #-----------------
    romeo.color("blue")
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    romeo.right(90)
    romeo.forward(15)
    romeo.right(90)
    romeo.penup()
    romeo.forward(10)
    romeo.right(90)
    romeo.penup()
    romeo.forward(5)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    #-----------------
    romeo.color("violet")
    romeo.begin_fill()
    romeo.goto(-55,0)
    romeo.goto(-25,0)
    romeo.goto(-25,-30)
    romeo.goto(-55,-30)
    romeo.goto(-55,0)
    romeo.end_fill()
    romeo.goto(-20,-15)
    romeo.right(90)
    #----------------
    romeo.color("blue")
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    romeo.right(90)
    romeo.forward(15)
    romeo.right(90)
    romeo.penup()
    romeo.forward(10)
    romeo.right(90)
    romeo.penup()
    romeo.forward(5)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    #----------------
    romeo.color("green")
    romeo.begin_fill()
    romeo.goto(5,0)
    romeo.goto(35,0)
    romeo.goto(35,-30)
    romeo.goto(5,-30)
    romeo.goto(5,0)
    romeo.end_fill()
    romeo.goto (50,-10)
#-----------------------
    romeo.color("blue")
    romeo.right(90)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    romeo.right(90)
    romeo.forward(10)
    romeo.right(90)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
#-----------------------
    romeo.goto(100,0)
    romeo.color("red")
    romeo.begin_fill()
    romeo.circle(15)
    romeo.end_fill()
    romeo.goto (0,-140)
#-----------------------
def Romeo_Writes_Var_04():
    romeo.color("white")
    romeo.goto(-100,-20)
    romeo.write("X", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    #-----------------
    romeo.goto(-40,-20)
    romeo.write("Z", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    #-----------------
    romeo.goto(20,-20)
    romeo.write("Y", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    #-----------------
    romeo.goto(100,-20)
    romeo.write("R", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
#---------------------
def Romeo_Draws_Boxes_05():
    romeo.showturtle()
    romeo.speed(0)
    romeo.penup()
    romeo.color("violet")
    romeo.begin_fill()
    romeo.goto(-115,-40)
    romeo.goto(-85,-40)
    romeo.goto(-85,-70)
    romeo.goto(-115,-70)
    romeo.goto(-115,-40)
    romeo.end_fill()
    romeo.goto(-80,-50)
    romeo.penup()
    #-----------------
    romeo.color("blue")
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    romeo.right(90)
    romeo.forward(15)
    romeo.right(90)
    romeo.penup()
    romeo.forward(10)
    romeo.right(90)
    romeo.penup()
    romeo.forward(5)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    #-----------------
    romeo.color("purple")
    romeo.begin_fill()
    romeo.goto(-55,-40)
    romeo.goto(-25,-40)
    romeo.goto(-25,-70)
    romeo.goto(-55,-70)
    romeo.goto(-55,-40)
    romeo.end_fill()
    romeo.goto(-20,-50)
    romeo.right(90)
    #----------------
    romeo.color("blue")
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    romeo.right(90)
    romeo.forward(15)
    romeo.right(90)
    romeo.penup()
    romeo.forward(10)
    romeo.right(90)
    romeo.penup()
    romeo.forward(5)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    #----------------
    romeo.color("green")
    romeo.begin_fill()
    romeo.goto(5,-40)
    romeo.goto(35,-40)
    romeo.goto(35,-70)
    romeo.goto(5,-70)
    romeo.goto(5,-40)
    romeo.end_fill()
    romeo.goto (50,-45)
#-----------------------
    romeo.color("blue")
    romeo.right(90)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    romeo.right(90)
    romeo.forward(10)
    romeo.right(90)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
#-----------------------
    romeo.goto(100,-40)
    romeo.color("red")
    romeo.begin_fill()
    romeo.circle(15)
    romeo.end_fill()
    romeo.goto (0,-140)
    romeo.penup()
#-----------------------
def Romeo_Writes_Var_05():
    romeo.color("white")
    romeo.goto(-100,-60)
    romeo.write("Z", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    #-----------------
    romeo.goto(-40,-60)
    romeo.write("X", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    #-----------------
    romeo.goto(20,-60)
    romeo.write("Y", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    #-----------------
    romeo.goto(100,-60)
    romeo.write("R", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
#---------------------
def Romeo_Draws_Boxes_06():
    romeo.showturtle()
    romeo.speed(0)
    romeo.penup()
    romeo.color("green")
    romeo.begin_fill()
    romeo.goto(-115,-80)
    romeo.goto(-85,-80)
    romeo.goto(-85,-110)
    romeo.goto(-115,-110)
    romeo.goto(-115,-80)
    romeo.end_fill()
    romeo.goto(-80,-95)
    romeo.penup()
    #-----------------
    romeo.color("blue")
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    romeo.right(90)
    romeo.forward(15)
    romeo.right(90)
    romeo.penup()
    romeo.forward(10)
    romeo.right(90)
    romeo.penup()
    romeo.forward(5)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    #-----------------
    romeo.color("purple")
    romeo.begin_fill()
    romeo.goto(-55,-80)
    romeo.goto(-25,-80)
    romeo.goto(-25,-110)
    romeo.goto(-55,-110)
    romeo.goto(-55,-80)
    romeo.end_fill()
    romeo.goto(-20,-95)
    romeo.right(90)
    #----------------
    romeo.color("blue")
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    romeo.right(90)
    romeo.forward(15)
    romeo.right(90)
    romeo.penup()
    romeo.forward(10)
    romeo.right(90)
    romeo.penup()
    romeo.forward(5)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    #----------------
    romeo.color("violet")
    romeo.begin_fill()
    romeo.goto(5,-80)
    romeo.goto(35,-80)
    romeo.goto(35,-110)
    romeo.goto(5,-110)
    romeo.goto(5,-80)
    romeo.end_fill()
    romeo.goto (50,-90)
#-----------------------
    romeo.color("blue")
    romeo.right(90)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
    romeo.right(90)
    romeo.forward(10)
    romeo.right(90)
    romeo.pendown()
    romeo.forward(20)
    romeo.penup()
#-----------------------
    romeo.goto(100,-80)
    romeo.color("red")
    romeo.begin_fill()
    romeo.circle(15)
    romeo.end_fill()
    romeo.goto (0,-140)
    romeo.penup()
#-----------------------
def Romeo_Writes_Var_06():
    romeo.color("white")
    romeo.goto(-100,-100)
    romeo.write("Y", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    #-----------------
    romeo.goto(-40,-100)
    romeo.write("X", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    #-----------------
    romeo.goto(20,-100)
    romeo.write("Z", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    #-----------------
    romeo.goto(100,-100)
    romeo.write("R", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
#---------------------
def Romeo_Fills_9Circles():
    romeo.goto(-180,150)
    romeo.ht()
    romeo.speed(0)
    for x in range (9):
        romeo.showturtle()
        romeo.penup()
        romeo.goto((-180+x*45),150)
        romeo.color(colors[x])
        romeo.begin_fill()
        romeo.circle(15)
        romeo.end_fill()
        romeo.penup()
        #print ('tn', tn)
        romeo.goto (0,-160)
#---------------------
def Number_selector():
    Tn1.goto(-180,150)
    Tn1.st()
    Tn2.goto(-135,150)
    Tn2.st()
    Tn3.goto(-90,150)
    Tn3.st()
    Tn4.goto(-45,150)
    Tn4.st()
    Tn5.goto(0,150)
    Tn5.st()
    Tn6.goto(45,150)
    Tn6.st()
    Tn7.goto(90,150)
    Tn7.st()
    Tn8.goto(135,150)
    Tn8.st()
    Tn9.goto(180,150)
    Tn9.st()




    #---------------------
def Turtle_selector():
    #---Draw cell (end game)
    Tc_end.color('red')
    Tc_end.st()
    Tc_end.penup()
    Tc_end.goto(160, 20)
    print ('Tc_end_pos',Tc_end.pos())
    #-------------
    #Turtle cell poitioner
    Tc1.goto(-180,110)
    Tc1.st()
    Tc2.goto(-135,110)
    Tc2.st()
    Tc3.goto(-90,110)
    Tc3.st()
    Tc4.goto(-45,110)
    Tc4.st()
    Tc5.goto(0,110)
    Tc5.st()
    Tc6.goto(45,110)
    Tc6.st()
    Tc7.goto(90,110)
    Tc7.st()
    Tc8.goto(135,110)
    Tc8.st()
    Tc9.goto(175,110)
    Tc9.st()

    #------------------------
    #write name cells
def Romeo_Draws_9Boxes():
    romeo.color("blue")
    romeo.penup()
    romeo.goto(-180,150)
    romeo.speed(0)
    for x in range (9):
        romeo.goto((-183+x*45),120)
        romeo.write(Boxes[x])
        romeo.penup()
    #---------------
    romeo.goto(160,30)
    romeo.write('END', None, align="center",font=("Arial",10,"normal"))
    romeo.goto (0,-160)
#-------------------------
def Romeo_Draws_Numbers():
    romeo.color("white")
    romeo.penup()
    romeo.goto(-180,150)
    romeo.speed(0)
    for x in range (9):
        romeo.goto((-180+x*45),155)
        romeo.write((x+1), None, align="center",font=("Arial",12,"normal"))
        romeo.penup()
    romeo.goto (0,-160)
#---------------------
#----------------
def Romeo_Fills_Row1():
    romeo.showturtle()
    romeo.color('pink')
    romeo.speed(0)
    romeo.begin_fill()
    romeo.goto(-45,70)
    romeo.goto(45,70)
    romeo.goto(45,40)
    romeo.goto(-45,40)
    romeo.goto(-45,70)
    romeo.end_fill()
    romeo.penup()
    romeo.goto(0,-130)    
#-------------------------
def Romeo_Fills_Row2():
    romeo.showturtle()
    romeo.color('pink')
    romeo.speed(0)
    romeo.begin_fill()
    romeo.goto(-45,40)
    romeo.goto(45,40)
    romeo.goto(45,10)
    romeo.goto(-45,10)
    romeo.goto(-45,40)
    romeo.end_fill()
    romeo.penup()
    romeo.goto(0,-130)
#-------------------------
def Romeo_Fills_Row3():
    romeo.showturtle()
    romeo.color('pink')
    romeo.speed(10)
    romeo.begin_fill()
    romeo.goto(-45,10)
    romeo.goto(45,10)
    romeo.goto(45,-20)
    romeo.goto(-45,-20)
    romeo.goto(-45,10)
    romeo.end_fill()
    romeo.penup()
    romeo.goto(0,-130)
#-------------------------
def Romeo_Fills_Ch1():
    romeo.showturtle()
    romeo.color('pink')
    romeo.speed(0)
    romeo.begin_fill()
    romeo.goto(-45,70)
    romeo.goto(-15,70)
    romeo.goto(-15,-20)
    romeo.goto(-45,-20)
    romeo.goto(-45,70)
    romeo.end_fill()
    romeo.penup()
    romeo.goto(0,-130)  
#-------------------------
def Romeo_Fills_Ch2():
    romeo.showturtle()
    romeo.color('pink')
    romeo.speed(10)
    romeo.begin_fill()
    romeo.goto(-15,70)
    romeo.goto(15,70)
    romeo.goto(15,-20)
    romeo.goto(-15,-20)
    romeo.goto(-15,70)
    romeo.end_fill()
    romeo.penup()
    romeo.goto(0,-130) 
#-------------------------
def Romeo_Fills_Ch3():
    romeo.showturtle()
    romeo.color('pink')
    romeo.speed(0)
    romeo.begin_fill()
    romeo.goto(15,70)
    romeo.goto(45,70)
    romeo.goto(45,-20)
    romeo.goto(15,-20)
    romeo.goto(15,70)
    romeo.end_fill()
    romeo.penup()
    romeo.goto(0,-130)     
#-------------------------
def Romeo_Fills_Dh1():
    romeo.showturtle()
    romeo.color('pink')
    romeo.speed(0)
    romeo.begin_fill()
    romeo.goto(-45,70)
    romeo.goto(-15,70)
    romeo.goto(-15,40)
    romeo.goto(-45,40)
    romeo.goto(-45,70)
    romeo.end_fill()
    romeo.penup()
    romeo.goto(0,-130)
    #-----------------
    romeo.begin_fill()
    romeo.goto(-15,40)
    romeo.goto(15,40)
    romeo.goto(15,10)
    romeo.goto(-15,10)
    romeo.goto(-15,40)
    romeo.end_fill()
    romeo.penup()
    romeo.goto(0,-130)
    #-----------------
    romeo.begin_fill()
    romeo.goto(15,10)
    romeo.goto(45,10)
    romeo.goto(45,-20)
    romeo.goto(15,-20)
    romeo.goto(15,10)
    romeo.end_fill()
    romeo.penup()
    romeo.goto(0,-130)
    
    
#-------------------------
def Romeo_Fills_Dh2():
    romeo.showturtle()
    romeo.color('pink')
    romeo.speed(0)
    romeo.begin_fill()
    romeo.goto(15,70)
    romeo.goto(45,70)
    romeo.goto(45,40)
    romeo.goto(15,40)
    romeo.goto(15,70)
    romeo.end_fill()
    romeo.penup()
    romeo.goto(0,-130)
    #-----------------
    romeo.begin_fill()
    romeo.goto(-15,40)
    romeo.goto(15,40)
    romeo.goto(15,10)
    romeo.goto(-15,10)
    romeo.goto(-15,40)
    romeo.end_fill()
    romeo.penup()
    romeo.goto(0,-130)
    #-----------------
    romeo.begin_fill()
    romeo.goto(-45,10)
    romeo.goto(-15,10)
    romeo.goto(-15,-20)
    romeo.goto(-45,-20)
    romeo.goto(-45,10)
    romeo.end_fill()
    romeo.penup()
    romeo.goto(0,-130)
#--------------------------
def Random_generator():
    global r_number, r_cell
    if len(Boxes)>0:
        r_number = Numbers[randint(0,(len(Numbers)-1))] # randomizzazione di Numbers[r_number]
        r_cell = Boxes[randint(0,len(Boxes)-1)]
    else:
        end_game=True
        End_Game()
                
#-------------------------
def Randomizer():
    global rc
    global rn
    global counter
    global level
    global sequence
    global R_cells
    global Mem_numbers,Mem_cells
    global matrix_temp, Mem_matrix
    global r_number, r_cell
    while len(Numbers) > 1 and counter < limit:
        counter=counter+1
        
        # riduttore di randomizzazione
        if len(matrix_temp)>0:
            Mem_matrix.update(matrix_temp)
            
            for c in matrix_temp:
                Mem_numbers.append(matrix_temp[c])
                print(Mem_numbers)
            # procedura riduzione numeri
            Numbers_remover()
        print('............................')
        print('Mem_matrix= ',Mem_matrix)
        print('matrix_temp',matrix_temp)
        print('Mem_numbers= ', Mem_numbers)
        #------------------------------------
        print('RIDUTTORE per BOXES')
        Boxes_remover()
         
        matrix_temp={}
        print('matrix_temp vuota',matrix_temp)
        print('***********************')
        print('Boxes= ',Boxes)
        print('Mem_matrix= ',Mem_matrix)
        print('=======================')
        print ('Mem_numbers= ', Mem_numbers)
        print ('Numbers= ', Numbers)
        #------------------------------------
        #-----Random_Generator----------
        Random_generator()
        #-----------------------         
        #r_cell = 'c'+str(r_cell)
        R_Cells.append(r_cell)
        rc = set(R_Cells)
        #----Limit len(R_Cells)---
        if counter > 10:
            del R_Cells[0]
        #rc = set(r_cell)
        #-------------------------
        #R_Numbers.append(r_number)
        #rn = set(R_Numbers)
        #rn = set(cells.values())
        #rn = set(str(r_number))
        #------------------
        
        if len(rc)> len(rn):
            print("errore")
            rc.pop()
        #print("R_Cells =",R_Cells)
        #print("R_Number=", R_Numbers)
        #print("accoppiata", " r_cell=",r_cell, " r_number=",r_number)
        #romeo.goto(Cell_Pos[r_cell])
        #romeo.write(r_number)
        for c in cells.keys():
            if c!=r_cell:
                #print ('c=',c,)
                if cells[c] == r_number:
                    #print('**** invalid number', sel_number, 'c=',c)
                    #print('sel_number is set to 0')
                    r_number = 0
                    cells[r_cell]=r_number 
                    break          
            cells[r_cell]=r_number
            if r_number > 0:
                rn = set(cells.values())
                #-----------------------
        print("----")
        print("counter=",counter)
        print("rc=",rc)
        print("rn=",rn)
        print("accoppiata", " r_cell=",r_cell, " r_number=",r_number)
        print("---")
        #---------------------------
        bea.color('red')
        bea.showturtle()
        romeo.hideturtle()
        #-----------------
        bea.goto(-50,120)
        bea.write ("I still remain",  None, align="center", font = ("Arial", 12, "normal"))
        bea.goto(10,120)
        attempts=limit - counter
        bea.write (attempts,  None, align="center", font = ("Arial", 12, "normal"))
        bea.goto(70,120)
        bea.write ("attempts",  None, align="center", font = ("Arial", 12, "normal"))
        #----------------
        bea.goto(Cell_Pos[r_cell])
        bea.write(r_number)
        bea.goto(0,-120)
        romeo.penup()
        romeo.goto(0,-120)
        bea.hideturtle()
        romeo.showturtle()
        T_Turns_Right(romeo)
        bea.clear()
        #---------------
        processing()
        writer.penup()
        writer.showturtle()
        writer_Draws_Matrix()
        writer.goto(0,-140)
        writer.hideturtle()
        romeo.showturtle()
        T_Turns_Left(romeo)
        writer.clear()
        Gradient()
        #----- controllo sequenze -----
        check_sequence()
        level=0
        print('sequence_counter= ',sequence_counter)
        print('counter_row1= ',counter_row1)
        print('counter_row2= ',counter_row2)
        print('counter_row3= ',counter_row3)
        print('counter_ch1= ',counter_ch1)
        print('counter_ch2= ',counter_ch2)
        print('counter_ch3= ',counter_ch3)
        print('counter_dh1= ',counter_dh1)
        print('counter_dh2= ',counter_dh2)
#----------------------------------------
def Permutation_System():
    global end_game
    writer.color('red')
    writer.penup()
    writer.goto (0, -120)
    romeo.goto(0,-120)
    T_Turns_Left(romeo)
    writer.write ("now I search for valid sequences",  None, align="center", font = ("Arial", 12, "normal"))
    Romeo_Draws_Equation()
    Romeo_Finds_Sequence()
    writer.clear()
    writer.color('blue')
    writer.goto(-180,70)
    for i in range (0,6):
        writer.goto((-180+(60*i),70))
        writer.write(Sequences[i])
    writer.goto(-180,50)
    for i in range (0,6):
        writer.goto((-180+(60*i),50))
        writer.write(Sequences[i+6])
    writer.goto(-180,30)
    for i in range (0,6):
        writer.goto((-180+(60*i),30))
        writer.write(Sequences[i+12])
    writer.goto(-180,10)
    for i in range (0,6):
        writer.goto((-180+(60*i),10))
        writer.write(Sequences[i+18])
    writer.goto(-180,-10)   
    for i in range (0,6):
        writer.goto((-180+(60*i),-10))
        writer.write(Sequences[i+24])
    writer.goto(-180,-30)   
    for i in range (0,6):
        writer.goto((-180+(60*i),-30))
        writer.write(Sequences[i+30])
        writer.goto(-180,-50)
    for i in range (0,6):
        writer.goto((-180+(60*i),-50))
        writer.write(Sequences[i+36])
        writer.goto(-180,-70)
    for i in range (0,6):
        writer.goto((-180+(60*i),-70))
        writer.write(Sequences[i+42])
    #----------------------------------
    writer.goto(0,-100)
    writer.color('blue')
    writer.write ("all the sequences give the result 15",  None, align="center", font = ("Arial", 12, "normal"))
    writer.hideturtle()
    romeo.goto(0,-160)
    writer.goto(0,-160)
    T_Turns_Right(romeo)
    #-------------------------------
    Filter_Num()
    T_Turns_Right(romeo)
    Sequentializer()
    T_Turns_Right(romeo)
    Demo_Seq()
    #------ THE END ----
    T_Fills_Square(romeo,-45,70,45,-20)
    T_Draws_Square(romeo,-45,70)
    romeo.goto(-100,-130)
    writer.goto(0,-130)
    bea.goto(100,-130)
    romeo.showturtle()
    bea.showturtle()
    writer.showturtle()
    T_Turns_Turtles()
    end_game=True
    End_Game()
         
#---------------------
def Romeo_Finds_Sequence():
    global s, x, y, z, r
    Int_Num=10
    counter=0
    N_seq=0
    for z in range(1,Int_Num):
        
        for y in range(1,Int_Num):

            for x in range (1,Int_Num):
                counter= counter+1
                r=x+y+z
                print('counter', counter,'sequence =',  z,y,x, 'RESULT=',r)
                if x != y and x != z and y !=z:
                    writer.clear()
                    T_Draws_Var_10(writer,s=True)
                    if r == 15:
                        N_seq=N_seq+1
                        R_15_Seq=(x,y,z)
                        Sequences.append(R_15_Seq)
                        R_15_Seq=()
                        writer.goto(0,180)
                        writer.color('red')
                        writer.write('well! I memorize the sequence', None, align="center",font=("Arial",12,"bold"))
                        writer.goto(0,-140)
                        writer.color('white')
                        T_Turns_Right(romeo)
                    
            print('N_seq= ',N_seq)
            writer.goto(0,0)
            writer.color('blue')
            writer.write(N_seq, None, align="center",font=("Arial",12,"bold"))
            writer.goto(0,20)
            writer.write('stored Sequences', None, align="center",font=("Arial",12,"bold"))
            writer.goto(0,-140)
            T_Turns_Left(romeo)
            romeo.hideturtle()
            writer.color('white')
            print('-----------------')
    print('N_seq= ',N_seq)
    print(Sequences)               
#----------------------
def Romeo_Draws_Equation():
    if romeo.heading()==270:
        romeo.right(180)
        # case of the even counter
    T_Draws_Boxes_10(romeo)
    T_Draws_Var_10(writer)
    romeo.color("blue")
    romeo.goto(0,100)
    romeo.write("remember: commutative property of the sum of real numbers", None, align="center",font=("Arial",10,"bold"))
    romeo.goto(0,-140)
    T_Turns_Left(romeo)  
#----------------------
def T_Draws_Boxes_10(turtle_name): 
    t= turtle_name
    t.right(90)
    t.penup()
    t.showturtle()
    t.speed(0)
    t.penup()
    t.color("purple")
    t.begin_fill()
    t.goto(-115,160)
    t.goto(-85,160)
    t.goto(-85,130)
    t.goto(-115,130)
    t.goto(-115,160)
    t.end_fill()
    t.goto(-80,145)
    
    #-----------------
    t.color("blue")
    t.pendown()
    t.forward(20)
    t.penup()
    t.right(90)
    t.forward(15)
    t.right(90)
    t.penup()
    t.forward(10)
    t.right(90)
    t.penup()
    t.forward(5)
    t.pendown()
    t.forward(20)
    t.penup()
    #-----------------
    t.color("green")
    t.begin_fill()
    t.goto(-55,160)
    t.goto(-25,160)
    t.goto(-25,130)
    t.goto(-55,130)
    t.goto(-55,160)
    t.end_fill()
    t.goto(-20,145)
    t.right(90)
    #----------------
    t.color("blue")
    t.pendown()
    t.forward(20)
    t.penup()
    t.right(90)
    t.forward(15)
    t.right(90)
    t.penup()
    t.forward(10)
    t.right(90)
    t.penup()
    t.forward(5)
    t.pendown()
    t.forward(20)
    t.penup()
    #----------------
    t.color("violet")
    t.begin_fill()
    t.goto(5,160)
    t.goto(35,160)
    t.goto(35,130)
    t.goto(5,130)
    t.goto(5,160)
    t.end_fill()
    t.goto (50,150)
#-----------------------
    t.color("blue")
    t.right(90)
    t.pendown()
    t.forward(20)
    t.penup()
    t.right(90)
    t.forward(10)
    t.right(90)
    t.pendown()
    t.forward(20)
    t.penup()
#-----------------------
    t.goto(100,160)
    t.color("red")
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.goto (0,-140)
    t.hideturtle()
#-----------------------
def T_Draws_Var_10(turtle_name,s=None):
    t = turtle_name
    t.showturtle()
    t.penup()
    t.color("white")
    t.speed(0)
    t.goto(-100,140)
    if s == None:
        t.write("X", None, align="center",font=("Arial",10,"normal"))
    else:
        t.write(x, None, align="center",font=("Arial",10,"normal"))        
    t.goto(0,0)
    #-----------------
    t.goto(-40,140)
    if s == None:
        t.write("Y", None, align="center",font=("Arial",10,"normal"))
    else:
        t.write(y, None, align="center",font=("Arial",10,"normal"))
    t.goto(0,0)
    #-----------------
    t.goto(20,140)
    if s == None:
        t.write("Z", None, align="center",font=("Arial",10,"normal"))
    else:
        t.write(z, None, align="center",font=("Arial",10,"normal"))
    t.goto(0,0)
    #-----------------
    t.goto(100,140)
    if s == None:
        t.write("R", None, align="center",font=("Arial",10,"normal"))
    else:
        t.write(r, None, align="center",font=("Arial",10,"normal"))
    
    t.goto(0,0)
    t.hideturtle()
#---------------------
def Filter_Num():
    global s_similar,n,sequence
    counter=0
    center_num=[]
    indice=[]
    for i in range(0,len(Sequences)):
        center_num.append(Sequences[i][1])
    print('center_num=',center_num)
    print('...........................')
    
    for n in range(1,10):
        sequence=center_num.count(n)
        for x in range(1,10):
            indice=center_num.index(n)
       
        print('n= ',n, 'sequence', sequence)
        writer.clear()
        T_Writes_Info(writer,n,sequence)
    print('__________________')    
    for x in Sequences:
        
        part=x
        
        for simil in range (1,10):
            if simil == part[1]:
                #print('x=',x)
               
                s_similar[x]=(simil)

                #print ('simil',simil)
                #print('---')
    print('s_similar=',s_similar)
    print('*********************************')
#--------------------------
def T_Writes_Info(turtle_name,n,sequence):
    t = turtle_name
    t.color('red')
    t.penup()
    t.goto(0,60)
    t.showturtle()
    t.write('counting sequences of the central number', None, align="center",font=("Arial",10,"normal"))
    #t.goto(-120,60)
    #T_Turns_Left(romeo)
    t.goto(-100,0)
    t.write('central number',  None, align="center",font=("Arial",12,"normal"))
    t.goto(-40,0)
    t.write(n,  None, align="center",font=("Arial",12,"normal"))
    t.goto(50,0)
    t.write('- number of sequence =',  None, align="center",font=("Arial",12,"normal"))
    t.goto(140,0)
    t.write(sequence,  None, align="center",font=("Arial",12,"normal"))
    t.hideturtle()
    t.goto(0,-140)
    T_Turns_Right(romeo)
    t.clear()
#--------------------------
def Sequentializer():
    global temp_seq
    global seq
    for i in range (1,10):
        
        for c in s_similar:
            if i == c[1]:
                temp_seq.append(c)
                print('i=',i)
                print('****')
                
        print('temp_seq= ',temp_seq)
        T_Writes_Info_Seq(writer,temp_seq)
        seq.append(temp_seq)
        temp_seq=[]
    print('seq', seq)
#--------------------------------
#----------------------------
def T_Writes_Combination(turtle_name,x,y):
    t=turtle_name
    t.penup()
    t.showturtle()
    t.color('blue')
    t.speed(0)
    t.goto(x,y)
    c='c'
    d=30
    for l in range (3):
        t.goto(x+15+(d*l),y-25)
        t.write(cells[c+str(l+1)],  None, align="center",font=("Arial",12,"normal"))
        #print (c, cells[c])
        #------------------
    for l in range (3):
        t.goto(x+15+(d*l),y-55)
        t.write(cells[c+str(3+l+1)],  None, align="center",font=("Arial",12,"normal"))
        #print (c, cells[c])
        #------------------   
    for l in range (3):
        t.goto(x+15+(d*l),y-85)
        t.write(cells[c+str(6+l+1)],  None, align="center",font=("Arial",12,"normal"))
        #print (c, cells[c])
        #------------------      
    t.goto(x-15,y+5)
    t.write(d_h1,  None, align="center",font=("Arial",12,"normal"))
    t.goto(x+15,y+5)
    t.write(ch1,  None, align="center",font=("Arial",12,"normal"))
    t.goto(x+45,y+5)
    t.write(ch2,  None, align="center",font=("Arial",12,"normal"))
    t.goto(x+75,y+5)
    t.write(ch3,  None, align="center",font=("Arial",12,"normal"))
    t.goto(x+110,y+5)
    t.write(d_h2,  None, align="center",font=("Arial",12,"normal"))
  
    #-----------------
    t.goto(x-15,y-25)
    t.write(r_l1,  None, align="center",font=("Arial",12,"normal"))
    t.goto(x+110,y-25)
    t.write(rw1,  None, align="center",font=("Arial",12,"normal"))
   
    #----------------
    t.goto(x-15,y-55)
    t.write(r_l2,  None, align="center",font=("Arial",12,"normal"))
    t.goto(x+110,y-55)
    t.write(rw2,  None, align="center",font=("Arial",12,"normal"))
    #------------------
    t.goto(x-15,y-85)
    t.write(r_l3,  None, align="center",font=("Arial",12,"normal"))
    t.goto(x+110,y-85)
    t.write(rw3,  None, align="center",font=("Arial",12,"normal"))
    #------------------
    t.goto(x-15,y-115)
    t.write(d_l1,  None, align="center",font=("Arial",12,"normal"))
    t.goto(x+15,y-115)
    t.write(cl1,  None, align="center",font=("Arial",12,"normal"))
    t.goto(x+45,y-115)
    t.write(cl2,  None, align="center",font=("Arial",12,"normal"))
    t.goto(x+75,y-115)
    t.write(cl3,  None, align="center",font=("Arial",12,"normal"))
    t.goto(x+110,y-115)
    t.write(d_l2,  None, align="center",font=("Arial",12,"normal"))
    t.hideturtle()
#----------------------------
def Select_1Seq(turtle_name,x,y):    
    t=turtle_name
    t.speed(0)
    t.penup()
    t.showturtle()
    t.color('blue')
    t.goto(x,y)
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.goto (0,55)
    t.hideturtle()
#----------------------------
def Select_2Seq(turtle_name,x,y):    
    t=turtle_name
    t.speed(0)
    t.penup()
    t.showturtle()
    t.color('blue')
    t.goto(x,y)
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.goto (0,55)
    t.hideturtle()
#----------------------------------
def Select_3Seq(turtle_name,x,y):    
    t=turtle_name
    t.speed(0)
    t.penup()
    t.showturtle()
    t.color('blue')
    t.goto(x,y)
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.goto (0,55)
    t.hideturtle()
#----------------------------------
def Select_4Seq(turtle_name,x,y):    
    t=turtle_name
    t.speed(0)
    t.penup()
    t.showturtle()
    t.color('blue')
    t.goto(x,y)
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.goto (0,55)
    t.hideturtle()
#----------------------------------
def Select_5Seq(turtle_name,x,y):    
    t=turtle_name
    t.penup()
    t.showturtle()
    t.color('blue')
    t.goto(x,y)
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.goto (0,55)
    t.hideturtle()
#----------------------------------
def Select_6Seq(turtle_name,x,y):    
    t=turtle_name
    t.penup()
    t.showturtle()
    t.color('blue')
    t.goto(x,y)
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.goto (0,55)
    t.hideturtle()
#*************************
def Show_The_Combinations():
    romeo.clear()
    bea.clear()
    writer.clear()
    writer.penup()
    writer.goto(0,190)
    writer.color('blue')
    writer.write("these are the first four combinations of sequences:",None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,170)
    writer.color('blue')
    writer.write("which are generated with the rotation to the right.",None, align="center",font=("Arial",10,"normal"))
    #--------------------
    writer.goto(0,150)
    writer.color('blue')
    writer.write("D  -  B  -  A  -  C <> !B  -  D  -  !C  -  A",None, align="center",font=("Arial",12,"bold"))
    #--------------------
    T_Fills_Square(romeo,-150,115,-60,25) 
    romeo.left(90)
    T_Draws_Square(romeo, -150, 115)
    Number_Distributor_M1()
    # D  -  B -  A -  C
    processing()
    T_Writes_Combination(bea,-150, 115)
    #---------------------------------
    T_Fills_Square(romeo, 50, 115, 140, 25) 
    romeo.right(90)
    T_Draws_Square(romeo, 50, 115)
    Number_Distributor_M2()
    # !B  -  D -  !C  -  A
    processing()
    T_Writes_Combination(bea,50, 115)
    #--------------------------------
    T_Fills_Square(romeo,-150, -45,-60,-135) 
    romeo.right(90)
    T_Draws_Square(romeo, -150, -45)
    Number_Distributor_M3()
    # !D -  !B  -  !A  -  !C
    processing()
    T_Writes_Combination(bea,-150, -45)
    #--------------------------------
    T_Fills_Square(romeo,50, -45, 140,-135) 
    romeo.right(90)
    T_Draws_Square(romeo, 50, -45)
    Number_Distributor_M4()
    # !B -  D  -  !A  -  !C
    processing()
    T_Writes_Combination(bea, 50, -45)
    #---------------------------------
    writer.goto(0,-180)
    writer.color('blue')
    writer.write("!D  -  !B  -  !A  -  !C <> B  -  !D -  !A -  C",None, align="center",font=("Arial",12,"bold"))
#**************************************
    #--- variants for M1 ---
    romeo.goto(0,0)
    T_Turns_Right(romeo)
    bea.clear()
    romeo.clear()
    #romeo.right(90)
    writer.clear()
    writer.penup()
    writer.goto(0,190)
    writer.color('blue')
    writer.write("Now the two specular variants for the first combination:",None, align="center",font=("Arial",10,"normal"))
   #---------------------
    writer.goto(-150,170)
    writer.color('blue')
    writer.write(seq[4][0],None, align="center",font=("Arial",12,"bold"))
    writer.goto(-50,170)
    writer.color('blue')
    writer.write(seq[4][1],None, align="center",font=("Arial",12,"bold"))
    writer.goto(50,170)
    writer.color('blue')
    writer.write(seq[4][2],None, align="center",font=("Arial",12,"bold"))
    writer.goto(150,170)
    writer.color('blue')
    writer.write(seq[4][3],None, align="center",font=("Arial",12,"bold"))
    #------------------------------------
    # variants for 1 combinations
    #--------------
    writer.goto(0,150)
    writer.color('blue')
    writer.write("vertical reflection <> horizontal reflection",None, align="center",font=("Arial",12,"bold"))
    romeo.left(90)
    T_Fills_Square(romeo,-150,115,-60,25)
    T_Draws_Square(romeo, -150, 115)
    Number_Distributor_M1()
    # D  -  B -  A -  C
    processing()
    T_Writes_Combination(bea,-150, 115)
    #---------------------------------
    #--- vertical reflection ----
    T_Fills_Square(romeo,-150, -45,-60,-135) 
    T_Draws_Square(romeo, -150, -45)
    Number_Distributor_M1U()
    # D  -  !B  -  !A  -  !C
    processing()
    T_Writes_Combination(bea,-150, -45)
    #---------------------------------
    #--- horizontaln reflection ---
    T_Fills_Square(romeo, 50, 115, 140, 25) 
    romeo.right(90)
    T_Draws_Square(romeo, 50, 115)
    Number_Distributor_M1R()
    # !D  -  B  -  A  -  C
    processing()
    T_Writes_Combination(bea,50, 115)
#------***------***------
    #--- variants for M2 ---
    romeo.goto(0,0)
    T_Turns_Right(romeo)
    bea.clear()
    romeo.clear()
    #romeo.right(90)
    writer.clear()
    writer.penup()
    writer.goto(0,190)
    writer.color('blue')
    writer.write("Now the two specular variants for the second combination:",None, align="center",font=("Arial",10,"normal"))
   #---------------------
    writer.goto(-150,170)
    writer.color('blue')
    writer.write(seq[4][0],None, align="center",font=("Arial",12,"bold"))
    writer.goto(-50,170)
    writer.color('blue')
    writer.write(seq[4][1],None, align="center",font=("Arial",12,"bold"))
    writer.goto(50,170)
    writer.color('blue')
    writer.write(seq[4][2],None, align="center",font=("Arial",12,"bold"))
    writer.goto(150,170)
    writer.color('blue')
    writer.write(seq[4][3],None, align="center",font=("Arial",12,"bold"))
    #------------------------------------
    # variants for 2 combinations
    #--------------
    writer.goto(0,150)
    writer.color('blue')
    writer.write("vertical reflection <> horizontal reflection",None, align="center",font=("Arial",12,"bold"))
    romeo.left(90)
    T_Fills_Square(romeo,-150,115,-60,25)
    T_Draws_Square(romeo, -150, 115)
    Number_Distributor_M2()
    # !B  -  D -  !C -  A
    processing()
    T_Writes_Combination(bea,-150, 115)
    #---------------------------------
    #--- vertical reflection ----
    T_Fills_Square(romeo,-150, -45,-60,-135) 
    T_Draws_Square(romeo, -150, -45)
    Number_Distributor_M2U()
    # D  -  !B  -  !A  -  !C
    processing()
    T_Writes_Combination(bea,-150, -45)
    #---------------------------------
    #--- horizontaln reflection ---
    T_Fills_Square(romeo, 50, 115, 140, 25) 
    romeo.right(90)
    T_Draws_Square(romeo, 50, 115)
    Number_Distributor_M2R()
    # !D  -  B  -  A  -  C
    processing()
    T_Writes_Combination(bea,50, 115)
#------***------***------
    #--- variants for M3 ---
    romeo.goto(0,0)
    T_Turns_Right(romeo)
    bea.clear()
    romeo.clear()
    writer.clear()
    writer.penup()
    writer.goto(0,190)
    writer.color('blue')
    writer.write("Now the two specular variants for the third combination:",None, align="center",font=("Arial",10,"normal"))
   #---------------------
    writer.goto(-150,170)
    writer.color('blue')
    writer.write(seq[4][0],None, align="center",font=("Arial",12,"bold"))
    writer.goto(-50,170)
    writer.color('blue')
    writer.write(seq[4][1],None, align="center",font=("Arial",12,"bold"))
    writer.goto(50,170)
    writer.color('blue')
    writer.write(seq[4][2],None, align="center",font=("Arial",12,"bold"))
    writer.goto(150,170)
    writer.color('blue')
    writer.write(seq[4][3],None, align="center",font=("Arial",12,"bold"))
    #------------------------------------
    # variants for 3 combinations
    #--------------
    writer.goto(0,150)
    writer.color('blue')
    writer.write("vertical reflection <> horizontal reflection",None, align="center",font=("Arial",12,"bold"))
    romeo.left(90)
    T_Fills_Square(romeo,-150,115,-60,25)
    T_Draws_Square(romeo, -150, 115)
    Number_Distributor_M3()
    # !D !B !A !C
    processing()
    T_Writes_Combination(bea,-150, 115)
    #---------------------------------
    #--- vertical reflection ----
    T_Fills_Square(romeo,-150, -45,-60,-135) 
    T_Draws_Square(romeo, -150, -45)
    Number_Distributor_M3U()
    # !D B C A
    processing()
    T_Writes_Combination(bea,-150, -45)
    #---------------------------------
    #--- horizontaln reflection ---
    T_Fills_Square(romeo, 50, 115, 140, 25) 
    romeo.right(90)
    T_Draws_Square(romeo, 50, 115)
    Number_Distributor_M3R()
    # D !B !C !A
    processing()
    T_Writes_Combination(bea,50, 115)
#*******************************
#------- LAST COMBINATION
    #--- variants for M4 ---
    romeo.goto(0,0)
    T_Turns_Right(romeo)
    bea.clear()
    romeo.clear()
    writer.clear()
    writer.penup()
    writer.goto(0,190)
    writer.color('blue')
    writer.write("Now the two specular variants for the LAST combination:",None, align="center",font=("Arial",10,"normal"))
   #---------------------
    writer.goto(-150,170)
    writer.color('blue')
    writer.write(seq[4][0],None, align="center",font=("Arial",12,"bold"))
    writer.goto(-50,170)
    writer.color('blue')
    writer.write(seq[4][1],None, align="center",font=("Arial",12,"bold"))
    writer.goto(50,170)
    writer.color('blue')
    writer.write(seq[4][2],None, align="center",font=("Arial",12,"bold"))
    writer.goto(150,170)
    writer.color('blue')
    writer.write(seq[4][3],None, align="center",font=("Arial",12,"bold"))
    #------------------------------------
    # variants for 4 combinations
    #--------------
    writer.goto(0,150)
    writer.color('blue')
    writer.write("vertical reflection <> horizontal reflection",None, align="center",font=("Arial",12,"bold"))
    romeo.left(90)
    T_Fills_Square(romeo,-150,115,-60,25)
    T_Draws_Square(romeo, -150, 115)
    Number_Distributor_M4()
    # B !D A C
    processing()
    T_Writes_Combination(bea,-150, 115)
    #---------------------------------
    #--- vertical reflection ----
    T_Fills_Square(romeo,-150, -45,-60,-135) 
    T_Draws_Square(romeo, -150, -45)
    Number_Distributor_M4U()
    # B D !A !C
    processing()
    T_Writes_Combination(bea,-150, -45)
    #---------------------------------
    #--- horizontaln reflection ---
    T_Fills_Square(romeo, 50, 115, 140, 25) 
    romeo.right(90)
    T_Draws_Square(romeo, 50, 115)
    Number_Distributor_M4R()
    # !B !D C A
    processing()
    T_Writes_Combination(bea,50, 115)    
    #--- end of the combinations with result 15 ---
    romeo.goto(90,-30)
    romeo.write("I found", None, align="center",font=("Arial",12,"normal"))
    romeo.goto(90,-50)
    romeo.write("12", None, align="center",font=("Arial",12,"normal"))
    romeo.goto(90,-70)
    romeo.write("combinations", None, align="center",font=("Arial",12,"normal"))
    writer.goto(40,-130)
    writer.write("Romeo - Writer - Bea")
    writer.goto(90,-150)
    writer.write("they thank you", None, align="center",font=("Arial",12,"normal"))
    writer.goto(90,-170)
    writer.write("for playing together", None, align="center",font=("Arial",12,"normal"))
    romeo.goto(50,-100)
    writer.goto(90,-100)
    bea.goto(130,-100)
    bea.left(90)
    romeo.showturtle()
    bea.showturtle()
    writer.showturtle()
    T_Turns_Turtles()
    Final_Greetings()
    
    
#*****************************  
def Final_Greetings():
    global end_game
    romeo.clear()
    writer.clear()
    bea.clear()
    writer.goto(0,170)
    writer.color("blue")
    writer.write("The results you've seen", None, align="center",font=("Arial",12,"normal"))
    writer.goto(0,150)
    writer.write("they are not due to artificial intelligence", None, align="center",font=("Arial",12,"normal"))
    writer.goto(0,130)
    writer.write("but to a hard work of calculation.", None, align="center",font=("Arial",12,"normal"))
    writer.goto(0,110)
    writer.write("Look in the program code", None, align="center",font=("Arial",12,"normal"))
    writer.goto(0,90)
    writer.write("maybe you'll find some interesting things ...", None, align="center",font=("Arial",12,"normal"))
    writer.goto(0,-70)
    writer.write("you also have fun studying ...", None, align="center",font=("Arial",12,"normal"))
    writer.goto(-50,0)
    romeo.goto(0,0)
    bea.goto(50,0)
    romeo.showturtle()
    bea.showturtle()
    writer.showturtle()
    T_Turns_Turtles()
    #end_game=True
    #End_Game()
    
#*************************
def Show_Combinations():
    romeo.clear()
    bea.clear()
    writer.clear()
    writer.penup()
    writer.goto(0,190)
    writer.color('blue')
    writer.write("let's consider the first four sequences:", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,170)
    writer.write(seq[4],None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,150)
    writer.color('blue')
    writer.write("Seq. 1 - Seq. 2 - Seq. 3 - Seq. 4                                                     ",None, align="center",font=("Arial",10,"normal"))
    romeo.penup()
    T_Fills_S1_4Boxes(romeo)
    S1_1Combinations(writer)
    T_Turns_Right(romeo)
    T_Fills_Square(romeo,-45,-65,45,-155)
    romeo.left(90)
    T_Draws_Square(romeo, -45, -65)
    bea.goto(0,55)
    T_Fills_8Boxes(romeo, -15, -35)
    #*********************************
    bea.right(180) # move to the center 4 boxes
    Select_1Seq(bea,-145,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C1()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #---------------------
    Select_2Seq(bea,0,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C2()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #--------------
    Select_3Seq(bea,145,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C3()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #--------------
    Select_4Seq(bea,-145,0)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C4()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #--------------
    Select_5Seq(bea,0,0)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C5()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #--------------
    Select_6Seq(bea,145,0)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C6()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    #------------------
    First_Consideration()
    #--------------------
    S2_5Combinations(writer)
    romeo.goto(0,55)
    T_Turns_Right(romeo)
    #------------------------
    Select_1Seq(bea,-145,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S2C1()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #----------------------
    Select_2Seq(bea,0,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S2C2()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #------------------------
    Select_3Seq(bea,145,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S2C3()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #------------------------
    Select_4Seq(bea,-145,0)
    T_Turns_Right(bea)
    Number_Distributor_05_S2C4()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #-------------------
    Select_5Seq(bea,0,0)
    T_Turns_Right(bea)
    Number_Distributor_05_S2C5()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #--------------
    Select_6Seq(bea,145,0)
    T_Turns_Right(bea)
    Number_Distributor_05_S2C6()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #---------------------
    Second_Consideration()
    #---------------------
    
    S1_2Combinations(writer)
    romeo.goto(0,55)
    T_Turns_Right(romeo)
    #------------------------
    Select_1Seq(bea,-145,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C7()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #---------------------
    Select_2Seq(bea,0,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C8()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #----------------------
    Select_3Seq(bea,145,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C9()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #--------------
    Select_4Seq(bea,-145,0)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C10()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #--------------
    Select_5Seq(bea,0,0)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C11()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #--------------
    Select_6Seq(bea,145,0)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C12()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    #------------------
    Third_Consideration()
    #------------------
    S2_6Combinations(writer)
    romeo.goto(0,55)
    T_Turns_Right(romeo)
    #------------------------
    Select_1Seq(bea,-145,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S2C7()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #---------------------
    Select_2Seq(bea,0,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S2C8()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #----------------------
    Select_3Seq(bea,145,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S2C9()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #--------------
    Select_4Seq(bea,-145,0)
    T_Turns_Right(bea)
    Number_Distributor_05_S2C10()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #--------------
    Select_5Seq(bea,0,0)
    T_Turns_Right(bea)
    Number_Distributor_05_S2C11()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #--------------
    Select_6Seq(bea,145,0)
    T_Turns_Right(bea)
    Number_Distributor_05_S2C12()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    #------------------
    Fourth_Consideration()
    #------------------ 
    S1_3Combinations(writer)
    romeo.goto(0,55)
    T_Turns_Right(romeo)
    #------------------------
    Select_1Seq(bea,-145,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C13()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #---------------------
    Select_2Seq(bea,0,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C14()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #----------------------
    Select_3Seq(bea,145,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C15()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #--------------
    Select_4Seq(bea,-145,0)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C16()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #--------------
    Select_5Seq(bea,0,0)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C17()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #--------------
    Select_6Seq(bea,145,0)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C18()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    #--------------
    #------------------
    Fifth_Consideration()
    #------------------
    S2_7Combinations(writer)
    romeo.goto(0,55)
    T_Turns_Right(romeo)

    #------------------------
    Select_1Seq(bea,-145,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S2C13()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #---------------------
    Select_2Seq(bea,0,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S2C14()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #----------------------
    Select_3Seq(bea,145,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S2C15()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #--------------
    Select_4Seq(bea,-145,0)
    T_Turns_Right(bea)
    Number_Distributor_05_S2C16()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #--------------
    Select_5Seq(bea,0,0)
    T_Turns_Right(bea)
    Number_Distributor_05_S2C17()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #--------------
    Select_6Seq(bea,145,0)
    T_Turns_Right(bea)
    Number_Distributor_05_S2C18()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    #------------------
    Sixth_Consideration()
    #----------------------------------
    S1_4Combinations(writer)
    romeo.goto(0,55)
    T_Turns_Right(romeo)
    #------------------------
    Select_1Seq(bea,-145,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C19()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #---------------------
    Select_2Seq(bea,0,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C20()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()
    #----------------------
    Select_3Seq(bea,145,100)
    T_Turns_Right(bea)
    Number_Distributor_05_S1C21()
    processing()
    T_Writes_Combination(bea,-45,-65)
    bea.goto(0,50)
    bea.color("red")
    bea.write("ATTENTION to this configuration: the solution is visible!",None, align="center",font=("Arial",10,"normal"))
    bea.goto(0,55)
    T_Turns_Right(bea)
    bea.clear()

##    #--------------
##    Select_4Seq(bea,-145,0)
##    T_Turns_Right(bea)
##    Number_Distributor_05_S1C22()
##    processing()
##    T_Writes_Combination(bea,-45,-65)
##    bea.goto(0,55)
##    T_Turns_Right(bea)
##    bea.clear()
##    #--------------
##    Select_5Seq(bea,0,0)
##    T_Turns_Right(bea)
##    Number_Distributor_05_S1C23()
##    processing()
##    T_Writes_Combination(bea,-45,-65)
##    bea.goto(0,55)
##    T_Turns_Right(bea)
##    bea.clear()
##    #--------------
##    Select_6Seq(bea,145,0)
##    T_Turns_Right(bea)
##    Number_Distributor_05_S1C24()
##    processing()
##    T_Writes_Combination(bea,-45,-65)
##    bea.goto(0,55)
##    T_Turns_Right(bea)
##    
##    #--------------
##    Seventh_Consideration()
##    #------------------
##    S2_8Combinations(writer)
##    romeo.goto(0,55)
##    T_Turns_Right(romeo)
##    #------------------------
##    Select_1Seq(bea,-145,100)
##    T_Turns_Right(bea)
##    Number_Distributor_05_S2C19()
##    processing()
##    T_Writes_Combination(bea,-45,-65)
##    bea.goto(0,55)
##    T_Turns_Right(bea)
##    bea.clear()
##    #---------------------
##    Select_2Seq(bea,0,100)
##    T_Turns_Right(bea)
##    Number_Distributor_05_S2C20()
##    processing()
##    T_Writes_Combination(bea,-45,-65)
##    bea.goto(0,55)
##    T_Turns_Right(bea)
##    bea.clear()
##    #----------------------
##    Select_3Seq(bea,145,100)
##    T_Turns_Right(bea)
##    Number_Distributor_05_S2C21()
##    processing()
##    T_Writes_Combination(bea,-45,-65)
##    bea.goto(0,50)
##    T_Turns_Right(bea)
##    bea.clear()
##    #--------------
##    Select_4Seq(bea,-145,0)
##    T_Turns_Right(bea)
##    Number_Distributor_05_S2C22()
##    processing()
##    T_Writes_Combination(bea,-45,-65)
##    bea.goto(0,55)
##    T_Turns_Right(bea)
##    bea.clear()
##    #--------------
##    Select_5Seq(bea,0,0)
##    T_Turns_Right(bea)
##    Number_Distributor_05_S2C23()
##    processing()
##    T_Writes_Combination(bea,-45,-65)
##    bea.goto(0,55)
##    T_Turns_Right(bea)
##    bea.clear()
##    #--------------
##    Select_6Seq(bea,145,0)
##    T_Turns_Right(bea)
##    Number_Distributor_05_S2C24()
##    processing()
##    T_Writes_Combination(bea,-45,-65)
    
    T_Turns_Right(bea)
    #-----------------
    Show_Solutions()

    #------------------------------------------
    Show_The_Combinations()

    
    
#----------------------------
    
#----------------------------
def Demo_Seq():
    T_Fills_Square(romeo,-45,70,45,-20)
    T_Draws_Square(romeo,-45,70)
    T_Fills_C5(romeo)
    T_Turns_Right(romeo)
    Example_1()
    T_Turns_Right(romeo)
    #romeo.clear()
    writer.clear()
    Example_2()
    T_Turns_Right(romeo)
    writer.clear()
    Example_3()
    T_Turns_Right(romeo)
    writer.clear()
    Example_4()
    T_Turns_Right(romeo)
    writer.clear()
    Example_5()
    T_Turns_Right(romeo)
    writer.clear()
    Example_6()
    T_Turns_Right(romeo)
    writer.clear()
    Example_7()
    T_Turns_Right(romeo)
    writer.clear()
    Example_8()
    T_Turns_Right(romeo)
    writer.clear()
    Example_9()
    T_Turns_Right(romeo)
    romeo.left(90)
    writer.clear()
    Base_Solutions()
    Show_Combinations()

#----------------------------
#-------------------------
def Number_Distributor_01():
    
    print(seq[0])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[0][0][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[0][1][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[0][2][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[0][3][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#-------------------------
def Number_Distributor_02():
    
    print(seq[1])
    k=0       
#-------------------------
def Number_Distributor_03():
    
    print(seq[2])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[2][0][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[2][1][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[2][2][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[2][3][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]    
#-------------------------
def Number_Distributor_04():
    
    print(seq[3])
    k=0       
#-------------------------
def Number_Distributor_05():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][0][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][1][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][2][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][3][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#***********************************
#---------Distributor _05_S1C1 ------------
    # ---A B C D --- 
def Number_Distributor_05_S1C1():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][0][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][1][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][2][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][3][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor _05_S1C2 ------------
    # ---A B D C ---
def Number_Distributor_05_S1C2():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][0][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][1][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][3][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][2][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor _05_S1C3 ------------
    # ---A C B D ---
def Number_Distributor_05_S1C3():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][0][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][2][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][1][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][3][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor _05_S1C4 ------------
    # ---A C D B ---
def Number_Distributor_05_S1C4():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][0][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][2][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][3][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][1][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor _05_S1C5 ------------
    # ---A D B C ---
def Number_Distributor_05_S1C5():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][0][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][3][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][1][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][2][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor _05_S1C6 ------------
    # ---A D C B ---
def Number_Distributor_05_S1C6():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][0][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][3][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][2][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][1][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#*****************************************
#--- sequences 5 - 6 - 7- 8 ---
#---------Distributor _05_S2C1 ------------
        #--- !A !B !C !D ---
def Number_Distributor_05_S2C1():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][4][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][5][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][6][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][7][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor _05_S2C2 ------------
        #--- !A !B! !D !C ---

def Number_Distributor_05_S2C2():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][4][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][5][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][7][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][6][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor _05_S2C3 ------------
        #--- !A !C !B !D ---
def Number_Distributor_05_S2C3():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][4][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][6][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][5][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][7][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor _05_S2C4 ------------
        #--- !A !C !D !B ---
def Number_Distributor_05_S2C4():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][4][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][6][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][7][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][5][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor _05_S2C5 ------------
        #--- !A !D !B !C ---
def Number_Distributor_05_S2C5():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][4][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][7][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][5][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][6][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor _05_S2C6 ------------
        #--- !A !D !C !B ---
def Number_Distributor_05_S2C6():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][4][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][7][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][6][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][5][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]

#**************************
#---------Distributor _05_S1C7 ------------
        #--- B A C D ---
def Number_Distributor_05_S1C7():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][1][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][0][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][2][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][3][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor _05_S1C8 ------------
        #--- B A D C ---
def Number_Distributor_05_S1C8():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][1][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][0][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][3][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][2][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S1C9 ------------
        #--- B C A D ---

def Number_Distributor_05_S1C9():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][1][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][2][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][0][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][3][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S1C10 ------------
        #--- B C D A ---
        
def Number_Distributor_05_S1C10():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][1][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][2][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][3][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][0][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]

#---------Distributor _05_S1C11 ------------
    #--- B D A C ---
def Number_Distributor_05_S1C11():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][1][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][3][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][0][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][2][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S1C12 ------------
    #--- B D C A ---
def Number_Distributor_05_S1C12():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][1][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][3][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][2][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][0][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#********************************
        
#--- sequences 5 - 6 - 7- 8 ---
#---------Distributor _05_S2C7 ------------
    #--- !B !A !C !D ---
def Number_Distributor_05_S2C7():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][5][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][4][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][6][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][7][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S2C8 ------------
    #--- !B !A !D !C ---

def Number_Distributor_05_S2C8():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][5][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][4][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][7][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][6][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S2C9 ------------
    #--- !B !C !A !D ---

def Number_Distributor_05_S2C9():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][5][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][6][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][4][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][7][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S2C10 ------------
    #--- !B !C !D !A ---
def Number_Distributor_05_S2C10():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][5][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][6][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][7][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][4][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S2C11 ------------
    #--- !B !D !A !C ---
def Number_Distributor_05_S2C11():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][5][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][7][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][4][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][6][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor _05_S2C12 ------------
    #--- !B !D !C !A ---
def Number_Distributor_05_S2C12():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][5][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][7][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][6][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][4][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#**************************
#---------Distributor _05_S1C13 ------------
    #--- C A B D ---        
        
def Number_Distributor_05_S1C13():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][2][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][0][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][1][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][3][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S1C14 ------------
    #--- C A D B ---
        
def Number_Distributor_05_S1C14():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][2][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][0][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][1][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][3][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S1C15 ------------
    #--- C B A D ---
def Number_Distributor_05_S1C15():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][2][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][1][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][0][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][3][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S1C16 ------------
    #--- C B D A ---
def Number_Distributor_05_S1C16():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][2][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][1][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][3][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][0][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor _05_S1C17 ------------
    #--- C D A B ---
def Number_Distributor_05_S1C17():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][2][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][3][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][0][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][1][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor _05_S1C18 ------------
    #--- C D B A ---
def Number_Distributor_05_S1C18():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][2][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][3][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][1][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][0][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#******************************
#--- sequences 5 - 6 - 7- 8 ---
#---------Distributor _05_S2C13 ------------
    #--- !C !A !B !D ---
def Number_Distributor_05_S2C13():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][6][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][4][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][5][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][7][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        4
#---------Distributor _05_S2C14 ------------
    #--- !C !A !D !B ---
def Number_Distributor_05_S2C14():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][6][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][4][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][7][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][5][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S2C15 ------------
    #--- !C !B !A !D ---
def Number_Distributor_05_S2C15():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][6][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][5][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][4][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][7][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S2C16 ------------
    #--- !C !B !D !A ---
def Number_Distributor_05_S2C16():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][6][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][4][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][7][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][4][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S2C17 ------------
    #--- !C !D !A !B ---
def Number_Distributor_05_S2C17():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][6][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][7][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][4][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][5][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S2C18 ------------
    #--- !C !D !B !A ---
def Number_Distributor_05_S2C18():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][6][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][7][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][5][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][4][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#**************************
#---- last time for the first 4 sequences ---
#**************************
#---------Distributor _05_S1C19 ------------
    #--- D A B C ---
def Number_Distributor_05_S1C19():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][3][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][0][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][1][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][2][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
    
#---------Distributor _05_S1C20 ------------
    #--- D A C B ---
def Number_Distributor_05_S1C20():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][3][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][0][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][2][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][1][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
    
#---------Distributor _05_S1C21 ------------
    #--- D B A C --- ALL RESULT TO 15 ---
def Number_Distributor_05_S1C21():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][3][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][1][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][0][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][2][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S1C122 ------------
    #--- D B C A ---#---------------------------
def Number_Distributor_05_S1C22():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][3][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][1][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][2][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][0][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S1C23 ------------
    #--- D C A B ---
def Number_Distributor_05_S1C23():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][3][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][2][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][0][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][1][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S1C24 ------------
    #--- D C B A ---
def Number_Distributor_05_S1C24():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][3][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][2][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][1][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][0][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#*******************
#--- last sequences 5 - 6 - 7- 8 ---
#*********************
#---------Distributor _05_S2C19 ------------
    #--- !D !A !B !C ---
def Number_Distributor_05_S2C19():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][7][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][4][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][5][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][6][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S2C20 ------------
    #--- !D !A !C !B ---
def Number_Distributor_05_S2C20():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][7][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][4][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][6][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][5][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S2C21 ------------
    #--- !D !B !A !C ---
def Number_Distributor_05_S2C21():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][7][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][5][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][4][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][6][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S2C22 ------------
    #--- !D !B !C !A ---
def Number_Distributor_05_S2C22():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][7][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][5][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][6][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][4][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#---------Distributor _05_S2C23 ------------
    #--- !D !C !A !B ---
def Number_Distributor_05_S2C23():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][7][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][6][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][4][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][5][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
                
        
#---------Distributor _05_S2C24 ------------
    #--- !D !C !B !A ---
def Number_Distributor_05_S2C24():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][7][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][6][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][5][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][4][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#**************************
#---------Distributor_M1 ------------
# D  -  !B  -  A  -  C    
def Number_Distributor_M1():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][3][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][1][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][0][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][2][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor_M2 ------------
# !B  -  D  -  !C -  A   
def Number_Distributor_M2():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][5][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][3][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][4][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][0][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor_M3 ------------
# !D  -  B!  -  !A  -  C   
def Number_Distributor_M3():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][6][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][5][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][7][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][4][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor_M4 ------------
#  B  -  !D  -  C  -  !A  
def Number_Distributor_M4():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][1][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][6][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][2][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][7][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#*******************************
#--- variants for  1 combination ---
#---------Distributor_M1U ------------
# D  -  !B  -  !A  -  !C 
def Number_Distributor_M1U():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][3][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][5][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][4][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][7][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor_M1R ------------
# !D  -  B  -  A  -  C
def Number_Distributor_M1R():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][6][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][1][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][2][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][0][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#************************************
#--- variants for  2 combination ---
#---------Distributor_M2U ------------
# !B !D !A C
def Number_Distributor_M2U():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][5][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][6][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][7][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][2][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor_M2R ------------
# B D A !C
def Number_Distributor_M2R():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][1][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][3][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][0][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][4][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
        
#***********************************
#--- variants for  3  combination ---
#---------Distributor_M3U ------------
# !D B C A 
def Number_Distributor_M3U():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][6][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][1][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][2][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][0][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor_M3R ------------
# D !B !C !A
def Number_Distributor_M3R():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][3][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][5][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][4][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][7][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]        
#**************************************
#--- variants for  4  combination ---
#---------Distributor_M4U ------------
# B D A !C
def Number_Distributor_M4U():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][1][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][3][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][0][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][4][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]
#---------Distributor_M4R ------------
# !B !D !A C
def Number_Distributor_M4R():
    
    print(seq[4])
    k=0
    for w in sorted(row2_seq):
        #print('w',w)
        
        row2_seq[w]=seq[4][5][k]
        k=k+1
    print(row2_seq)
    for z in row2_seq:
        cells[z]=row2_seq[z]
    k=0
    for w in sorted(ch2_seq):
        #print('w',w)
        
        ch2_seq[w]=seq[4][6][k]
        k=k+1
    print(ch2_seq)
    for z in ch2_seq:
        cells[z]=ch2_seq[z]
    k=0
    for w in sorted(dh1_seq):
        #print('w',w)
       
        dh1_seq[w]=seq[4][7][k]
        k=k+1
    print(dh1_seq)
    for z in dh1_seq:
        cells[z]=dh1_seq[z]
    k=0
    for w in sorted(dh2_seq):
        #print('w',w)
       
        dh2_seq[w]=seq[4][2][k]
        k=k+1
    print(dh2_seq)
    for z in dh2_seq:
        cells[z]=dh2_seq[z]  
    
        
#**************************
#-END SEQUENCES  - 5 -
#*****************************

def Number_Distributor_06():
    
    print(seq[5])
    k=0       
#-------------------------
def Number_Distributor_07():
    
    print(seq[6])
    k=0      

#-------------------------
def Number_Distributor_08():
    
    print(seq[7])
    k=0      
#-------------------------
def Number_Distributor_09():
    
    print(seq[8])
    k=0      
#-------------------------
def Example_1():
    
    romeo.goto(0,-70)
    romeo.write("You remember? the c5 box is always central !!!", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    T_Turns_Right(romeo)
    writer.color('blue')
    writer.penup()
    writer.goto(0,-90)
    writer.write("I try to use the sequences with the central number 1", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-140)    
    T_Turns_Right(writer)
    writer.showturtle()
    writer.goto(0,-110)
    writer.write(seq[0], None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-140)
    T_Turns_Right(writer)
    print('------------------------')
    Number_Distributor_01()
    processing()
    writer_Draws_Matrix()
    writer.goto(0,-130)
    writer.color('red')
    writer.write("as you can see, it's not the solution ...", None, align="center",font=("Arial",12,"normal"))
    writer.goto(0,-140)
    T_Turns_Right(writer)
#----------------------------
def Example_2():
    
    romeo.goto(0,-70)
    romeo.write("You remember? the c5 box is always central !!!", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    T_Turns_Right(romeo)
    writer.color('blue')
    writer.penup()
    writer.goto(0,-90)
    writer.write("I try to use the sequences with the central number 2", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-140)    
    T_Turns_Right(writer)
    writer.showturtle()
    writer.goto(0,-110)
    writer.write(seq[1], None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-140)
    T_Turns_Right(writer)
    print('------------------------')
    Number_Distributor_02()
    writer.goto(0,-125)
    writer.color('red')
    writer.write("*  _       *  _       *  _   ...   _      *  _          _  *", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-130)
    writer.color('red')
    writer.write(" _____      _____    _____                                         ", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-150)    
    writer.write("there are only three possible valid sequences and not four ...", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-160)
    romeo.goto(0,-160)
    T_Turns_Right(writer)
#----------------------------
def Example_3():
    
    romeo.goto(0,-70)
    romeo.write("You remember? the c5 box is always central !!!", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    T_Turns_Right(romeo)
    writer.color('blue')
    writer.penup()
    writer.goto(0,-90)
    writer.write("I try to use the sequences with the central number 3", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-140)    
    T_Turns_Right(writer)
    writer.showturtle()
    writer.goto(0,-110)
    writer.write(seq[2], None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-140)
    T_Turns_Right(writer)
    print('------------------------')
    Number_Distributor_03()
    processing()
    writer_Draws_Matrix()
    writer.goto(0,-130)
    writer.color('red')
    writer.write("there are double numbers ...", None, align="center",font=("Arial",12,"normal"))
    writer.goto(0,-150)
    writer.write("as you can see, even this is not the solution...", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-180)
    romeo.goto(0,-180)
    T_Turns_Right(writer)
   
#----------------------------
def Example_4():
    
    romeo.goto(0,-70)
    romeo.write("You remember? the c5 box is always central !!!", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    T_Turns_Right(romeo)
    writer.color('blue')
    writer.penup()
    writer.goto(0,-90)
    writer.write("I try to use the sequences with the central number 4", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-140)    
    T_Turns_Right(writer)
    writer.showturtle()
    writer.goto(0,-110)
    writer.write(seq[3], None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-140)
    T_Turns_Right(writer)
    print('------------------------')
    Number_Distributor_04()
    writer.goto(0,-125)
    writer.color('red')
    writer.write("*  _       *  _       *  _    ... *  _      *  _          _  *", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-130)
    writer.color('red')
    writer.write(" _____                  _____                                ______", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-150)    
    writer.write("there are only three possible valid sequences and not four ...", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-160)
    romeo.goto(0,-160)
    T_Turns_Right(writer)
    
#----------------------------
def Example_5():
    
    romeo.goto(0,-70)
    romeo.write("You remember? the c5 box is always central !!!", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    T_Turns_Right(romeo)
    writer.color('blue')
    writer.penup()
    writer.goto(0,-90)
    writer.write("I try to use the sequences with the central number 5", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-140)    
    T_Turns_Right(writer)
    writer.showturtle()
    writer.goto(0,-110)
    #--- correction of sequencing function ---
    seq[4]=seq5
    #-------------
    writer.write(seq[4], None, align="center",font=("Arial",10,"normal"))
    #stop
    writer.goto(0,-140)
    T_Turns_Right(writer)
    print('------------------------')
    Number_Distributor_05()
    processing()
    writer_Draws_Matrix()
    writer.goto(0,-130)
    writer.color('red')
    writer.write("very interesting: there are no double numbers!", None, align="center",font=("Arial",12,"normal"))
    writer.goto(0,-150)
    writer.write("and there are four specular valid combinations...", None, align="center",font=("Arial",12,"normal"))
    writer.goto(0,-180)
    romeo.goto(0,-180)
    T_Turns_Right(writer)

#----------------------------
def Example_6():
    
    romeo.goto(0,-70)
    romeo.write("You remember? the c5 box is always central !!!", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    T_Turns_Right(romeo)
    writer.color('blue')
    writer.penup()
    writer.goto(0,-90)
    writer.write("I try to use the sequences with the central number 6", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-140)    
    T_Turns_Right(writer)
    writer.showturtle()
    writer.goto(0,-110)
    writer.write(seq[5], None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-140)
    T_Turns_Right(writer)
    print('------------------------')
    Number_Distributor_06()
    writer.goto(0,-125)
    writer.color('red')
    writer.write("*  _       *  _       *  _    ... *  _      *  _          _  *", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-130)
    writer.color('red')
    writer.write(" _____                  _____       ____                           ", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-150)    
    writer.write("there are only three possible valid sequences and not four ...", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-160)
    romeo.goto(0,-160)
    T_Turns_Right(writer)
#----------------------------
def Example_7():
    
    romeo.goto(0,-70)
    romeo.write("You remember? the c5 box is always central !!!", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    T_Turns_Right(romeo)
    writer.color('blue')
    writer.penup()
    writer.goto(0,-90)
    writer.write("I try to use the sequences with the central number 7", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-140)    
    T_Turns_Right(writer)
    writer.showturtle()
    writer.goto(0,-110)
    writer.write(seq[6], None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-140)
    T_Turns_Right(writer)
    print('------------------------')
    Number_Distributor_07()
    writer.goto(0,-125)
    writer.color('red')
    writer.write("  *  _       *  _    ... *  _      *  _    ", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-130)
    writer.color('red')
    writer.write("   _____                   _____               ", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-150)    
    writer.write("there are only three possible valid sequences and not four ...", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-160)
    romeo.goto(0,-160)
    T_Turns_Right(writer)
#----------------------------
def Example_8():
    
    romeo.goto(0,-70)
    romeo.write("You remember? the c5 box is always central !!!", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    T_Turns_Right(romeo)
    writer.color('blue')
    writer.penup()
    writer.goto(0,-90)
    writer.write("I try to use the sequences with the central number 8", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-140)    
    T_Turns_Right(writer)
    writer.showturtle()
    writer.goto(0,-110)
    writer.write(seq[7], None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-140)
    T_Turns_Right(writer)
    print('------------------------')
    Number_Distributor_08()
    writer.goto(0,-125)
    writer.color('red')
    writer.write("*  _       *  _       *  _    ...   _  *      _  *        _  *", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-130)
    writer.color('red')
    writer.write(" _____      _____    _____                                         ", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-150)    
    writer.write("there are only three possible valid sequences and not four ...", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-160)
    romeo.goto(0,-160)
    T_Turns_Right(writer)
    
#----------------------------
def Example_9():
    
    romeo.goto(0,-70)
    romeo.write("You remember? the c5 box is always central !!!", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    T_Turns_Right(romeo)
    writer.color('blue')
    writer.penup()
    writer.goto(0,-90)
    writer.write("I try to use the sequences with the central number 9", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-140)    
    T_Turns_Right(writer)
    writer.showturtle()
    writer.goto(0,-110)
    writer.write(seq[8], None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-140)
    T_Turns_Right(writer)
    print('------------------------')
    Number_Distributor_09()
    writer.goto(0,-125)
    writer.color('red')
    writer.write("  *  _       *  _    ... *  _      *  _    ", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-130)
    writer.color('red')
    writer.write("   _____     _____                             ", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-150)    
    writer.write("there are only two possible valid sequences and not four ...", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-160)
    romeo.goto(0,-160)
    T_Turns_Right(writer)
    
#----------------------------
def Base_Solutions():

    writer.goto(0,-100)
    writer.color('blue')
    writer.write("as we have experimented, only the sequences of the number 5 are valid!", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-85)
    writer.write(seq[4], None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,10)
    writer.write("5", None, align="center",font=("Arial",12,"normal"))
    writer.goto(0,-115)
    writer.write("they are four specular sequences without double numbers...", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-135)    
    writer.write("do you remember the commutative / permutative property of the sum?", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-150)    
    writer.write("we apply this property to the geometric arrangement of the sequences...", None, align="center",font=("Arial",10,"normal"))
    writer.goto(0,-170)    
    writer.write("let's see together how we can combine the sequences ...", None, align="center",font=("Arial",12,"normal"))
    writer.goto(0,-180)
    romeo.goto(0,-180)
    T_Turns_Right(writer)

#----------------------------
#---------------------------       
def T_Writes_Info_Seq(turtle_name, temp_seq):
    t = turtle_name
    t.color('blue')
    t.penup()
    t.goto(0,60)
    t.showturtle()
    t.write('Homogeneous sequences by central number', None, align="center",font=("Arial",12,"normal"))
    #T_Turns_Left(romeo)
    t.goto(0,0)
    t.write(temp_seq, None, align="center",font=("Arial",12,"normal"))
    t.hideturtle()
    t.goto(0,-140)
    T_Turns_Right(romeo)
    t.clear()
#---------------------
#---- questions-------
#---------------------
def Writer_Writes_Explanations():
    writer.penup()
    writer.color ("red")
    writer.goto(0,-60)
    for i in range (45):
        romeo.left(i)
    writer.right(90)
    # Writer explains the games
    writer.goto (-150,-70)
    writer.right(90)
    writer.write("In this game you must find the combination of the positioning")
    writer.goto(-150,-80)
    writer.write("of the numbers from 1 to 9")
    writer.goto(-150,-90)
    writer.write("in order to obtain the their sum for each row")
    writer.goto(-150,-100)
    writer.write("for each column and for the diagonals always")
    writer.goto(-150,-110)
    writer.write("results 15")
    writer.goto (0,-120)
    writer.left(90)
    
#--------------------------   
def Writer_Writes_Numbers():
    writer.goto(-65,80)
    for i in range (4):
        writer.write("15")
        writer.goto((-30+(i*30)),80)   
    for i in range (4):
        writer.write("15")
        writer.goto(60,(50-i*30))
       
    for i in range (4):
        writer.write("15")
        writer.goto((25-i*30),-40)
        
    for i in range (4):
        writer.write("15")
        writer.goto(-65,(-10+i*30))
    writer.goto(0,-160)
    romeo.goto(0,-140)
#--------------------------
def clicca():
    global answer
    while (answer == ''):
        Y.onclick(turn_Y)
        #print ('risposta', answer)
        N.onclick(turn_N)
        time.sleep(1)
        #print('???????')
#------------------------
def Cell_selection():
    while (answer == ''):
        Tc_end.onclick(turn_Tc_E)
        #--------------
        Tc1.onclick(turn_Tc1)
        Tc2.onclick(turn_Tc2)
        Tc3.onclick(turn_Tc3)
        Tc4.onclick(turn_Tc4)
        Tc5.onclick(turn_Tc5)
        Tc6.onclick(turn_Tc6)
        Tc7.onclick(turn_Tc7)
        Tc8.onclick(turn_Tc8)
        Tc9.onclick(turn_Tc9)
#----------------------------
def Number_selection():
    while (answer == None):
        Tn1.onclick(turn_Tn1)
        Tn2.onclick(turn_Tn2)
        Tn3.onclick(turn_Tn3)
        Tn4.onclick(turn_Tn4)
        Tn5.onclick(turn_Tn5)
        Tn6.onclick(turn_Tn6)
        Tn7.onclick(turn_Tn7)
        Tn8.onclick(turn_Tn8)
        Tn9.onclick(turn_Tn9)




def turn_Y(x, y):
    global answer
    Y.shape('square')
    Y.clear()
    Y.left(180)
    #time.sleep(3)
    #writer.clear()
    answer = 'Y'
    #print ('answer   ', answer)
    click_ok = True
    time.sleep(1)
    Y.hideturtle()
    N.hideturtle()
#----------------
def turn_N(x, y):
    global answer
    N.shape('square')
    N.clear()
    N.left(180)
    time.sleep(3)
    writer.clear()
    answer = 'N'
    #print ('answer   ', answer)
    N.hideturtle()
    Y.hideturtle()
#----------------  
def turn_Tc_E(x, y):
    global answer
    print('select end game')
    Tc_end.shape('square')
    Tc_end.clear()
    Tc_end.left(180)
    #time.sleep()
    #writer.clear()
    answer = 'E'
    #print ('answer   ', answer)
    Tc_end.hideturtle()
    
#--------------------
def turn_Tc1(x, y):
    global answer
    print('select c1')
    Tc1.left(180)
    answer = 'c1'
    
    #-----------
def turn_Tc2(x, y):
    global answer
    print('select c2')
    Tc2.left(180)
    answer = 'c2'
    
    #-----------
def turn_Tc3(x, y):
    global answer
    print('select c3')
    Tc3.left(180)
    answer = 'c3'
    #-----------
def turn_Tc4(x, y):
    global answer
    print('select c4')
    Tc4.left(180)
    answer = 'c4'
    #-----------
def turn_Tc5(x, y):
    global answer
    print('select c5')
    Tc5.left(180)
    answer = 'c5'
    #-----------
def turn_Tc6(x, y):
    global answer
    print('select c6')
    Tc6.left(180)
    answer = 'c6'
    #-----------
def turn_Tc7(x, y):
    global answer
    print('select c7')
    Tc7.left(180)
    answer = 'c7'
    #-----------
def turn_Tc8(x, y):
    global answer
    print('select c8')
    Tc8.left(180)
    answer = 'c8'
    #-----------
def turn_Tc9(x, y):
    global answer
    print('select c9')
    Tc9.left(180)
    answer = 'c9'
    #-----------
#*******************
def turn_Tn1(x, y):
    global answer
    print('select number 1')
    Tn1.left(180)
    answer = 1
    #-----------
def turn_Tn2(x, y):
    global answer
    print('select number 2')
    Tn2.left(180)
    answer = 2
    #-----------
def turn_Tn3(x, y):
    global answer
    print('select number 3')
    Tn3.left(180)
    answer = 3
    #-----------
def turn_Tn4(x, y):
    global answer
    print('select number 3')
    Tn3.left(180)
    answer = 4
    #-----------
def turn_Tn5(x, y):
    global answer
    print('select number 3')
    Tn3.left(180)
    answer = 5
    #-----------
def turn_Tn6(x, y):
    global answer
    print('select number 3')
    Tn3.left(180)
    answer = 6
    #-----------
def turn_Tn7(x, y):
    global answer
    print('select number 3')
    Tn3.left(180)
    answer = 7
    #-----------
def turn_Tn8(x, y):
    global answer
    print('select number 3')
    Tn3.left(180)
    answer = 8
    #-----------
def turn_Tn9(x, y):
    global answer
    print('select number 3')
    Tn3.left(180)
    answer = 9
    #-----------

def Writer_Asks():   
    writer.color('green')
    writer.goto (-150,-120)
    writer.write("if you want to try to find a solution click here for     YES     or    NOT")
    writer.goto (-150,-170)
    Y.st()
    Y.color = ('blue')
    Y.goto(100,-130)
    N.color = ('red')
    N.st()
    N.goto(150,-130)
    answer = ''
    clicca() 
    print('e adesso?')
   
def Writer_control():
    global answer 
    global end_game   
    if answer == "Y":
        answer = ''
        writer.goto(-150,-130)
        writer.write("your answer is  YES! and now to play...")
        #start_player = True
        writer.color ("white")
        writer.begin_fill()
        writer.goto(-200,-70)
        writer.goto(400,-70)
        writer.goto(400,-200)
        writer.goto(-200,-200)
        writer.goto(-200,-70)
        writer.end_fill()
        writer.color ("green")
        writer.goto (0, -90)
        writer.write ("INSTRUCTIONS",  None, align="center", font = ("Arial", 12, "normal"))
        writer.goto (-160, -100)
        writer.write ("select the cell name by clicking on the corresponding cell under the names")
        writer.goto (-160, -110)
        writer.write ("the red turtle will move to the cell!")
        writer.goto (-160, -120)
        writer.write ("Now select a number by clicking on the corresponding box")
        writer.goto (-160, -130)
        writer.write ("for the cell where the is the turThe number will be written on the cell where the red turtle is located")
        writer.goto (-160, -140)
        writer.write ("repeat these entries for all cells, if you want to finish, select the red cell 'END'")
        writer.goto (-160, -150)
        writer.color ("blue")
        writer.goto (-160, -160)
        writer.write ("well, let's start the game!")
        #.......................
        Romeo_Turns_Left()
        romeo.goto (0,-170)
        romeo.color ("blue")
        romeo.showturtle()
        # time lag
        # the player plays
        # preparazione ambiente....
        romeo.home()
        romeo.goto(0,180)
        romeo.write("First choose the cell and then choose the number", None, align="center",font=("Arial",10,"bold"))
        Romeo_Fills_9Circles()
        romeo.goto(0,-160)
        T_Turns_Right(romeo)
        Romeo_Draws_Numbers()
        romeo.goto(0,-160)
        romeo.color("blue")
        T_Turns_Right(romeo)
        #Romeo_Draws_Numbers()
        #Romeo_Fills_9Cells()
        Turtle_selector()
        Romeo_Draws_9Boxes()
        Number_selector()
        

        Start_Game()
        #start questions an answers
    elif answer == "N":
        answer = ''
        writer.goto(-150,-120)
        writer.write("your answer is  NO!, So you want me to try it?   ->  YES    ->  NOT")
        Y.st()
        Y.color = ('blue')
        Y.goto(100,-130)
        N.color = ('red')
        N.st()
        N.goto(150,-130)
        answer = ''
        clicca() 
        print('e adesso?')

        #answer_1 = input("your answer is  NO!, So you want me to try it? "+"tipe 'y' or 'n' ")
        if answer == "Y":
            answer = ''
            #start_romeo = True
            writer.goto (-150,-150)
            writer.write("your answer is  YES! then i try to solve the game...")
            # romeo find a solution
            Romeo_Plays()
        elif answer == "N":
            answer = ''
            writer.goto (-150,-150)
            writer.write("your answer is  NO!, then i play alone")
            romeo.goto(0,-170)
            Romeo_Turns_Right()
            Romeo_Plays_Alone()
            
        else:
            writer.goto (-150,-150)
            writer.write("and now what do i do? I greet you, bye")
            romeo.goto (0,-190)
            writer.goto(0, -190)
            Romeo_Turns_Left()
            end_game=True
            End_Game()
    else:
        writer.goto (-150,-150)
        writer.write("and now what do i do? I greet you, bye")
        romeo.goto (0,-190)
        writer.goto(0, -190)
        Romeo_Turns_Left()
        end_game=True
        End_Game()
    # stop
#--------------------------
def First_Graphic():
        print ('CELL CONSTRUCTOR')
        print('_____________________________')
        romeo.screen.setup(width=0.75, height=0.75, startx=None, starty=None)
        Romeo_Fills_Square()
        #------------------
        T_Draws_Square(romeo,-45,70)
        #-----------------------
        Romeo_Writes_Names()
        #-----------------------
        Writer_Writes_Explanations()
        #-----------------------
        Writer_Writes_Numbers()
        #-----------------------
        T_Turns_Left(romeo)
        romeo.right(90)
        #-----------------------
        Writer_Asks()
        print ("I' m here .................")

        Writer_control()
    
#--------------------------
def ask_cell():
    global end_game
    global sel_cell
    if end_game == False:





        #sel_cell = input ("insert a name of a cell c1 ... c9     ")
        print (' your sel_cell is = ', sel_cell)
        if sel_cell == 'E':
            end_game =True
            return sel_cell
        if sel_cell in cells.keys():
            print('your sel_cell is valid', sel_cell)
            
            return sel_cell
        # controlli------          
        else:
            print ("oops... a valid name from c1 to c9")
            print('this number is wrong:')
            Start_Game()
 
            
#------------------------------------------------------------
def ask_number():
    global end_game
    global answer
    global sel_number
    sel_number = answer
    print( 'sel_number in ask', sel_number, "   ", "answer in ask", answer)
    if end_game == False:
        try:
            #sel_number = int(input ("enter a number..."))
            sel_number = anwser
            #print( 'sel_number in ask', sel_number, "   ", "answer in ask", answer)

            if 0 < sel_number < 10:
                print('this is the number chosen: ', sel_number)
                
                return sel_number
            # controlli------           
            else:
                print ("oops... a valid number from 1 to 9, but not present in list...")
                print('this number is wrong:')
                #ask_number()
        except:
            print("a valid number frome 1 a 9!")
            #ask_number()
   
#----------------------------------------
def control():
    global sel_number
    print('************ control ***************')

    for c in cells.keys():
        if c!=sel_cell:
            #print ('c=',c,)
            if cells[c] == sel_number:
                print('**** invalid number', sel_number, 'c=',c)
                print('sel_number is set to 0')
                sel_number = 0
                cells[sel_cell]=sel_number
                break
        
        cells[sel_cell] = sel_number
              
#-------------------------------------------------
def processing():
    global sequence_counter
    global r_l1,r_l2,r_l3
    global rw1, rw2, rw3
    global cl1, cl2, cl3
    global ch1, ch2, ch3
    global d_h1,d_h2,d_l1,d_l2
    global row1_l, row2_l,row3_l
    global ch1_l,ch2_l,ch3_l
    global d_h1l, d_h2l
    global row1_seq, row2_seq, row3_seq
    global ch1_seq, ch2_seq, ch3_seq
    global dh1_seq, dh2_seq
    global counter_row1, counter_row2, counter_row3
    global counter_ch1, counter_ch2, counter_ch3
    global counter_dh1, counter_dh2
    #----------------------------------------------------
    if cells['c1']>0 and cells['c2']>0 and cells['c3']>0:
        r_l1 = cells['c1'] + cells['c2'] + cells['c3']
        if r_l1 == 15:
            sequence_counter = sequence_counter+1
            counter_row1=counter_row1+1
            row1_l=True
            row1_seq= {'c1':cells['c1'], 'c2':cells['c2'], 'c3':cells['c3']}
        
    r_l1 = cells['c1'] + cells['c2'] + cells['c3']
    #----------------------------------------------------
    if cells['c4']>0 and cells['c5']>0 and cells['c6']>0:
        r_l2 = cells['c4'] + cells['c5'] + cells['c6']
        if r_l2 == 15:
            sequence_counter = sequence_counter+1
            counter_row2=counter_row1+1
            row2_l=True
            row2_seq= {'c4':cells['c4'], 'c5':cells['c5'], 'c6':cells['c6']}
            
    r_l2 = cells['c4'] + cells['c5'] + cells['c6']
    #----------------------------------------------------
    if cells['c7']>0 and cells['c8']>0 and cells['c9']>0:
        r_l3 = cells['c7'] + cells['c8'] + cells['c9']
        if r_l3 == 15:
            sequence_counter = sequence_counter+1
            counter_row3=counter_row1+1
            row3_l=True
            row3_seq= {'c7':cells['c7'], 'c8':cells['c8'], 'c9':cells['c9']}
        
    r_l3 = cells['c7'] + cells['c8'] + cells['c9']   
    #---------------------------------------------
    if cells['c1']>0 and cells['c4']>0 and cells['c7']>0:
        ch1 = cells['c1'] + cells['c4'] + cells['c7']
        if ch1 == 15:
            sequence_counter = sequence_counter+1
            counter_ch1=counter_ch1+1
            ch1_l=True
            ch1_seq= {'c1':cells['c1'], 'c4':cells['c4'], 'c7':cells['c7']}
            
        
    ch1 = cells['c1'] + cells['c4'] + cells['c7']
    #---------------------------------------------------
    if cells['c2']>0 and cells['c5']>0 and cells['c8']>0:
        ch2 = cells['c2'] + cells['c5'] + cells['c8']
        if ch2 == 15:
            sequence_counter = sequence_counter+1
            counter_ch2=counter_ch2+1
            ch2_l=True
            ch2_seq= {'c2':cells['c2'], 'c5':cells['c5'], 'c8':cells['c8']}
            
    ch2 = cells['c2'] + cells['c5'] + cells['c8']        
    #----------------------------------------------------        
    if cells['c3']>0 and cells['c6']>0 and cells['c9']>0:
        ch3 = cells['c3'] + cells['c6'] + cells['c9']
        if ch3 == 15:
            sequence_counter = sequence_counter+1
            counter_ch3=counter_ch3+1
            ch3_l=True
            ch3_seq= {'c3':cells['c3'], 'c6':cells['c6'], 'c9':cells['c9']}
            
    ch3 = cells['c3'] + cells['c6'] + cells['c9']   
    #---------------------------------------------
    if cells['c1']>0 and cells['c5']>0 and cells['c9']>0:
        d_h1 = cells['c1'] + cells['c5'] + cells['c9']
        if d_h1 == 15:
            sequence_counter = sequence_counter+1
            counter_dh1=counter_dh1+1
            d_h1l=True
            dh1_seq= {'c1':cells['c1'], 'c5':cells['c5'], 'c9':cells['c9']}
            
            
    d_h1 = cells['c1'] + cells['c5'] + cells['c9']    
    #---------------------------------------------  
    if cells['c3']>0 and cells['c5']>0 and cells['c7']>0:
        d_h2 = cells['c3'] + cells['c5'] + cells['c7']
        if d_h2 == 15:
            sequence_counter = sequence_counter+1
            counter_dh2=counter_dh2+1
            d_h2l=True
            dh2_seq= {'c3':cells['c3'], 'c5':cells['c5'], 'c7':cells['c7']}
            
    d_h2 = cells['c3'] + cells['c5'] + cells['c7']    
    #---------------------------------------------
    d_l1 = d_h2
    d_l2 = d_h1
    cl1 = ch1
    cl2 = ch2
    cl3 = ch3
    rw1 = r_l1
    rw2 = r_l2
    rw3 = r_l3
    #---------------------------------------------
    print('d_h1 ', d_h1,' ch1 ',ch1, ' - ch2  ', ch2,' - ch3  ',ch3, ' - d_h2', d_h2)
    print('r_l1 ',r_l1, ' c1  ',cells['c1'],' -  c2  ',cells['c2'], ' -  c3  ',cells['c3'], ' - rw1 ', rw1)
    print('r_l2 ',r_l2, ' c4  ',cells['c4'],' -  c5  ',cells['c5'], ' -  c6  ',cells['c6'], ' - rw2 ', rw2)
    print('r_l3 ',r_l3, ' c7  ',cells['c7'],' - c 8  ',cells['c8'], ' -  c9  ',cells['c9'], ' - rw3 ', rw3)
    print('d_l1 ', d_l1,' cl1 ', cl1, '  - cl2 ', cl2,' - cl3  ', cl3, ' - d_l2', d_l2)
    
#-------------------------------------------------
def Gradient():
    global level
    if end_game == False:
         
        print ('==========================================')
        print ('check results')
        
        if r_l1 == 15 and row1_l:
            print ('row one is correct')
            level=level+0.125
        else:
            print ('row one is NOT correct')
        if r_l2 == 15 and row2_l:
            print ('row two is correct')
            level=level+0.125
        else:
            print ('row two is NOT correct')
        if r_l3 == 15 and row3_l:
            print ('row three is correct')
            level=level+0.125
        else:
            print ('row three is NOT correct')
        #-------------------------------------
        if ch1 == 15 and ch1_l:
            print ('column one is correct')
            level=level+0.125
        else:
            print ('column one is NOT correct')
        if ch2 == 15 and ch2_l:
            print ('colum two is correct')
            level=level+0.125
        else:
            print ('column two is NOT correct')
        if ch3 == 15 and ch3_l:
            print ('column three is correct')
            level=level+0.125
        else:
            print ('column three is NOT correct')
        if d_h1 == 15 and d_h1l:
            print ('first diegonal is correct')
            level=level+0.125
        else:
            print ('first diegonal is NOT correct')           
        if d_h2 == 15 and d_h2l:
            print ('second diagonal is correct')
            level=level+0.125
        else:
            print ('second diagonal is NOT correct')            
        #-------------------------------------
        if level == 1:
            print ('I SOLVED THE MATRIX...')
            Final_considerations()
        else:
            level = level*100
            print ('Gradiend is', level, ' %')
            Final_considerations()
        
#---------------------------------------------
def check_sequence():
    global level
    global matrix_temp
    global row1_m, row2_m, row3_m
    global ch1_m, ch2_m, ch3_m
    global dh1_m, dh2_m
    if level > 0:
        #--------------------------
        if row1_l == True and row1_m == False:
            for c in row1_seq:
                matrix_temp[c]=row1_seq[c]
            Romeo_Fills_Row1()
            row1_m = True
        if row2_l == True and row2_m == False:
            for c in row2_seq:
                matrix_temp[c]=row2_seq[c]
            Romeo_Fills_Row2()
            row2_m = True
        if row3_l == True and row3_m == False:
            for c in row3_seq:
                matrix_temp[c]=row3_seq[c]
            Romeo_Fills_Row3()
            row3_m = True
        #--------------------------
        if ch1_l == True and ch1_m == False:
            for c in ch1_seq:
                matrix_temp[c]=ch1_seq[c]
            Romeo_Fills_Ch1()
            ch1_m = True
        if ch2_l == True and ch2_m == False:
            for c in ch2_seq:
                matrix_temp[c]=ch2_seq[c]
            Romeo_Fills_Ch2()
            ch2_m = True
        if ch3_l == True and ch3_m == False:
            for c in ch3_seq:
                matrix_temp[c]=ch3_seq[c]
            Romeo_Fills_Ch3()
            ch3_m = True
        #-------------------------
        if d_h1l == True and dh1_m == False:
            for c in dh1_seq:
                matrix_temp[c]=dh1_seq[c]
            Romeo_Fills_Dh1()
            dh1_m = True
        if d_h2l == True and dh2_m == False:
            for c in dh2_seq:
                matrix_temp[c]=dh2_seq[c]
            Romeo_Fills_Dh2()
            dh2_m = True
    print ('Mem_matrix= ', Mem_matrix)

#---------------------------------------------
def Numbers_remover():
    print('Numbers = ',Numbers)
    print('Mem_numbers = ',Mem_numbers)
    print('-------')
    for x in Mem_numbers:
        #print('Numbers = ',Numbers)
        for n in Numbers:
            print('x=',x,'n= ',n)
            print('Numbers = ',Numbers)
            if x == n:
                print('remove', 'x= ',x,'n= ',n)
                Numbers.remove(x)
                print('Numbers = ',Numbers)
 
    print('*******************')
    print(Numbers)
    print(Mem_numbers)
    print('***********')
    
#---------------------------
def Boxes_remover():
    global Boxes
    print('Boxes= ', Boxes)
    print('Mem_matrix= ',Mem_matrix)
    print('-------')
    for c in Mem_matrix:
        print('c=',c)
        for b in Boxes:
            if b == c:
                print('Remove', 'b= ',b, 'c= ',c)
                Boxes.remove(b)
    #--------------------------------
    print('Boxes= ',Boxes)
    print('Mem_matrix= ',Mem_matrix)
    print('***********')   

#-------------------------------------------------
def writer_Draws_Matrix():
    writer.color('green')
    for c in cells:
        writer.goto(Cell_Pos[c])
        writer.write(cells[c],  None, align="center",font=("Arial",12,"normal"))
        #print (c, cells[c])
        #------------------
    writer.goto(-65,80)
    writer.write(d_h1)
    writer.goto(-30,80)
    writer.write(ch1)
    writer.goto(0,80)
    writer.write(ch2)
    writer.goto(30,80)
    writer.write(ch3)
    writer.goto(65,80)
    writer.write(d_h2)
    #-----------------
    writer.goto(-65,50)
    writer.write(r_l1)
    writer.goto(65,50)
    writer.write(rw1)
    #----------------
    writer.goto(-65,20)
    writer.write(r_l2)
    writer.goto(65,20)
    writer.write(rw2)
    #------------------
    writer.goto(-65,-10)
    writer.write(r_l3)
    writer.goto(65,-10)
    writer.write(rw3)
    #------------------
    writer.goto(-65,-40)
    writer.write(d_l1)
    writer.goto(-30,-40)
    writer.write(cl1)
    writer.goto(0,-40)
    writer.write(cl2)
    writer.goto(30,-40)
    writer.write(cl3)
    writer.goto(65,-40)
    writer.write(d_l2)
        
#-------------------------------------------------
def Draw_Matrix():
    if end_game == False:
        player.clear()
        player.write(sel_number,  None, align="center",font=("Arial",12,"normal"))
        writer.clear()
        writer_Draws_Matrix()
#--------------------------
def Romeo_Plays_Alone():
    global end_game
    romeo.clear()
    writer.clear()
    bea.clear()
    #--------------------
    T_Fills_Square(romeo,-45,115,45,25) 
    romeo.left(90)
    T_Draws_Square(romeo, -45, 115)
    #------------------
    romeo.color("orange")
    romeo.goto(-30,90)
    romeo.write("C1",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(-0,90)
    romeo.write("C2",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(30,90)
    romeo.write("C3",None, align="center",font=("Arial",12,"normal"))
    #------------------
    romeo.color("magenta")
    romeo.goto(-30,60)
    romeo.write("C4",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(-0,60)
    romeo.write("C5",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(30,60)
    romeo.write("C6",None, align="center",font=("Arial",12,"normal"))
    #------------------
    romeo.color("green")
    romeo.goto(-30,30)
    romeo.write("C7",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(-0,30)
    romeo.write("C8",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(30,30)
    romeo.write("C9",None, align="center",font=("Arial",12,"normal"))
##    Number_Distributor_M1()
##    # D  -  B -  A -  C
##    processing()
##    T_Writes_Combination(bea,-45, 115)
    romeo.goto(0,-130)
    romeo.goto(0,-30)
    romeo.write("Thank you for playing with the Romeo turtle",None, align="center",font=("Arial",12,"normal"))
    romeo.goto(0,-50)
    romeo.speed("slowest")
    Romeo_Turns_Left()
    #romeo.clear()
    #bea.clear()
    end_game=True
    End_Game()
    
        
#--------------------------
def Romeo_Plays():
    global end_game
    romeo.color("blue")
    #romeo.showturtle()
    print('now I try...')
    # time lag
    romeo.goto(0,170)
    T_Turns_Right(romeo)
    #-----------
    romeo.goto(0,140)
    romeo.write("first of all I analyze the geometry", None, align="center",font=("Arial",10,"normal"))
    #------------------
    romeo.right(90)
    writer.clear()
    Romeo_Draws_R01()
    romeo.write("This is the original arrangement of the cells, but ...", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-160)
    romeo.write("if I turn my attention to the right...", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-170)
    # time lag
    T_Turns_Right(romeo)
    romeo.clear()
    romeo.color("pink")
    Romeo_Fills_Square()
    romeo.color("blue")
    Romeo_Draws_R02()
    romeo.write("this will be the result...", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-160)
    romeo.write("I can still keep turning my attention to the right...", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-170)
    # time lag
    T_Turns_Right(romeo)
    #-------------------
    romeo.clear()
    romeo.color("orange")
    Romeo_Fills_Square()
    romeo.color("blue")
    Romeo_Draws_R03()
    #---------------
    romeo.write("this will be the result...", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-130)
    romeo.write("I can continue to turn my attention to the right once again...", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    # time lag
    T_Turns_Right(romeo)
    #-------------------
    romeo.clear()
    romeo.color("purple")
    Romeo_Fills_Square()
    romeo.color("blue")
    Romeo_Draws_R04()
    romeo.write("end now ... this is the result...", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    romeo.write("...there are many points of view right?", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-150)
    romeo.write("...if one is left-handed he turns his attention to the left and then ...", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-170)
    T_Turns_Right(romeo)
    romeo.goto (0,150)
    # Turn to the left
    T_Turns_Left(romeo)
    romeo.clear()
    romeo.color("green")
    Romeo_Fills_Square()
    romeo.color("blue")
    Romeo_Draws_L01()
    romeo.write("this will be the first result...", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-130)
    romeo.write("I can continue to turn my attention to the left...", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    T_Turns_Left(romeo)
    romeo.clear()
    romeo.color("violet")
    Romeo_Fills_Square()
    romeo.color("blue")
    Romeo_Draws_L02()
    romeo.write("this will be the second result...", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-130)
    romeo.write("I can continue to turn my attention to the left...", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-160)
    #-----------------
    T_Turns_Left(romeo)
    romeo.clear()
    romeo.color("brown")
    Romeo_Fills_Square()
    romeo.color("blue")
    Romeo_Draws_L03()
    romeo.write("this will be the third result...", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-130)
    romeo.write("I can continue to turn my attention to the left for the last time...", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    #-----------------
    T_Turns_Left(romeo)
    romeo.clear()
    romeo.color("grey")
    Romeo_Fills_Square()
    romeo.color("blue")
    Romeo_Draws_L04()
    romeo.write("I saw that there are many ways to arrange the boxes !!!", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    T_Turns_Left(romeo)
    romeo.clear()
    romeo.goto(0,-100)
    romeo.write("there is also vertical symmetry !!!", None, align="center",font=("Arial",10,"normal"))
    #--- vertical reflection ---
    Show_Vertical_Reflection()
    romeo.goto(0,-140)
    T_Turns_Left(romeo)
    romeo.clear()
    romeo.goto(0,-100)
    romeo.write("and also horizontal symmetry!!!", None, align="center",font=("Arial",10,"normal"))
    #--- horizontal reflection ---
    Show_Horizontal_Reflection()
    romeo.goto(0,-140)
    T_Turns_Left(romeo)
    romeo.clear()
    #..............................
    romeo.goto(0,-120)
    romeo.write("but the c5 box is always central !!!", None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-140)
    T_Turns_Left(romeo)
    romeo.color("lightgreen")
    Romeo_Fills_Square()
    romeo.right(90)
    #-----------------
    romeo.color("red")
    Romeo_Fills_C5()
    romeo.penup()
    romeo.goto(0,15)
    romeo.color("white")
    romeo.write('c5', None, align="center",font=("Arial",10,"normal"))
    romeo.goto(0,-150)
    romeo.color("blue")
    romeo.write("this is very very interesting !!!", None, align="center",font=("Arial",10,"bold"))
    romeo.goto(0,-160)
    T_Turns_Left(romeo)
    romeo.clear()
    romeo.goto(0,180)
    romeo.write("Now let's analyze the mathematical peculiarity of the sum.", None, align="center",font=("Arial",10,"bold"))
    Romeo_Draws_Boxes_01()
    Romeo_Writes_Var_01()
    romeo.color("blue")
    romeo.goto(0,90)
    romeo.write("Commutative property of the sum of real numbers", None, align="center",font=("Arial",10,"bold"))
    romeo.goto(0,-140)
    T_Turns_Left(romeo)
    #--------------------
    romeo.right(180)
    Romeo_Draws_Boxes_02()
    Romeo_Writes_Var_02()
    romeo.color("blue")
    T_Turns_Left(romeo)
    #------------------
    romeo.right(180)
    Romeo_Draws_Boxes_03()
    Romeo_Writes_Var_03()
    romeo.color("blue")
    T_Turns_Left(romeo)
    #------------------
    romeo.right(180)
    Romeo_Draws_Boxes_04()
    Romeo_Writes_Var_04()
    romeo.color("blue")
    T_Turns_Left(romeo)
    #------------------
    romeo.right(180)
    Romeo_Draws_Boxes_05()
    Romeo_Writes_Var_05()
    romeo.color("blue")
    T_Turns_Left(romeo)
    #------------------
    romeo.right(180)
    Romeo_Draws_Boxes_06()
    Romeo_Writes_Var_06()
    romeo.color("blue")
    T_Turns_Left(romeo)
    romeo.write(" well, there are many possibilities: n! (Factorial)", None, align="center",font=("Arial",10,"bold"))
    romeo.goto(0,-180)
    T_Turns_Right(romeo)
    romeo.clear()
    romeo.goto(0,180)
    romeo.write(" therefore, there are 9 numbers, which can only be used once", None, align="center",font=("Arial",10,"bold"))
    romeo.goto (0,160)
    #-------------------
    Romeo_Fills_9Circles()
    romeo.goto(0,-160)
    T_Turns_Right(romeo)
    Romeo_Draws_Numbers()
    romeo.goto(0,-160)
    romeo.color("blue")
    T_Turns_Right(romeo)
    romeo.color("grey")
    Romeo_Fills_Square()
    romeo.color("blue")
    T_Draws_Square(romeo,-45,70)
    bea.goto(0,-100)
    bea.color("red")
    bea.write(" I will limit the attempts to 150 ...", None, align="center",font=("Arial",10,"bold"))
    bea.goto(0,-160)
    T_Turns_Right(bea)
    bea.clear()
    romeo.color("blue")
   #------------------------
    #----randomizer---
    Randomizer()
    #-----------------------
    writer_Draws_Matrix()
    #------------------
    end_game=True
    End_Game()
#---------------------------------------------
def Final_considerations():
    if level == 1:
        # matrix is solved
        romeo.goto (0,-80)
        romeo.color('blue')
        romeo.write('I solved the matrix...',  None, align="center",font=("Arial",10,"bold"))
        romeo.goto (0,-100)
        romeo.write('but I was very lucky...',  None, align="center",font=("Arial",10,"bold"))
        romeo.goto (0,-120)
        romeo.write('it does not happen very often...',  None, align="center",font=("Arial",10,"bold"))
        romeo.goto(0,-170)
        romeo.hideturtle()
        end_game=True
        End_Game()
    else:
        #matrix is not solved
        #if (len(Boxes)==0 or counter==limit) and level>1:
        if ((len(Boxes)==2 and cells['c5']!=5) or counter==limit):
            #stop
            romeo.goto (0,-130)
            romeo.color('blue')
            romeo.write("I'm sorry but I was not lucky...",  None, align="center",font=("Arial",10,"bold"))
            romeo.goto (0,-140)
            romeo.write('but this is not an intelligent system...',  None, align="center",font=("Arial",10,"bold"))
            romeo.goto (0,-150)
            romeo.write('I try to solve with a better system...',  None, align="center",font=("Arial",10,"bold"))
            romeo.goto(0,-160)
            T_Turns_Right(romeo)
            romeo.clear()
            writer.clear()
            #--------------------------
            Permutation_System()
            end_game=True
            End_Game()
#---------------------------------------------
def game_over():
    global level
    if end_game == True:
        player.hideturtle() 
        print ('==========================================================================')
        print ('check results')
        try:
            if r_l1 == 15 and row1_l:
                print ('row one is correct')
                level=level+0.125
            else:
                print ('row one is NOT correct')
            if r_l2 == 15 and row2_l:
                print ('row two is correct')
                level=level+0.125
            else:
                print ('row two is NOT correct')
            if r_l3 == 15 and row3_l:
                print ('row three is correct')
                level=level+0.125
            else:
                print ('row three is NOT correct')
            #-------------------------------------
            if ch1 == 15 and ch1_l:
                print ('column one is correct')
                level=level+0.125
            else:
                print ('column one is NOT correct')
            if ch2 == 15 and ch2_l:
                print ('colum two is correct')
                level=level+0.125
            else:
                print ('column two is NOT correct')
            if ch3 == 15 and ch3_l:
                print ('column three is correct')
                level=level+0.125
            else:
                print ('column three is NOT correct')
            if d_h1 == 15 and d_h1l:
                print ('first diegonal is correct')
                level=level+0.125
            else:
                print ('first diegonal is NOT correct')           
            if d_h2 == 15 and d_h2l:
                print ('second diagonal is correct')
                level=level+0.125
            else:
                print ('second diagonal is NOT correct')            
            #------------------------------------
            if level == 1:
                print ('YOU AS SOLVED THE MATRIX...')
                writer.goto(0,-80)
                writer.write('YOU AS SOLVED THE MATRIX...',  None, align="center",font=("Arial",10,"bold"))
                Writer.goto(0,-100)
                writer.write('... CONGRATULATIONS...',  None, align="center",font=("Arial",10,"bold"))
                writer.goto(0,-130)
                T_Turns_Right(writer)
            else:
                level= level*100
                print ('YOUR LEVEL IS ', level, ' %')
                writer.goto(0,-100)
                writer.write('YOUR LEVEL IS ',  None, align="center",font=("Arial",10,"bold"))
                writer.goto(70,-100)
                writer.write(level,  None, align="center",font=("Arial",10,"bold"))
                writer.goto(0,-130)
                writer.write('try again...',  None, align="center",font=("Arial",10,"bold"))
                writer.goto(0,-150)
                T_Turns_Right(writer)
        except NameError:
            End_Game()
            
#--------------------------------------------------
def End_Game():
    if end_game == True:      
        print ('BYE BYE')
        #writer.clear()
        player.clear()
        writer.goto (0,-170)
    writer.write('END GAME... BYE BYE')

#--------- start game from player -----------------------------
def Start_Game():
    global end_game
    global answer
    global sel_cell
    global sel_number

    while end_game == False:
        player.color ("red")
        player.penup()
        player.goto(0,-150)
        player.showturtle()
        player.left(90)
        #-----------------
        
        print('Tc_end >',Tc_end.pos())
        Cell_selection()
        sel_cell = answer
        ask_cell()
        #---------------
        if sel_cell == 'E':
            answer = ''
            end_game = True
            game_over()
        #---------------
        else:
            print('this is sel_cell: ', sel_cell)
            #----  turtle  graphics-----------
            player.goto(Cell_Pos[sel_cell])
            answer = None
            #-------------------------------------
            Number_selection()
            print( 'il numero selezionato è', answer)

            #sel_number = answer
            #print ('sel_number', sel_number)
            #print('sel_cell=', sel_cell, "   ", 'sel_number=', sel_number)


            ask_number()
            print('sel_cell=', sel_cell, "   ", 'sel_number=', sel_number)
            # assegnazione in di cells
            control()
            #cells[sel_cell] = sel_number
            print ('cells=', cells)
            #---------------------
            processing()
        #--- turtle graphics----
            Draw_Matrix()
            answer = ''
            sel_cell = ''
            sel_number = None
    #---------------------------------
    # --- Your Level ---
            
            
    End_Game()
#------------------------------------------------------------
if __name__=='__main__':
    """ Main void.

    Is the main void executed when started. It does:
    - request for inputation number of sequences
    - calculation of the result starting from 1 up to the number of sequences
    - print data table S, O, P, D

    """
    First_Graphic()
    End_Game()