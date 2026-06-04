class Solution:
    def isPalindrome(self, s: str) -> bool:
        sWithoutSpace = "".join([char for char in s.replace(" ","").lower() if char.isalnum()])
        for i in range(len(sWithoutSpace)):
            if sWithoutSpace[i] != sWithoutSpace[-i-1]: return False
        return True