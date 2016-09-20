#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():

    while True:

        while not wall_is_on_the_left():
            move_left()

        while not wall_is_on_the_right() and wall_is_beneath():
            move_right()

        if wall_is_beneath():
            break

        move_down()

    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
