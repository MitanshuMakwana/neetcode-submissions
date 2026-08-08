class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newSet = set(nums)
        longest = 0

        for num in newSet:
            if (num - 1) not in newSet:
                nextNum = num + 1
                curr_len = 1
                while nextNum in newSet:
                    curr_len += 1
                    nextNum += 1
                longest = max(longest, curr_len)
        return longest
