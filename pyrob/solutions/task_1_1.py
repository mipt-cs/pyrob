#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_1():

    move_right()
    move_right()
    move_down()

run_tasks(verbose=True)
