class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        count=0
        for ch in patterns:
            if ch in word:
                count+=1
        return count
