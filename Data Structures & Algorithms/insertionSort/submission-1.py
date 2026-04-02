# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = []
        
        if n == 0:
            return res
        
        # Add initial state
        res.append(pairs[:])
        
        for i in range(1, n):
            j = i - 1
            
            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                # Swap
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1
            
            # Save state after this insertion
            res.append(pairs[:])
        
        return res