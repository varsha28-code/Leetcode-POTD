Python Solution (Without Built-in math.gcd)
---------------
class Solution:
    def findGCD(self, nums):
        mn = min(nums)
        mx = max(nums)
        while mx != 0:
            mn, mx = mx, mn % mx
        return mn


Python Solution (Using Built-in math.gcd)
---------------
from math import gcd
class Solution:
    def findGCD(self, nums):
        return gcd(min(nums), max(nums))
