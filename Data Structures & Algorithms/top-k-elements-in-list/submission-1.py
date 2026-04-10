

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        arr = []
        for key, freq in counts.items():
            arr.append([freq, key])
        arr.sort()

        temp = []
        while len(temp) < k:
            temp.append(arr.pop()[1])
        return temp    