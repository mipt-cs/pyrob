#!/usr/bin/python3

import pyrob.core as rob
from . import check_filled_cells


class Task:
    CHECKS = 1

    def load_level(self):
        rob.set_field_size(9, 19)

        rob.set_parking_cell(1, 16)

        self.cells_to_be_filled = []

        def mark_cell(i, j):
            rob.set_cell_type(i, j, rob.CELL_TO_BE_FILLED)
            self.cells_to_be_filled.append((i, j))

        for i in range(5):
            mark_cell(2, 1 + 4*i)
            mark_cell(2, 2 + 4*i)
            mark_cell(2, 0 + 4*i)
            mark_cell(3, 1 + 4*i)
            mark_cell(1, 1 + 4*i)

        rob.goto(0, 0)

    def check_solution(self):
        if not rob.is_parking_point():
            return False

        return check_filled_cells(self.cells_to_be_filled)