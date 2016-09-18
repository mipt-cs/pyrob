#!/usr/bin/python3

from tkinter import Tk, Canvas
import math
import time

WIDTH = 800
HEIGHT = 800


def init():

    global tk
    tk = Tk()

    global canvas
    canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg='white')
    canvas.pack()


def render_maze():
    import pyrob.core as rob

    canvas.delete('all')

    m, n = rob.get_field_size()

    global cell_size
    cell_size = min((WIDTH-20) // n, (HEIGHT-20) // m)
    wall_thickness = math.floor(cell_size * 0.1/2)
    grid_thickness = math.ceil(wall_thickness / 5)

    global start_x, start_y
    start_x = (WIDTH - cell_size*n) // 2
    start_y = (HEIGHT - cell_size * m) // 2

    global robot_offset
    robot_radius = math.floor((cell_size - 2*wall_thickness)*0.9/2)
    robot_offset = (cell_size - 2*robot_radius) // 2

    lines = []
    for i in range(m):
        for j in range(n):
            x = start_x + j*cell_size
            y = start_y + i*cell_size

            wt = wall_thickness if rob.is_blocked(i, j, rob.WALL_LEFT) else grid_thickness
            ws = (x, y)
            we = (x + wt - 1, y + cell_size - 1)
            lines.append((ws, we))

            wt = wall_thickness if rob.is_blocked(i, j, rob.WALL_TOP) else grid_thickness
            ws = (x, y)
            we = (x + cell_size - 1, y + wt - 1)
            lines.append((ws, we))

            wt = wall_thickness if rob.is_blocked(i, j, rob.WALL_RIGHT) else grid_thickness
            ws = (x + cell_size - wt, y)
            we = (x + cell_size - 1, y + cell_size - 1)
            lines.append((ws, we))

            wt = wall_thickness if rob.is_blocked(i, j, rob.WALL_BOTTOM) else grid_thickness
            ws = (x, y + cell_size - wt)
            we = (x + cell_size - 1, y + cell_size - 1)
            lines.append((ws, we))

    lines.append(((start_x - wall_thickness, start_y - wall_thickness), (start_x + n*cell_size + wall_thickness, start_y + wall_thickness)))
    lines.append(((start_x - wall_thickness, start_y + m*cell_size), (start_x + n*cell_size + wall_thickness, start_y + m*cell_size + wall_thickness)))
    lines.append(((start_x - wall_thickness, start_y - wall_thickness), (start_x, start_y + m*cell_size + wall_thickness)))
    lines.append(((start_x + n*cell_size, start_y - wall_thickness), (start_x + n*cell_size + wall_thickness, start_y + m*cell_size + wall_thickness)))

    for ws, we in lines:
        canvas.create_rectangle(*ws, *we, fill='black')

    canvas.create_oval(0, 0, 2*robot_radius, 2*robot_radius, tags='robot')


def update_robot_position(delay):

    def callback(i, j):
        global start_x, start_y, cell_size, robot_offset
        x1, y1 = tuple(map(int, canvas.coords('robot')[:2]))
        x2 = start_x + cell_size*j + robot_offset
        y2 = start_y + cell_size*i + robot_offset
        canvas.move('robot', x2-x1, y2-y1)

        tk.update_idletasks()
        tk.update()

        time.sleep(delay or 0.3)

    return callback
