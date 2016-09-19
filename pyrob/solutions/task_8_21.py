#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():

    left = wall_is_on_the_right()
    down = wall_is_above()

    for i in range(9):
        if left:
            move_left()
        else:
            move_right()

        if down:
            move_down()
        else:
            move_up()


if __name__ == '__main__':
    run_tasks()
