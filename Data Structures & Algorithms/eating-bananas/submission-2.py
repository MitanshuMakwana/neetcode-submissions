class Solution:
    def getHours(self, piles, mid):
        hours = 0

        for pile in piles:
            hours += (pile+mid-1)//mid  #ceil division
        return hours
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        l = 1                 # min limit can eat
        r = max(piles)        # max limit can eat

        while l<=r:
            mid = (l+r)//2

            if self.getHours(piles,mid) > h:
                l = mid + 1
            else:
                k = mid
                r = mid-1
        return k        