class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in temp:
                return [temp[diff], i]

            temp[num] = i