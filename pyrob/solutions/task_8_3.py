#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_3():

    while True:
        if wall_is_above() or wall_is_beneath():
            fill_cell()

        if wall_is_on_the_right():
            break
        else:
            move_right()


if __name__ == '__main__':
    run_tasks()
