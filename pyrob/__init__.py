#!/usr/bin/python3

import functools
import importlib
import logging

import pyrob.core
import pyrob.utils
import pyrob.viz

tasks_to_run = []

logger = logging.getLogger(__name__)


def get_task_class(task_id):
    module = importlib.import_module('pyrob.tasks.' + task_id)
    return module.Task


def task(f):

    @functools.wraps(f)
    def wrapper():
        task_id = f.__name__
        print('Running task ' + task_id)
        clazz = get_task_class(task_id)
        for i in range(clazz.CHECKS):
            pyrob.core.on_position_changed = None

            _task = clazz()
            with pyrob.utils.allow_internal(True):
                _task.load_level()

            pyrob.core.on_position_changed = pyrob.viz.update_robot_position

            pyrob.viz.render_maze()
            pyrob.viz.update_robot_position(*pyrob.core.get_pos())

            passed = True
            try:
                f()
            except Exception as e:
                logger.error('Caught exception: {}'.format(e))
                passed = False

            with pyrob.utils.allow_internal(True):
                passed = passed and _task.check_solution()

    tasks_to_run.append(wrapper)
    return wrapper


def run_tasks(verbose=False):

    logging.basicConfig(level=(logging.DEBUG if verbose else logging.INFO))

    pyrob.viz.init()

    for t in tasks_to_run:
        logger.info('Starting task {}'.format(t.__name__))
        t()
        logger.info('Task {} finished'.format(t.__name__))
