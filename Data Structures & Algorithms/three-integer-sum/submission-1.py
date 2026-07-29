class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()

        for i in range(n):
            seen = set()
            for j in range(i + 1, n):
                target = -(nums[i] + nums[j])

                if target in seen:
                    triplet = tuple(sorted([nums[i], nums[j], target]))
                    ans.add(triplet)

                seen.add(nums[j])

        return [list(x) for x in ans]