class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        lsum = sum(int(x) for x in num[:n//2] if x != '?')
        rsum = sum(int(x) for x in num[n//2:] if x != '?')
        lq = num[:n//2].count('?')
        rq = num[n//2:].count('?')
        if (lq + rq) % 2:
            return True
        return lsum - rsum != (rq - lq) // 2 * 9
        
