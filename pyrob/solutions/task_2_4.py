#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():

    for i in range(5):
        for j in range(10):
            move_right()
            fill_cell()
            move_right()
            move_down()
            fill_cell()
            move_down()
            move_left()
            fill_cell()
            move_up()
            fill_cell()
            move_left()
            fill_cell()
            move_up()

            if j != 9:
                move_right(4)

        move_left(36)

        if i != 4:
            move_down(4)


if __name__ == '__main__':
    run_tasks()
