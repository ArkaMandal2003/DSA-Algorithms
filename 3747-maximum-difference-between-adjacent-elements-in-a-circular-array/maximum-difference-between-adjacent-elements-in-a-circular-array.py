class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res = []
        n = len(nums)
        for i in range(n-1):
            res += [abs(nums[i+1]-nums[i])]
        res += [abs(nums[0]-nums[n-1])]
        return max(res)