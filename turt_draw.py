#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:26:28 2020

@author: Dr. Z
this is a turtle that moves around randomly with its pen up
"""

import math
import random
from turtle import * #import the library of commands that you'd like to use
colormode(255)

#Create a panel to draw on. 
panel = Screen()
panel.clear()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#Don't change this line (puts (0,0) at upper left corner)
panel.setworldcoordinates(0, w, h, 0)

#=======Add your code here======
rando = Turtle()
colormode(255)
rando.up()
rando.goto(300,300) #start in center

for frame in range(1000):
    rando.forward(random.randint(10,50))
    rando.right(random.randint(0,180))
    xpos = rando.position()[0]
    ypos = rando.position()[1]
