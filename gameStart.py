#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:37:35 2020

@author: Dr. Z
@author: YOUR NAME

***DESCRIPTION: What does your game do? What is the goal? How do you know when you win or lose?***
"""


import random
from turtle import * #import the library of commands that you'd like to use
colormode(255)

#Create a panel to draw on. 
setup()
panel = Screen()
panel.clear()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#Don't change this line (puts (0,0) at upper left corner)
panel.setworldcoordinates(0, w, h, 0)

#========================MAKE VARIABLES=======================
panel.bgcolor('blue')



#=====================INITIAL CONDITIONS=======================
    
# Define your start variables here!
fps = 30 # framerate for animation
run = True

#=====================GAME LOOP=======================

while run:

    # Add your game activity here
    
    #if <END CONDITION>:
    #   run = False
    
    delay(fps) #set frame rate
    update() # update the image with each "frame"

panel.mainloop() # keep listeners on for mouse press
        