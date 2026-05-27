class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}

        # Store last occurrence of lowercase letters
        # and first occurrence of uppercase letters
        for i, ch in enumerate(word):
            if ch.islower():
                last_lower[ch] = i
            else:
                c = ch.lower()
                if c not in first_upper:
                    first_upper[c] = i

        count = 0

        # Check special characters
        for c in last_lower:
            if c in first_upper and last_lower[c] < first_upper[c]:
                count += 1

        return count
