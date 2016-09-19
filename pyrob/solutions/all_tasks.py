#!/usr/bin/python3

import sys
from pyrob.api import *

import task_1_1
import task_1_2
import task_2_1
import task_2_2
import task_2_4
import task_3_1
import task_3_3
import task_5_2
import task_5_3
import task_5_4
import task_5_7


if __name__ == '__main__':
    res = run_tasks(headless=True)
    sys.exit(0 if res else -1)
