"""
File: draw_line.py
Name: Kevin Tan
-------------------------
TODO:
Let's write a code that will help you draw a line with every two clicks.
First click: show a circle.
Second click: draw a line from the circle made by first cluck with the circle disappears.
Let's do it!
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
# Constants control the diameter of the window
WINDOW_WIDTH = 850
WINDOW_HEIGHT = 550

# Global variables
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, title='DrawALine')
SIZE = 50
x = 1000  # default, any number > WINDOW_WIDTH
y = 1000  # default, any number > WINDOW_HEIGHT
count = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_a_line)


def draw_a_line(mouse):
    global x, y, count
    count += 1
    if count % 2 == 1:
        circle = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        circle.filled = True
        circle.fill_color = 'white'
        window.add(circle)
        x = circle.x+SIZE/2
        y = circle.y+SIZE/2
    else:
        obj = window.get_object_at(x, y)
        window.remove(obj)
        line = GLine(x, y, mouse.x, mouse.y)
        line.color = 'black'
        window.add(line)


if __name__ == "__main__":
    main()
