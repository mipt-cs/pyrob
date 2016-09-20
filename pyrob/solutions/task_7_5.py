#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():

    d = 0
    _d = 0

    move_right()

    while not wall_is_on_the_right():
        if _d == 0:
            fill_cell()
            d += 1
            _d = d
        move_right()
        _d -= 1


if __name__ == '__main__':
    run_tasks()
