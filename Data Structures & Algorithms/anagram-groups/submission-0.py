class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            sWord = "".join(sorted(word))
            if sWord in groups:
                groups[sWord].append(word)
            else:
                groups[sWord] = [word]

        return [x for x in groups.values()]
        