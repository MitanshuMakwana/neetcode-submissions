class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n-1

        while l<r:
            num_sum = numbers[l] + numbers[r]
            if target==num_sum:
                return[l+1, r+1]
            elif num_sum<target:
                l+=1
            else:
                r-=1