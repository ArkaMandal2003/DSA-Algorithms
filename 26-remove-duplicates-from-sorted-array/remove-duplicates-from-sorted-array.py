class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i= 0
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        elif len(nums) == 2:
            if nums[0] == nums[1]:
                del nums[1]
                return len(nums)
            else:
                return len(nums)
        else:
            while i <= len(nums) - 2:
                if nums[i] == nums[i+1]:
                    del nums[i]
                else:
                    i = i + 1
        
        return len(nums)

