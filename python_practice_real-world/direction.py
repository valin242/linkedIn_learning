import time
import os
from termcolor import colored
import math
'''
Challenge:

Write a function that draws a square

Pass in the size of the square


def drawSquare(size)
'''
class Canvas:
    def __init__(self, width, height) -> None:
        self._x = width
        self._y = height

        # This is a grid that contains data about where teh TerminalScribe have visited
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    # what to do when out of bounds (less than 0, greater than or equal to the inputed boundaries)
    def hitsWall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    # method to draw on the cells on a canvas
    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark # updates the elements at pos (x,y) and sets it to the mark/character that is passed in 

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    # print the current state of the canvas
    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas])) # print that row


class TerminalScribe:
    def __init__(self,canvas) -> None:
        self.canvas = canvas 
        self.trail = '.' # trail that drags behind to create that line
        self.mark = '*' # character printed to the canvas at the scribes current location
        self.framerate = 0.2
        self.pos = [0,0] # default position at top left corner

        self.direction = [0,1]

    def setDegrees(self, degrees):
        radians = (degrees/180) * math.pi
        self.direction = [math.sin(radians), -math.cos(radians)]