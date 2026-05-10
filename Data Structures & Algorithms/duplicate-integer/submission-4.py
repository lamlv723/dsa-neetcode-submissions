class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n_list = len(nums)
        nums_set = set(nums)
        n_set = len(nums_set)
        if n_list != n_set:
            return True

        return False