class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = 0;
        nums.sort()
        while n<len(nums)-1:
            if nums[n] == nums[n+1]:
                return True
            n+=1
        return False
        