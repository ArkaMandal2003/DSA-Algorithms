class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0):
            return False
        else:
            s = str(x)
            if s[::-1] == s:
                return True
            else:
                return False

             