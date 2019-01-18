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
        dict = {}
        for word in strs:
            if word[0] in dict:
                dict[word[0]].append(word)
            else:
                dict[word[0]] = [word]
        prefixes = []
        for letter in dict:
            if len(dict[letter]) > 1:
                prefixes.append(self.commonprefix(dict[letter]))
        longest = ''
        for prefix in prefixes:
            if len(prefix) > len(longest):
                longest = prefix
        return longest

    def commonprefix(self, m):
        if not m: return ''
        s1 = min(m)
        s2 = max(m)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1
