class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        multiple = k
        while True:
            if multiple not in nums:
                return multiple
            multiple += k
        
