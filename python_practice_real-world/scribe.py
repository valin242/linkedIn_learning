import time
import os

# Printing a moving dot
# def clear():
#     os.system('cls' if os.name == 'nt' else 'clear')


# for i in range(0, 20):
#     print('\n\n\n') # makes space up top
#     print(' ' * i + '.')
#     time.sleep(0.1) # delay for 10th of a second
#     clear()

class Canvas:
    def __init__(self, width, height) -> None:
        self._x = width
        self._y = height
        self._canvas = [['' for y in range(self._y)] for x in range(self._x)]

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
        self.pos = [0,0] # default position at top left corner

        self.mark = '*' # character printed to the canvas at the scribes current location
        self.trail = '.' # trail that drags behind to create that line
    
    # moves scribes from current position to new position that gets passed in
    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail) # put the trail character in the old position
        self.pos = pos # update to the new position
        self.canvas.setPos(self.pos, self.mark) # put the mark in the updated position
        self.canvas.print()


canvas = Canvas(20, 20)
scribe = TerminalScribe(canvas)

for i in range(0, 10):
    for j in range(0, 10):
        time.sleep(0.1)
        scribe.draw((i, j))
