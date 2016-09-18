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


def task(*args, **kwargs):

    def decorator(f):

        @functools.wraps(f)
        def wrapper():
            task_id = f.__name__
            print('Running task ' + task_id)
            clazz = get_task_class(task_id)
            passed = True
            for i in range(clazz.CHECKS):
                pyrob.core.on_position_changed = None

                _task = clazz()
                with pyrob.utils.allow_internal(True):
                    _task.load_level()

                pyrob.core.on_position_changed = pyrob.viz.update_robot_position(delay)

                pyrob.viz.render_maze()
                pyrob.core.on_position_changed(*pyrob.core.get_pos())

                try:
                    f()
                except Exception as e:
                    logger.error('Caught exception: {}'.format(e))
                    passed = False

                with pyrob.utils.allow_internal(True):
                    passed = passed and _task.check_solution()

                if passed:
                    logger.debug('Test #{} passed for task {}'.format(i + 1, task_id))
                else:
                    logger.error('Test #{} failed for task {}'.format(i+1, task_id))
                    break

            return passed

        tasks_to_run.append(wrapper)
        return wrapper

    if 'delay' in kwargs:
        delay = kwargs['delay']
        return decorator
    else:
        delay = None
        return decorator(args[0])


def run_tasks(verbose=False):

    logging.basicConfig(level=(logging.DEBUG if verbose else logging.INFO))

    pyrob.viz.init()

    passed = 0
    for t in tasks_to_run:
        logger.info('Starting task {}'.format(t.__name__))
        status = t()
        if status:
            passed += 1
        logger.info('Task {} finished: {}'.format(t.__name__, ('+' if status else '-')))

    logger.info('Total: {}/{}'.format(passed, len(tasks_to_run)))