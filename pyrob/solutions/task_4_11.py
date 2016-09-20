#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():

    move_right()
    move_down()

    for i in range(1, 14):
        for j in range(i):
            fill_cell()
            move_right()
        for j in range(i):
            move_left()

        move_down()


if __name__ == '__main__':
    run_tasks()
