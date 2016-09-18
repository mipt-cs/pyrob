#!/usr/bin/python3

from pyrob.api import *


@task
def sample1():

    for i in range(8):
        right()

    for i in range(8):
        down()

run_tasks(verbose=True)
