class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        longest = 0  #keeping count
        new_set = set()  #keeping track of duplicate
        n = len(s)

        # O(n)
        for r in range(n):
            while s[r] in new_set:  #current window is invalid as r[s] already in set
                  new_set.remove(s[l])
                  l += 1
            
            # valid window 
            w = (r-l)+1
            longest = max(longest, w)
            new_set.add(s[r])
        return longest
