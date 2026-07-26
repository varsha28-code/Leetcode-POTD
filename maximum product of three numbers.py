class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prod=1
        for i in nums:
            prod=prod*i
        return prod
