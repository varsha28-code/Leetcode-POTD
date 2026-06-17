class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)

        lengths = [0] * (n + 1)

        # Compute lengths after each operation
        for i, ch in enumerate(s):
            cur = lengths[i]

            if 'a' <= ch <= 'z':
                lengths[i + 1] = cur + 1

            elif ch == '*':
                lengths[i + 1] = max(0, cur - 1)

            elif ch == '#':
                lengths[i + 1] = cur * 2

            else:  # '%'
                lengths[i + 1] = cur

        if k >= lengths[n]:
            return '.'

        # Reverse simulation
        for i in range(n - 1, -1, -1):
            ch = s[i]
            prev_len = lengths[i]

            if 'a' <= ch <= 'z':
                if k == prev_len:
                    return ch

            elif ch == '*':
                pass

            elif ch == '#':
                if prev_len > 0:
                    k %= prev_len

            else:  # '%'
                if prev_len > 0:
                    k = prev_len - 1 - k

        return '.'
        
