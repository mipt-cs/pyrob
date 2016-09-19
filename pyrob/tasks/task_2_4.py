#!/usr/bin/python3

import pyrob.core as rob
from . import check_filled_cells


class Task:
    CHECKS = 1

    def load_level(self, n):
        rob.set_field_size(19, 39)

        rob.set_parking_cell(16, 0)

        self.cells_to_be_filled = []

        def mark_cell(i, j):
            rob.set_cell_type(i, j, rob.CELL_TO_BE_FILLED)
            self.cells_to_be_filled.append((i, j))

        for i in range(5):
            for j in range(10):
                _j = 4*j
                _i = 4*i
                mark_cell(_i + 1, _j + 1)
                mark_cell(_i + 1, _j + 2)
                mark_cell(_i + 1, _j + 0)
                mark_cell(_i + 2, _j + 1)
                mark_cell(_i + 0, _j + 1)

        rob.goto(0, 0)

    def check_solution(self):
        if not rob.is_parking_point():
            return False

        return check_filled_cells(self.cells_to_be_filled)