class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # Both from front
        front = right + 1

        # Both from back
        back = n - left

        # One from front, one from back
        both = (left + 1) + (n - right)

        return min(front, back, both)
        
