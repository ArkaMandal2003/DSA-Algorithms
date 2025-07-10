class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for item in arr:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
        
        l = []

        for item in freq:
            if item == freq[item]:
                l = l + [item]

        if len(l) > 0:
            return max(l)
        else:
            return -1