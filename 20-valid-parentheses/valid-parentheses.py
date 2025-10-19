class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for item in s:
            if item in hashmap:
                if stack == []:
                    return False
                top = stack.pop()
                if hashmap[item] != top:
                    return False
            else:
                stack.append(item)

        if stack:
            return False
        return True