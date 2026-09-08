class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(1, n + 1):
            # Convert number to string
            s = str(i)
            # Every 3 digits after the first group needs a comma
            if len(s) >= 4:
                count += (len(s) - 1) // 3
        return count
        
