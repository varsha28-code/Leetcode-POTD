class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digits = [int(d) for d in str(n)]
        sum = 0
        mul = 1
        for digit in digits:
            sum += digit
            mul *= digit
        return n % (sum + mul) == 0
