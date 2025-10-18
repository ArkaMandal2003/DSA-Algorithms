class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True 
        else:
            s1 = ''.join(letter.lower() for letter in s if letter.isalnum())
            if s1[::-1] == s1:
                return True
            else:
                return False 