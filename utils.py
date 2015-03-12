import time

__author__ = 'Alfred'


def performance(inits=False):
    """
    Performance measerement tool
    :param inits: init START time on first call
    """
    if inits or 'START' not in globals():
        global START
        START = in_millis(time.time())
    else:
        end = in_millis(time.time())
        print end - START
        START = end


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
    # see my answer on unused variable complain
    # http://stackoverflow.com/questions/5477134/how-can-i-get-around-declaring-an-unused-variable-in-a-for-loop/
    for dummy in range(1, size):
        wrapper(function_name, bignum)
    performance()
