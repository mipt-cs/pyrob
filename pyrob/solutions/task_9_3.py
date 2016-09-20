#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():

    m = 1
    while not wall_is_on_the_right():
        m += 1
        move_right()

    while not wall_is_on_the_left():
        move_left()

    for i in range(m):
        for j in range(m):
            if i != j and i != m - 1 - j:
                fill_cell()
            if j != m-1:
                move_right()

        while not wall_is_on_the_left():
            move_left()

        if i != m-1:
            move_down()


if __name__ == '__main__':
    run_tasks()
