#!/usr/bin/python3

import sys
from pyrob.api import run_tasks

from pyrob.solutions import task_1_1
from pyrob.solutions import task_1_2
from pyrob.solutions import task_2_1
from pyrob.solutions import task_2_2
from pyrob.solutions import task_2_4
from pyrob.solutions import task_3_1
from pyrob.solutions import task_3_3
from pyrob.solutions import task_5_2
from pyrob.solutions import task_5_3
from pyrob.solutions import task_5_4
from pyrob.solutions import task_5_7
from pyrob.solutions import task_8_21
from pyrob.solutions import task_8_22
from pyrob.solutions import task_8_27
from pyrob.solutions import task_8_28
from pyrob.solutions import task_8_29
from pyrob.solutions import task_4_3
from pyrob.solutions import task_4_11
from pyrob.solutions import task_5_10
from pyrob.solutions import task_6_6
from pyrob.solutions import task_8_30
from pyrob.solutions import task_9_3
from pyrob.solutions import task_7_5
from pyrob.solutions import task_7_6
from pyrob.solutions import task_7_7
from pyrob.solutions import task_8_18
from pyrob.solutions import task_8_2
from pyrob.solutions import task_8_3
from pyrob.solutions import task_8_4
from pyrob.solutions import task_8_6
from pyrob.solutions import task_8_10
from pyrob.solutions import task_8_11


if __name__ == '__main__':
    res = run_tasks(headless=True)
    sys.exit(0 if res else -1)
