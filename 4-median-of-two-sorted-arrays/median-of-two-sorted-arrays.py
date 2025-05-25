class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = []
        n = nums1 + nums2

        for i in range(1, len(n)):
            key = n[i]
            j= i - 1
            while j>=0 and n[j]>key:
                n[j+1] = n[j]
                j = j - 1
            n[j+1] = key
        
        l = len(n)
        if l %2 == 0:
            index = int(l/2)
            med = ((n[index] + n[index-1]) / 2)
            return med
        else:
            index = int((l-1)/2)
            return n[index]


