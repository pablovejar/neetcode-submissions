class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        count = [0]*26
        freq = [0]*26
        k = len(s1)
        for c in s1:
            count[ord(c)-ord('a')] +=1
        
        for c in s2[:k]:
            freq[ord(c)-ord('a')] +=1

        if count == freq:
            return True
        
        for r in range(k,len(s2)):
            freq[ord(s2[r])-ord('a')] +=1
            freq[ord(s2[r-k])-ord('a')] -=1
            if freq == count:
                return True
        return False

