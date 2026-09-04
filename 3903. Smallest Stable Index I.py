class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            # Find maximum from 0 to i
            left_max = nums[0]
            for j in range(1, i + 1):
                left_max = max(left_max, nums[j])
            # Find minimum from i to n-1
            right_min = nums[i]
            for j in range(i + 1, n):
                right_min = min(right_min, nums[j])
            # Check stability
            if left_max - right_min <= k:
                return i
        return -1
