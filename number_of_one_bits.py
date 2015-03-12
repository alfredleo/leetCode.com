# encoding: utf-8
# module number_of_one_bits
"""
Write a function that takes an unsigned integer and returns the number of '1' bits it
has (also known as the Hamming weight). For example, the 32-bit integer '11' has binary
representation 00000000000000000000000000001011, so the function should return 3.
"""
from utils import test_speed

__author__ = 'Alfred'


class Solution(object):
    """
    >>> print Solution.by_wegner(342423334234234423423L)
    30
    >>> print Solution.by_string(342423334234234423423L)
    30
    >>> print Solution.hamming_weight(11)
    3
    """

    @staticmethod
    def hamming_weight(num):
        """ Starting function for algorithms to call
        :param num: an integer
        :return: an integer
        """
        # return Solution.by_string(num)
        return Solution.by_wegner(num)

    @staticmethod
    def by_string(num):
        """ Algorithm by string
        """
        return (bin(num)).count('1')

    @staticmethod
    def by_wegner(num):
        """ Wegner 1960 algorithm implementation
        """
        count = 0
        while num != 0:
            num &= num - 1
            count += 1
        return count


OBJECTIVES = ['performance', 'test']
OBJECTIVE = OBJECTIVES[1]

if OBJECTIVE == OBJECTIVES[0]:
    print 'by_string: '
    test_speed(Solution.by_string)
    print 'by_wagner: '
    test_speed(Solution.by_wegner)
elif OBJECTIVE == OBJECTIVES[1] and __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
