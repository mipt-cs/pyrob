#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():

    c = 0

    while True:
        if cell_is_filled():
            c += 1
            if c == 5:
                break
        move_right()


if __name__ == '__main__':
    run_tasks()
