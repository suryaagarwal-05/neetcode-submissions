class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # n = 0;
        # nums.sort()
        # while n<len(nums)-1:
        #     if nums[n] == nums[n+1]:
        #         return True
        #     n+=1
        # return False
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False        