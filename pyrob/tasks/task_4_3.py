#!/usr/bin/python3

import pyrob.core as rob
from pyrob.tasks import check_filled_cells


class Task:
    CHECKS = 1

    def load_level(self, n):
        rob.set_field_size(15, 29)

        self.cells_to_fill = []

        for i in range(1, 13):
            for j in range(1, 28):
                rob.set_cell_type(i, j, rob.CELL_TO_BE_FILLED)
                self.cells_to_fill.append((i, j))

        rob.set_parking_cell(13, 1)

        rob.goto(1, 0)


    def check_solution(self):

        return check_filled_cells(self.cells_to_fill) and rob.is_parking_point()
