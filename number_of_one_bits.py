__author__ = 'Alfred'

"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known
as the Hamming weight). For example, the 32-bit integer '11' has binary representation
00000000000000000000000000001011, so the function should return 3.
"""


class Solution:
    """
    >>> print Solution().hammingWeight(342423432423423423423423423L)
    58

    >>> print Solution().hammingWeight(11)
    3

    """
    # @param n, an integer
    # @return an integer
    def hammingWeight(this, n):
        return (bin(n)).count('1')


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)


