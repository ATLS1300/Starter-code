#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use
colormode(255)

#Create a panel to draw on. 
panel = Screen()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#Don't change this line (puts (0,0) at upper left corner)
panel.setworldcoordinates(0, w, h, 0)

#=======Add your code here======

window = Screen()
window.clear()
window.bgcolor("orange")

Harry = Turtle()
Harry.shape("circle")
Harry.forward(50)
Harry.backward(100) #pixels
Harry.left(90) #degrees
Harry.forward(100)
Harry.right(30)
Harry.backward(150)

Harry.goto(0,0)
Harry.goto(100,100)

Harry.up() 
Harry.goto(200,200)
Harry.down()
Harry.forward(200)

Harry.circle(50) #radius
Harry.dot(50) #diameter