# coding=utf-8
"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Total Accepted: 27937
Total Submissions: 39276
Difficulty: Easy
Contributors: Samuri
"""


class Solution(object):
    """
    >>> s = Solution()
    >>> s.hammingDistance1(1,4)
    2
    >>> s.hammingDistance1(0,2**(2**28) - 1)
    268435456
    """

    def hammingDistance(self, x, y):
        """
        Beats 95.74 - 47.86 % submissions on 10.02.2017 (36-45 ms)
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(y ^ x).count('1')

    def hammingDistance1(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        import gmpy2
        return gmpy2.popcount(x ^ y)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
