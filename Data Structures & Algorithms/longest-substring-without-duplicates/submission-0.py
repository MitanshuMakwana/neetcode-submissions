class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        n = len(s)
        new_sett = set()

        for right in range(n):
            while s[right] in new_sett:
                new_sett.remove(s[left])
                left += 1
            
            win_len = (right - left)+1
            max_len = max(max_len, win_len)
            new_sett.add(s[right])
        return max_len