class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for num in s:
            # Is this number the start of a sequence?
            if (num - 1) not in s:
                nextNum = num + 1
                curr_len = 1
                while nextNum in s:
                    curr_len += 1
                    nextNum += 1
                longest = max(longest, curr_len)
        return longest

# Time Complexity = O(n) every no. is visited 1 time 