from utils import test_speed

__author__ = 'Alfred'

"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known
as the Hamming weight). For example, the 32-bit integer '11' has binary representation
00000000000000000000000000001011, so the function should return 3.
"""


class Solution:
    """
    >>> s = Solution()
    >>> print s.by_wegner(342423334234234423423L)
    30
    >>> print s.by_string(342423334234234423423L)
    30

    >>> print s.hammingWeight(11)
    3
    """

    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        return self.by_string(n)
        # return self.by_wegner(n)


    def by_string(self, n):
        """
        Algorithm by string
        """
        return (bin(n)).count('1')

    def by_wegner(self, n):
        """
        Wegner 1960 algorithm implementation
        """
        count = 0
        while n != 0:
            n &= n - 1
            count += 1
        return count


objectives = ['performance', 'test']
objective = objectives[0]

if objective == objectives[0]:
    s = Solution()
    print('by_string: ')
    test_speed(s.by_string)
    print('by_wagner: ')
    test_speed(s.by_wegner)
elif objective == objectives[1] and __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
