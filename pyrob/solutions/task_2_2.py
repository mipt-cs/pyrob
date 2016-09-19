#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():

    move_down()

    for i in range(5):
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

        if i != 4:
            move_right(4)


run_tasks()
