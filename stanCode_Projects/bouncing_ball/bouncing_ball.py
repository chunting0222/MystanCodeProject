"""
File: bouncing_ball.py
Name: Kevin Tan
-------------------------
TODO:
Make a program to simulate how a ball drop in real word.
With control of mouseclick, start with a click, and after first one,
second goes with another click, and total is three times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
TIMES_LIMIT = 3  # 玩幾次的限制
vy = 0
can_drop = True
count = 0

# Put a ball in the initial position.
window = GWindow(800, 500, title='bouncing_ball.py')
ball0 = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball0.filled = True
ball0.fill_color = 'greenyellow'
ball0.color = 'black'
window.add(ball0)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(move_ball)


def move_ball(mouse):
    global can_drop, count
    if mouse.x <= window.width and mouse.y <= window.height and count < TIMES_LIMIT:
        can_drop = True
        drop_the_ball(ball0)


def drop_the_ball(ball):
    global can_drop, vy, count
    while True:
        if can_drop:
            vy += GRAVITY
            ball.move(VX, vy)
            if ball.y >= window.height:
                vy = -vy * REDUCE
                print(vy)
                if ball.x - ball.width > window.width:
                    can_drop = False
                    ball.x = START_X
                    ball.y = START_Y
                    # ball.filled = True
                    # ball.fill_color = 'greenyellow'
                    # ball.color = 'black'
                    # window.add(ball)
                    vy = 0
                    count += 1
                    print(count)
                    break
            pause(DELAY)


if __name__ == "__main__":
    main()
