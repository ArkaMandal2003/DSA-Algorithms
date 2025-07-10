class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x in range(1,4):
            return 1
        else:    
            for i in range(x//2+2):
                if i*i == x:
                    return i
                    break
                elif i*i > x:
                    return i-1
                    break
                else:
                    continue