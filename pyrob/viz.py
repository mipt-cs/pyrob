#!/usr/bin/python3

from tkinter import Tk, Canvas
import time
import pyrob.core as rob

CELL_SIZE = 40
WALL_THICKNESS = 2
GRID_THICKNESS = 1
WALL_COLOR = 'black'

X_OFFSET = 20
Y_OFFSET = 20

ROBOT_RADIUS = (CELL_SIZE - 2*WALL_THICKNESS - 10) // 2
ROBOT_OFFSET = (CELL_SIZE - 2*ROBOT_RADIUS) // 2
ROBOT_THICKNESS = 5
ROBOT_COLOR = 'gray'
ROBOT_SUCCESS_FILL_COLOR = 'green'
ROBOT_FAILURE_FILL_COLOR = 'orange'
ROBOT_CRASH_COLOR = 'red'
ROBOT_ERROR_FILL_COLOR = 'brown'

ON_TASK_COMPLETE_DELAY = 1
ON_TASK_ERRORED_DELAY = 1
ON_ROBOT_CRASHED_DELAY = 10
ON_TASK_FAILURE_DELAY = 10

CELL_COLOR_MAP = {
    rob.CELL_EMPTY: 'white',
    rob.CELL_TO_BE_FILLED: 'yellow',
    rob.CELL_FILLED: 'blue'
}

PARKING_POINT_RADIUS = ROBOT_RADIUS
PARKING_POINT_OFFSET = ROBOT_OFFSET
PARKING_POINT_COLOR = 'black'


def init():

    global tk
    tk = Tk()
    tk.resizable(0, 0)


def render_maze(task_id):

    for w in tk.winfo_children():
        w.destroy()

    m, n = rob.get_field_size()

    w = CELL_SIZE*n + 2*X_OFFSET
    h = CELL_SIZE*m + 2* Y_OFFSET

    sw = tk.winfo_screenwidth()
    sh = tk.winfo_screenheight()
    x = (sw - w) // 2
    y = (sh - h) // 2

    tk.title("pyrob :: " + task_id)
    tk.geometry('{}x{}+{}+{}'.format(w, h, x, y))

    global canvas
    canvas = Canvas(tk, width=w, height=h)
    canvas.pack()

    lines = []
    cells = []
    parking_points = []
    for i in range(m):
        for j in range(n):

            x = X_OFFSET + j*CELL_SIZE
            y = Y_OFFSET + i*CELL_SIZE

            cs = (x, y)
            ce = (x + CELL_SIZE - 1, y + CELL_SIZE - 1)
            cells.append((i, j, cs, ce))

            if rob.is_parking_cell(i, j):
                parking_points.append((x + PARKING_POINT_OFFSET, y + PARKING_POINT_OFFSET))

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

    def rect(start, end, *args, **kwargs):
        canvas.create_rectangle(*start, end[0] + 1, end[1] + 1, *args, **kwargs)

    for i, j, cs, ce in cells:
        color = CELL_COLOR_MAP[rob.get_cell_type(i, j)]
        rect(cs, ce, fill=color, width=0, tags='{}_{}'.format(i, j))

    for ws, we in lines:
        rect(ws, we, fill=WALL_COLOR, width=0)

    for (x, y) in parking_points:
        canvas.create_oval(x, y, x + 2*PARKING_POINT_RADIUS, y + 2*PARKING_POINT_RADIUS, width=0, fill=PARKING_POINT_COLOR)

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


def change_widget_fill_color(tag, color):
    canvas.itemconfigure(tag, fill=color)

    tk.update_idletasks()
    tk.update()


def on_task_errored():
    change_widget_fill_color('robot', ROBOT_ERROR_FILL_COLOR)
    time.sleep(ON_TASK_ERRORED_DELAY)


def on_task_completed(success):
    change_widget_fill_color('robot', ROBOT_SUCCESS_FILL_COLOR if success else ROBOT_FAILURE_FILL_COLOR)
    time.sleep(ON_TASK_COMPLETE_DELAY if success else ON_TASK_FAILURE_DELAY)


def on_robot_crashed():
    change_widget_fill_color('robot', ROBOT_CRASH_COLOR)
    time.sleep(ON_ROBOT_CRASHED_DELAY)


def update_cell_color(i, j, type):
    change_widget_fill_color('{}_{}'.format(i, j), CELL_COLOR_MAP[type])