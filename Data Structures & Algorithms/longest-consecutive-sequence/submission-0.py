class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        store = set(nums)

        for num in nums:
            curr, streak = num, 0
            while curr in store:
                streak += 1
                curr += 1
            ans = max(ans, streak)

        return ans