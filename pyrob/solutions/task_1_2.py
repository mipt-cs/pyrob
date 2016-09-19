#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():

    move_right()
    move_right()
    move_down()
    move_down()
    fill_cell()
    move_down()
    move_right()
    move_right()

run_tasks(verbose=True)
