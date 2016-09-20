#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():

    c = 0
    while not wall_is_on_the_right():
        if cell_is_filled():
            c += 1
            if c == 3:
                break
        else:
            c = 0

        move_right()


if __name__ == '__main__':
    run_tasks()
