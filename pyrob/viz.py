#!/usr/bin/python3

from tkinter import Tk, Canvas
import time

CELL_SIZE = 50
WALL_THICKNESS = 3
GRID_THICKNESS = 1
WALL_COLOR = 'black'

X_OFFSET = 20
Y_OFFSET = 20

ROBOT_RADIUS = (CELL_SIZE - 2*WALL_THICKNESS - 10) // 2
ROBOT_OFFSET = (CELL_SIZE - 2*ROBOT_RADIUS) // 2
ROBOT_THICKNESS = 5
ROBOT_COLOR = 'gray'


def init():

    global tk
    tk = Tk()
    tk.resizable(0, 0)


def render_maze():
    import pyrob.core as rob

    for w in tk.winfo_children():
        w.destroy()

    m, n = rob.get_field_size()

    w = CELL_SIZE*n + 2*X_OFFSET
    h = CELL_SIZE*m + 2* Y_OFFSET

    sw = tk.winfo_screenwidth()
    sh = tk.winfo_screenheight()
    x = (sw - w) // 2
    y = (sh - h) // 2

    tk.geometry('{}x{}+{}+{}'.format(w, h, x, y))

    global canvas
    canvas = Canvas(tk, width=w, height=h)
    canvas.pack()

    lines = []
    for i in range(m):
        for j in range(n):
            x = X_OFFSET + j*CELL_SIZE
            y = Y_OFFSET + i*CELL_SIZE

            if i > 9 or j > 9:
                continue

            wt = WALL_THICKNESS if rob.is_blocked(i, j, rob.WALL_LEFT) else GRID_THICKNESS
            ws = (x, y)
            we = (x + wt - 1, y + CELL_SIZE - 1)
            lines.append((ws, we))

            wt = WALL_THICKNESS if rob.is_blocked(i, j, rob.WALL_TOP) else GRID_THICKNESS
            ws = (x, y)
            we = (x + CELL_SIZE - 1, y + wt - 1)
            lines.append((ws, we))

            wt = WALL_THICKNESS if rob.is_blocked(i, j, rob.WALL_RIGHT) else GRID_THICKNESS
            ws = (x + CELL_SIZE - wt, y)
            we = (x + CELL_SIZE - 1, y + CELL_SIZE - 1)
            lines.append((ws, we))

            wt = WALL_THICKNESS if rob.is_blocked(i, j, rob.WALL_BOTTOM) else GRID_THICKNESS
            ws = (x, y + CELL_SIZE - wt)
            we = (x + CELL_SIZE - 1, y + CELL_SIZE - 1)
            lines.append((ws, we))

    lines.append(((X_OFFSET - WALL_THICKNESS, Y_OFFSET - WALL_THICKNESS), (X_OFFSET + n*CELL_SIZE + WALL_THICKNESS, Y_OFFSET + WALL_THICKNESS)))
    lines.append(((X_OFFSET - WALL_THICKNESS, Y_OFFSET + m*CELL_SIZE), (X_OFFSET + n*CELL_SIZE + WALL_THICKNESS, Y_OFFSET + m*CELL_SIZE + WALL_THICKNESS)))
    lines.append(((X_OFFSET - WALL_THICKNESS, Y_OFFSET - WALL_THICKNESS), (X_OFFSET, Y_OFFSET + m*CELL_SIZE + WALL_THICKNESS)))
    lines.append(((X_OFFSET + n*CELL_SIZE, Y_OFFSET - WALL_THICKNESS), (X_OFFSET + n*CELL_SIZE + WALL_THICKNESS, Y_OFFSET + m*CELL_SIZE + WALL_THICKNESS)))

    for ws, we in lines:
        canvas.create_rectangle(*ws, we[0]+1, we[1]+1, fill=WALL_COLOR, width=0)

    canvas.create_oval(0, 0, 2*ROBOT_RADIUS, 2*ROBOT_RADIUS, tags='robot', width=ROBOT_THICKNESS, outline=ROBOT_COLOR)


def update_robot_position(delay):

    def callback(i, j):
        x1, y1 = tuple(map(int, canvas.coords('robot')[:2]))
        x2 = X_OFFSET + CELL_SIZE*j + ROBOT_OFFSET
        y2 = Y_OFFSET + CELL_SIZE*i + ROBOT_OFFSET
        canvas.move('robot', x2-x1, y2-y1)

        tk.update_idletasks()
        tk.update()

        time.sleep(delay or 0.3)

    return callback
