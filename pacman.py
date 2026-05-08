from random import choice
from turtle import (Turtle, setup, hideturtle, tracer, update, listen, onkey, ontimer, done)
from freegames import floor, vector

GHOST_SPEED = 8 
PACMAN_SPEED = 5
TILE_SIZE = 20
TIMER_MS = 100
state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(PACMAN_SPEED, 0)
pacman = vector(-40, -80)
ghosts = [
    [vector(-180, 160), vector(GHOST_SPEED, 0)],
    [vector(-180, -160), vector(0, GHOST_SPEED)],
    [vector(100, 160), vector(0, -GHOST_SPEED)],
    [vector(100, -160), vector(-GHOST_SPEED, 0)],
]
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

def valid(point):
     index = offset(point)
     if 0 <= index < len(titles):
         return titles[index] != 0
     return False

def world():


def move():

def smart_aim(ghost_pos):
      direction = [
      
          vector( GHOST_SPEED,           0),
          vector(-GHOST_SPEED,           0),
          vector(           0,  GHOST_SPEED),
          vector(           0, -GHOST_SPEED),
      ]
      best_dir = None
      best_dir = float('inf')
      for d in directions:
        next_pos = ghost_pos + d
        if valid(next_pos):
            dist = abs(next_pos.x - pacman.x) + abs(next_pos.y - pacman.y)
            if dist < best_dist:
                best_dist = dist
                best_dir  = d
 
    return best_dir
def draw():
    path.up()
    path.goto(pacman.x + 10, pacman.y + 10)
    path.dot(20, 'yellow')
    ghost_colors = ['red', 'pink', 'cyan', 'orange']
    for i, (ghost_pos, _) in enumerate(ghosts):
        path.goto(ghost_pos.x + 10, ghost_pos.y + 10)
        path.dot(20, ghost_colors[i % len(ghost_colors)])
    update()
def change(x, y):
      new_aim = vector(x, y)
      if valid(pacman + new_aim):
          aim.x = x
          aim.y = y

from turtle import bgcolor
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
world()
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change( PACMAN_SPEED,       0), 'Right')
onkey(lambda: change(-PACMAN_SPEED,            0), 'Left')
onkey(lambda: change(           0,  PACMAN_SPEED), 'Up')
onkey(lambda: change(           0, -PACMAN_SPEED), 'Down') 
move()
done()
 
