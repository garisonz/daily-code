class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        length = len(nums)
        tmp = []
        k = 0

        for i in nums:
            if i == val:
                count += 1
                continue
            tmp.append(i)

        for i in range(len(tmp)):
            nums[i] = tmp[i]

        k = length - count
        return k
