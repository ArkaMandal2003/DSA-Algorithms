class Solution:
    def reverse(self, x: int) -> int:
        MAX_VALUE = pow(2, 31) - 1
        l = list(map(int, str(abs(x))))
        num = 0
        y = len(l)
        for i in range(y):
            num = num + (l[i] * pow(10 , i))
        if x >= 0 and num <= MAX_VALUE:
            return num
        elif num > MAX_VALUE:
            return 0 
        else:
            return num * (-1)
        