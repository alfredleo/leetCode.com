from utils import testSpeed

__author__ = 'Alfred'

"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known
as the Hamming weight). For example, the 32-bit integer '11' has binary representation
00000000000000000000000000001011, so the function should return 3.
"""


class Solution:
    """
    >>> s = Solution()
    >>> print s.byWegner(342423334234234423423L)
    30
    >>> print s.byString(342423334234234423423L)
    30

    >>> print s.hammingWeight(11)
    3
    """

    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        return self.byString(n)
        # return self.byWegner(n)


    def byString(self, n):
        """
        Algorithm by string
        """
        return (bin(n)).count('1')

    def byWegner(self, n):
        """
        Wegner 1960 algorithm implementation
        """
        count = 0
        while n != 0:
            n &= n - 1
            count += 1
        return count


objectives = ['performance', 'test']
objective = objectives[1]

if (objective == objectives[0]):
    s = Solution()
    print('byString: ')
    testSpeed(s.byString)
    print('byWagner: ')
    testSpeed(s.byWegner)
elif objective == objectives[1] and __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)


