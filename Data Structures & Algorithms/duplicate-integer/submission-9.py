class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Method 1
        # return len(set(nums)) != len(nums)

        # Method 2: Sorting first
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True

        return False
