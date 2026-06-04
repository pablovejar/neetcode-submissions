class Solution:
    def isPalindrome(self, s: str) -> bool:
        # sWithoutSpace = "".join([char for char in s.replace(" ","").lower() if char.isalnum()])
        # for i in range(len(sWithoutSpace)):
        #     if sWithoutSpace[i] != sWithoutSpace[-i-1]: return False
        i = 0
        j = -1
        while i < len(s) and j > -len(s):
            if not s[i].isalnum(): 
                i += 1
                continue
            if not s[j].isalnum():
                j -=1
                continue
            if s[i].lower() != s[j].lower():
                return False
            else:
                i +=1
                j -=1

        return True