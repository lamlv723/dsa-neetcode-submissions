class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # Brute force. Time: O(n^2) | Space: O(1)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if((nums[i] + nums[j] == target)):
        #             return [i, j]
        # return []

        # Hashmap. Time: O(n) | Space: O(n)
        num_map = {}
        for j in range(n):
            cur = nums[j]
            diff = target - cur

            i = num_map.get(diff)
            if i is not None:
                return [i, j]
            
            num_map[cur] = j

        return []

