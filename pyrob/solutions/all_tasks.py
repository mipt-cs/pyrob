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
import task_8_21
import task_8_22
import task_8_27
import task_8_28
import task_8_29
import task_4_3
import task_4_11
import task_5_10
import task_6_6
import task_8_30
import task_9_3
import task_7_5
import task_7_6
import task_7_7
import task_8_18


if __name__ == '__main__':
    res = run_tasks(headless=True)
    sys.exit(0 if res else -1)
