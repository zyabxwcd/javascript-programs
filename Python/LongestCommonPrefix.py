class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs.count("") >= 1:
            return ''
        elif len(strs) == 1:
            return strs[0]
        
        if not strs: return ''
        s1 = min(strs)
        s2 = max(strs)
        for index, char in enumerate(s1):
            if char != s2[index]:
                return s1[:index]
        return s1