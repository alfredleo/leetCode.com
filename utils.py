# encoding: utf-8
# module utils
"""
This is a support module for algorithms performance check
"""
import time

__author__ = 'alfredleo@gmail.com (Alfred)'

START = 0


def performance(inits=False):
    """
    Performance measerement tool
    :param inits: init starting time on first call
    """
    if inits:
        # TODO(Alfred): Implement performance testing without global variable.
        # Could not come with a good solution to store START variable from
        # call to call without class creation, so using global here and added
        # disable to pylint.
        global START  # pylint: disable=global-statement
        START = in_millis(time.time())
    else:
        end = in_millis(time.time())
        print '-->', end - START, 'milliseconds'
        START = end


def in_millis(val):
    """
    Converts float time in seconds to milliseconds
    :type t: time in seconds of type float
    :return: current time in milliseconds
    """
    return int(round(val * 1000))


def wrapper(func, *args):
    """
    Call function by name and argumets
    :param func:
    :param args:
    """
    func(*args)


def test_speed(function_name, bignum=(2 ^ 999), size=10000000):
    """
    Test algorithms speed
    :param size:
    :param function_name:
    :param bignum:
    """
    performance(True)
    # see my answer on unused variable complain
    # http://stackoverflow.com/questions/5477134/how-can-i-get-around-declaring-an-unused-variable-in-a-for-loop/
    for dummy in range(1, size):
        wrapper(function_name, bignum)
    performance()
