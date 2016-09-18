#!/usr/bin/python3

from pyrob.api import *


@task
def sample1():

    move_up()


@task
def sample2():

    move_down()


run_tasks(verbose=True)
