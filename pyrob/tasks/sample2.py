#!/usr/bin/python3

import pyrob.core as rob


class Task:
    CHECKS = 1

    def load_level(self):
        rob.set_field_size(10, 10)

    def check_solution(self):
        pass