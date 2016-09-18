import unittest

import pyrob.core as rob
import pyrob.utils
from pyrob.core import RobotCrashed


class MovementTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pyrob.utils.allow_internal(True)

    @classmethod
    def setUp(cls):
        rob.set_field_size(10, 10)

    def testLeft(self):
        rob.goto(0, 9)
        for i in range(8):
            rob.left()
            self.assertEqual(rob.get_pos(), (0, 8 - i))

        rob.goto(0, 9)
        rob.left(9)

        self.assertEqual(rob.get_pos(), (0, 0))

    def testRight(self):
        rob.goto(0, 0)
        for i in range(8):
            rob.right()
            self.assertEqual(rob.get_pos(), (0, i + 1))

        rob.goto(0, 0)
        rob.right(9)

        self.assertEqual(rob.get_pos(), (0, 9))

    def testUp(self):
        rob.goto(9, 0)
        for i in range(8):
            rob.up()
            self.assertEqual(rob.get_pos(), (8 - i, 0))

        rob.goto(9, 0)
        rob.up(9)

        self.assertEqual(rob.get_pos(), (0, 0))

    def testDown(self):
        rob.goto(0, 0)
        for i in range(8):
            rob.down()
            self.assertEqual(rob.get_pos(), (i + 1, 0))

        rob.goto(0, 0)
        rob.down(9)

        self.assertEqual(rob.get_pos(), (9 , 0))

    def testWallCrash(self):
        rob.goto(0, 0)

        for move, test in [('right', 'up'), ('down', 'right'), ('left', 'down'), ('up', 'left')]:
            for i in range(10):
                with self.assertRaises(RobotCrashed):
                    getattr(rob, test)()

                if i != 9:
                    getattr(rob, move)()

        rob.goto(0, 0)
        with self.assertRaises(RobotCrashed):
            rob.right(10)

        rob.goto(0, 0)
        with self.assertRaises(RobotCrashed):
            rob.down(10)

        rob.goto(9, 9)
        with self.assertRaises(RobotCrashed):
            rob.left(10)

        rob.goto(9, 9)
        with self.assertRaises(RobotCrashed):
            rob.up(10)