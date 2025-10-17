class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        m = dividend
        n = divisor
        if int(m/n) > pow(2,31)-1:
            return (pow(2,31)-1)
        elif int(m/n) < -pow(2,31):
            return -pow(2,31)
        else:
            r = int(m/n)
            return r

