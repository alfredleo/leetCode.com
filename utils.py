import time

__author__ = 'Alfred'


def performance(inits=False):
    """
    Performance measerement tool
    :param inits: init start time on first call
    """
    if inits or 'start' not in globals():
        global start
        start = in_millis(time.time())
    else:
        end = in_millis(time.time())
        print end - start
        start = end


def in_millis(t):
    return int(round(t * 1000))


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
    """
    performance(True)
    for i in range(1, size):
        wrapper(function_name, bignum)
    performance()
