

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        count = 0

        for num in nums:

            if num == 0:
                count = 0
            if num == 1:
                count += 1

            ans = max(ans, count)
        return ans