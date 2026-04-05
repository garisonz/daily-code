class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxRight = -1
        for i in reversed(range(len(arr))):
            curr = arr[i]
            arr[i] = maxRight
            maxRight = max(maxRight, curr)
        return arr